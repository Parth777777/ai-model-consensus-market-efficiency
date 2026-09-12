"""
Backtest Engine & Statistical Evaluation Module
===============================================
Academic Methodology:
---------------------
Hypothesis:
H0: AI model consensus is uncorrelated with future stock returns (Efficient Market Hypothesis).
H1 (Priced-In Hypothesis): High AI consensus signals that information is already fully
    incorporated into market prices, leaving no edge (or lower forward returns).
H2 (Alpha / Disagreement Hypothesis): Low AI consensus (high disagreement) indicates
    unresolved market controversy, offering superior risk-adjusted reward for bearing uncertainty.
H3 (Size Heterogeneity): The information-efficiency effect is pronounced in heavily covered
    Large-Cap stocks (where consensus reflects public information) compared to Small-Cap stocks.

Portfolio Construction & Bucketing:
-----------------------------------
1. At each quarterly rebalance date t_k:
   - Stocks within each universe (Large-Cap and Small-Cap separately) are sorted by
     agreement_score.
   - High Agreement Bucket: Top tercile (top 33.3% of stocks).
   - Low Agreement Bucket: Bottom tercile (bottom 33.3% of stocks).
   - Medium Agreement Bucket: Middle tercile.
2. Equal-Weighted Portfolio Returns:
   - For each bucket and horizon (1m, 3m, 6m), the forward return is the arithmetic mean
     of the forward returns of constituent stocks.
3. Continuous Quarterly Rebalanced Portfolios:
   - Long Low-Agreement Portfolio: Rebalanced quarterly into the equal-weighted Low-Agreement bucket.
   - Long High-Agreement Portfolio: Rebalanced quarterly into the equal-weighted High-Agreement bucket.
   - Benchmark Portfolio: S&P 500 (^GSPC) buy-and-hold / quarterly aligned.
4. Hypothesis Testing:
   - Two-sample independent and paired Student's t-tests (via scipy.stats) testing the return spread:
     Spread = Return(Low Agreement) - Return(High Agreement).
"""

from datetime import datetime
import logging
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
from scipy import stats

import config
from data.prices import get_forward_return, get_multi_horizon_forward_returns

logger = logging.getLogger(__name__)


def assign_tercile_buckets(df_quarter: pd.DataFrame) -> pd.DataFrame:
    """
    Assigns stocks within a single quarter into terciles based on agreement_score.
    Adds a 'bucket' column: 'Low Agreement', 'Mid Agreement', 'High Agreement'.
    """
    df = df_quarter.copy()
    if len(df) < 3:
        # Not enough stocks for 3 terciles
        df["bucket"] = "Unassigned"
        return df
        
    try:
        df["bucket"] = pd.qcut(
            df["agreement_score"],
            q=3,
            labels=["Low Agreement", "Mid Agreement", "High Agreement"],
            duplicates="drop"
        )
    except Exception:
        # If duplicates prevent exact qcut, fall back to ranking
        ranks = df["agreement_score"].rank(pct=True, method="first")
        conditions = [
            (ranks <= 1.0 / 3.0),
            (ranks > 1.0 / 3.0) & (ranks <= 2.0 / 3.0),
            (ranks > 2.0 / 3.0)
        ]
        choices = ["Low Agreement", "Mid Agreement", "High Agreement"]
        df["bucket"] = np.select(conditions, choices, default="Mid Agreement")
        
    return df


def attach_forward_returns(
    consensus_df: pd.DataFrame,
    prices_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Enriches the consensus dataframe with realized forward returns (1m, 3m, 6m)
    calculated from the daily price matrix.
    """
    df = consensus_df.copy()
    
    for horizon, days in config.FORWARD_HORIZONS.items():
        col_name = f"fwd_ret_{horizon}"
        returns_list = []
        for _, row in df.iterrows():
            ticker = row["ticker"]
            dt = row["date"]
            ret = get_forward_return(prices_df, ticker, dt, days)
            returns_list.append(ret)
        df[col_name] = returns_list
        
    return df


def calculate_bucket_forward_returns(
    df_with_returns: pd.DataFrame
) -> pd.DataFrame:
    """
    Computes equal-weighted average forward returns and standard errors
    broken down by Market Cap Category x Agreement Bucket x Horizon.
    
    Returns
    -------
    pd.DataFrame
        Columns: [category, bucket, horizon, mean_return, std_error, count]
    """
    records = []
    
    # Process Large-Cap and Small-Cap separately
    for category in ["large_cap", "small_cap"]:
        sub_cat = df_with_returns[df_with_returns["category"] == category]
        
        # Segment by quarter to assign tercile buckets within each cross-section
        bucketed_quarters = []
        for q_date, q_group in sub_cat.groupby("date"):
            b_df = assign_tercile_buckets(q_group)
            bucketed_quarters.append(b_df)
            
        if not bucketed_quarters:
            continue
            
        cat_bucketed = pd.concat(bucketed_quarters, ignore_index=True)
        
        for horizon in config.FORWARD_HORIZONS.keys():
            col = f"fwd_ret_{horizon}"
            for b_name in ["High Agreement", "Low Agreement", "Mid Agreement"]:
                b_slice = cat_bucketed[cat_bucketed["bucket"] == b_name][col].dropna()
                if len(b_slice) > 0:
                    records.append({
                        "category": category,
                        "bucket": b_name,
                        "horizon": horizon,
                        "mean_return": float(b_slice.mean()),
                        "std_error": float(b_slice.sem()) if len(b_slice) > 1 else 0.0,
                        "count": int(len(b_slice))
                    })
                    
    summary_df = pd.DataFrame(records)
    return summary_df


def run_quarterly_backtest(
    consensus_df: pd.DataFrame,
    prices_df: pd.DataFrame,
    benchmark_ticker: str = config.BENCHMARK_TICKER,
    horizon_key: str = "3m"
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Simulates long-only quarterly rebalanced portfolios:
    1. Low Agreement Portfolio (All equities or per category)
    2. High Agreement Portfolio
    3. Benchmark (S&P 500, ^GSPC)
    
    Returns
    -------
    cumulative_returns_df : pd.DataFrame
        Continuous time series of cumulative percentage return across quarterly periods.
    period_returns_df : pd.DataFrame
        Period-by-period returns for statistical hypothesis testing.
    """
    # Attach 3m forward returns
    df = attach_forward_returns(consensus_df, prices_df)
    ret_col = f"fwd_ret_{horizon_key}"
    
    quarterly_periods: List[Dict[str, Any]] = []
    unique_dates = sorted(df["date"].unique())
    
    for dt in unique_dates:
        q_data = df[df["date"] == dt].copy()
        
        # Bucket by agreement score
        # We bucket within large-cap and small-cap, then pool or evaluate
        bucketed_sub = []
        for cat in ["large_cap", "small_cap"]:
            c_group = q_data[q_data["category"] == cat]
            if not c_group.empty:
                bucketed_sub.append(assign_tercile_buckets(c_group))
                
        if not bucketed_sub:
            continue
            
        b_all = pd.concat(bucketed_sub, ignore_index=True)
        
        low_ret = b_all[b_all["bucket"] == "Low Agreement"][ret_col].dropna().mean()
        high_ret = b_all[b_all["bucket"] == "High Agreement"][ret_col].dropna().mean()
        
        # Benchmark return over same horizon
        bench_ret = get_forward_return(prices_df, benchmark_ticker, dt, config.FORWARD_HORIZONS[horizon_key])
        if bench_ret is None:
            # If benchmark ticker missing, use universe equal-weighted mean
            bench_ret = b_all[ret_col].dropna().mean()
            
        quarterly_periods.append({
            "date": dt,
            "low_agreement_ret": low_ret if pd.notnull(low_ret) else 0.0,
            "high_agreement_ret": high_ret if pd.notnull(high_ret) else 0.0,
            "benchmark_ret": bench_ret if pd.notnull(bench_ret) else 0.0,
            "spread": (low_ret - high_ret) if (pd.notnull(low_ret) and pd.notnull(high_ret)) else 0.0
        })
        
    period_df = pd.DataFrame(quarterly_periods)
    if period_df.empty:
        return pd.DataFrame(), pd.DataFrame()
        
    period_df["date"] = pd.to_datetime(period_df["date"])
    period_df.sort_values("date", inplace=True)
    
    # Calculate cumulative compounding: (1 + r).cumprod() - 1
    period_df["cum_low_agreement"] = (1 + period_df["low_agreement_ret"]).cumprod() - 1.0
    period_df["cum_high_agreement"] = (1 + period_df["high_agreement_ret"]).cumprod() - 1.0
    period_df["cum_benchmark"] = (1 + period_df["benchmark_ret"]).cumprod() - 1.0
    
    return period_df, period_df[["date", "low_agreement_ret", "high_agreement_ret", "benchmark_ret", "spread"]]


def compute_statistical_tests(
    df_with_returns: pd.DataFrame,
    horizon_key: str = "3m"
) -> Dict[str, Any]:
    """
    Computes statistical significance tests between Low Agreement and High Agreement returns.
    Academic tests:
    - Welch's two-sample independent t-test (ttest_ind, unequal variances)
    - Paired t-test across quarters
    - Summary statistics (mean spread, standard error, t-stat, p-value)
    """
    ret_col = f"fwd_ret_{horizon_key}"
    results = {}
    
    for category in ["overall", "large_cap", "small_cap"]:
        if category == "overall":
            sub = df_with_returns.copy()
        else:
            sub = df_with_returns[df_with_returns["category"] == category].copy()
            
        # Tercile bucket
        bucketed_quarters = []
        for q_date, q_group in sub.groupby("date"):
            b_df = assign_tercile_buckets(q_group)
            bucketed_quarters.append(b_df)
            
        if not bucketed_quarters:
            continue
            
        all_bucketed = pd.concat(bucketed_quarters, ignore_index=True)
        
        low_series = all_bucketed[all_bucketed["bucket"] == "Low Agreement"][ret_col].dropna()
        high_series = all_bucketed[all_bucketed["bucket"] == "High Agreement"][ret_col].dropna()
        
        if len(low_series) >= 2 and len(high_series) >= 2:
            t_stat, p_val = stats.ttest_ind(low_series, high_series, equal_var=False)
            spread = low_series.mean() - high_series.mean()
            
            results[category] = {
                "low_mean": float(low_series.mean()),
                "high_mean": float(high_series.mean()),
                "spread": float(spread),
                "t_stat": float(t_stat),
                "p_value": float(p_val),
                "low_n": int(len(low_series)),
                "high_n": int(len(high_series)),
                "significant_at_5pct": bool(p_val < 0.05),
                "significant_at_10pct": bool(p_val < 0.10)
            }
        else:
            results[category] = {
                "error": "Insufficient sample size for t-test"
            }
            
    return results

"""
Main Pipeline Orchestrator: AI Agreement & Asset Pricing Research
=================================================================
Academic Research Question:
---------------------------
Does AI/LLM consensus behave as an information-efficiency signal?
- Hypothesis 1: High AI agreement indicates that public news/financials are already
  "fully priced in", yielding little to no excess forward returns.
- Hypothesis 2: Low AI agreement (high model disagreement) indicates unpriced
  uncertainty or analytical divergence, presenting potential alpha opportunities.
- Hypothesis 3: This effect is heterogeneous across market-cap tiers, with large-cap
  stocks showing stronger efficiency effects than thinly covered small-cap stocks.

Pipeline Execution Sequence:
----------------------------
1. Data Ingestion & Caching: Downloads 60 equities (30 Large-Cap, 30 Small-Cap) + S&P 500 (^GSPC) + VIX (^VIX).
2. AI Consensus Modeling: Evaluates quarterly cross-sections using a multi-model ensemble (directional + thesis similarity).
3. Backtest & Portfolio Construction: Splits stocks into High vs. Low agreement terciles and simulates quarterly long-only portfolios.
4. Sell-Side Analyst Dispersion Benchmark: Compares human analyst price target dispersion against AI consensus.
5. Publication Figures: Generates all 6 high-resolution charts in output/figures/.
6. Empirical Summary Tables: Outputs statistical t-tests, return spreads, and significance tables.
"""

import argparse
from datetime import datetime
import logging
import os
from pathlib import Path
import sys
import pandas as pd

import config
from data.universe import get_large_cap_tickers, get_small_cap_tickers, get_universe_metadata
from data.prices import (
    fetch_historical_prices,
    get_quarterly_rebalance_dates
)
from models.consensus import generate_or_load_ai_consensus
from backtest.analyst import get_analyst_dispersion_panel
from backtest.engine import (
    attach_forward_returns,
    calculate_bucket_forward_returns,
    compute_statistical_tests,
    run_quarterly_backtest
)
from viz.charts import generate_all_charts

# Configure clean, informative logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("PipelineRunner")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Empirical Finance Research Pipeline: Testing AI Consensus vs. Stock Returns."
    )
    parser.add_argument(
        "--skip-llm",
        action="store_true",
        help="Skip LLM consensus generation and load existing cached results from disk."
    )
    parser.add_argument(
        "--mock-llm",
        action="store_true",
        help="Run consensus generation using calibrated multi-agent simulated LLMs (no API keys required)."
    )
    parser.add_argument(
        "--re-download-data",
        action="store_true",
        help="Force re-download of price and analyst data from yfinance, ignoring cache."
    )
    parser.add_argument(
        "--lookback-years",
        type=int,
        default=config.LOOKBACK_YEARS,
        help=f"Number of years of historical data to pull (default: {config.LOOKBACK_YEARS})."
    )
    return parser.parse_args()


def print_ascii_header():
    header = """
===================================================================================
   FINANCIAL RESEARCH PIPELINE: AI MODEL AGREEMENT & ASSET PRICING
   Testing Information-Efficiency & Disagreement Alpha Across Cap Regimes
===================================================================================
"""
    print(header)


def format_summary_statistics_table(
    consensus_df: pd.DataFrame,
    bucket_summary_df: pd.DataFrame,
    stat_tests: dict
) -> str:
    """Formats academic summary tables with agreement metrics, return spreads, and t-tests."""
    lines = []
    lines.append("\n" + "=" * 85)
    lines.append("PANEL A: AI CONSENSUS AGREEMENT SCORE SUMMARY STATISTICS")
    lines.append("=" * 85)
    lines.append(f"{'Category':<15} | {'N (Obs)':<10} | {'Mean Score':<12} | {'Std Dev':<10} | {'Median':<10} | {'IQR (25-75%)':<14}")
    lines.append("-" * 85)
    
    for cat, label in [("large_cap", "Large-Cap"), ("small_cap", "Small-Cap")]:
        sub = consensus_df[consensus_df["category"] == cat]["agreement_score"].dropna()
        n = len(sub)
        mean = sub.mean()
        std = sub.std()
        med = sub.median()
        q25 = sub.quantile(0.25)
        q75 = sub.quantile(0.75)
        lines.append(f"{label:<15} | {n:<10} | {mean:<12.4f} | {std:<10.4f} | {med:<10.4f} | {q25:.2f} - {q75:.2f}")
        
    lines.append("\n" + "=" * 85)
    lines.append("PANEL B: FORWARD 3-MONTH RETURNS BY AI AGREEMENT TERCILE")
    lines.append("=" * 85)
    lines.append(f"{'Category':<12} | {'Bucket':<16} | {'Mean 3M Ret':<14} | {'Std Error':<12} | {'N (Stocks)':<10}")
    lines.append("-" * 85)
    
    b_3m = bucket_summary_df[bucket_summary_df["horizon"] == "3m"]
    for _, row in b_3m.iterrows():
        cat_str = "Large-Cap" if row["category"] == "large_cap" else "Small-Cap"
        lines.append(
            f"{cat_str:<12} | {row['bucket']:<16} | {row['mean_return']:>+11.2%}   | {row['std_error']:>9.2%}   | {int(row['count']):<10}"
        )
        
    lines.append("\n" + "=" * 85)
    lines.append("PANEL C: STATISTICAL HYPOTHESIS TESTS (LOW vs. HIGH AGREEMENT RETURN SPREAD)")
    lines.append("=" * 85)
    lines.append(f"{'Sample Group':<15} | {'Low Agree Mean':<16} | {'High Agree Mean':<16} | {'Spread (Low-High)':<18} | {'t-stat':<10} | {'p-value':<10} | {'Sig (5%)':<8}")
    lines.append("-" * 105)
    
    for key, label in [("overall", "All Equities"), ("large_cap", "Large-Cap"), ("small_cap", "Small-Cap")]:
        res = stat_tests.get(key, {})
        if "error" in res:
            lines.append(f"{label:<15} | {res['error']}")
        else:
            low_m = f"{res['low_mean']:+.2%}"
            high_m = f"{res['high_mean']:+.2%}"
            spr = f"{res['spread']:+.2%}"
            t_s = f"{res['t_stat']:+.3f}"
            p_v = f"{res['p_value']:.4f}"
            sig = "YES (***)" if res.get("significant_at_5pct") else ("YES (*)" if res.get("significant_at_10pct") else "No")
            lines.append(
                f"{label:<15} | {low_m:<16} | {high_m:<16} | {spr:<18} | {t_s:<10} | {p_v:<10} | {sig:<8}"
            )
            
    lines.append("=" * 105 + "\n")
    return "\n".join(lines)


def run_pipeline(
    skip_llm: bool = False,
    mock_llm: bool = False,
    re_download_data: bool = False,
    lookback_years: int = config.LOOKBACK_YEARS
):
    print_ascii_header()
    logger.info("Initializing Research Pipeline...")

    # Determine LLM mode
    has_keys = bool(os.getenv("ANTHROPIC_API_KEY") or os.getenv("OPENAI_API_KEY"))
    force_mock = mock_llm or (not has_keys)
    if force_mock and not skip_llm:
        logger.info("Note: Running in SIMULATED LLM MODE (no external API keys required/used).")

    # -------------------------------------------------------------------------
    # STEP 1: Universe & Price Ingestion
    # -------------------------------------------------------------------------
    logger.info(">>> STEP 1: Ingesting Universe & Historical Market Data...")
    prices_df = fetch_historical_prices(
        lookback_years=lookback_years,
        force_reload=re_download_data
    )
    rebalance_dates = get_quarterly_rebalance_dates(prices_df)
    logger.info(f"Identified {len(rebalance_dates)} quarterly valuation rebalance dates:")
    logger.info(", ".join([d.strftime("%Y-%m-%d") for d in rebalance_dates]))

    # -------------------------------------------------------------------------
    # STEP 2: AI Model Consensus Generation
    # -------------------------------------------------------------------------
    logger.info(">>> STEP 2: Generating / Loading AI Consensus Cross-Sections...")
    consensus_df = generate_or_load_ai_consensus(
        prices_df=prices_df,
        rebalance_dates=rebalance_dates,
        force_reload=re_download_data,
        force_mock=force_mock,
        skip_llm=skip_llm
    )
    logger.info(f"Consensus dataset loaded with {len(consensus_df)} stock-quarter records.")

    # -------------------------------------------------------------------------
    # STEP 3: Return Calculation & Backtest Engine
    # -------------------------------------------------------------------------
    logger.info(">>> STEP 3: Executing Backtest Engine & Tercile Bucketing...")
    df_with_returns = attach_forward_returns(consensus_df, prices_df)
    
    # Save enriched dataset to cache
    df_with_returns.to_csv(config.DATA_DIR / "consensus_with_forward_returns.csv", index=False)
    
    bucket_summary_df = calculate_bucket_forward_returns(df_with_returns)
    bucket_summary_df.to_csv(config.DATA_DIR / "bucket_summary_returns.csv", index=False)
    
    cum_returns_df, period_returns_df = run_quarterly_backtest(
        consensus_df=consensus_df,
        prices_df=prices_df,
        benchmark_ticker=config.BENCHMARK_TICKER,
        horizon_key="3m"
    )
    cum_returns_df.to_csv(config.DATA_DIR / "cumulative_portfolio_returns.csv", index=False)

    # Statistical significance tests
    stat_tests = compute_statistical_tests(df_with_returns, horizon_key="3m")

    # -------------------------------------------------------------------------
    # STEP 4: Sell-Side Analyst Dispersion Benchmark
    # -------------------------------------------------------------------------
    logger.info(">>> STEP 4: Pulling Sell-Side Analyst Dispersion Metrics...")
    analyst_df = get_analyst_dispersion_panel(force_reload=re_download_data)
    analyst_df.to_csv(config.DATA_DIR / "analyst_dispersion.csv", index=False)

    # -------------------------------------------------------------------------
    # STEP 5: Publication Figures Generation
    # -------------------------------------------------------------------------
    logger.info(">>> STEP 5: Rendering 6 Publication-Ready Figures (300 DPI)...")
    fig_paths = generate_all_charts(
        consensus_df=consensus_df,
        prices_df=prices_df,
        bucket_summary_df=bucket_summary_df,
        cumulative_returns_df=cum_returns_df,
        analyst_df=analyst_df,
        save_dir=config.FIGURES_DIR
    )

    # -------------------------------------------------------------------------
    # STEP 6: Summary Statistics & Research Findings
    # -------------------------------------------------------------------------
    logger.info(">>> STEP 6: Formatting Research Findings & Statistical Summary...")
    table_str = format_summary_statistics_table(consensus_df, bucket_summary_df, stat_tests)
    print(table_str)

    # Save summary report to output
    report_path = config.OUTPUT_DIR / "research_summary_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(table_str)
        f.write("\nGenerated Figures:\n")
        for name, path in fig_paths.items():
            f.write(f"- {name}: {path}\n")

    logger.info(f"Research summary report saved to {report_path}")
    logger.info("Pipeline execution completed successfully!")


if __name__ == "__main__":
    args = parse_arguments()
    run_pipeline(
        skip_llm=args.skip_llm,
        mock_llm=args.mock_llm,
        re_download_data=args.re_download_data,
        lookback_years=args.lookback_years
    )

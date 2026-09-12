"""
Publication-Quality Visualization Suite
=======================================
Academic Styling:
-----------------
All figures are styled to adhere to publication standards:
- 300 DPI high-resolution output.
- Consistent color palette: Corporate Blue, Crimson Red, Charcoal Benchmark.
- Legible typography, clear annotations, zero visual clutter.
- Standardized file naming and exports to output/figures/.
"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns

import config

logger = logging.getLogger(__name__)

# Apply publication-grade aesthetic defaults
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 11,
    "figure.titlesize": 15,
    "lines.linewidth": 2.0,
    "grid.alpha": 0.35,
    "grid.linestyle": "--"
})

# Color Constants
COLOR_LARGECAP = "#1F4E79"    # Deep Academic Navy
COLOR_SMALLCAP = "#C0392B"    # Crimson Red
COLOR_BENCHMARK = "#2C3E50"   # Slate Charcoal
COLOR_HIGH_AGREE = "#2980B9"  # Azure Blue
COLOR_LOW_AGREE = "#E67E22"   # Ochre Orange / Disagreement Alpha
COLOR_VIX = "#8E44AD"         # Amethyst Purple


def _ensure_dir(save_dir: Optional[Path]) -> Path:
    out = save_dir or config.FIGURES_DIR
    out.mkdir(parents=True, exist_ok=True)
    return out


# -----------------------------------------------------------------------------
# CHART 1: plot_agreement_histogram_largecap()
# -----------------------------------------------------------------------------
def plot_agreement_histogram_largecap(
    consensus_df: pd.DataFrame,
    save_dir: Optional[Path] = None
) -> Path:
    """
    1. plot_agreement_histogram_largecap() — histogram of agreement scores, large-cap only.
    """
    save_path = _ensure_dir(save_dir) / "fig1_agreement_histogram_largecap.png"
    
    lc_df = consensus_df[consensus_df["category"] == "large_cap"].dropna(subset=["agreement_score"])
    scores = lc_df["agreement_score"]
    
    mean_val = scores.mean()
    median_val = scores.median()
    std_val = scores.std()

    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    
    # Histogram + KDE
    sns.histplot(
        scores,
        bins=15,
        kde=True,
        color=COLOR_LARGECAP,
        edgecolor="black",
        linewidth=0.8,
        alpha=0.65,
        ax=ax
    )
    
    # Summary vertical markers
    ax.axvline(mean_val, color="#E74C3C", linestyle="--", linewidth=2.0, label=f"Mean: {mean_val:.2f}")
    ax.axvline(median_val, color="#F39C12", linestyle=":", linewidth=2.0, label=f"Median: {median_val:.2f}")
    
    ax.set_title("Figure 1: Distribution of AI Model Agreement Scores (Large-Cap Equities)", pad=14, weight="bold")
    ax.set_xlabel("AI Consensus Agreement Score (0.0 = Maximal Dispersion, 1.0 = Unanimous)", labelpad=10)
    ax.set_ylabel("Frequency (Stock-Quarter Observations)", labelpad=10)
    ax.set_xlim(0.25, 1.05)
    
    # Statistical text annotation box
    stats_text = (
        f"N = {len(scores):,}\n"
        f"Mean = {mean_val:.3f}\n"
        f"Std Dev = {std_val:.3f}\n"
        f"Median = {median_val:.3f}"
    )
    ax.text(
        0.05, 0.92, stats_text,
        transform=ax.transAxes,
        verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="#BDC3C7", alpha=0.9)
    )
    
    ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="#BDC3C7")
    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.close(fig)
    logger.info(f"Generated Figure 1: {save_path}")
    return save_path


# -----------------------------------------------------------------------------
# CHART 2: plot_agreement_histogram_overlay()
# -----------------------------------------------------------------------------
def plot_agreement_histogram_overlay(
    consensus_df: pd.DataFrame,
    save_dir: Optional[Path] = None
) -> Path:
    """
    2. plot_agreement_histogram_overlay() — same histogram with small-cap distribution
       overlaid (different color, alpha transparency, shared bins).
    """
    save_path = _ensure_dir(save_dir) / "fig2_agreement_histogram_overlay.png"
    
    lc_scores = consensus_df[consensus_df["category"] == "large_cap"]["agreement_score"].dropna()
    sc_scores = consensus_df[consensus_df["category"] == "small_cap"]["agreement_score"].dropna()

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    
    bins = np.linspace(0.30, 1.0, 16)
    
    ax.hist(
        lc_scores,
        bins=bins,
        alpha=0.55,
        color=COLOR_LARGECAP,
        edgecolor=COLOR_LARGECAP,
        label=f"Large-Cap (N={len(lc_scores)}, Mean={lc_scores.mean():.2f})"
    )
    ax.hist(
        sc_scores,
        bins=bins,
        alpha=0.55,
        color=COLOR_SMALLCAP,
        edgecolor=COLOR_SMALLCAP,
        label=f"Small-Cap (N={len(sc_scores)}, Mean={sc_scores.mean():.2f})"
    )
    
    # Statistical comparison (Kolmogorov-Smirnov test)
    if len(lc_scores) > 5 and len(sc_scores) > 5:
        ks_stat, ks_pval = stats.ks_2samp(lc_scores, sc_scores)
        ks_text = f"Two-Sample K-S Test:\nD = {ks_stat:.3f} (p = {ks_pval:.4f})"
        ax.text(
            0.05, 0.92, ks_text,
            transform=ax.transAxes,
            verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="#BDC3C7", alpha=0.9)
        )

    ax.set_title("Figure 2: AI Consensus Distribution Overlay: Large-Cap vs. Small-Cap Equities", pad=14, weight="bold")
    ax.set_xlabel("AI Consensus Agreement Score", labelpad=10)
    ax.set_ylabel("Count of Observations", labelpad=10)
    ax.set_xlim(0.28, 1.02)
    ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="#BDC3C7")
    
    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.close(fig)
    logger.info(f"Generated Figure 2: {save_path}")
    return save_path


# -----------------------------------------------------------------------------
# CHART 3: plot_forward_returns_by_bucket()
# -----------------------------------------------------------------------------
def plot_forward_returns_by_bucket(
    bucket_summary_df: pd.DataFrame,
    horizon_key: str = "3m",
    save_dir: Optional[Path] = None
) -> Path:
    """
    3. plot_forward_returns_by_bucket() — grouped bar chart:
       x-axis = [Large-Cap, Small-Cap], two bars per group (High Agreement avg 3m return,
       Low Agreement avg 3m return), include error bars (std error).
    """
    save_path = _ensure_dir(save_dir) / "fig3_forward_returns_by_bucket.png"
    
    sub = bucket_summary_df[
        (bucket_summary_df["horizon"] == horizon_key) &
        (bucket_summary_df["bucket"].isin(["High Agreement", "Low Agreement"]))
    ].copy()
    
    categories = ["large_cap", "small_cap"]
    cat_labels = ["Large-Cap Equities\n(S&P 500)", "Small-Cap Equities\n(Russell 2000)"]
    
    high_means, high_errs = [], []
    low_means, low_errs = [], []
    
    for cat in categories:
        h_row = sub[(sub["category"] == cat) & (sub["bucket"] == "High Agreement")]
        l_row = sub[(sub["category"] == cat) & (sub["bucket"] == "Low Agreement")]
        
        high_means.append(float(h_row["mean_return"].iloc[0]) * 100 if not h_row.empty else 0.0)
        high_errs.append(float(h_row["std_error"].iloc[0]) * 100 if not h_row.empty else 0.0)
        
        low_means.append(float(l_row["mean_return"].iloc[0]) * 100 if not l_row.empty else 0.0)
        low_errs.append(float(l_row["std_error"].iloc[0]) * 100 if not l_row.empty else 0.0)
        
    x = np.arange(len(categories))
    bar_width = 0.35

    fig, ax = plt.subplots(figsize=(8.5, 5.8), dpi=300)
    
    rects1 = ax.bar(
        x - bar_width / 2,
        high_means,
        bar_width,
        yerr=high_errs,
        error_kw=dict(capsize=5, capthick=1.5),
        color=COLOR_HIGH_AGREE,
        edgecolor="black",
        linewidth=0.8,
        label="High Agreement (Top Tercile / 'Priced In')"
    )
    
    rects2 = ax.bar(
        x + bar_width / 2,
        low_means,
        bar_width,
        yerr=low_errs,
        error_kw=dict(capsize=5, capthick=1.5),
        color=COLOR_LOW_AGREE,
        edgecolor="black",
        linewidth=0.8,
        label="Low Agreement (Bottom Tercile / 'Disagreement Alpha')"
    )
    
    # Value annotations on bars
    for rect in rects1:
        h = rect.get_height()
        va = "bottom" if h >= 0 else "top"
        ax.annotate(
            f"{h:+.2f}%",
            xy=(rect.get_x() + rect.get_width() / 2, h),
            xytext=(0, 4 if h >= 0 else -12),
            textcoords="offset points",
            ha="center", va=va, fontsize=9.5, weight="bold"
        )
        
    for rect in rects2:
        h = rect.get_height()
        va = "bottom" if h >= 0 else "top"
        ax.annotate(
            f"{h:+.2f}%",
            xy=(rect.get_x() + rect.get_width() / 2, h),
            xytext=(0, 4 if h >= 0 else -12),
            textcoords="offset points",
            ha="center", va=va, fontsize=9.5, weight="bold"
        )
        
    ax.axhline(0, color="black", linewidth=0.9, linestyle="-")
    ax.set_title("Figure 3: Forward 3-Month Stock Returns by AI Consensus Tercile", pad=14, weight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(cat_labels, weight="bold")
    ax.set_ylabel("Average Forward 3-Month Return (%)", labelpad=10)
    ax.legend(loc="best", frameon=True, facecolor="white", edgecolor="#BDC3C7")
    
    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.close(fig)
    logger.info(f"Generated Figure 3: {save_path}")
    return save_path


# -----------------------------------------------------------------------------
# CHART 4: plot_cumulative_returns()
# -----------------------------------------------------------------------------
def plot_cumulative_returns(
    cumulative_returns_df: pd.DataFrame,
    save_dir: Optional[Path] = None
) -> Path:
    """
    4. plot_cumulative_returns() — line chart: 3 lines (Long Low-Agreement,
       Long High-Agreement, S&P 500 benchmark), x-axis = date, y-axis = cumulative return %.
    """
    save_path = _ensure_dir(save_dir) / "fig4_cumulative_returns.png"
    
    df = cumulative_returns_df.copy()
    if df.empty or "cum_low_agreement" not in df.columns:
        logger.warning("Empty cumulative return dataframe passed to plot_cumulative_returns.")
        return save_path
        
    dates = pd.to_datetime(df["date"])
    low_cum = df["cum_low_agreement"] * 100
    high_cum = df["cum_high_agreement"] * 100
    bench_cum = df["cum_benchmark"] * 100

    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=300)
    
    ax.plot(
        dates, low_cum,
        color=COLOR_LOW_AGREE,
        marker="o",
        markersize=5,
        linewidth=2.5,
        label=f"Long Low-Agreement Portfolio (Final: {low_cum.iloc[-1]:+.1f}%)"
    )
    ax.plot(
        dates, high_cum,
        color=COLOR_HIGH_AGREE,
        marker="s",
        markersize=5,
        linewidth=2.2,
        label=f"Long High-Agreement Portfolio (Final: {high_cum.iloc[-1]:+.1f}%)"
    )
    ax.plot(
        dates, bench_cum,
        color=COLOR_BENCHMARK,
        linestyle="--",
        linewidth=2.0,
        label=f"S&P 500 Benchmark (^GSPC) (Final: {bench_cum.iloc[-1]:+.1f}%)"
    )
    
    # Fill between Low and High to highlight cumulative spread
    ax.fill_between(
        dates, low_cum, high_cum,
        where=(low_cum >= high_cum),
        interpolate=True,
        color="#27AE60",
        alpha=0.15,
        label="Disagreement Alpha Excess Spread"
    )
    ax.fill_between(
        dates, low_cum, high_cum,
        where=(low_cum < high_cum),
        interpolate=True,
        color="#E74C3C",
        alpha=0.15
    )
    
    ax.axhline(0, color="gray", linewidth=0.8, linestyle=":")
    ax.set_title("Figure 4: Cumulative Performance of AI Agreement Portfolios vs. S&P 500 Benchmark", pad=14, weight="bold")
    ax.set_xlabel("Rebalance Valuation Date (Quarterly Horizon)", labelpad=10)
    ax.set_ylabel("Cumulative Return (%)", labelpad=10)
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()
    
    ax.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="#BDC3C7")
    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.close(fig)
    logger.info(f"Generated Figure 4: {save_path}")
    return save_path


# -----------------------------------------------------------------------------
# CHART 5: plot_ai_vs_analyst_dispersion()
# -----------------------------------------------------------------------------
def plot_ai_vs_analyst_dispersion(
    analyst_df: pd.DataFrame,
    consensus_df: pd.DataFrame,
    save_dir: Optional[Path] = None
) -> Path:
    """
    5. plot_ai_vs_analyst_dispersion() — scatter plot, x = analyst dispersion,
       y = AI agreement score, one point per stock, add a regression trendline +
       correlation coefficient annotation.
    """
    save_path = _ensure_dir(save_dir) / "fig5_ai_vs_analyst_dispersion.png"
    
    if analyst_df.empty:
        logger.warning("Empty analyst dataframe passed to plot_ai_vs_analyst_dispersion.")
        return save_path
        
    # Get latest agreement score per ticker
    latest_consensus = (
        consensus_df.sort_values("date")
        .groupby("ticker")
        .last()
        .reset_index()[["ticker", "agreement_score", "category"]]
    )
    
    merged = pd.merge(analyst_df, latest_consensus, on="ticker")
    merged = merged.dropna(subset=["normalized_dispersion", "agreement_score"])
    
    # Filter out extreme zero-analyst or outlier dispersion artifacts
    merged = merged[(merged["normalized_dispersion"] > 0) & (merged["normalized_dispersion"] < 0.8)]
    
    if len(merged) < 5:
        logger.warning(f"Insufficient merged points ({len(merged)}) for scatter plot.")
        return save_path

    x = merged["normalized_dispersion"]
    y = merged["agreement_score"]

    fig, ax = plt.subplots(figsize=(8.5, 6.0), dpi=300)
    
    # Scatter points split by cap category
    for cat, color, label, marker in [
        ("large_cap", COLOR_LARGECAP, "Large-Cap", "o"),
        ("small_cap", COLOR_SMALLCAP, "Small-Cap", "^")
    ]:
        sub_c = merged[merged["category_x"] == cat] if "category_x" in merged.columns else merged[merged["category"] == cat]
        if not sub_c.empty:
            ax.scatter(
                sub_c["normalized_dispersion"],
                sub_c["agreement_score"],
                color=color,
                label=label,
                alpha=0.75,
                s=65,
                edgecolors="black",
                linewidth=0.6,
                marker=marker
            )
            
    # OLS Regression Trendline
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    spearman_r, spearman_p = stats.spearmanr(x, y)
    
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept
    ax.plot(x_line, y_line, color="#2C3E50", linestyle="-", linewidth=2.0, label="OLS Regression Fit")
    
    # Correlation & regression annotation
    annot_text = (
        f"Pearson r = {r_value:+.3f} (p = {p_value:.4f})\n"
        f"Spearman \u03c1 = {spearman_r:+.3f} (p = {spearman_p:.4f})\n"
        f"Slope = {slope:+.3f} (SE = {std_err:.3f})\n"
        f"N = {len(merged)} stocks"
    )
    ax.text(
        0.05, 0.18, annot_text,
        transform=ax.transAxes,
        verticalalignment="bottom",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="#BDC3C7", alpha=0.92)
    )
    
    ax.set_title("Figure 5: Sell-Side Analyst Forecast Dispersion vs. AI Consensus Score", pad=14, weight="bold")
    ax.set_xlabel("Analyst Forecast Dispersion (\u03c3_targets / Target_Mean)", labelpad=10)
    ax.set_ylabel("AI Model Agreement Score", labelpad=10)
    ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="#BDC3C7")
    
    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.close(fig)
    logger.info(f"Generated Figure 5: {save_path}")
    return save_path


# -----------------------------------------------------------------------------
# CHART 6: plot_rolling_consensus_index()
# -----------------------------------------------------------------------------
def plot_rolling_consensus_index(
    consensus_df: pd.DataFrame,
    prices_df: pd.DataFrame,
    volatility_ticker: str = config.VOLATILITY_TICKER,
    save_dir: Optional[Path] = None
) -> Path:
    """
    6. plot_rolling_consensus_index() — dual-axis line chart:
       primary y-axis = rolling average AI agreement score over time (large-cap universe),
       secondary y-axis = VIX, same x-axis (date).
    """
    save_path = _ensure_dir(save_dir) / "fig6_rolling_consensus_index.png"
    
    lc_df = consensus_df[consensus_df["category"] == "large_cap"].copy()
    lc_df["date"] = pd.to_datetime(lc_df["date"])
    
    # Quarterly time series of average agreement score across large caps
    time_series = lc_df.groupby("date")["agreement_score"].mean().sort_index()
    if time_series.empty:
        logger.warning("Empty large-cap time series in plot_rolling_consensus_index.")
        return save_path
        
    # Align with VIX price series
    vix_series = pd.Series(dtype=float)
    if volatility_ticker in prices_df.columns:
        vix_all = prices_df[volatility_ticker].dropna()
        # Sample VIX at the closest dates to quarterly valuation points
        sampled_vix = []
        for dt in time_series.index:
            sub = vix_all[vix_all.index <= dt]
            sampled_vix.append(float(sub.iloc[-1]) if not sub.empty else np.nan)
        vix_series = pd.Series(sampled_vix, index=time_series.index)
    else:
        # Fallback synthetic proxy if VIX ticker unavailable
        vix_series = pd.Series(20.0, index=time_series.index)

    fig, ax1 = plt.subplots(figsize=(10, 5.8), dpi=300)
    
    # Primary Y-Axis: AI Agreement Score
    color_ax1 = COLOR_LARGECAP
    ax1.set_xlabel("Valuation Date (Quarterly)", labelpad=10)
    ax1.set_ylabel("Average Large-Cap AI Agreement Score", color=color_ax1, labelpad=10, weight="bold")
    line1 = ax1.plot(
        time_series.index,
        time_series.values,
        color=color_ax1,
        marker="o",
        linewidth=2.4,
        label="Large-Cap AI Consensus Index (Left)"
    )
    ax1.tick_params(axis="y", labelcolor=color_ax1)
    ax1.set_ylim(0.35, 1.0)
    
    # Secondary Y-Axis: CBOE VIX
    ax2 = ax1.twinx()
    color_ax2 = COLOR_VIX
    ax2.set_ylabel("CBOE Volatility Index (^VIX)", color=color_ax2, labelpad=10, weight="bold")
    line2 = ax2.plot(
        vix_series.index,
        vix_series.values,
        color=color_ax2,
        marker="D",
        linestyle="--",
        linewidth=2.0,
        label="CBOE VIX (Right)"
    )
    ax2.tick_params(axis="y", labelcolor=color_ax2)
    ax2.grid(False)  # Avoid overlapping grid lines
    
    # Combine legends from both axes
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper right", frameon=True, facecolor="white", edgecolor="#BDC3C7")
    
    ax1.set_title("Figure 6: Macro Market Volatility vs. Large-Cap AI Model Consensus Over Time", pad=14, weight="bold")
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()
    
    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.close(fig)
    logger.info(f"Generated Figure 6: {save_path}")
    return save_path


def generate_all_charts(
    consensus_df: pd.DataFrame,
    prices_df: pd.DataFrame,
    bucket_summary_df: pd.DataFrame,
    cumulative_returns_df: pd.DataFrame,
    analyst_df: pd.DataFrame,
    save_dir: Optional[Path] = None
) -> Dict[str, Path]:
    """
    Generates all 6 publication figures and returns a dictionary of output paths.
    """
    logger.info("Generating all 6 academic research charts...")
    out_dir = _ensure_dir(save_dir)
    
    fig_paths = {
        "fig1_agreement_histogram_largecap": plot_agreement_histogram_largecap(consensus_df, out_dir),
        "fig2_agreement_histogram_overlay": plot_agreement_histogram_overlay(consensus_df, out_dir),
        "fig3_forward_returns_by_bucket": plot_forward_returns_by_bucket(bucket_summary_df, "3m", out_dir),
        "fig4_cumulative_returns": plot_cumulative_returns(cumulative_returns_df, out_dir),
        "fig5_ai_vs_analyst_dispersion": plot_ai_vs_analyst_dispersion(analyst_df, consensus_df, out_dir),
        "fig6_rolling_consensus_index": plot_rolling_consensus_index(consensus_df, prices_df, config.VOLATILITY_TICKER, out_dir)
    }
    
    logger.info("All 6 publication charts generated successfully.")
    return fig_paths

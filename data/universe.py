"""
Universe Definition Module
==========================
Academic Rationale:
-------------------
In financial economics and efficient market hypothesis (EMH) literature, information
efficiency is hypothesized to be a function of analyst and media coverage:
1. Large-Cap Universe (S&P 500 constituents): Heavily covered by dozens of sell-side
   equity research analysts, quant desks, and financial news agencies. Here, AI consensus
   may primarily reflect public common knowledge, making high consensus a sign of an
   asset being "fully priced in" (potential exhaustion of excess returns).
2. Small-Cap Universe (Russell 2000 constituents): Characterized by thinner coverage,
   higher information asymmetry, and idiosyncratic retail flow. In this regime, AI
   consensus might extract genuine synthesis of under-researched signals, or conversely,
   sharp model disagreement may indicate high unpriced uncertainty and potential alpha.

This module provides hardcoded, curated lists of 30 large-cap and 30 small-cap equities
alongside market index overlays (^GSPC for S&P 500, ^VIX for implied volatility).
"""

from typing import Dict, List
import pandas as pd
import config


def get_large_cap_tickers() -> List[str]:
    """Returns the list of 30 hardcoded S&P 500 large-cap tickers."""
    return list(config.LARGE_CAP_TICKERS)


def get_small_cap_tickers() -> List[str]:
    """Returns the list of 30 hardcoded Russell 2000 small-cap tickers."""
    return list(config.SMALL_CAP_TICKERS)


def get_all_equity_tickers() -> List[str]:
    """Returns all 60 equity tickers across both market-cap regimes."""
    return get_large_cap_tickers() + get_small_cap_tickers()


def get_benchmark_tickers() -> List[str]:
    """Returns benchmark index and volatility tickers (^GSPC, ^VIX)."""
    return [config.BENCHMARK_TICKER, config.VOLATILITY_TICKER]


def get_ticker_category(ticker: str) -> str:
    """
    Returns the market-cap category for a given ticker symbol.
    
    Parameters
    ----------
    ticker : str
        Stock ticker symbol.
        
    Returns
    -------
    str
        'large_cap', 'small_cap', or 'benchmark'
    """
    t = ticker.upper()
    if t in config.LARGE_CAP_TICKERS:
        return "large_cap"
    elif t in config.SMALL_CAP_TICKERS:
        return "small_cap"
    elif t in [config.BENCHMARK_TICKER, config.VOLATILITY_TICKER]:
        return "benchmark"
    else:
        return "unknown"


def get_universe_metadata() -> pd.DataFrame:
    """
    Generates a structured metadata DataFrame for all tickers in the study.
    
    Returns
    -------
    pd.DataFrame
        Table with columns: ['ticker', 'category', 'benchmark_flag']
    """
    records = []
    for ticker in config.LARGE_CAP_TICKERS:
        records.append({"ticker": ticker, "category": "large_cap", "is_benchmark": False})
    for ticker in config.SMALL_CAP_TICKERS:
        records.append({"ticker": ticker, "category": "small_cap", "is_benchmark": False})
    for ticker in [config.BENCHMARK_TICKER, config.VOLATILITY_TICKER]:
        records.append({"ticker": ticker, "category": "benchmark", "is_benchmark": True})
        
    df = pd.DataFrame(records)
    return df

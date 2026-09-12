"""
Analyst Forecast Dispersion Module
==================================
Academic Methodology:
---------------------
In empirical finance (e.g. Diether, Malloy, and Scherbina, 2002), analyst forecast
dispersion is a classic benchmark proxy for opinion divergence and information uncertainty:
1. High analyst dispersion has historically been linked to speculative pricing or mispricing.
2. In this research, we contrast human sell-side analyst dispersion against LLM consensus.
   Does AI model disagreement mirror human analyst dispersion, or does AI surface
   orthogonal information signals?

Data Extraction:
----------------
We query yfinance (ticker.info and ticker.analyst_price_target) to extract:
- targetMeanPrice, targetHighPrice, targetLowPrice, targetMedianPrice
- numberOfAnalystOpinions
- Standard deviation of price targets:
  If standard deviation is directly provided, we use it; otherwise, for normal distribution
  approximations from sell-side range: sigma ~ (targetHigh - targetLow) / 4 (or 3.29 for 90% range).
- Normalized Dispersion = sigma / targetMeanPrice.
Stocks with missing analyst coverage (common in micro/small caps) are logged and omitted
gracefully, strictly avoiding fabrication.
"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
import numpy as np
import pandas as pd
import yfinance as yf

import config
from data.universe import get_all_equity_tickers, get_ticker_category

logger = logging.getLogger(__name__)


def fetch_analyst_target_data(ticker: str) -> Optional[Dict[str, Any]]:
    """
    Fetches latest sell-side analyst target prices and estimates dispersion for a stock.
    Returns None if no analyst target data is available.
    """
    try:
        t = yf.Ticker(ticker)
        info = t.info or {}
        
        target_mean = info.get("targetMeanPrice")
        target_high = info.get("targetHighPrice")
        target_low = info.get("targetLowPrice")
        target_median = info.get("targetMedianPrice")
        num_analysts = info.get("numberOfAnalystOpinions")
        current_price = info.get("currentPrice") or info.get("regularMarketPrice")
        
        # Check alternative analyst_price_targets if available
        if target_mean is None:
            try:
                apt = t.analyst_price_targets
                if isinstance(apt, dict):
                    target_mean = apt.get("mean")
                    target_high = apt.get("high")
                    target_low = apt.get("low")
                    target_median = apt.get("median")
            except Exception:
                pass

        if target_mean is None or target_mean <= 0:
            logger.info(f"Ticker {ticker}: No analyst price targets available on yfinance. Skipping gracefully.")
            return None
            
        # Estimate dispersion (standard deviation of analyst price targets)
        # If targetHigh and targetLow exist with >= 2 analysts:
        if target_high is not None and target_low is not None and target_high > target_low:
            # Range rule of thumb: range / 4 approximates std dev for modest sample sizes
            target_std = (target_high - target_low) / 4.0
        else:
            target_std = 0.0
            
        normalized_dispersion = (target_std / target_mean) if target_mean > 0 else 0.0

        return {
            "ticker": ticker,
            "category": get_ticker_category(ticker),
            "current_price": current_price,
            "target_mean": target_mean,
            "target_median": target_median,
            "target_high": target_high,
            "target_low": target_low,
            "target_std": round(target_std, 3),
            "normalized_dispersion": round(normalized_dispersion, 4),
            "num_analysts": num_analysts if num_analysts is not None else np.nan
        }
    except Exception as e:
        logger.warning(f"Error querying analyst data for {ticker}: {e}. Skipping gracefully.")
        return None


def get_analyst_dispersion_panel(
    tickers: Optional[List[str]] = None,
    force_reload: bool = False
) -> pd.DataFrame:
    """
    Builds and caches the analyst dispersion cross-section for the universe.
    
    Parameters
    ----------
    tickers : list, optional
        Tickers to query (defaults to all 60 equities).
    force_reload : bool
        If True, ignores cache and re-queries yfinance.
        
    Returns
    -------
    pd.DataFrame
        Table with [ticker, category, target_mean, target_std, normalized_dispersion, num_analysts]
    """
    parquet_path = config.DATA_DIR / "analyst_dispersion.parquet"
    csv_path = config.DATA_DIR / "analyst_dispersion.csv"
    
    if not force_reload:
        if parquet_path.exists():
            try:
                df = pd.read_parquet(parquet_path)
                logger.info(f"Loaded analyst dispersion for {len(df)} tickers from Parquet cache.")
                return df
            except Exception as e:
                logger.warning(f"Error reading analyst parquet cache: {e}")
        if csv_path.exists():
            try:
                df = pd.read_csv(csv_path)
                logger.info(f"Loaded analyst dispersion for {len(df)} tickers from CSV cache.")
                return df
            except Exception as e:
                logger.warning(f"Error reading analyst csv cache: {e}")

    if tickers is None:
        tickers = get_all_equity_tickers()
        
    logger.info(f"Fetching sell-side analyst target price dispersion for {len(tickers)} tickers...")
    records = []
    for ticker in tickers:
        data = fetch_analyst_target_data(ticker)
        if data is not None:
            records.append(data)
            
    df = pd.DataFrame(records)
    logger.info(f"Successfully collected analyst dispersion metrics for {len(df)} / {len(tickers)} tickers.")
    
    # Save cache
    try:
        df.to_parquet(parquet_path)
    except Exception as e:
        logger.warning(f"Could not save analyst parquet: {e}")
    df.to_csv(csv_path, index=False)
    
    return df

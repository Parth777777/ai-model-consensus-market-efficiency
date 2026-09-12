"""
Price Data Ingestion and Return Engineering Module
==================================================
Academic Rationale:
-------------------
To test asset pricing and information efficiency rigorously, price series must be:
1. Adjusted for splits, dividends, and corporate actions (yfinance Adjusted Close).
2. Cleanly aligned across all trading dates to prevent lookahead bias.
3. Formatted to compute forward multi-horizon holding period returns (1m = 21 trading days,
   3m = 63 trading days, 6m = 126 trading days) relative to quarterly consensus evaluation dates.
4. Cached locally to ensure exact reproducibility across multiple runs without
   relying on live network connections or hitting rate limits.
"""

from datetime import datetime, timedelta
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
import yfinance as yf

import config
from data.universe import get_all_equity_tickers, get_benchmark_tickers

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")


def get_prices_cache_path(name: str = "historical_prices") -> Path:
    """Returns the parquet/csv cache file path."""
    return config.DATA_DIR / f"{name}.parquet"


def fetch_historical_prices(
    tickers: Optional[List[str]] = None,
    lookback_years: int = config.LOOKBACK_YEARS,
    force_reload: bool = False,
    cache_name: str = "historical_prices"
) -> pd.DataFrame:
    """
    Downloads and caches historical daily adjusted close prices for given tickers.
    
    Parameters
    ----------
    tickers : Optional[List[str]]
        List of stock tickers. If None, defaults to all 60 equities + benchmark tickers.
    lookback_years : int
        Number of years of historical data to pull.
    force_reload : bool
        If True, ignores existing cache and re-downloads from yfinance.
    cache_name : str
        Filename stem for local cache.
        
    Returns
    -------
    pd.DataFrame
        DataFrame with DateTimeIndex and ticker symbols as columns (Adjusted Close).
    """
    parquet_path = config.DATA_DIR / f"{cache_name}.parquet"
    csv_path = config.DATA_DIR / f"{cache_name}.csv"
    
    # Check if local cache already exists
    if not force_reload:
        if parquet_path.exists():
            try:
                df = pd.read_parquet(parquet_path)
                logger.info(f"Loaded {df.shape[1]} tickers across {len(df)} days from Parquet cache.")
                return df
            except Exception as e:
                logger.warning(f"Failed to read parquet cache ({e}). Trying CSV fallback...")
        if csv_path.exists():
            try:
                df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
                logger.info(f"Loaded {df.shape[1]} tickers from CSV cache.")
                return df
            except Exception as e:
                logger.warning(f"Failed to read CSV cache ({e}). Re-downloading...")

    if tickers is None:
        tickers = get_all_equity_tickers() + get_benchmark_tickers()

    end_date = datetime.now()
    start_date = end_date - timedelta(days=int(lookback_years * 365.25 + 30))
    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")

    logger.info(f"Downloading historical daily prices for {len(tickers)} tickers ({start_str} to {end_str})...")
    
    # yfinance batch download
    try:
        raw_data = yf.download(
            tickers=tickers,
            start=start_str,
            end=end_str,
            interval="1d",
            auto_adjust=False,
            progress=False,
            threads=True
        )
    except Exception as e:
        logger.error(f"yfinance batch download encountered an error: {e}")
        raw_data = pd.DataFrame()

    prices_dict: Dict[str, pd.Series] = {}

    if isinstance(raw_data, pd.DataFrame) and not raw_data.empty:
        # Check if MultiIndex columns exist (Price, Ticker)
        if isinstance(raw_data.columns, pd.MultiIndex):
            if "Adj Close" in raw_data.columns.levels[0]:
                adj_close_df = raw_data["Adj Close"]
            elif "Close" in raw_data.columns.levels[0]:
                adj_close_df = raw_data["Close"]
            else:
                adj_close_df = pd.DataFrame()
            
            for ticker in tickers:
                if ticker in adj_close_df.columns:
                    series = adj_close_df[ticker].dropna()
                    if len(series) > 50:  # Minimum viable trading history
                        prices_dict[ticker] = series
                    else:
                        logger.warning(f"Ticker {ticker} returned insufficient price points ({len(series)}).")
        elif "Adj Close" in raw_data.columns:
            # Single ticker case
            ticker = tickers[0]
            prices_dict[ticker] = raw_data["Adj Close"].dropna()

    # Individual fallback for any missing tickers
    missing_tickers = [t for t in tickers if t not in prices_dict]
    if missing_tickers:
        logger.info(f"Retrying {len(missing_tickers)} tickers individually...")
        for ticker in missing_tickers:
            try:
                hist = yf.Ticker(ticker).history(start=start_str, end=end_str, auto_adjust=False)
                if not hist.empty:
                    close_col = "Adj Close" if "Adj Close" in hist.columns else "Close"
                    series = hist[close_col].dropna()
                    if len(series) > 50:
                        prices_dict[ticker] = series
                    else:
                        logger.warning(f"Ticker {ticker} skipped: insufficient history ({len(series)} points).")
                else:
                    logger.warning(f"Ticker {ticker} returned empty history (possibly delisted). Skipping gracefully.")
            except Exception as ex:
                logger.warning(f"Error fetching {ticker}: {ex}. Skipping ticker gracefully.")

    if not prices_dict:
        raise ValueError("Could not download price data for any ticker. Check internet connection or ticker list.")

    combined_df = pd.DataFrame(prices_dict)
    combined_df.sort_index(inplace=True)
    combined_df.index = pd.to_datetime(combined_df.index).tz_localize(None)

    # Save to local cache
    try:
        combined_df.to_parquet(parquet_path)
        logger.info(f"Successfully cached prices to {parquet_path}")
    except Exception as e:
        logger.warning(f"Could not save to Parquet ({e}). Saving to CSV...")
        combined_df.to_csv(csv_path)

    return combined_df


def get_forward_return(
    prices_df: pd.DataFrame,
    ticker: str,
    as_of_date: Union[str, pd.Timestamp, datetime],
    horizon_days: int
) -> Optional[float]:
    """
    Computes forward percentage return for a stock over a given trading-day horizon.
    
    Parameters
    ----------
    prices_df : pd.DataFrame
        Daily adjusted close price matrix (Date index x Tickers).
    ticker : str
        Stock ticker symbol.
    as_of_date : str or Timestamp or datetime
        Reference date (t0).
    horizon_days : int
        Number of forward trading days (e.g. 21, 63, 126).
        
    Returns
    -------
    Optional[float]
        Forward return as a decimal (e.g. 0.052 for +5.2%), or None if data insufficient.
    """
    if ticker not in prices_df.columns:
        return None
        
    s = prices_df[ticker].dropna()
    if s.empty:
        return None
        
    dt = pd.to_datetime(as_of_date).tz_localize(None)
    sub = s[s.index >= dt]
    if len(sub) <= horizon_days:
        return None
        
    p0 = sub.iloc[0]
    p_future = sub.iloc[horizon_days]
    
    if p0 <= 0 or np.isnan(p0) or np.isnan(p_future):
        return None
        
    ret = float((p_future - p0) / p0)
    return ret


def get_multi_horizon_forward_returns(
    prices_df: pd.DataFrame,
    ticker: str,
    as_of_date: Union[str, pd.Timestamp, datetime]
) -> Dict[str, Optional[float]]:
    """
    Computes forward returns at 1m (21d), 3m (63d), and 6m (126d) horizons.
    """
    return {
        label: get_forward_return(prices_df, ticker, as_of_date, days)
        for label, days in config.FORWARD_HORIZONS.items()
    }


def get_recent_price_context(
    prices_df: pd.DataFrame,
    ticker: str,
    as_of_date: Union[str, pd.Timestamp, datetime]
) -> Dict[str, Union[float, str]]:
    """
    Extracts trailing price dynamics (momentum, annualized volatility, current price)
    as of a specified date to supply empirical context to LLM consensus prompts.
    """
    if ticker not in prices_df.columns:
        return {"current_price": "N/A", "mom_1m": "N/A", "mom_3m": "N/A", "vol_30d": "N/A"}
        
    s = prices_df[ticker].dropna()
    dt = pd.to_datetime(as_of_date).tz_localize(None)
    hist = s[s.index <= dt]
    
    if len(hist) < 22:
        return {"current_price": "N/A", "mom_1m": "N/A", "mom_3m": "N/A", "vol_30d": "N/A"}
        
    current_price = float(hist.iloc[-1])
    p_21d = float(hist.iloc[-21]) if len(hist) >= 21 else current_price
    p_63d = float(hist.iloc[-63]) if len(hist) >= 63 else p_21d
    
    mom_1m = (current_price - p_21d) / p_21d if p_21d > 0 else 0.0
    mom_3m = (current_price - p_63d) / p_63d if p_63d > 0 else 0.0
    
    # 30-day realized volatility annualized
    pct_changes = hist.pct_change().dropna()
    window = pct_changes.iloc[-30:] if len(pct_changes) >= 30 else pct_changes
    vol_30d = float(window.std() * np.sqrt(252)) if len(window) > 5 else 0.0
    
    return {
        "current_price": round(current_price, 2),
        "mom_1m": f"{mom_1m:+.1%}",
        "mom_3m": f"{mom_3m:+.1%}",
        "vol_30d": f"{vol_30d:.1%}"
    }


def get_quarterly_rebalance_dates(
    prices_df: pd.DataFrame,
    start_date: Optional[Union[str, datetime]] = None,
    end_date: Optional[Union[str, datetime]] = None
) -> List[pd.Timestamp]:
    """
    Determines quarterly rebalancing dates aligned to actual trading days.
    Usually spaced every ~63 trading days (calendar quarter-ends: March, June, September, December).
    """
    dates = prices_df.index.sort_values()
    if start_date:
        dates = dates[dates >= pd.to_datetime(start_date)]
    if end_date:
        dates = dates[dates <= pd.to_datetime(end_date)]
        
    # Resample to quarterly frequency and find the last active trading day of each quarter
    series = pd.Series(1, index=dates)
    quarterly_last_days = series.resample("QE").last().dropna().index
    
    # Map to actual available trading days in the dataset
    valid_rebalance_dates: List[pd.Timestamp] = []
    for q_dt in quarterly_last_days:
        sub = dates[dates <= q_dt]
        if not sub.empty:
            valid_rebalance_dates.append(sub[-1])
            
    # Remove the very last date if it has no forward 3m data
    if valid_rebalance_dates:
        last_dt = valid_rebalance_dates[-1]
        remaining = dates[dates > last_dt]
        if len(remaining) < config.FORWARD_HORIZONS["3m"]:
            valid_rebalance_dates.pop()
            
    return valid_rebalance_dates

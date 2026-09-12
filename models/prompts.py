"""
Financial Context Prompt Construction Module
============================================
Academic Rationale:
-------------------
To simulate how multiple independent financial models or human research analysts
form investment recommendations, prompts must provide a standardized information set
reflecting public information available at time t0 (to avoid lookahead bias):
1. Recent Price Action & Volatility (1-month, 3-month momentum, 30-day realized volatility).
2. Fundamental Earnings Metrics (revenue and EPS growth or surprise).
3. Qualitative News Context (stubbed modularly for plug-in news APIs).

Models are instructed to output strict, machine-parseable JSON containing:
- Recommendation call: "buy" | "hold" | "sell"
- 12-month Target Price: float
- Investment Thesis: exactly one concise sentence summarizing the primary driver.
"""

from datetime import datetime
import json
import logging
from typing import Any, Dict, List, Optional, Union
import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are an academic quantitative researcher evaluating historical market information for an empirical asset pricing study.
Your objective is to analyze the historical context as of the valuation date and classify the expected 12-month forward relative performance trajectory (e.g., relative to the broader market index).

CRITICAL INSTRUCTIONS:
1. You are NOT providing personal financial advice. This is an academic simulation assessing public information efficiency.
2. You must respond ONLY with a valid JSON object. Do not include markdown fences, greetings, or commentary outside the JSON.
3. The JSON schema must strictly be:
{
    "call": "outperform" | "neutral" | "underperform",
    "target_price": <positive float representing estimated 12-month forward fair value in USD>,
    "thesis": "<exactly one concise sentence summarizing the primary fundamental or technical driver>"
}
Note: "outperform" corresponds to bullish/buy trajectory, "neutral" to market-perform/hold, and "underperform" to bearish/sell trajectory.
4. Ensure target_price is a reasonable estimate relative to the current trading price.
"""


def fetch_recent_news_stub(ticker: str, as_of_date: Union[str, datetime]) -> List[str]:
    """
    Placeholder for news headline feed.
    
    TODO: plug in news source (e.g. NewsAPI, Bloomberg, Benzinga, or SEC EDGAR filings)
    to feed real-time sentiment signals into the quarterly consensus prompt.
    """
    dt_str = pd.to_datetime(as_of_date).strftime("%Y-%m-%d")
    # Clean representative market-context stub
    return [
        f"Quarterly industry demand indicators remain steady as of {dt_str}.",
        f"Supply chain and cost structure adjustments evaluated by institutional investors for {ticker}.",
        f"Management commentary highlights operational execution and competitive market positioning."
    ]


def fetch_earnings_context(ticker: str, as_of_date: Union[str, datetime]) -> Dict[str, Any]:
    """
    Extracts latest quarterly earnings metrics available as of the valuation date
    using yfinance quarterly financials. Skips gracefully if data is missing.
    """
    earnings_info: Dict[str, Any] = {
        "revenue": "Not reported / unavailable",
        "net_income": "Not reported / unavailable",
        "eps_headline": "Not reported / unavailable"
    }
    
    try:
        t = yf.Ticker(ticker)
        # Check quarterly financials
        qf = t.quarterly_financials
        if isinstance(qf, pd.DataFrame) and not qf.empty:
            # Filter columns prior to valuation date
            dt = pd.to_datetime(as_of_date).tz_localize(None)
            valid_cols = [c for c in qf.columns if pd.to_datetime(c).tz_localize(None) <= dt]
            if valid_cols:
                latest_col = valid_cols[0]  # Most recent past quarter
                if "Total Revenue" in qf.index:
                    rev = qf.loc["Total Revenue", latest_col]
                    if pd.notnull(rev):
                        earnings_info["revenue"] = f"${float(rev):,.0f}"
                if "Net Income" in qf.index:
                    ni = qf.loc["Net Income", latest_col]
                    if pd.notnull(ni):
                        earnings_info["net_income"] = f"${float(ni):,.0f}"
                        
        # Check quarterly income statement if quarterly financials had missing entries
        if earnings_info["revenue"] == "Not reported / unavailable":
            q_is = t.quarterly_income_stmt
            if isinstance(q_is, pd.DataFrame) and not q_is.empty:
                dt = pd.to_datetime(as_of_date).tz_localize(None)
                valid_cols = [c for c in q_is.columns if pd.to_datetime(c).tz_localize(None) <= dt]
                if valid_cols:
                    latest_col = valid_cols[0]
                    if "Total Revenue" in q_is.index:
                        rev = q_is.loc["Total Revenue", latest_col]
                        if pd.notnull(rev):
                            earnings_info["revenue"] = f"${float(rev):,.0f}"
    except Exception as e:
        logger.debug(f"Earnings extraction note for {ticker}: {e}")
        
    return earnings_info


def build_consensus_prompt(
    ticker: str,
    as_of_date: Union[str, datetime],
    price_context: Dict[str, Any],
    earnings_context: Optional[Dict[str, Any]] = None,
    news_headlines: Optional[List[str]] = None
) -> str:
    """
    Constructs the standardized financial context prompt for LLM evaluation.
    
    Parameters
    ----------
    ticker : str
        Stock ticker symbol.
    as_of_date : str or datetime
        Quarterly valuation date.
    price_context : dict
        Trailing price metrics (current price, 1m mom, 3m mom, 30d vol).
    earnings_context : dict, optional
        Quarterly fundamental figures (revenue, net income).
    news_headlines : list, optional
        Recent market news context.
        
    Returns
    -------
    str
        Complete prompt text for the LLM.
    """
    dt_str = pd.to_datetime(as_of_date).strftime("%Y-%m-%d")
    
    if earnings_context is None:
        earnings_context = fetch_earnings_context(ticker, as_of_date)
        
    if news_headlines is None:
        news_headlines = fetch_recent_news_stub(ticker, as_of_date)
        
    curr_price = price_context.get("current_price", "N/A")
    mom_1m = price_context.get("mom_1m", "N/A")
    mom_3m = price_context.get("mom_3m", "N/A")
    vol_30d = price_context.get("vol_30d", "N/A")
    
    headlines_formatted = "\n".join([f"  - {h}" for h in news_headlines])
    
    prompt = f"""EVALUATION REQUEST:
Ticker: {ticker}
Valuation Date: {dt_str}

MARKET CONTEXT AS OF {dt_str}:
- Current Trading Price: ${curr_price}
- Trailing 1-Month Return: {mom_1m}
- Trailing 3-Month Return: {mom_3m}
- 30-Day Realized Annualized Volatility: {vol_30d}

LATEST QUARTERLY FUNDAMENTAL HEADLINES:
- Total Revenue: {earnings_context.get('revenue', 'N/A')}
- Net Income: {earnings_context.get('net_income', 'N/A')}

RECENT MARKET & SECTOR HEADLINES:
{headlines_formatted}

YOUR TASK:
Provide your academic relative forward trajectory evaluation in strict JSON format:
{{"call": "outperform"|"neutral"|"underperform", "target_price": <float>, "thesis": "<one sentence>"}}
"""
    return prompt

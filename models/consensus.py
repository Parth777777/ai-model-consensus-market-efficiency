"""
AI Consensus Index Calculation Module
=====================================
Academic Methodology:
---------------------
This module quantifies the degree of consensus among an ensemble of LLMs.
Agreement is broken down into two distinct empirical dimensions:
1. Directional Agreement:
   Measures categorical alignment on the discrete recommendation (buy/hold/sell).
   directional_agreement = max(count(call in {buy, hold, sell})) / N
   A value of 1.0 means unanimous call (e.g. 4/4 buy), whereas 0.33 indicates maximal dispersion.

2. Thesis Semantic Similarity:
   Captures the underlying qualitative rationale and causal explanations.
   Two models may both recommend "buy", but one may cite momentum and another margin expansion.
   We compute the average pairwise cosine similarity of the thesis sentence embeddings
   using sentence-transformers ('all-MiniLM-L6-v2'):
   thesis_similarity = (2 / (N*(N-1))) * sum_{i < j} cosine_sim(emb_i, emb_j)

3. Combined Agreement Index:
   A composite index combining both signals:
   agreement_score = (w_dir * directional_agreement) + (w_the * thesis_similarity)
   (Default weights: 60% directional, 40% thesis similarity).
"""

from collections import Counter
from datetime import datetime
import json
import logging
from pathlib import Path
import time
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

import config
from data.universe import get_all_equity_tickers, get_ticker_category
from data.prices import get_quarterly_rebalance_dates, get_recent_price_context
from models.llm_clients import BaseLLMClient, ModelOutput, get_active_llm_clients
from models.prompts import build_consensus_prompt, fetch_earnings_context, fetch_recent_news_stub

logger = logging.getLogger(__name__)

# Global singleton for SentenceTransformer model
_SENTENCE_MODEL = None
_FALLBACK_EMBEDDER = None


def get_sentence_model():
    """Lazy loader for sentence-transformers embedding model."""
    global _SENTENCE_MODEL, _FALLBACK_EMBEDDER
    if _SENTENCE_MODEL is not None:
        return _SENTENCE_MODEL
        
    try:
        from sentence_transformers import SentenceTransformer
        logger.info(f"Loading embedding model '{config.EMBEDDING_MODEL_NAME}' for thesis similarity...")
        _SENTENCE_MODEL = SentenceTransformer(config.EMBEDDING_MODEL_NAME)
        return _SENTENCE_MODEL
    except Exception as e:
        logger.warning(f"Could not load sentence-transformers model ({e}). Using TF-IDF fallback embedder.")
        
        # Simple TF-IDF cosine fallback
        from sklearn.feature_extraction.text import TfidfVectorizer
        class FallbackEmbedder:
            def encode(self, texts: List[str]) -> np.ndarray:
                vec = TfidfVectorizer().fit_transform(texts)
                return vec.toarray()
                
        _FALLBACK_EMBEDDER = FallbackEmbedder()
        return _FALLBACK_EMBEDDER


def compute_pairwise_cosine_similarity(embeddings: np.ndarray) -> float:
    """
    Computes average pairwise cosine similarity across N thesis embeddings.
    
    Parameters
    ----------
    embeddings : np.ndarray
        Array of shape (N, embedding_dim)
        
    Returns
    -------
    float
        Average pairwise cosine similarity in [-1.0, 1.0]. Returns 1.0 if N <= 1.
    """
    n = len(embeddings)
    if n <= 1:
        return 1.0
        
    # Normalize vectors to unit length
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1e-12
    normalized = embeddings / norms
    
    # Cosine similarity matrix
    sim_matrix = np.dot(normalized, normalized.T)
    
    # Extract strictly upper triangle entries
    upper_tri_indices = np.triu_indices(n, k=1)
    pairwise_sims = sim_matrix[upper_tri_indices]
    
    avg_sim = float(np.mean(pairwise_sims))
    # Clip to [0, 1] range for stability in consensus scoring
    return max(0.0, min(1.0, avg_sim))


def calculate_agreement_score(
    model_outputs: List[Tuple[str, ModelOutput]],
    directional_weight: float = config.DIRECTIONAL_WEIGHT,
    thesis_weight: float = config.THESIS_WEIGHT
) -> Dict[str, Any]:
    """
    Calculates directional agreement, thesis similarity, and composite score.
    
    Parameters
    ----------
    model_outputs : list of (model_name, ModelOutput)
        List of outputs from each evaluated LLM.
    directional_weight : float
        Weight assigned to directional consensus (default 0.60).
    thesis_weight : float
        Weight assigned to semantic thesis similarity (default 0.40).
        
    Returns
    -------
    dict
        Structured agreement metrics.
    """
    if not model_outputs:
        return {
            "agreement_score": 0.0,
            "directional_agreement": 0.0,
            "thesis_similarity": 0.0,
            "avg_target_price": np.nan,
            "calls_summary": {},
            "num_models": 0
        }
        
    num_models = len(model_outputs)
    calls = [output.call for _, output in model_outputs]
    target_prices = [output.target_price for _, output in model_outputs if output.target_price > 0]
    theses = [output.thesis for _, output in model_outputs]
    
    # 1. Directional Agreement: max frequency / total models
    call_counts = Counter(calls)
    max_count = max(call_counts.values()) if call_counts else 0
    directional_agreement = max_count / num_models if num_models > 0 else 0.0
    
    # 2. Thesis Similarity: Pairwise Cosine Similarity of Embeddings
    model = get_sentence_model()
    try:
        embeddings = model.encode(theses)
        if isinstance(embeddings, list):
            embeddings = np.array(embeddings)
        thesis_similarity = compute_pairwise_cosine_similarity(embeddings)
    except Exception as e:
        logger.warning(f"Embedding computation error: {e}. Defaulting thesis similarity to 0.5")
        thesis_similarity = 0.5
        
    # 3. Combined Score: Weighted average normalized to [0.0, 1.0]
    combined_score = (directional_weight * directional_agreement) + (thesis_weight * thesis_similarity)
    
    avg_tp = float(np.mean(target_prices)) if target_prices else np.nan
    
    return {
        "agreement_score": round(combined_score, 4),
        "directional_agreement": round(directional_agreement, 4),
        "thesis_similarity": round(thesis_similarity, 4),
        "avg_target_price": round(avg_tp, 2) if not np.isnan(avg_tp) else np.nan,
        "calls_summary": dict(call_counts),
        "num_models": num_models
    }


def evaluate_stock_consensus(
    ticker: str,
    as_of_date: Union[str, datetime],
    prices_df: pd.DataFrame,
    llm_clients: List[BaseLLMClient]
) -> Dict[str, Any]:
    """
    Runs prompt construction and queries the committee of LLMs for a single stock-date.
    """
    price_ctx = get_recent_price_context(prices_df, ticker, as_of_date)
    earnings_ctx = fetch_earnings_context(ticker, as_of_date)
    news_ctx = fetch_recent_news_stub(ticker, as_of_date)
    
    prompt = build_consensus_prompt(
        ticker=ticker,
        as_of_date=as_of_date,
        price_context=price_ctx,
        earnings_context=earnings_ctx,
        news_headlines=news_ctx
    )
    
    model_outputs: List[Tuple[str, ModelOutput]] = []
    for client in llm_clients:
        out = client.generate_recommendation(prompt)
        if out is not None:
            model_outputs.append((client.model_name, out))
            
    agreement_metrics = calculate_agreement_score(model_outputs)
    
    # Serialize model details for research audit trail
    serialized_calls = [
        {"model": m, "call": o.call, "target_price": o.target_price, "thesis": o.thesis}
        for m, o in model_outputs
    ]
    
    record = {
        "ticker": ticker,
        "date": pd.to_datetime(as_of_date).strftime("%Y-%m-%d"),
        "category": get_ticker_category(ticker),
        "agreement_score": agreement_metrics["agreement_score"],
        "directional_agreement": agreement_metrics["directional_agreement"],
        "thesis_similarity": agreement_metrics["thesis_similarity"],
        "avg_target_price": agreement_metrics["avg_target_price"],
        "num_models": agreement_metrics["num_models"],
        "calls_json": json.dumps(serialized_calls)
    }
    return record


def generate_or_load_ai_consensus(
    prices_df: pd.DataFrame,
    tickers: Optional[List[str]] = None,
    rebalance_dates: Optional[List[pd.Timestamp]] = None,
    force_reload: bool = False,
    force_mock: bool = False,
    skip_llm: bool = False
) -> pd.DataFrame:
    """
    Generates or loads the full panel of AI model agreement scores across all stocks and dates.
    
    Parameters
    ----------
    prices_df : pd.DataFrame
        Historical price matrix.
    tickers : list, optional
        Equities to evaluate (defaults to all 60 large + small caps).
    rebalance_dates : list, optional
        Quarterly dates to evaluate.
    force_reload : bool
        If True, re-runs model evaluations even if cached.
    force_mock : bool
        If True, forces use of simulated models.
    skip_llm : bool
        If True, attempts to load existing cached data.
        
    Returns
    -------
    pd.DataFrame
        Table with [ticker, date, category, agreement_score, directional_agreement,
                    thesis_similarity, avg_target_price, num_models, calls_json]
    """
    parquet_path = config.DATA_DIR / "ai_consensus.parquet"
    csv_path = config.DATA_DIR / "ai_consensus.csv"
    
    # 1. Load from cache if requested or available
    if (skip_llm or not force_reload):
        if parquet_path.exists():
            try:
                df = pd.read_parquet(parquet_path)
                logger.info(f"Loaded {len(df)} consensus records from Parquet cache.")
                return df
            except Exception as e:
                logger.warning(f"Parquet load error: {e}. Trying CSV fallback...")
        if csv_path.exists():
            try:
                df = pd.read_csv(csv_path)
                logger.info(f"Loaded {len(df)} consensus records from CSV cache.")
                return df
            except Exception as e:
                logger.warning(f"CSV load error: {e}.")
                
    if skip_llm:
        raise FileNotFoundError(
            f"Requested --skip-llm but no consensus cache exists at {parquet_path} or {csv_path}. "
            f"Run without --skip-llm once (or with --mock-llm) to generate consensus dataset."
        )

    if tickers is None:
        tickers = get_all_equity_tickers()
        
    if rebalance_dates is None:
        rebalance_dates = get_quarterly_rebalance_dates(prices_df)

    logger.info(f"Generating AI Consensus Panel: {len(tickers)} tickers across {len(rebalance_dates)} quarterly dates...")
    total_evals = len(tickers) * len(rebalance_dates)
    logger.info(f"Total stock-date evaluations to process: {total_evals}")

    llm_clients = get_active_llm_clients(force_mock=force_mock)
    logger.info(f"Active LLM Committee: {[c.model_name for c in llm_clients]}")

    records: List[Dict[str, Any]] = []
    start_time = time.time()
    
    processed = 0
    for dt_idx, q_dt in enumerate(rebalance_dates, 1):
        dt_str = q_dt.strftime("%Y-%m-%d")
        logger.info(f"--- Evaluating Quarter {dt_idx}/{len(rebalance_dates)}: {dt_str} ---")
        
        for t_idx, ticker in enumerate(tickers, 1):
            try:
                rec = evaluate_stock_consensus(ticker, q_dt, prices_df, llm_clients)
                records.append(rec)
            except Exception as e:
                logger.error(f"Error evaluating consensus for {ticker} at {dt_str}: {e}. Skipping stock.")
                
            processed += 1
            if processed % 20 == 0 or processed == total_evals:
                elapsed = time.time() - start_time
                rate = processed / elapsed if elapsed > 0 else 0
                logger.info(f"Progress: {processed}/{total_evals} evaluations ({processed/total_evals:.1%}) | Speed: {rate:.1f} evals/sec")
                
            # Batch sleep to prevent API throttling
            if processed % config.BATCH_SIZE == 0:
                time.sleep(config.RATE_LIMIT_SLEEP_SEC)

    df_consensus = pd.DataFrame(records)
    
    # Save cache
    try:
        df_consensus.to_parquet(parquet_path)
        logger.info(f"Saved AI consensus dataset to {parquet_path}")
    except Exception as e:
        logger.warning(f"Could not save Parquet: {e}")
    df_consensus.to_csv(csv_path, index=False)
    logger.info(f"Saved AI consensus dataset to {csv_path}")

    return df_consensus

"""
Central Configuration for AI Agreement & Market Efficiency Research Pipeline.
=============================================================================
This file defines ticker universes, sampling dates, model parameters,
agreement scoring weights, and storage directories for the empirical paper.
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# DIRECTORY PATHS
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
DATA_DIR = OUTPUT_DIR / "data"
FIGURES_DIR = OUTPUT_DIR / "figures"
CACHE_DIR = OUTPUT_DIR / "cache"

for directory in [DATA_DIR, FIGURES_DIR, CACHE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# UNIVERSE DEFINITIONS
# -----------------------------------------------------------------------------
# 30 Leading S&P 500 Large-Cap Equities (Heavily covered by sell-side & media)
LARGE_CAP_TICKERS = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL",
    "META", "BRK-B", "JPM", "V", "LLY",
    "UNH", "XOM", "JNJ", "PG", "HD",
    "MA", "COST", "ABBV", "MRK", "BAC",
    "CVX", "CRM", "NFLX", "AMD", "PEP",
    "KO", "TMO", "WMT", "MCD", "CSCO"
]

# 30 Representative Liquid Russell 2000 Small-Cap Equities (Thinly covered)
SMALL_CAP_TICKERS = [
    "KNSL", "SAIA", "MEDP", "SSD", "EXPO",
    "FORM", "CRVL", "TKR", "POWI", "CALM",
    "PLUS", "FSS", "AMWD", "ATKR", "BRC",
    "CNO", "CSGS", "ENSG", "FIX", "GBCI",
    "GPI", "HLNE", "HWKN", "IBP", "KAR",
    "MC", "OII", "PRDO", "SHOO", "SLVM"
]

BENCHMARK_TICKER = "^GSPC"  # S&P 500 Index
VOLATILITY_TICKER = "^VIX"   # CBOE Volatility Index

# -----------------------------------------------------------------------------
# SAMPLING & BACKTEST HORIZONS
# -----------------------------------------------------------------------------
LOOKBACK_YEARS = 4  # 3-5 years historical lookback for empirical validation
FORWARD_HORIZONS = {
    "1m": 21,   # ~1 month (21 trading days)
    "3m": 63,   # ~3 months (63 trading days)
    "6m": 126   # ~6 months (126 trading days)
}

# -----------------------------------------------------------------------------
# AI CONSENSUS INDEX WEIGHTS
# -----------------------------------------------------------------------------
# Agreement score = (directional_weight * directional_agreement) +
#                   (thesis_weight * thesis_similarity)
DIRECTIONAL_WEIGHT = 0.60
THESIS_WEIGHT = 0.40

# LLM Prompt Settings
MAX_RETRIES = 3
BATCH_SIZE = 5
RATE_LIMIT_SLEEP_SEC = 1.0  # Pause between API call batches

# Sentence Transformer Model for Embedding Theses
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

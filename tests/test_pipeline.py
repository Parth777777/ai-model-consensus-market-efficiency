"""
Test Suite for AI Agreement Financial Research Pipeline
=======================================================
Validates universe structure, prompt construction, JSON parsing,
consensus agreement calculations, tercile bucketing, and backtesting.
"""

import unittest
import numpy as np
import pandas as pd

import config
from data.universe import (
    get_large_cap_tickers,
    get_small_cap_tickers,
    get_all_equity_tickers,
    get_ticker_category
)
from models.prompts import build_consensus_prompt
from models.llm_clients import (
    MockLLMClient,
    ModelOutput,
    parse_and_validate_json
)
from models.consensus import (
    calculate_agreement_score,
    compute_pairwise_cosine_similarity
)
from backtest.engine import (
    assign_tercile_buckets,
    compute_statistical_tests
)


class TestUniverse(unittest.TestCase):
    def test_universe_sizes(self):
        lc = get_large_cap_tickers()
        sc = get_small_cap_tickers()
        self.assertEqual(len(lc), 30, "Large-cap universe must have exactly 30 tickers.")
        self.assertEqual(len(sc), 30, "Small-cap universe must have exactly 30 tickers.")
        self.assertEqual(len(set(lc)), 30, "Large-cap tickers must be unique.")
        self.assertEqual(len(set(sc)), 30, "Small-cap tickers must be unique.")
        # Ensure no overlap between large and small cap
        overlap = set(lc).intersection(set(sc))
        self.assertEqual(len(overlap), 0, f"Overlap between large and small cap: {overlap}")

    def test_ticker_categories(self):
        self.assertEqual(get_ticker_category("AAPL"), "large_cap")
        self.assertEqual(get_ticker_category("KNSL"), "small_cap")
        self.assertEqual(get_ticker_category("^GSPC"), "benchmark")


class TestPromptAndLLM(unittest.TestCase):
    def test_prompt_construction(self):
        price_ctx = {
            "current_price": 180.50,
            "mom_1m": "+3.5%",
            "mom_3m": "+10.2%",
            "vol_30d": "18.5%"
        }
        prompt = build_consensus_prompt("AAPL", "2024-03-31", price_ctx)
        self.assertIn("AAPL", prompt)
        self.assertIn("180.5", prompt)
        self.assertIn("Valuation Date", prompt)

    def test_json_parsing_and_validation(self):
        valid_json = '{"call": "buy", "target_price": 210.50, "thesis": "Robust cloud revenue growth."}'
        out = parse_and_validate_json(valid_json)
        self.assertIsNotNone(out)
        self.assertEqual(out.call, "buy")
        self.assertEqual(out.target_price, 210.50)
        self.assertEqual(out.thesis, "Robust cloud revenue growth.")

        # Test markdown fences
        fence_json = '```json\n{"call": "SELL", "target_price": "$120.00", "thesis": "Margin compression headwinds."}\n```'
        out_fence = parse_and_validate_json(fence_json)
        self.assertIsNotNone(out_fence)
        self.assertEqual(out_fence.call, "sell")
        self.assertEqual(out_fence.target_price, 120.0)

    def test_mock_llm_client(self):
        client = MockLLMClient("TestQuant", investment_style="momentum")
        prompt = "Current Trading Price: $150.00\nTrailing 3-Month Return: +15.0%"
        output = client.generate_recommendation(prompt)
        self.assertIsNotNone(output)
        self.assertIn(output.call, ["buy", "hold", "sell"])
        self.assertGreater(output.target_price, 0)
        self.assertTrue(len(output.thesis) > 10)


class TestAgreementScoring(unittest.TestCase):
    def test_directional_agreement_unanimous(self):
        outputs = [
            ("M1", ModelOutput(call="buy", target_price=100.0, thesis="Strong fundamentals and growth.")),
            ("M2", ModelOutput(call="buy", target_price=105.0, thesis="Earnings momentum accelerating.")),
            ("M3", ModelOutput(call="buy", target_price=110.0, thesis="Operational efficiency driving margins.")),
        ]
        res = calculate_agreement_score(outputs)
        self.assertEqual(res["directional_agreement"], 1.0)
        self.assertGreater(res["thesis_similarity"], 0.0)
        self.assertGreater(res["agreement_score"], 0.6)

    def test_directional_agreement_dispersed(self):
        outputs = [
            ("M1", ModelOutput(call="buy", target_price=100.0, thesis="Positive momentum.")),
            ("M2", ModelOutput(call="hold", target_price=90.0, thesis="Neutral outlook.")),
            ("M3", ModelOutput(call="sell", target_price=80.0, thesis="Downside risks.")),
        ]
        res = calculate_agreement_score(outputs)
        self.assertAlmostEqual(res["directional_agreement"], 1.0 / 3.0, places=2)

    def test_pairwise_cosine_similarity(self):
        # 3 identical vectors should have similarity 1.0
        identical = np.array([[1.0, 0.0], [1.0, 0.0], [1.0, 0.0]])
        sim = compute_pairwise_cosine_similarity(identical)
        self.assertAlmostEqual(sim, 1.0, places=4)


class TestBacktestLogic(unittest.TestCase):
    def test_tercile_bucketing(self):
        df = pd.DataFrame({
            "ticker": [f"T{i}" for i in range(9)],
            "agreement_score": [0.1, 0.2, 0.3, 0.5, 0.55, 0.6, 0.8, 0.85, 0.9]
        })
        bucketed = assign_tercile_buckets(df)
        counts = bucketed["bucket"].value_counts()
        self.assertEqual(counts.get("Low Agreement", 0), 3)
        self.assertEqual(counts.get("Mid Agreement", 0), 3)
        self.assertEqual(counts.get("High Agreement", 0), 3)


if __name__ == "__main__":
    unittest.main()

"""
Multi-Provider LLM Client Architecture
======================================
Academic & Architectural Design:
--------------------------------
To test model consensus, we require independent predictions from multiple AI architectures.
This module abstracts different LLM providers (Anthropic, OpenAI, Extensible APIs) into a
unified interface with:
1. Strict JSON schema validation via Pydantic.
2. Robust parsing (handling Markdown fences, extraneous whitespace, retry on failure).
3. Configurable rate limiting and exponential backoff.
4. Deterministic Simulated LLM Client: Allows the research pipeline to run end-to-end
   without requiring immediate API credits or environment tokens, while producing
   realistic, diverse financial calls (momentum vs. value vs. volatility sensitivities).
"""

from abc import ABC, abstractmethod
import hashlib
import json
import logging
import os
import re
import time
from typing import Any, Dict, List, Literal, Optional, Tuple, Union
from pydantic import BaseModel, Field, ValidationError

import config
from models.prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class ModelOutput(BaseModel):
    """Strict schema for financial recommendation output."""
    call: Literal["buy", "hold", "sell"]
    target_price: float = Field(gt=0, description="12-month forward price target in USD")
    thesis: str = Field(min_length=5, description="One-sentence investment thesis")


def parse_and_validate_json(raw_text: str) -> Optional[ModelOutput]:
    """
    Strips code fences and parses JSON strictly adhering to ModelOutput schema.
    """
    clean_text = raw_text.strip()
    
    # Strip ```json ... ``` code fences if present
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", clean_text, re.DOTALL)
    if match:
        clean_text = match.group(1)
    else:
        # Look for the outermost curly braces
        brace_match = re.search(r"(\{.*\})", clean_text, re.DOTALL)
        if brace_match:
            clean_text = brace_match.group(1)
            
    try:
        data = json.loads(clean_text)
        # Normalize call string to canonical categories: buy / hold / sell
        if "call" in data and isinstance(data["call"], str):
            raw_call = data["call"].lower().strip().replace("-", "_").replace(" ", "_")
            if raw_call in ["buy", "outperform", "bullish", "overweight", "positive"]:
                data["call"] = "buy"
            elif raw_call in ["sell", "underperform", "bearish", "underweight", "negative"]:
                data["call"] = "sell"
            elif raw_call in ["hold", "neutral", "market_perform", "equal_weight", "in_line"]:
                data["call"] = "hold"
            else:
                # Default unknown to hold / neutral
                data["call"] = "hold"
        # Ensure target_price is a float
        if "target_price" in data and isinstance(data["target_price"], (int, float, str)):
            # Strip dollar signs or commas
            clean_tp = str(data["target_price"]).replace("$", "").replace(",", "").strip()
            data["target_price"] = float(clean_tp)
            
        validated = ModelOutput(**data)
        return validated
    except (json.JSONDecodeError, ValidationError, ValueError) as e:
        logger.warning(f"Failed to parse LLM response into ModelOutput: {e}. Raw: {clean_text[:100]}...")
        return None


class BaseLLMClient(ABC):
    """Abstract base class for all LLM providers."""
    
    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def generate_recommendation(self, prompt: str) -> Optional[ModelOutput]:
        """Sends the prompt and returns validated ModelOutput or None."""
        pass


class AnthropicClient(BaseLLMClient):
    """Anthropic Claude API client."""
    
    def __init__(self, model_name: str = "claude-3-5-sonnet-20241022", api_key: Optional[str] = None):
        super().__init__(model_name)
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self._client = None
        if self.api_key:
            try:
                import anthropic
                self._client = anthropic.Anthropic(api_key=self.api_key)
            except ImportError:
                logger.warning("anthropic package not installed.")

    def generate_recommendation(self, prompt: str) -> Optional[ModelOutput]:
        if not self._client:
            logger.warning("Anthropic client not initialized (missing API key or package).")
            return None

        for attempt in range(1, config.MAX_RETRIES + 1):
            try:
                response = self._client.messages.create(
                    model=self.model_name,
                    max_tokens=300,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": prompt}]
                )
                raw_content = response.content[0].text
                parsed = parse_and_validate_json(raw_content)
                if parsed:
                    return parsed
                logger.warning(f"[{self.model_name}] Attempt {attempt} returned malformed JSON. Retrying...")
            except Exception as e:
                logger.warning(f"[{self.model_name}] API call failed on attempt {attempt}: {e}")
                time.sleep(2 ** attempt)
        return None


class OpenAIClient(BaseLLMClient):
    """OpenAI GPT API client."""
    
    def __init__(self, model_name: str = "gpt-4o-mini", api_key: Optional[str] = None):
        super().__init__(model_name)
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._client = None
        if self.api_key:
            try:
                import openai
                self._client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                logger.warning("openai package not installed.")

    def generate_recommendation(self, prompt: str) -> Optional[ModelOutput]:
        if not self._client:
            logger.warning("OpenAI client not initialized (missing API key or package).")
            return None

        for attempt in range(1, config.MAX_RETRIES + 1):
            try:
                response = self._client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    max_tokens=300,
                    temperature=0.2
                )
                raw_content = response.choices[0].message.content or ""
                parsed = parse_and_validate_json(raw_content)
                if parsed:
                    return parsed
                logger.warning(f"[{self.model_name}] Attempt {attempt} returned malformed JSON. Retrying...")
            except Exception as e:
                logger.warning(f"[{self.model_name}] API call failed on attempt {attempt}: {e}")
                time.sleep(2 ** attempt)
        return None


class MockLLMClient(BaseLLMClient):
    """
    Deterministic Simulated LLM Client.
    ===================================
    Designed for:
    1. Environments without active API keys.
    2. Zero-cost unit testing and reproducible paper backtests.
    
    It models distinct financial research styles (e.g. Momentum-biased,
    Value-biased, Mean-reversion, Quality-focused) using deterministic
    hash-seeded analysis of the financial prompt features.
    """
    
    def __init__(self, model_id: str, investment_style: str = "momentum"):
        super().__init__(f"Simulated-{model_id}")
        self.investment_style = investment_style.lower()

    def generate_recommendation(self, prompt: str) -> Optional[ModelOutput]:
        # Deterministic pseudo-random seed based on prompt text + model name
        seed_val = int(hashlib.md5(f"{self.model_name}_{prompt}".encode("utf-8")).hexdigest()[:8], 16)
        
        # Extract current price from prompt text
        curr_price = 100.0
        price_match = re.search(r"Current Trading Price:\s*\$([0-9\.]+)", prompt)
        if price_match:
            try:
                curr_price = float(price_match.group(1))
            except ValueError:
                curr_price = 100.0
                
        # Extract momentum
        mom_3m = 0.0
        mom_match = re.search(r"Trailing 3-Month Return:\s*([+-]?[0-9\.]+)%", prompt)
        if mom_match:
            try:
                mom_3m = float(mom_match.group(1)) / 100.0
            except ValueError:
                mom_3m = 0.0

        # Style-dependent decision rule
        hash_noise = (seed_val % 100) / 100.0 - 0.5  # -0.5 to +0.5
        
        if self.investment_style == "momentum":
            score = mom_3m * 2.0 + hash_noise * 0.3
            if score > 0.08:
                call = "buy"
                target_price = curr_price * (1.12 + abs(hash_noise) * 0.08)
                thesis = f"Strong upward medium-term momentum ({mom_3m:+.1%}) signals continued institutional accumulation."
            elif score < -0.08:
                call = "sell"
                target_price = curr_price * (0.88 - abs(hash_noise) * 0.08)
                thesis = f"Persistent negative price trajectory ({mom_3m:+.1%}) indicates structural distribution headwinds."
            else:
                call = "hold"
                target_price = curr_price * (1.02 + hash_noise * 0.05)
                thesis = f"Consolidating trading range warrants a neutral rating until breakout confirmation."
                
        elif self.investment_style == "value":
            # Value investors prefer pullbacks and fade overbought momentum
            score = -mom_3m * 1.5 + hash_noise * 0.4
            if score > 0.10:
                call = "buy"
                target_price = curr_price * (1.15 + abs(hash_noise) * 0.05)
                thesis = f"Recent price softening provides an attractive risk-adjusted entry point against fundamental book value."
            elif score < -0.10:
                call = "sell"
                target_price = curr_price * (0.85 - abs(hash_noise) * 0.05)
                thesis = f"Elevated multi-month valuation multiples leave little safety margin against forward earnings revisions."
            else:
                call = "hold"
                target_price = curr_price * (1.00 + hash_noise * 0.04)
                thesis = f"Fair valuation reflects balanced risk-reward relative to sector peers."
                
        elif self.investment_style == "quality":
            # Quality investors look for steady moderate returns
            score = hash_noise
            if mom_3m > 0.02 and hash_noise > -0.1:
                call = "buy"
                target_price = curr_price * (1.10 + abs(hash_noise) * 0.06)
                thesis = f"Stable financial profile and durable competitive moat support long-term compounding potential."
            elif mom_3m < -0.10 or hash_noise < -0.3:
                call = "sell"
                target_price = curr_price * (0.90 - abs(hash_noise) * 0.05)
                thesis = f"Heightened earnings volatility and cyclical margin pressures elevate downside risk."
            else:
                call = "hold"
                target_price = curr_price * (1.04 + hash_noise * 0.04)
                thesis = f"Defensive operational balance sheet balanced by limited immediate re-rating catalysts."
                
        else:  # Consensus / Balanced Model
            if mom_3m > 0.05:
                call = "buy" if hash_noise > -0.2 else "hold"
                target_price = curr_price * 1.10
                thesis = f"Positive operating execution and robust revenue traction support upside."
            elif mom_3m < -0.05:
                call = "sell" if hash_noise < 0.2 else "hold"
                target_price = curr_price * 0.90
                thesis = f"Macro headwinds and declining momentum justify a defensive posture."
            else:
                call = "hold"
                target_price = curr_price * 1.01
                thesis = f"Balanced near-term catalysts recommend maintaining current position."

        return ModelOutput(
            call=call,
            target_price=round(float(target_price), 2),
            thesis=thesis
        )


def get_active_llm_clients(force_mock: bool = False) -> List[BaseLLMClient]:
    """
    Returns the active set of 3 to 5 LLM clients.
    If API keys are available in the environment and force_mock=False, initializes
    Anthropic and OpenAI clients. Otherwise, initializes 4 calibrated simulated LLMs
    representing diverse investment philosophies (Momentum, Value, Quality, Balanced).
    """
    has_anthropic = bool(os.getenv("ANTHROPIC_API_KEY"))
    has_openai = bool(os.getenv("OPENAI_API_KEY"))
    
    clients: List[BaseLLMClient] = []

    if not force_mock and (has_anthropic or has_openai):
        logger.info("Initializing live LLM clients with environment API keys...")
        if has_anthropic:
            clients.append(AnthropicClient(model_name="claude-3-5-sonnet-20241022"))
            clients.append(AnthropicClient(model_name="claude-3-haiku-20240307"))
        if has_openai:
            clients.append(OpenAIClient(model_name="gpt-4o"))
            clients.append(OpenAIClient(model_name="gpt-4o-mini"))
            
        # Ensure at least 3 models by supplementing with an additional model
        if len(clients) < 3:
            logger.info("Adding simulated model to achieve minimum 3-model committee.")
            clients.append(MockLLMClient(model_id="Balanced-Macro", investment_style="balanced"))
    else:
        logger.info("No API keys detected in environment (or mock mode requested).")
        logger.info("Initializing 4 simulated institutional LLM research models (Momentum, Value, Quality, Balanced).")
        clients = [
            MockLLMClient(model_id="AI-Momentum-Quant", investment_style="momentum"),
            MockLLMClient(model_id="AI-Fundamental-Value", investment_style="value"),
            MockLLMClient(model_id="AI-Quality-Compounder", investment_style="quality"),
            MockLLMClient(model_id="AI-Macro-Tactical", investment_style="balanced")
        ]
        
    return clients

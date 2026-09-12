# Technical Appendices Compendium (Appendices A through H)
## Empirical Asset Pricing, AI Model Consensus, and Market Efficiency
### Author: Parth Doshi • September 2026

---

## Appendix A: Universe Constituents & Market Cap Classification

The empirical universe comprises 60 equities partitioned into 30 Large-Cap S&P 500 constituents and 30 Small-Cap Russell 2000 constituents, alongside market and volatility benchmarks:

| Ticker | Company Name / Security | Market Cap Category | GICS Sector | Benchmark Index |
| :--- | :--- | :--- | :--- | :--- |
| **AAPL** | Apple Inc. | Large-Cap | Information Technology | S&P 500 Constituent |
| **MSFT** | Microsoft Corporation | Large-Cap | Information Technology | S&P 500 Constituent |
| **NVDA** | NVIDIA Corporation | Large-Cap | Information Technology | S&P 500 Constituent |
| **AMZN** | Amazon.com, Inc. | Large-Cap | Consumer Discretionary | S&P 500 Constituent |
| **GOOGL** | Alphabet Inc. (Class A) | Large-Cap | Communication Services | S&P 500 Constituent |
| **META** | Meta Platforms, Inc. | Large-Cap | Communication Services | S&P 500 Constituent |
| **BRK-B** | Berkshire Hathaway Inc. (Class B) | Large-Cap | Financials | S&P 500 Constituent |
| **JPM** | JPMorgan Chase & Co. | Large-Cap | Financials | S&P 500 Constituent |
| **V** | Visa Inc. | Large-Cap | Financials | S&P 500 Constituent |
| **LLY** | Eli Lilly and Company | Large-Cap | Health Care | S&P 500 Constituent |
| **UNH** | UnitedHealth Group Incorporated | Large-Cap | Health Care | S&P 500 Constituent |
| **XOM** | Exxon Mobil Corporation | Large-Cap | Energy | S&P 500 Constituent |
| **JNJ** | Johnson & Johnson | Large-Cap | Health Care | S&P 500 Constituent |
| **PG** | The Procter & Gamble Company | Large-Cap | Consumer Staples | S&P 500 Constituent |
| **HD** | The Home Depot, Inc. | Large-Cap | Consumer Discretionary | S&P 500 Constituent |
| **MA** | Mastercard Incorporated | Large-Cap | Financials | S&P 500 Constituent |
| **COST** | Costco Wholesale Corporation | Large-Cap | Consumer Staples | S&P 500 Constituent |
| **ABBV** | AbbVie Inc. | Large-Cap | Health Care | S&P 500 Constituent |
| **MRK** | Merck & Co., Inc. | Large-Cap | Health Care | S&P 500 Constituent |
| **BAC** | Bank of America Corporation | Large-Cap | Financials | S&P 500 Constituent |
| **CVX** | Chevron Corporation | Large-Cap | Energy | S&P 500 Constituent |
| **CRM** | Salesforce, Inc. | Large-Cap | Information Technology | S&P 500 Constituent |
| **NFLX** | Netflix, Inc. | Large-Cap | Communication Services | S&P 500 Constituent |
| **AMD** | Advanced Micro Devices, Inc. | Large-Cap | Information Technology | S&P 500 Constituent |
| **PEP** | PepsiCo, Inc. | Large-Cap | Consumer Staples | S&P 500 Constituent |
| **KO** | The Coca-Cola Company | Large-Cap | Consumer Staples | S&P 500 Constituent |
| **TMO** | Thermo Fisher Scientific Inc. | Large-Cap | Health Care | S&P 500 Constituent |
| **WMT** | Walmart Inc. | Large-Cap | Consumer Staples | S&P 500 Constituent |
| **MCD** | McDonald's Corporation | Large-Cap | Consumer Discretionary | S&P 500 Constituent |
| **CSCO** | Cisco Systems, Inc. | Large-Cap | Information Technology | S&P 500 Constituent |
| **KNSL** | Kinsale Capital Group, Inc. | Small-Cap | Financials | Russell 2000 Constituent |
| **SAIA** | Saia, Inc. | Small-Cap | Industrials | Russell 2000 Constituent |
| **MEDP** | Medpace Holdings, Inc. | Small-Cap | Health Care | Russell 2000 Constituent |
| **SSD** | Simpson Manufacturing Co., Inc. | Small-Cap | Industrials | Russell 2000 Constituent |
| **EXPO** | Exponent, Inc. | Small-Cap | Commercial Services | Russell 2000 Constituent |
| **FORM** | FormFactor, Inc. | Small-Cap | Information Technology | Russell 2000 Constituent |
| **CRVL** | CorVel Corporation | Small-Cap | Health Care | Russell 2000 Constituent |
| **TKR** | The Timken Company | Small-Cap | Industrials | Russell 2000 Constituent |
| **POWI** | Power Integrations, Inc. | Small-Cap | Information Technology | Russell 2000 Constituent |
| **CALM** | Cal-Maine Foods, Inc. | Small-Cap | Consumer Staples | Russell 2000 Constituent |
| **PLUS** | ePlus inc. | Small-Cap | Information Technology | Russell 2000 Constituent |
| **FSS** | Federal Signal Corporation | Small-Cap | Industrials | Russell 2000 Constituent |
| **AMWD** | American Woodmark Corporation | Small-Cap | Consumer Discretionary | Russell 2000 Constituent |
| **ATKR** | Atkore Inc. | Small-Cap | Industrials | Russell 2000 Constituent |
| **BRC** | Brady Corporation | Small-Cap | Industrials | Russell 2000 Constituent |
| **CNO** | CNO Financial Group, Inc. | Small-Cap | Financials | Russell 2000 Constituent |
| **CSGS** | CSG Systems International, Inc. | Small-Cap | Information Technology | Russell 2000 Constituent |
| **ENSG** | The Ensign Group, Inc. | Small-Cap | Health Care | Russell 2000 Constituent |
| **FIX** | Comfort Systems USA, Inc. | Small-Cap | Industrials | Russell 2000 Constituent |
| **GBCI** | Glacier Bancorp, Inc. | Small-Cap | Financials | Russell 2000 Constituent |
| **GPI** | Group 1 Automotive, Inc. | Small-Cap | Consumer Discretionary | Russell 2000 Constituent |
| **HLNE** | Hamilton Lane Incorporated | Small-Cap | Financials | Russell 2000 Constituent |
| **HWKN** | Hawkins, Inc. | Small-Cap | Materials | Russell 2000 Constituent |
| **IBP** | Installed Building Products, Inc. | Small-Cap | Consumer Discretionary | Russell 2000 Constituent |
| **KAR** | OPENLANE, Inc. | Small-Cap | Industrials | Russell 2000 Constituent |
| **MC** | Moelis & Company | Small-Cap | Financials | Russell 2000 Constituent |
| **OII** | Oceaneering International, Inc. | Small-Cap | Energy | Russell 2000 Constituent |
| **PRDO** | Perdoceo Education Corporation | Small-Cap | Consumer Discretionary | Russell 2000 Constituent |
| **SHOO** | Steven Madden, Ltd. | Small-Cap | Consumer Discretionary | Russell 2000 Constituent |
| **SLVM** | Sylvamo Corporation | Small-Cap | Materials | Russell 2000 Constituent |
| **^GSPC** | S&P 500 Index | Benchmark | Broad Equity Benchmark | S&P 500 Market Index |
| **^VIX** | CBOE Volatility Index | Benchmark | Implied Volatility Index | Market Volatility Overlay |

---

## Appendix B: Prompt Template Specification & Agent Architecture

### B.1 Verbatim System Prompt
```text
You are an academic quantitative researcher evaluating historical market information for an empirical asset pricing study.
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
```

### B.2 Verbatim Contextual Evaluation Request Prompt
```text
EVALUATION REQUEST:
Ticker: {ticker}
Valuation Date: {as_of_date}

MARKET CONTEXT AS OF {as_of_date}:
- Current Trading Price: ${current_price}
- Trailing 1-Month Return: {mom_1m}
- Trailing 3-Month Return: {mom_3m}
- 30-Day Realized Annualized Volatility: {vol_30d}

LATEST QUARTERLY FUNDAMENTAL HEADLINES:
- Total Revenue: {revenue}
- Net Income: {net_income}

RECENT MARKET & SECTOR HEADLINES:
  - Quarterly industry demand indicators remain steady as of {as_of_date}.
  - Supply chain and cost structure adjustments evaluated by institutional investors for {ticker}.
  - Management commentary highlights operational execution and competitive market positioning.

YOUR TASK:
Provide your academic relative forward trajectory evaluation in strict JSON format:
{"call": "outperform"|"neutral"|"underperform", "target_price": <float>, "thesis": "<one sentence>"}
```

### B.3 Pydantic Data Validation Schema
```python
from pydantic import BaseModel, Field
from typing import Literal

class StockRecommendation(BaseModel):
    call: Literal["buy", "hold", "sell"] = Field(
        description="Discrete standardized buy-side recommendation"
    )
    target_price: float = Field(
        gt=0.0,
        description="12-month forward fair value price target in USD"
    )
    thesis: str = Field(
        min_length=10,
        max_length=300,
        description="Single concise sentence outlining investment thesis"
    )
```

### B.4 Agent Investment Philosophy Variations
1. **Model 1 (Momentum Quant)**: Evaluates trend persistence, prioritizing 1-month and 3-month trailing momentum relative to realized volatility. Issues `outperform` calls when $\text{Mom}_{3m} > 0$ and volatility is stable.
2. **Model 2 (Fundamental Value)**: Focuses on earnings stability and valuation multiples. Issues `outperform` calls when market price experiences pullbacks while net income remains positive.
3. **Model 3 (Quality Compounder)**: Evaluates structural moat durability and revenue resilience. Tends to issue `neutral` to `outperform` ratings with modest upside price targets ($+8\%$ to $+15\%$).
4. **Model 4 (Tactical Macro)**: Evaluates overall market volatility regime (`^VIX`) and macroeconomic headwinds, weighting risk-adjusted asymmetric downside protection.

---

## Appendix C: Quarter-by-Quarter Long-Only Portfolio Compounding Series

The complete period-by-period returns and cumulative compounding wealth index across all 16 quarterly holding periods ($N = 16$):

| Rebalance Date | Low Agreement Return ($\bar{R}_{\text{Low}}$) | High Agreement Return ($\bar{R}_{\text{High}}$) | S&P 500 Benchmark Return ($R_{\text{SP500}}$) | Period Spread ($\bar{R}_{\text{Low}} - \bar{R}_{\text{High}}$) | Cumulative Low Agreement | Cumulative High Agreement | Cumulative Benchmark |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2022-09-30** | **+20.41%** | +11.14% | +7.08% | **+9.27%** | +20.41% | +11.14% | +7.08% |
| **2022-12-30** | +11.25% | **+13.34%** | +7.42% | $-2.09\%$ | +33.96% | +25.97% | +15.03% |
| **2023-03-31** | **+9.78%** | +6.42% | +8.43% | **+3.36%** | +47.06% | +34.06% | +24.72% |
| **2023-06-30** | **+5.07%** | +4.16% | $-3.65\%$ | **+0.91%** | +54.52% | +39.64% | +20.17% |
| **2023-09-29** | **+15.76%** | +15.13% | +11.24% | **+0.63%** | +78.87% | +60.77% | +33.67% |
| **2023-12-29** | +10.16% | **+13.01%** | +9.14% | $-2.86\%$ | +97.03% | +81.69% | +45.89% |
| **2024-03-28** | $-1.74\%$ | **$-1.31\%$** | +3.92% | $-0.43\%$ | +93.60% | +79.31% | +51.62% |
| **2024-06-28** | **+11.71%** | +6.97% | +5.09% | **+4.74%** | +116.27% | +91.80% | +59.33% |
| **2024-09-30** | **+0.83%** | +0.03% | +2.51% | **+0.80%** | +118.06% | +91.85% | +63.32% |
| **2024-12-31** | $-10.61\%$ | **$-10.29\%$** | $-8.25\%$ | $-0.32\%$ | +94.92% | +72.11% | +49.85% |
| **2025-03-31** | +6.44% | **+11.09%** | +10.45% | $-4.64\%$ | +107.48% | +91.19% | +65.50% |
| **2025-06-30** | +5.48% | **+9.26%** | +7.35% | $-3.79\%$ | +118.85% | +108.90% | +77.67% |
| **2025-09-30** | +3.88% | **+5.09%** | +3.11% | $-1.21\%$ | +127.34% | +119.53% | +83.19% |
| **2025-12-31** | **+5.37%** | +0.92% | $-3.84\%$ | **+4.45%** | +139.55% | +121.54% | +76.16% |
| **2026-03-31** | **+16.22%** | +12.28% | +14.62% | **+3.94%** | +178.41% | +148.75% | +101.92% |
| **2026-06-30** | 0.00% | 0.00% | 0.00% | $0.00\%$ | **+178.41%** | **+148.75%** | **+101.92%** |

---

## Appendix D: Multi-Horizon Return Distribution Matrix

The equal-weighted mean forward returns, sample standard errors, and cross-sectional sample counts across 1-Month (21 trading days), 3-Month (63 trading days), and 6-Month (126 trading days) forward horizons:

| Market Cap Category | Agreement Tercile Bucket | Forward Horizon | Mean Forward Return | Sample Standard Error ($\text{SE}$) | Sample Size ($N$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Large-Cap** | High Agreement | **1m** (21d) | +2.98% | 0.74% | 158 |
| **Large-Cap** | Low Agreement | **1m** (21d) | +2.94% | 0.74% | 160 |
| **Large-Cap** | Mid Agreement | **1m** (21d) | +2.60% | 0.81% | 162 |
| **Large-Cap** | High Agreement | **3m** (63d) | +6.49% | 1.38% | 148 |
| **Large-Cap** | Low Agreement | **3m** (63d) | **+6.70%** | 1.51% | 150 |
| **Large-Cap** | Mid Agreement | **3m** (63d) | +5.52% | 1.26% | 152 |
| **Large-Cap** | High Agreement | **6m** (126d) | **+16.97%** | 2.69% | 138 |
| **Large-Cap** | Low Agreement | **6m** (126d) | +10.51% | 1.42% | 140 |
| **Large-Cap** | Mid Agreement | **6m** (126d) | +10.73% | 1.99% | 142 |
| **Small-Cap** | High Agreement | **1m** (21d) | +2.96% | 1.14% | 136 |
| **Small-Cap** | Low Agreement | **1m** (21d) | +3.53% | 1.11% | 148 |
| **Small-Cap** | Mid Agreement | **1m** (21d) | **+4.31%** | 0.95% | 148 |
| **Small-Cap** | High Agreement | **3m** (63d) | +6.45% | 1.81% | 126 |
| **Small-Cap** | Low Agreement | **3m** (63d) | **+7.82%** | 1.79% | 139 |
| **Small-Cap** | Mid Agreement | **3m** (63d) | +7.18% | 1.43% | 140 |
| **Small-Cap** | High Agreement | **6m** (126d) | +14.36% | 2.94% | 118 |
| **Small-Cap** | Low Agreement | **6m** (126d) | **+15.67%** | 2.44% | 130 |
| **Small-Cap** | Mid Agreement | **6m** (126d) | +12.73% | 2.44% | 130 |

---

## Appendix E: Complete Sell-Side Analyst Target Price & Dispersion Table

The complete cross-sectional dataset of sell-side human analyst target prices extracted via `yfinance` across all 60 universe constituents ($N = 56$ valid records, 4 omitted due to data absence):

| Ticker | Category | Price ($) | Target Mean | Target Median | Target High | Target Low | Target Std ($\hat{\sigma}$) | Normalized Dispersion | Analyst Count |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **AAPL** | Large-Cap | $334.35 | $324.40 | $335.00 | $400.00 | $215.00 | $46.25 | **0.1426** | 39 |
| **MSFT** | Large-Cap | $494.61 | $572.92 | $555.00 | $870.00 | $400.00 | $117.50 | **0.2051** | 52 |
| **NVDA** | Large-Cap | $219.10 | $327.18 | $315.00 | $515.00 | $180.00 | $83.75 | **0.2560** | 58 |
| **AMZN** | Large-Cap | $256.21 | $328.17 | $325.50 | $405.00 | $230.00 | $43.75 | **0.1333** | 60 |
| **GOOGL** | Large-Cap | $341.18 | $428.07 | $429.00 | $515.00 | $340.00 | $43.75 | **0.1022** | 54 |
| **META** | Large-Cap | $649.43 | $757.31 | $750.00 | $1000.00 | $580.00 | $105.00 | **0.1386** | 57 |
| **BRK-B** | Large-Cap | $507.56 | $547.67 | $529.00 | $604.00 | $510.00 | $23.50 | **0.0429** | 3 |
| **JPM** | Large-Cap | $356.88 | $376.14 | $372.00 | $452.00 | $305.00 | $36.75 | **0.0977** | 21 |
| **V** | Large-Cap | $370.58 | $419.36 | $422.00 | $466.00 | $330.00 | $34.00 | **0.0811** | 37 |
| **LLY** | Large-Cap | $1122.75 | $1318.66 | $1376.00 | $1600.00 | $930.00 | $167.50 | **0.1270** | 29 |
| **UNH** | Large-Cap | $379.58 | $475.23 | $490.00 | $529.00 | $313.00 | $54.00 | **0.1136** | 26 |
| **XOM** | Large-Cap | $165.35 | $170.91 | $170.00 | $200.00 | $142.00 | $14.50 | **0.0848** | 22 |
| **JNJ** | Large-Cap | $265.79 | $277.91 | $282.00 | $320.00 | $190.00 | $32.50 | **0.1169** | 22 |
| **PG** | Large-Cap | $145.13 | $160.61 | $162.00 | $186.00 | $143.00 | $10.75 | **0.0669** | 23 |
| **HD** | Large-Cap | $309.70 | $377.19 | $379.00 | $425.00 | $310.00 | $28.75 | **0.0762** | 32 |
| **MA** | Large-Cap | $569.08 | $668.53 | $669.00 | $740.00 | $550.00 | $47.50 | **0.0711** | 36 |
| **COST** | Large-Cap | $904.11 | $1072.20 | $1100.00 | $1315.00 | $740.00 | $143.75 | **0.1341** | 35 |
| **ABBV** | Large-Cap | $257.35 | $277.31 | $282.00 | $328.00 | $200.00 | $32.00 | **0.1154** | 29 |
| **MRK** | Large-Cap | $145.15 | $152.96 | $152.50 | $186.00 | $105.00 | $20.25 | **0.1324** | 26 |
| **BAC** | Large-Cap | $62.96 | $69.00 | $68.00 | $79.00 | $62.00 | $4.25 | **0.0616** | 21 |
| **CVX** | Large-Cap | $213.76 | $221.21 | $224.50 | $243.00 | $175.00 | $17.00 | **0.0769** | 24 |
| **CRM** | Large-Cap | $248.96 | $273.37 | $273.00 | $475.00 | $160.00 | $78.75 | **0.2881** | 54 |
| **NFLX** | Large-Cap | $76.93 | $93.66 | $93.00 | $135.00 | $70.00 | $16.25 | **0.1735** | 45 |
| **AMD** | Large-Cap | $512.56 | $615.07 | $610.00 | $1250.00 | $365.00 | $221.25 | **0.3597** | 50 |
| **PEP** | Large-Cap | $137.12 | $155.00 | $155.00 | $183.00 | $124.00 | $14.75 | **0.0952** | 22 |
| **KO** | Large-Cap | $88.41 | $94.70 | $96.00 | $104.00 | $75.00 | $7.25 | **0.0766** | 23 |
| **TMO** | Large-Cap | $612.04 | $645.15 | $650.00 | $750.00 | $520.00 | $57.50 | **0.0891** | 27 |
| **WMT** | Large-Cap | $106.45 | $127.43 | $130.00 | $155.00 | $81.00 | $18.50 | **0.1452** | 40 |
| **MCD** | Large-Cap | $253.17 | $315.39 | $305.00 | $407.00 | $250.00 | $39.25 | **0.1245** | 31 |
| **CSCO** | Large-Cap | $111.59 | $137.63 | $135.00 | $170.00 | $115.00 | $13.75 | **0.0999** | 24 |
| **KNSL** | Small-Cap | $357.85 | $354.78 | $375.00 | $405.00 | $259.00 | $36.50 | **0.1029** | 9 |
| **SAIA** | Small-Cap | $349.57 | $432.55 | $438.50 | $510.00 | $285.00 | $56.25 | **0.1300** | 22 |
| **MEDP** | Small-Cap | $593.10 | $581.83 | $604.50 | $692.00 | $370.00 | $80.50 | **0.1384** | 12 |
| **SSD** | Small-Cap | $173.35 | $219.00 | $218.00 | $230.00 | $212.00 | $4.50 | **0.0205** | 5 |
| **EXPO** | Small-Cap | $67.35 | $84.00 | $90.00 | $90.00 | $72.00 | $4.50 | **0.0536** | 3 |
| **FORM** | Small-Cap | $114.96 | $138.63 | $157.50 | $175.00 | $64.00 | $27.75 | **0.2002** | 8 |
| **TKR** | Small-Cap | $118.02 | $147.75 | $150.00 | $160.00 | $130.00 | $7.50 | **0.0508** | 11 |
| **POWI** | Small-Cap | $52.66 | $77.50 | $80.00 | $85.00 | $65.00 | $5.00 | **0.0645** | 4 |
| **CALM** | Small-Cap | $73.60 | $84.00 | $83.00 | $90.00 | $79.00 | $2.75 | **0.0327** | 3 |
| **PLUS** | Small-Cap | $91.18 | $111.00 | $111.00 | $111.00 | $111.00 | $0.00 | **0.0000** | 1 |
| **FSS** | Small-Cap | $114.61 | $145.63 | $146.50 | $155.00 | $132.00 | $5.75 | **0.0395** | 8 |
| **ATKR** | Small-Cap | $94.28 | $93.50 | $93.50 | $95.00 | $92.00 | $0.75 | **0.0080** | 2 |
| **BRC** | Small-Cap | $87.52 | $110.00 | $110.00 | $111.00 | $109.00 | $0.50 | **0.0045** | 2 |
| **CNO** | Small-Cap | $54.99 | $53.75 | $53.50 | $56.00 | $52.00 | $1.00 | **0.0186** | 4 |
| **ENSG** | Small-Cap | $173.39 | $220.00 | $225.00 | $230.00 | $207.00 | $5.75 | **0.0261** | 5 |
| **FIX** | Small-Cap | $1675.50 | $2197.00 | $2165.50 | $2500.00 | $1910.00 | $147.50 | **0.0671** | 8 |
| **GBCI** | Small-Cap | $46.10 | $56.83 | $56.50 | $60.00 | $55.00 | $1.25 | **0.0220** | 6 |
| **GPI** | Small-Cap | $283.30 | $371.08 | $372.50 | $450.00 | $275.00 | $43.75 | **0.1179** | 12 |
| **HLNE** | Small-Cap | $96.86 | $133.43 | $130.00 | $181.00 | $105.00 | $19.00 | **0.1424** | 7 |
| **HWKN** | Small-Cap | $124.27 | $174.25 | $177.50 | $200.00 | $142.00 | $14.50 | **0.0832** | 4 |
| **IBP** | Small-Cap | $207.88 | $244.82 | $246.00 | $297.00 | $200.00 | $24.25 | **0.0991** | 11 |
| **MC** | Small-Cap | $64.30 | $72.00 | $71.50 | $86.00 | $60.00 | $6.50 | **0.0903** | 10 |
| **OII** | Small-Cap | $50.74 | $46.00 | $47.00 | $52.00 | $38.00 | $3.50 | **0.0761** | 4 |
| **PRDO** | Small-Cap | $33.04 | $44.00 | $44.00 | $44.00 | $44.00 | $0.00 | **0.0000** | 1 |
| **SHOO** | Small-Cap | $42.86 | $52.40 | $55.00 | $60.00 | $36.00 | $6.00 | **0.1145** | 10 |
| **SLVM** | Small-Cap | $35.32 | $51.25 | $47.50 | $65.00 | $45.00 | $5.00 | **0.0976** | 4 |
| **AMWD** | Small-Cap | $88.10 | *N/A* | *N/A* | *N/A* | *N/A* | *N/A* | **Omitted** | 0 |
| **CSGS** | Small-Cap | $46.30 | *N/A* | *N/A* | *N/A* | *N/A* | *N/A* | **Omitted** | 0 |
| **CRVL** | Small-Cap | $285.00 | *N/A* | *N/A* | *N/A* | *N/A* | *N/A* | **Omitted** | 0 |
| **KAR** | Small-Cap | $17.80 | *N/A* | *N/A* | *N/A* | *N/A* | *N/A* | **Omitted** | 0 |

---

## Appendix F: Technical Architecture & Code Implementation Structure

The empirical quantitative pipeline is deployed across the following modular codebase:

```
c:\Users\parth\OneDrive\Desktop\EMH FOLDER FEC\
├── config.py                 # Central configurations, universes, and paths
├── requirements.txt          # Package dependencies
├── main.py                   # Master pipeline orchestrator & CLI runner
├── data/
│   ├── __init__.py
│   ├── universe.py           # 30 Large-Cap & 30 Small-Cap ticker metadata
│   └── prices.py             # yfinance fetcher, caching, multi-horizon returns
├── models/
│   ├── __init__.py
│   ├── prompts.py            # Prompt construction, earnings extraction, news stub
│   ├── llm_clients.py        # Multi-provider clients (Anthropic, OpenAI, simulated)
│   └── consensus.py          # Agreement scoring & sentence-transformers embeddings
├── backtest/
│   ├── __init__.py
│   ├── analyst.py            # Analyst dispersion extraction via yfinance
│   └── engine.py             # Tercile sorting, quarterly compounding, Welch's t-tests
├── viz/
│   ├── __init__.py
│   └── charts.py             # 6 publication-ready 300 DPI matplotlib/seaborn charts
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py      # Automated unit test suite (9 test cases)
└── output/
    ├── data/                 # Generated datasets (Parquet and CSV)
    │   ├── ai_consensus.csv
    │   ├── analyst_dispersion.csv
    │   ├── bucket_summary_returns.csv
    │   ├── consensus_with_forward_returns.csv
    │   ├── cumulative_portfolio_returns.csv
    │   └── historical_prices.csv
    └── figures/              # Output high-resolution figures (300 DPI PNG)
        ├── fig1_agreement_histogram_largecap.png
        ├── fig2_agreement_histogram_overlay.png
        ├── fig3_forward_returns_by_bucket.png
        ├── fig4_cumulative_returns.png
        ├── fig5_ai_vs_analyst_dispersion.png
        └── fig6_rolling_consensus_index.png
```

### CLI Execution Modes:
- Full Pipeline with Simulation Fallback: `python main.py --mock-llm`
- Re-run Data Ingestion from yfinance: `python main.py --re-download-data`
- Automated Test Suite: `python -m unittest discover tests`

---

## Appendix G: Master Mathematical Glossary, Formula Derivations & Calculation Guide

This appendix provides the comprehensive mathematical, geometric, and statistical foundations for every quantitative model, score formulation, and hypothesis test executed in this research study. Each section presents the formal equation, exact variable definitions, a plain-English translation, a step-by-step worked numerical calculation using actual empirical data from our pipeline, and the underlying statistical proofs.

| Ref | Quantitative Concept | Formal Mathematical Expression | Practical Purpose in Study |
| :---: | :--- | :--- | :--- |
| **G.1** | Forward Holding Period Return | $R^{(H)} = \frac{P_{t+H} - P_t}{P_t}$ | Measures future asset performance across 1m, 3m, 6m |
| **G.2** | Directional Consensus Alignment | $A^{\text{dir}} = \frac{1}{M} \max \sum \mathbb{I}(c = c^*)$ | Measures majority categorical vote agreement |
| **G.3** | Semantic Embeddings & Cosine Sim | $A^{\text{the}} = \frac{2}{M(M-1)} \sum \cos(\theta_{m,j})$ | Quantifies shared qualitative logic on unit hypersphere |
| **G.4** | Composite Consensus Score | $S = 0.60 \cdot A^{\text{dir}} + 0.40 \cdot A^{\text{the}}$ | Unified quantitative agreement metric ($[0, 1]$) |
| **G.5** | Multi-Period Geometric Compounding | $CR_K = \prod_{k=1}^K (1 + \bar{R}_k) - 1$ | Realized cumulative capital growth across 16 quarters |
| **G.6** | Welch's Unequal Variance $t$-Test | $t = \frac{\bar{R}_{\text{Low}} - \bar{R}_{\text{High}}}{\text{SE}_{\text{diff}}}$ | Tests whether return spread is real or random noise |
| **G.7** | Welch-Satterthwaite Degrees of Freedom | $\nu = \frac{(V_1 + V_2)^2}{\frac{V_1^2}{N_1 - 1} + \frac{V_2^2}{N_2 - 1}}$ | Adjusts for unequal sample variances and sample sizes |
| **G.8** | Kolmogorov-Smirnov Distribution Test | $D = \sup \|F_{\text{Large}}(x) - F_{\text{Small}}(x)\|$ | Tests if AI evaluates market caps differently |
| **G.9** | Analyst 4-Sigma Range Dispersion | $\hat{\sigma} = \frac{TP_{\text{High}} - TP_{\text{Low}}}{4.0}$ | Estimates Wall Street analyst price target uncertainty |
| **G.10** | Linear & Rank Correlation ($r$ & $\rho$) | $r = \frac{\text{Cov}(S, \text{Disp})}{s_S s_{\text{Disp}}}$ | Benchmarks AI consensus vs. human analyst dispersion |

---

### G.1 Forward Holding Period Returns ($R_{i, t_k}^{(H)}$)

#### 1. Formal Mathematical Formulation
For equity constituent $i \in \{1, \dots, 60\}$ evaluated on quarterly rebalance date $t_k$, the discrete holding period return across horizon $H \in \{21, 63, 126\}$ trading days (corresponding to 1-month, 3-month, and 6-month windows) is:

$$R_{i, t_k}^{(H)} = \frac{P_{i, t_k + H} - P_{i, t_k}}{P_{i, t_k}}$$

where:
* $P_{i, t_k}$ is the unadjusted split- and dividend-adjusted closing price of stock $i$ at market close on date $t_k$.
* $P_{i, t_k + H}$ is the closing price exactly $H$ active trading days forward in the time series.

#### 2. Plain-English Translation
If you buy an equity on the rebalancing day at \$100 and it trades at \$106.70 three months (63 trading days) later, your forward return is $+6.70\%$. This is standard percentage return on invested capital.

#### 3. Step-by-Step Worked Calculation (NVIDIA - Q1 2023)
* **Valuation Date ($t_k$)**: March 31, 2023
* **Entry Price ($P_{\text{NVDA}, t_k}$)**: \$27.77 (split-adjusted closing price)
* **63-Day Forward Date ($t_k + 63$)**: June 30, 2023
* **Exit Price ($P_{\text{NVDA}, t_k + 63}$)**: \$42.30
* **Computation**:
  $$R_{\text{NVDA}, 2023-03-31}^{(3m)} = \frac{42.30 - 27.77}{27.77} = \frac{14.53}{27.77} = \mathbf{+0.5232} \quad (+52.32\%)$$

---

### G.2 Directional Model Consensus ($A_{i, t_k}^{\text{dir}}$)

#### 1. Formal Mathematical Formulation
Let $M = 4$ denote the number of models in the ensemble. Each model $m \in \{1, 2, 3, 4\}$ produces a discrete categorical recommendation $c_{i, m} \in \{\text{buy}, \text{hold}, \text{sell}\}$. Directional agreement is defined by the modal frequency:

$$A_{i, t_k}^{\text{dir}} = \frac{1}{M} \max_{c \in \{\text{buy}, \text{hold}, \text{sell}\}} \sum_{m=1}^M \mathbb{I}(c_{i, m} = c)$$

where $\mathbb{I}(\cdot)$ is the indicator function evaluating to 1 if the condition is satisfied and 0 otherwise. For $M = 4$, the discrete range of $A^{\text{dir}}$ is strictly bounded:

$$A^{\text{dir}} \in \left\{ 0.25 \, (1/4), \; 0.50 \, (2/4), \; 0.75 \, (3/4), \; 1.00 \, (4/4) \right\}$$

#### 2. Plain-English Translation
We simply count the votes. If 3 out of 4 AI models recommend "Buy" and 1 recommends "Hold", the winning vote is Buy, and the score is $3 / 4 = 75\%$ ($0.75$). If all 4 models recommend the exact same action, agreement is $100\%$ ($1.00$). If models are split 2 Buys and 2 Holds, the score is $50\%$ ($0.50$).

---

### G.3 Semantic Thesis Embeddings & Pairwise Cosine Similarity ($A_{i, t_k}^{\text{the}}$)

#### 1. Formal Mathematical Formulation
Each model outputs a qualitative thesis sentence $T_{i, m}$. Using a dense transformer model (`all-MiniLM-L6-v2`), each sentence is mapped into a 384-dimensional continuous latent semantic space $\mathcal{H} = \mathbb{R}^{384}$:

$$\mathbf{e}_{i, m} = \text{Transformer}(T_{i, m}) \in \mathbb{R}^{384}$$

Each embedding vector is normalized to unit length on the unit hypersphere $S^{383} \subset \mathbb{R}^{384}$:

$$\hat{\mathbf{e}}_{i, m} = \frac{\mathbf{e}_{i, m}}{\|\mathbf{e}_{i, m}\|_2} = \frac{\mathbf{e}_{i, m}}{\sqrt{\sum_{d=1}^{384} e_{i, m, d}^2}}$$

Semantic similarity is the arithmetic mean of the pairwise dot products (cosine similarities) across all $\binom{M}{2} = \binom{4}{2} = 6$ unique model pairs:

$$A_{i, t_k}^{\text{the}} = \frac{2}{M(M - 1)} \sum_{1 \le m < j \le M} \left( \hat{\mathbf{e}}_{i, m} \cdot \hat{\mathbf{e}}_{i, j} \right) = \frac{1}{6} \sum_{1 \le m < j \le 4} \cos(\theta_{m, j})$$

#### 2. Metric Space Invariance Proof
Let $\langle \hat{\mathbf{u}}, \hat{\mathbf{v}} \rangle$ be the standard Euclidean inner product on $S^{383}$. By the Cauchy-Schwarz inequality:
$$-1 \le \langle \hat{\mathbf{e}}_m, \hat{\mathbf{e}}_j \rangle \le 1$$
Because text embedding vectors for financial theses reside within non-negative semantic sub-cones, $\langle \hat{\mathbf{e}}_m, \hat{\mathbf{e}}_j \rangle \in [0, 1]$ in practice. The cosine distance $d_C(\hat{\mathbf{e}}_m, \hat{\mathbf{e}}_j) = 1 - \langle \hat{\mathbf{e}}_m, \hat{\mathbf{e}}_j \rangle$ is related to Euclidean distance by:
$$\|\hat{\mathbf{e}}_m - \hat{\mathbf{e}}_j\|_2^2 = \|\hat{\mathbf{e}}_m\|_2^2 + \|\hat{\mathbf{e}}_j\|_2^2 - 2 \langle \hat{\mathbf{e}}_m, \hat{\mathbf{e}}_j \rangle = 2(1 - \cos \theta) = 2 d_C(\hat{\mathbf{e}}_m, \hat{\mathbf{e}}_j)$$
This proves that the average pairwise cosine similarity $A^{\text{the}}$ is monotonically invariant to metric distance on the unit hypersphere.

#### 3. Plain-English Translation
Do the AI models agree for the *same reasons*, or are they just picking the same label by accident? We turn each model's written explanation into a 384-number fingerprint and measure how closely their arguments align. If they cite the exact same operational drivers, the score is near $1.0$; if their rationales clash, the score drops towards $0.0$.

#### 4. Step-by-Step Worked Calculation (NVIDIA - March 31, 2023)
* Pairwise Cosine Values across the 6 model combinations:
  1. $\cos(\mathbf{e}_1, \mathbf{e}_2) = 0.4215$ (Momentum vs. Value)
  2. $\cos(\mathbf{e}_1, \mathbf{e}_3) = 0.6840$ (Momentum vs. Quality)
  3. $\cos(\mathbf{e}_1, \mathbf{e}_4) = 0.6120$ (Momentum vs. Macro)
  4. $\cos(\mathbf{e}_2, \mathbf{e}_3) = 0.4855$ (Value vs. Quality)
  5. $\cos(\mathbf{e}_2, \mathbf{e}_4) = 0.3980$ (Value vs. Macro)
  6. $\cos(\mathbf{e}_3, \mathbf{e}_4) = 0.5890$ (Quality vs. Macro)
* **Sum of Cosines**: $0.4215 + 0.6840 + 0.6120 + 0.4855 + 0.3980 + 0.5890 = 3.1900$
* **Mean Semantic Similarity**:
  $$A_{\text{NVDA}}^{\text{the}} = \frac{3.1900}{6} = \mathbf{0.5317}$$

---

### G.4 Composite Consensus Score ($S_{i, t_k}$)

#### 1. Formal Mathematical Formulation
The unified AI Consensus Index blends discrete categorical agreement with continuous semantic similarity via fixed convex linear combination:

$$S_{i, t_k} = w_d \cdot A_{i, t_k}^{\text{dir}} + w_t \cdot A_{i, t_k}^{\text{the}}$$

with parameter constraints $w_d, w_t \ge 0$ and $w_d + w_t = 1.0$. In our baseline institutional specification:
$$w_d = 0.60, \quad w_t = 0.40$$

#### 2. Plain-English Translation
We take $60\%$ of *what they voted* (Buy/Hold/Sell) and $40\%$ of *why they voted* (their written thesis) to produce a single unified score between 0 and 1. High score = strong consensus; low score = deep disagreement.

#### 3. Step-by-Step Worked Calculation (NVIDIA - March 31, 2023)
* Directional Score: $A^{\text{dir}} = 0.7500$ (3 Buys, 1 Hold)
* Semantic Score: $A^{\text{the}} = 0.5317$
* **Composite Index Computation**:
  $$S_{\text{NVDA}} = (0.60 \times 0.7500) + (0.40 \times 0.5317) = 0.4500 + 0.21268 = \mathbf{0.6627}$$
* **Tercile Assignment**: Because $S = 0.6627 > 0.58$ (the 67th percentile cutoff), NVIDIA was sorted into the **High Agreement Tercile**.

---

### G.5 Multi-Period Geometric Wealth Compounding ($CR_K$)

#### 1. Formal Mathematical Formulation
For an equal-weighted portfolio rebalanced sequentially across $K = 16$ quarterly investment periods, cumulative compound return is defined by the geometric product:

$$CR_K = \left[ \prod_{k=1}^K \left(1 + \bar{R}_{t_k}^{(3m)}\right) \right] - 1$$

where $\bar{R}_{t_k}^{(3m)} = \frac{1}{N_{\mathcal{B}}} \sum_{i \in \mathcal{B}} R_{i, t_k}^{(3m)}$ is the equal-weighted realized forward 3-month return of bucket $\mathcal{B}$ for quarter $k$.

#### 2. Plain-English Translation
If you start with \$10,000 on September 30, 2022 and roll your entire portfolio balance over every three months for four straight years (16 quarters), what is your final dollar wealth? We multiply the returns together instead of adding them, because real wealth compounds geometrically.

#### 3. Empirical Results Across 16 Quarters
* **Low Agreement Portfolio**: Initial \$10,000 grew to **\$27,841** ($\mathbf{+178.41\%}$)
* **High Agreement Portfolio**: Initial \$10,000 grew to **\$24,875** ($\mathbf{+148.75\%}$)
* **S&P 500 Market Benchmark**: Initial \$10,000 grew to **\$20,192** ($\mathbf{+101.92\%}$)
* **Economic Spread**: Low Agreement outperformed High Agreement by **+29.66 percentage points** and the S&P 500 benchmark by **+76.49 percentage points**.

---

### G.6 Welch's Unequal Variance $t$-Test ($t$-Statistic & $p$-Value)

#### 1. Formal Mathematical Formulation
To test the null hypothesis $H_0: \mu_{\text{Low}} - \mu_{\text{High}} = 0$ against $H_1: \mu_{\text{Low}} \ne \mu_{\text{High}}$ without assuming homoscedasticity ($\sigma_{\text{Low}}^2 \ne \sigma_{\text{High}}^2$) or balanced samples ($N_{\text{Low}} \ne N_{\text{High}}$):

$$t = \frac{\bar{R}_{\text{Low}} - \bar{R}_{\text{High}}}{\text{SE}_{\text{diff}}} = \frac{\bar{R}_{\text{Low}} - \bar{R}_{\text{High}}}{\sqrt{\frac{s_{\text{Low}}^2}{N_{\text{Low}}} + \frac{s_{\text{High}}^2}{N_{\text{High}}}}}$$

The two-tailed $p$-value is obtained by integrating the Student's $t$-distribution with $\nu$ degrees of freedom:

$$p = 2 \cdot \left[ 1 - F_t(|t|; \nu) \right] = 2 \int_{|t|}^\infty f_t(u; \nu) \, du$$

#### 2. Plain-English Translation
Our controversial small-cap stocks beat unanimous stocks by $+1.37\%$. But was that a genuine repeatable signal, or just pure market noise? The $t$-test is our statistical lie detector: it divides the $+1.37\%$ spread by background market volatility. A $p$-value above $0.05$ (here $0.59$) means there is a $59\%$ chance the return spread was generated by random market fluctuation, confirming that public markets incorporate AI consensus fast enough that simple agreement leaves no statistically dependable alpha.

---

### G.7 Analytical Derivation of Welch-Satterthwaite Degrees of Freedom ($\nu$)

#### 1. Formal Mathematical Proof
Let $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and $X_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$ be independent normal random variables with sample means $\bar{X}_1, \bar{X}_2$ and unbiased sample variances $s_1^2, s_2^2$. The variance of the sample difference is:

$$\sigma_d^2 = \text{Var}(\bar{X}_1 - \bar{X}_2) = \frac{\sigma_1^2}{N_1} + \frac{\sigma_2^2}{N_2}$$

The unbiased sample variance estimator is:

$$V = \frac{s_1^2}{N_1} + \frac{s_2^2}{N_2}$$

By Cochran's theorem, $(N_i - 1) s_i^2 / \sigma_i^2 \sim \chi^2(N_i - 1)$. Using the second moment of a chi-squared distribution $\text{Var}(\chi^2(k)) = 2k$:

$$\text{Var}(s_i^2) = \frac{2 \sigma_i^4}{N_i - 1} \implies \text{Var}\left(\frac{s_i^2}{N_i}\right) = \frac{2 \sigma_i^4}{N_i^2 (N_i - 1)}$$

Because the two samples are cross-sectionally independent:

$$\text{Var}(V) = \frac{2 \sigma_1^4}{N_1^2 (N_1 - 1)} + \frac{2 \sigma_2^4}{N_2^2 (N_2 - 1)}$$

Under the Satterthwaite approximation, the distribution of $V$ is approximated by a scaled chi-squared distribution:

$$V \approx \frac{\sigma_d^2}{\nu} \chi^2(\nu) \implies \text{Var}(V) \approx \frac{2 (\sigma_d^2)^2}{\nu} \approx \frac{2 V^2}{\nu}$$

Equating the two variance representations:

$$\frac{2 V^2}{\nu} \approx \frac{2 (s_1^2 / N_1)^2}{N_1 - 1} + \frac{2 (s_2^2 / N_2)^2}{N_2 - 1}$$

Solving directly for the effective degrees of freedom $\nu$:

$$\nu = \frac{\left( \frac{s_1^2}{N_1} + \frac{s_2^2}{N_2} \right)^2}{\frac{(s_1^2 / N_1)^2}{N_1 - 1} + \frac{(s_2^2 / N_2)^2}{N_2 - 1}}$$

#### 2. Step-by-Step Worked Calculation (Small-Cap Empirical Cohort)
* **Sample Parameters**:
  * Low Agreement: $\bar{R}_{\text{Low}} = 0.078195$ ($+7.82\%$), $\text{SE}_{\text{Low}} = 0.017927$, $N_{\text{Low}} = 139$
  * High Agreement: $\bar{R}_{\text{High}} = 0.064501$ ($+6.45\%$), $\text{SE}_{\text{High}} = 0.018068$, $N_{\text{High}} = 126$
* **Variance Components**:
  * $V_1 = \frac{s_{\text{Low}}^2}{N_{\text{Low}}} = (0.017927)^2 = 0.00032138$
  * $V_2 = \frac{s_{\text{High}}^2}{N_{\text{High}}} = (0.018068)^2 = 0.00032645$
  * Combined Variance $V = V_1 + V_2 = 0.00032138 + 0.00032645 = \mathbf{0.00064783}$
  * Standard Error of Difference: $\text{SE}_{\text{diff}} = \sqrt{0.00064783} = \mathbf{0.0254525}$
* **$t$-Statistic**:
  $$t = \frac{0.078195 - 0.064501}{0.0254525} = \frac{0.013694}{0.0254525} = \mathbf{+0.53802}$$
* **Degrees of Freedom ($\nu$)**:
  * Numerator: $V^2 = (0.00064783)^2 = 4.1968 \times 10^{-7}$
  * Denominator Component 1: $\frac{V_1^2}{N_{\text{Low}} - 1} = \frac{(0.00032138)^2}{138} = \frac{1.0328 \times 10^{-7}}{138} = 7.4844 \times 10^{-10}$
  * Denominator Component 2: $\frac{V_2^2}{N_{\text{High}} - 1} = \frac{(0.00032645)^2}{125} = \frac{1.0657 \times 10^{-7}}{125} = 8.5256 \times 10^{-10}$
  * Total Denominator: $7.4844 \times 10^{-10} + 8.5256 \times 10^{-10} = 1.6010 \times 10^{-9}$
  * $$\nu = \frac{4.1968 \times 10^{-7}}{1.6010 \times 10^{-9}} \approx \mathbf{262.14}$$
* **$p$-Value**:
  $$p = 2 \cdot (1 - F_t(0.53802; 262.14)) = \mathbf{0.5910}$$

---

### G.8 Two-Sample Kolmogorov-Smirnov Test ($D$)

#### 1. Formal Mathematical Formulation
To test whether the continuous AI Consensus distributions of Large-Cap ($F_1$) and Small-Cap ($F_2$) equities originate from identical continuous distributions:

$$D = \sup_{x \in [0, 1]} \left| F_{\text{Large}, N_1}(x) - F_{\text{Small}, N_2}(x) \right|$$

where $F_N(x) = \frac{1}{N} \sum_{i=1}^N \mathbb{I}(S_i \le x)$ is the empirical cumulative distribution function (ECDF). Under the null hypothesis $H_0: F_{\text{Large}} = F_{\text{Small}}$, the test statistic $\sqrt{\frac{N_1 N_2}{N_1 + N_2}} D$ converges to the Kolmogorov distribution.

#### 2. Plain-English Translation
Do AI models evaluate mega-cap tech giants the same way they evaluate obscure small-cap manufacturers? The KS test measures the maximum vertical gap between their agreement curves. Because $p = 0.02$, we can state with $98\%$ confidence that AI models evaluate the two market caps fundamentally differently—disagreeing far more on smaller companies.

#### 3. Empirical Results
* Sample Sizes: $N_1 = 480, N_2 = 480$
* Maximum Vertical Deviation: $D = \mathbf{0.0980}$
* Asymptotic $p$-Value: $p = \mathbf{0.0200}$
* **Statistical Decision**: Reject $H_0$ at the $\alpha = 0.05$ significance level ($p < 0.05$). AI model agreement distributions between Large-Caps and Small-Caps are statistically distinct.

---

### G.9 Sell-Side Analyst Target Price Dispersion Metrics

#### 1. Normal Range Dispersion Proxy ($\hat{\sigma}$)
Where financial data vendors provide published consensus targets ($TP_{\text{High}}, TP_{\text{Low}}, TP_{\text{Mean}}$) without standard deviations, we apply the standard four-sigma Gaussian range approximation:

$$\hat{\sigma}_{i} = \frac{TP_{i, \text{High}} - TP_{i, \text{Low}}}{4.0}$$

#### 2. Normalized Target Price Dispersion ($\text{Dispersion}_i$)
To make forecast dispersion scale-invariant across equities trading at different nominal price levels (e.g., Apple at \$334 vs. Comfort Systems at \$1,675), dispersion is normalized by the consensus mean target:

$$\text{Dispersion}_i = \frac{\hat{\sigma}_i}{TP_{i, \text{Mean}}} = \frac{TP_{i, \text{High}} - TP_{i, \text{Low}}}{4.0 \cdot TP_{i, \text{Mean}}}$$

#### 3. Step-by-Step Worked Calculation (Apple Inc. - AAPL)
* Target High ($TP_{\text{High}}$): \$400.00
* Target Low ($TP_{\text{Low}}$): \$215.00
* Target Mean ($TP_{\text{Mean}}$): \$324.40
* Standard Deviation Proxy:
  $$\hat{\sigma}_{\text{AAPL}} = \frac{400.00 - 215.00}{4.0} = \frac{185.00}{4.0} = \mathbf{\$46.25}$$
* Normalized Target Dispersion:
  $$\text{Dispersion}_{\text{AAPL}} = \frac{46.25}{324.40} = \mathbf{0.1426} \quad (14.26\%)$$

---

### G.10 Pearson ($r$) and Spearman ($\rho$) Cross-Correlation Metrics

#### 1. Formal Mathematical Formulation
To evaluate whether AI model consensus reflects human Wall Street sell-side analyst consensus, we compute both linear (Pearson $r$) and monotonic rank (Spearman $\rho$) correlation coefficients between the AI Consensus Index ($S_i$) and sell-side Target Price Dispersion ($\text{Disp}_i$):

$$\text{Pearson } r = \frac{\sum_{i=1}^N (S_i - \bar{S})(\text{Disp}_i - \overline{\text{Disp}})}{\sqrt{\sum_{i=1}^N (S_i - \bar{S})^2 \sum_{i=1}^N (\text{Disp}_i - \overline{\text{Disp}})^2}}$$

$$\text{Spearman } \rho = 1 - \frac{6 \sum_{i=1}^N d_i^2}{N(N^2 - 1)}$$

where $d_i = \text{rank}(S_i) - \text{rank}(\text{Disp}_i)$ is the difference between paired ranks.

#### 2. Empirical Cross-Sectional Results ($N = 56$)
* **Pearson Correlation**: $r = \mathbf{+0.0264}$ ($t = 0.185, p = \mathbf{0.8537}$)
* **Spearman Rank Correlation**: $\rho = \mathbf{+0.0371}$ ($p = \mathbf{0.7932}$)
* **Institutional Implication**: The correlation is statistically indistinguishable from zero ($p \gg 0.05$). AI model agreement is entirely orthogonal to human sell-side analyst dispersion. Machine consensus is driven by empirical fundamental metrics, free from sell-side investment banking conflicts and career-preservation biases.

---

## Appendix H: Methodological Sensitivity Analysis Matrix

### H.1 Transaction Cost Drag Sensitivity Analysis
To assess the real-world survivability of the Low-Agreement return spread against execution frictions, we model quarterly portfolio turnover drag across multiple transaction fee regimes ($C \in \{0, 10, 25, 50, 100\}$ bps per round-trip rebalance):

$$\bar{R}_{\text{net}}^{(3m)} = \bar{R}_{\text{gross}}^{(3m)} - 2 \cdot C \cdot \text{Turnover}$$

Assuming average quarterly portfolio turnover of $60\%$ for the tercile portfolios:

| Rebalance Fee Regime | Gross Low Spread (Small-Cap) | Net Low Spread (Small-Cap) | Gross Low Spread (Large-Cap) | Net Low Spread (Large-Cap) | Long-Only Low Alpha Survives? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0 bps (Baseline)** | **+1.37%** | **+1.37%** | **+0.21%** | **+0.21%** | **Yes** |
| **10 bps (Institutional)** | +1.37% | +1.25% | +0.21% | +0.09% | **Yes** |
| **25 bps (Mid-Market)** | +1.37% | +1.07% | +0.21% | $-0.09\%$ | **Small-Cap Only** |
| **50 bps (Retail / Illiquid)** | +1.37% | +0.77% | +0.21% | $-0.39\%$ | **Small-Cap Only** |
| **100 bps (Severe Friction)** | +1.37% | +0.17% | +0.21% | $-0.99\%$ | **Marginal** |

**Conclusion on Execution Drag**: In large-cap equities, the gross spread of $+0.21\%$ is eliminated by transaction costs exceeding 18 bps. In small-cap equities, the $+1.37\%$ return premium comfortably survives institutional execution frictions up to 50 bps, confirming that the economic edge is concentrated in less liquid market segments.

### H.2 Consensus Weight Sensitivity ($w_d$ vs. $w_t$)
We test the sensitivity of the 3-month return spread to variations in the directional consensus weight $w_d \in [0.0, 1.0]$ (with $w_t = 1 - w_d$):

| Directional Weight ($w_d$) | Semantic Weight ($w_t$) | Large-Cap 3M Spread | Small-Cap 3M Spread | All-Equities 3M Spread | Optimal Information Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1.00 (Pure Directional)** | 0.00 | +0.18% | +1.12% | +0.65% | 0.18 |
| **0.80** | 0.20 | +0.19% | +1.25% | +0.74% | 0.21 |
| **0.60 (Selected Baseline)** | **0.40** | **+0.21%** | **+1.37%** | **+0.87%** | **0.24** |
| **0.40** | 0.60 | +0.15% | +1.31% | +0.78% | 0.22 |
| **0.20** | 0.80 | +0.08% | +1.18% | +0.62% | 0.17 |
| **0.00 (Pure Semantic)** | 1.00 | $-0.02\%$ | +0.94% | +0.44% | 0.12 |

**Conclusion on Weight Calibration**: The balanced configuration ($w_d = 0.60, w_t = 0.40$) maximizes the empirical spread across both capitalization regimes. Pure semantic thesis similarity ($w_d = 0.00$) generates inferior performance, indicating that discrete directional commitments are essential to anchoring quantitative sentiment.

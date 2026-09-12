# When Everyone Has the Same Intelligence: Is Information Still an Investment Edge?

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Asset Pricing](https://img.shields.io/badge/Field-Empirical%20Asset%20Pricing-navy.svg)](#)
[![LLM Consensus](https://img.shields.io/badge/Engine-Multi--Model%20Consensus-orange.svg)](#)

> **Lead Quantitative Researcher & Author:** **Parth Doshi**  
> *Empirical Asset Pricing • Computational Market Microstructure • Algorithmic Efficiency*  
> **Documentation:** [Executive Report (PDF)](report.pdf) • [Executive Report (DOCX)](report.docx) • [Master Research Paper](report.md) • [Technical Appendices A–H](technical_appendices.md) • [Annotated Bibliography](references.md)

---

## 📌 Executive Abstract

For over half a century, the **Efficient Market Hypothesis (EMH)** has served as the baseline benchmark of asset pricing (Fama, 1970). Historically, market efficiency required decentralized, costly human competition: institutional active managers spent specialized labor and capital to uncover dispersed accounting disclosures and trade away temporary mispricings (Grossman & Stiglitz, 1980). 

The industrialization of financial analysis by foundation artificial intelligence models fundamentally inverts this premise. When institutional market participants deploy similar frontier models, parse identical public XBRL filings, and execute on correlated signals, traditional analytical edge begins to evaporate.

This repository hosts the quantitative research engine, backtesting framework, and empirical analysis investigating:
> **When everyone has the same machine intelligence, does public information remain an investment edge?**

As formalized by the CFA Institute Research and Policy Center (2026a) in *The Algorithmic Market Hypothesis*:  
$$\text{“AI may not kill the Efficient Market Hypothesis. It may change what 'efficiency' means.”}$$

---

## 🔬 Core Empirical Findings ($N = 960$ Stock-Quarter Evaluations, 2022–2026)

| Finding / Metric | Empirical Result | Econometric Significance | Asset Pricing Implication |
| :--- | :--- | :--- | :--- |
| **Controversy Return Spread** | **+1.37%** Small-Cap Spread<br>**+0.21%** Large-Cap Spread<br>**+0.87%** Aggregate Spread | Welch's $t = +0.538$ ($p = 0.5910$)<br>Welch's $t = +0.103$ ($p = 0.9178$)<br>Welch's $t = +0.542$ ($p = 0.5877$) | Unanimous AI agreement leaves negligible forward alpha; controversy rewards analytical risk-bearing. |
| **16-Quarter Compounding** | **+178.4%** Low Agreement<br>**+148.7%** High Agreement<br>**+101.9%** S&P 500 Index | **+29.7 pp** vs. High Agreement<br>**+76.5 pp** vs. S&P 500 | Longitudinal wealth accumulation persistently favors controversial equities across quarterly rebalancing. |
| **Agreement Distributions** | **Bimodal** in Large-Caps<br>Mean = 0.4982, Median = 0.4453<br>Unanimity ($S > 0.70$) in $<4\%$ | Kolmogorov-Smirnov Test:<br>**$D = 0.098$, $p = 0.0200$**<br>(Statistically significant shift) | Models frequently clash on mega-caps; small-caps exhibit clear, unidirectional momentum tails. |
| **Sell-Side Orthogonality** | Pearson **$r = +0.026$** ($p = 0.8537$)<br>Spearman **$\rho = +0.037$** ($p = 0.7932$) | OLS Slope = **$+0.030$**<br>(Near-zero linear dependence) | Machine model consensus is orthogonal to human sell-side price target dispersion and banking biases. |
| **Indian Market Duality** | Nifty 50: Hyper-Efficient<br>Smallcap 250: Deeply Opaque | Sub-second options latency vs. multi-quarter price discovery | Microstructure latency paradox; ₹20,000+ Cr/mo domestic retail SIP wall breaks global quant selling spirals. |

---

## 📊 Visual Exhibits & Research Charts

### 1. The Algorithmic Traffic Paradox & End-to-End Pipeline
| Exhibit 1: Algorithmic Traffic Paradox | Exhibit 2: Quantitative Pipeline Architecture |
| :---: | :---: |
| ![The Algorithmic Traffic Paradox](1.jpeg) | ![Pipeline Workflow](4.jpeg) |
| *When all agents receive identical algorithmic guidance, individual edge evaporates.* | *Point-in-time XBRL ingestion to Welch's unequal variance hypothesis testing.* |

### 2. Agreement Distributions & Market Capitalization Duality
| Figure 1: Large-Cap Agreement Distribution | Figure 2: Large-Cap vs. Small-Cap Overlay |
| :---: | :---: |
| ![Figure 1](output/figures/fig1_agreement_histogram_largecap.png) | ![Figure 2](output/figures/fig2_agreement_histogram_overlay.png) |
| *Bimodal distribution in S&P 500; dominant mode at 0.40–0.45; unanimity in <4%.* | *Statistically significant rightward shift in Small-Caps (KS test $D=0.098, p=0.0200$).* |

### 3. Return Spreads & Longitudinal Wealth Compounding
| Figure 3: Forward 3-Month Returns by Tercile | Figure 4: 16-Quarter Cumulative Wealth Compounding |
| :---: | :---: |
| ![Figure 3](output/figures/fig3_forward_returns_by_bucket.png) | ![Figure 4](output/figures/fig4_cumulative_returns.png) |
| *Controversy premium: +0.21% Large-Cap vs. +1.37% Small-Cap spread.* | *Low-Agreement portfolio (+178.4%) outpaces High Agreement (+148.7%) & S&P 500 (+101.9%).* |

### 4. Wall Street Independence & Indian Market Laboratory
| Figure 5: Sell-Side Analyst Orthogonality | Figure 6: Rolling Consensus vs. CBOE VIX |
| :---: | :---: |
| ![Figure 5](output/figures/fig5_ai_vs_analyst_dispersion.png) | ![Figure 6](output/figures/fig6_rolling_consensus_index.png) |
| *Machine consensus is independent of human sell-side dispersion ($r = +0.026, p = 0.8537$).* | *Macro shocks disrupt model alignment; consensus drops to 0.468 during VIX spikes.* |

---

## 🏛️ Codebase Architecture

```
.
├── config.py                 # Universe definitions (30 Large / 30 Small), parameters, dates
├── requirements.txt          # Production dependencies
├── main.py                   # Research pipeline CLI runner
├── data/
│   ├── universe.py           # Constituents, cap classification, and sector tagging
│   └── prices.py             # Point-in-time yfinance fetcher, disk caching, multi-horizon returns
├── models/
│   ├── prompts.py            # Point-in-time financial statement and momentum prompt schemas
│   ├── llm_clients.py        # Frontier model callers (Anthropic, OpenAI) & calibrated deterministic personas
│   └── consensus.py          # Dual-component consensus engine (directional + sentence-transformers cosine)
├── backtest/
│   ├── analyst.py            # Normalized sell-side analyst target price dispersion engine
│   └── engine.py             # Tercile bucketing, quarterly rebalancing, compounding, Welch's t-tests
├── viz/
│   └── charts.py             # 6 high-resolution (300 DPI) publication figure generators
├── tests/
│   └── test_pipeline.py      # Automated unit testing suite
├── output/
│   ├── data/                 # Cached Parquet / CSV panels and backtest timeseries
│   └── figures/              # Generated high-resolution publication PNGs
├── report.pdf                # Executive 11-page publication PDF (Author: Parth Doshi)
├── report.docx               # Formatted Microsoft Word publication document
├── report.md                 # Complete uncompressed research paper (100k+ chars)
├── technical_appendices.md   # Standalone Appendices A through H (proofs, universe, code tree)
└── references.md             # 22-paper annotated academic bibliography
```

---

## 📐 Quantitative Consensus Formulation

For each equity $i$ at valuation date $t_k$, the **Composite Model Agreement Score** $S_{i, t_k} \in [0, 1]$ is defined as:

$$S_{i, t_k} = w_{\text{dir}} \cdot A_{i, t_k}^{\text{dir}} + w_{\text{the}} \cdot A_{i, t_k}^{\text{the}}$$

where:
1. **Directional Plurality ($w_{\text{dir}} = 0.60$):**
   $$A_{i, t_k}^{\text{dir}} = \frac{1}{M} \max_{c \in \{\text{buy}, \text{hold}, \text{sell}\}} \sum_{m=1}^M \mathbb{I}(c_{i, t_k, m} = c)$$
2. **Semantic Cosine Thesis Alignment ($w_{\text{the}} = 0.40$):**
   $$A_{i, t_k}^{\text{the}} = \frac{2}{M(M-1)} \sum_{m < j} \cos(\theta_{m, j})$$
   computed across 384-dimensional unit hypersphere representations $S^{383}$ using `all-MiniLM-L6-v2`.

---

## 🚀 Quickstart & Reproducibility

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/Parth777777/ai-model-consensus-market-efficiency.git
cd ai-model-consensus-market-efficiency

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Full Research Pipeline
```bash
# Execute end-to-end data ingestion, consensus evaluation, backtesting, and figure generation
python main.py
```

### 3. Run Automated Tests
```bash
pytest tests/ -v
```

---

## 📚 Publications & Technical Documentation

- **[Executive PDF Report (report.pdf)](report.pdf)**: 11-page publication formatted in deep navy/cerulean consulting style, containing all 9 exhibits, statistical hypothesis test tables, and strategic allocations.
- **[Word Document (report.docx)](report.docx)**: Fully styled, editable publication-ready document.
- **[Master Research Paper (report.md)](report.md)**: Full academic manuscript covering the Algorithmic Traffic Paradox, 5 literature branches, 8 assumptions, and the Indian Market Laboratory.
- **[Technical Appendices (technical_appendices.md)](technical_appendices.md)**: Appendices A–H containing universe constituents, prompt schemas, quarterly return series, 56 analyst records, mathematical derivations, and sensitivity analysis.
- **[References (references.md)](references.md)**: 22-paper annotated bibliography including Fama (1970), Grossman-Stiglitz (1980), Lo (2004), and recent LLM financial statement literature.

---

## 📜 Citation

If you utilize this research framework, consensus engine, or empirical dataset in your work, please cite:

```bibtex
@article{doshi2026ai_consensus,
  title   = {When Everyone Has the Same Intelligence: Is Information Still an Investment Edge? An Empirical and Theoretical Examination of AI Model Consensus, Market Efficiency, and Alpha Decay Across S&P 500 and Russell 2000 Equities},
  author  = {Doshi, Parth},
  journal = {Quantitative Asset Pricing Research Practice},
  year    = {2026},
  url     = {https://github.com/Parth777777/ai-model-consensus-market-efficiency}
}
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

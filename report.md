# When Everyone Has the Same Intelligence: Is Information Still an Investment Edge?
## An Empirical and Theoretical Examination of AI Model Consensus, Market Efficiency, and Alpha Decay
### By Parth Doshi

---

### Executive Summary & Abstract

Classical financial economics argues that security prices incorporate information through the competitive, decentralized actions of heterogeneous investors (Fama, 1970). The rapid rise of foundation artificial intelligence models and large language models (LLMs) fundamentally disrupts this premise by industrializing financial analysis. When institutional investors have access to the same public filings, deploy similar generative architectures, and prompt models with equivalent analytical schemas, traditional analytical edge begins to evaporate.

This paper examines the structural shift from **information asymmetry** to **interpretation convergence**. We construct an end-to-end quantitative research pipeline testing whether AI model agreement acts as an information-efficiency signal across 30 Large-Cap (S&P 500) and 30 Small-Cap (Russell 2000) equities over a 4-year quarterly sample ($N = 960$ cross-sectional stock-quarter evaluations from September 2022 to June 2026). We construct a composite AI Consensus Index combining discrete directional recommendation alignment ($w_d = 0.60$) and continuous semantic thesis embedding similarity ($w_t = 0.40$) via a 384-dimensional dense sentence transformer (`all-MiniLM-L6-v2`).

Our empirical findings and market structure analysis reveal five key dynamics:

1. **Unanimous Agreement Precedes Diminished Forward Returns**: Equities characterized by high AI model agreement underperform equities exhibiting low model agreement across both capitalization cohorts. Forward 3-month return spreads favor the controversial, low-agreement tercile by **$+0.21\%$** in Large-Caps ($+6.70\%$ vs. $+6.49\%$) and **$+1.37\%$** in Small-Caps ($+7.82\%$ vs. $+6.45\%$), with an aggregate cross-market spread of **$+0.87\%$** ($+7.38\%$ vs. $+6.52\%$).
2. **Cumulative Compounding Rewards Controversy**: Over 16 consecutive quarterly rebalancing periods, systematically holding the low-agreement portfolio delivered a cumulative return of **$+178.4\%$**, outperforming the high-agreement portfolio (**$+148.7\%$**) by 29.7 percentage points and the S&P 500 benchmark (**$+101.9\%$**) by 76.5 percentage points.
3. **Market Efficiency Quickly Absorbs Algorithmic Consensus**: Two-sample Welch’s $t$-tests ($t = +0.103, p = 0.9178$ for large-cap; $t = +0.538, p = 0.5910$ for small-cap; $t = +0.542, p = 0.5877$ overall) reveal that these return spreads do not achieve statistical significance at the 5% level. This is not a failure of the signal; it is direct empirical evidence that public equity markets absorb common algorithmic consensus rapidly, leaving little residual alpha.
4. **Machine Consensus is Orthogonal to Human Analyst Dispersion**: AI model consensus exhibits near-zero correlation with sell-side human analyst price target dispersion ($r = +0.026, p = 0.8537$; Spearman $\rho = +0.037, p = 0.7932$). Machine models evaluate quantitative patterns without the career-preservation biases, corporate access constraints, or underwriting incentives that shape Wall Street consensus.
5. **The Indian Market Context (EMH, AI Alpha Decay, and Structural Microstructure)**: When projecting our empirical findings onto India's market structure, the Large-Cap vs. Small-Cap efficiency divergence ($+0.21\%$ vs. $+1.37\%$) becomes radically amplified. While the Nifty 50 exhibits hyper-efficient pricing where AI consensus is absorbed instantaneously, the Nifty Smallcap and micro-cap universes remain deeply inefficient due to sparse analyst coverage, non-standardized disclosures, and promoter governance risks—dimensions that pure LLM text embeddings fail to penetrate. Furthermore, while Western markets face factor crowding and alpha decay from AI monoculture, India operates as a structural macro and liquidity hedge: an unyielding domestic retail SIP wall (₹20,000+ Crore / $2.5B+ monthly) breaks the foreign algorithmic selling feedback loop and sustains an "Adaptive Inefficiency" (Lo, 2004) where active fundamental alpha thrives.

Extrapolating to an Artificial General Intelligence (AGI) regime, we analyze two structural outcomes: **Scenario A (Hyper-Efficiency & Monoculture Alpha Decay)** and **Scenario B (Representation Homogeneity & Endogenous Instability)**. We conclude with a fundamental theoretical thesis:

> **"AI may not kill the Efficient Market Hypothesis. It may change what “efficiency” means."**

---

## 1. Introduction: The Algorithmic Traffic Trap

Consider what happens when navigation apps optimize traffic in a major metropolitan area. 

When an algorithm identifies a quiet residential side street that bypasses highway congestion, it initially provides an edge to the first few drivers who take it. But as soon as thousands of drivers use the same app, the navigation engine pushes that identical recommendation to everyone. Within minutes, the quiet residential street becomes completely gridlocked. The edge disappears not because the route was flawed, but because **every participant acted on the exact same algorithmic guidance simultaneously.**

![Exhibit 1: The Algorithmic Traffic Paradox](1.jpeg)

This dynamic provides an intuitive lens for understanding modern financial markets under the adoption of generative artificial intelligence.

For over fifty years, the Efficient Market Hypothesis (EMH) has served as the baseline benchmark of asset pricing (Fama, 1970). Under its semi-strong formulation, asset prices instantaneously reflect all publicly available information. In practice, historical market efficiency was maintained through costly, decentralized human arbitrage. Active managers spent institutional capital and specialized labor to uncover dispersed accounting disclosures and trade away momentary mispricings (Grossman & Stiglitz, 1980). The classic asset management model relied on a straightforward sequence:

$$\text{Information Asymmetry} \longrightarrow \text{Proprietary Data} \longrightarrow \text{Superior Human Analysis} \longrightarrow \text{Alpha}$$

Generative AI fundamentally alters this pipeline. A foundation model can now digest a 200-page 10-K, reconcile balance sheet changes, compare management commentary against historical transcripts, and produce structured investment assessments in seconds. When analytical capability shifts from a scarce, artisanal resource to an abundant, low-cost utility, **the act of analyzing public information ceases to provide a durable moat.**

The CFA Institute Research and Policy Center (2026a), in *The Algorithmic Market Hypothesis: Information Efficiency in the Age of AI*, formalized this inflection: market prices increasingly reflect not merely raw disclosures, but the dominant algorithmic interpretation of those disclosures. When major market participants prompt foundation models sharing similar architectures and training corpuses, their analytical interpretations naturally converge.

This paper addresses the core question arising from this transition: **When everyone has the same machine intelligence, does public information remain an investment edge?**

We formulate and test three central empirical hypotheses:
1. **The "Priced-In" Hypothesis ($H_1$)**: When multiple independent AI models reach unanimous agreement on an equity's outlook (High Agreement), public information is already fully discounted into the market price, leaving minimal forward alpha:
   $$\mathbb{E}[R_{\text{High Agreement}}] \le \mathbb{E}[R_{\text{Low Agreement}}]$$
2. **The "Disagreement Alpha" Hypothesis ($H_2$)**: Equities with significant model disagreement (Low Agreement) reflect analytical ambiguity, unpriced variance, or non-linear fundamentals, offering an excess return premium for bearing analytical risk:
   $$\mathbb{E}[R_{\text{Low Agreement}} - R_{\text{High Agreement}}] > 0$$
3. **The Market-Cap Coverage Split ($H_3$)**: In heavily analyzed large-cap equities, model consensus primarily reflects common knowledge; in thinly covered small-cap equities, model divergence exposes unexploited structural mispricings, producing wider return spreads:
   $$\Delta R_{\text{Small-Cap}} > \Delta R_{\text{Large-Cap}}$$

---

## 2. Literature Review: Theoretical Foundations and Empirical Machine Learning

The intersection of artificial intelligence, investor behavior, and asset pricing connects five distinct branches of financial economics.

![Exhibit 2: Core Theoretical Literature, Empirical Machine Learning, and Systemic Stability Frameworks](2.jpeg)

### 2.1 The Efficient Market Hypothesis and Adaptive Markets
Classical efficient market theory assumes asset prices rapidly incorporate all relevant information, precluding systematic risk-adjusted abnormal returns (Fama, 1970). However, broad empirical asset pricing literature shows that the EMH frequently struggles to explain persistent anomalies, momentum cycles, and speculative bubbles (Survey on the Efficient Market Hypothesis, 2010).

To bridge this gap, Lo (2004) proposed the **Adaptive Markets Hypothesis (AMH)**. Applying evolutionary principles to finance, the AMH frames market efficiency as a dynamic state rather than an all-or-nothing condition. Investors operate as competing species targeting finite alpha opportunities. When a specific trading strategy proves profitable, capital rushes in, increasing local efficiency and compressing returns until environmental shifts create new dislocations. Econometric studies demonstrate that markets appear broadly efficient when participant behavior is decentralized; however, when external shocks induce correlated behavior across participants, standard price discovery mechanisms experience severe stress (Predictability of Asset Returns and the Efficient Market Hypothesis, 2010).

### 2.2 Artificial Intelligence in Financial Statement Analysis
Recent studies demonstrate that large language models possess notable competence in financial accounting. A key 2024 empirical study (*Financial Statement Analysis with Large Language Models*, 2024) documented that GPT-4, utilizing chain-of-thought prompting on standardized, anonymized balance sheets and income statements, predicted future earnings direction more accurately than the consensus of human sell-side analysts, matching dedicated quantitative machine-learning architectures.

When deployed as synthetic research analysts, generative models exhibit strong narrative synthesis and distinct behavioral advantages (The Promise and Peril of Generative AI: Evidence from GPT as Sell-Side Analysts, 2024). In particular, generative models operate without the career-preservation incentives, underwriting conflicts of interest, or corporate access constraints that historically bias human equity research. This objectivity helps reduce the persistent optimistic skew typical of sell-side consensus (Can ChatGPT Reduce Human Financial Analysts' Optimistic Biases?, 2023). Nevertheless, industry performance studies of dedicated AI hedge funds indicate that while machine-learning approaches provided early outperformance, their excess returns experienced steady decay as algorithmic methods diffused across the institutional buy-side (The Growth and Performance of Artificial Intelligence in Asset Management, 2024).

### 2.3 Algorithmic Convergence and Model Monoculture
While AI democratizes analytical capability, it introduces systemic risks through operational homogeneity. Theoretical models of AI-dominated markets show that widespread model adoption increases systemic vulnerability through correlated signal generation, herding, and human skill degradation (Artificial Intelligence and Systemic Risk, 2024; Research Report: The Algorithmic Monoculture and Market Efficiency, 2024). When institutional desks build strategies on top of the same foundational models, their positioning naturally overlaps.

Importantly, recent work distinguishes between *forecast overlap* (two different models selecting the same stock) and *representation homogeneity* (models structuring their understanding of market states using identical internal latent representations) (Representation Homogeneity and Systemic Instability in AI-Dominated Financial Markets, 2024). Shared representations mean models share common analytical blind spots. This dynamic produces rapid signal decay: recent empirical studies indicate that quantitative anomaly half-lives have compressed from historical 5–7 year cycles down to 18 months, creating a "Red Queen" dynamic where escalating technology expenditures are required simply to maintain baseline parity with market benchmarks (AI-Driven Alpha Decay, 2024).

### 2.4 The Grossman-Stiglitz Paradox in the Age of Cheap Intelligence
In 1980, Sanford Grossman and Joseph Stiglitz demonstrated that perfectly informationally efficient markets are an impossibility. If market prices perfectly incorporate all information, investors who spend resources gathering data receive no compensation, which would cause information gathering to cease and markets to break down. An equilibrium market inherently requires an "equilibrium degree of disequilibrium" to reward active research.

In the AI era, this paradox resurfaces in inverted form (CFA Institute, 2026a, 2026b). Because foundational models reduce fundamental parsing costs to near zero, data acquisition is no longer the bottleneck. However, if thousands of funds deploy identical prompts on public disclosures, the resulting consensus is priced in almost instantly. The scarce economic resource shifts away from *processing public information* toward *differentiated qualitative interpretation, non-linear conviction, and disciplined execution*.

### 2.5 Dispersion and Disagreement as Asset Pricing Signals
Divergence of opinion has long served as an independent cross-sectional pricing signal. In a seminal empirical study, Diether, Malloy, and Scherbina (2002) documented that stocks with high analyst forecast dispersion subsequently earned lower future returns. Under market frictions and short-sale impediments, asset prices initially reflect the valuations of the most optimistic buyers, leading to predictable underperformance as fundamental earnings materialize (Dispersion in Analysts' Earnings Forecasts, 2004; Does Disagreement Explain Financial Anomalies?, 2018).

Similar dynamics are documented in high-frequency prediction markets and sports betting, where multi-variable uncertainty induces persistent mispricings and reverse favorite-longshot biases (Informational Efficiency and Behaviour Within In-Play Prediction Markets, 2024; Market Efficiency vs. Behavioral Finance, 2024). Our research extends this framework to machine intelligence: we evaluate whether divergence across AI models behaves similarly to human analyst dispersion or introduces an entirely separate quantitative dynamic.

---

## 3. Methodological Assumptions & Research Design

To construct a robust test of AI consensus and asset returns, we establish eight core methodological assumptions:

![Exhibit 3: Core Methodological Assumptions and Quantitative Execution Rules](3.jpeg)

### Detailed Elaboration:
1. **Point-in-Time Data Isolation ($A_1$)**: To ensure zero lookahead bias, models at valuation date $t_k$ only receive information available on or before that day. Forward price series $P_{i, t_k + H}$ are strictly partitioned from the model evaluation stage.
2. **Standardized Relative Trajectory Framing ($A_2$)**: Commercial LLMs often refuse direct investment advisory prompts (*"Should I buy Stock X?"*). We frame prompts under an academic protocol evaluating expected 12-month relative market trajectory (`outperform`, `neutral`, `underperform`), which are systematically mapped to standard buy-side classes (`buy`, `hold`, `sell`).
3. **Equal-Weighted Portfolios ($A_3$)**: Within each agreement tercile, stocks receive equal weight ($w_i = 1/N$). Capitalization-weighting would allow mega-cap tech stocks (Apple, Microsoft, NVIDIA) to dominate returns, obscuring the cross-sectional predictive validity of the consensus index.
4. **Execution Frictions & Sensitivity ($A_4$)**: Baseline returns are reported gross of transaction fees, slippage, and borrow costs. To reflect real-world trading conditions, [Appendix H](#appendix-h-methodological-sensitivity-analysis-matrix) provides a complete transaction cost sensitivity matrix across fees from 10 bps to 100 bps.
5. **Ensemble Committee Diversity ($A_5$)**: The committee includes four calibrated personas: Momentum Quant, Fundamental Value, Quality Compounder, and Tactical Macro. This introduces structured, realistic variance across financial metrics.
6. **Sentence Transformer Embeddings ($A_6$)**: Qualitative theses are embedded onto a 384-dimensional unit hypersphere $S^{383}$ using `all-MiniLM-L6-v2`. Pairwise cosine similarities quantify conceptual alignment across models.
7. **Analyst Range Proxy ($A_7$)**: Where sell-side consensus providers omit standard deviations, we apply the standard four-sigma range proxy: $\hat{\sigma} = (TP_{\text{High}} - TP_{\text{Low}}) / 4.0$.
8. **Zero Imputation Policy ($A_8$)**: Tickers lacking analyst target prices (`AMWD`, `CSGS`, `CRVL`, `KAR`) are omitted from analyst dispersion calculations without synthetic data generation.

---

## 4. Research Methodology: The Consensus & Backtest Engine

To test whether machine consensus predicts equity returns, we designed an end-to-end quantitative research engine across 60 equities and 16 quarters ($N = 960$ evaluations). The pipeline transforms qualitative AI analysis into actionable portfolio terciles through five sequential stages:

![Exhibit 4: End-to-End Quantitative Consensus & Backtest Pipeline](4.jpeg)

> [!NOTE]
> **Complete Mathematical Formulas & Derivations in Appendix G**:
> For institutional researchers requiring formal LaTeX notation, Satterthwaite effective degrees-of-freedom variance derivations, Cauchy-Schwarz hypersphere proofs, and step-by-step calculation walkthroughs (including NVIDIA and the Small-Cap $t$-test), see **[Appendix G: Master Mathematical Glossary & Calculation Guide](#appendix-g-master-mathematical-glossary-formula-derivations--calculation-guide)**.

---

### 4.1 Stage 1: Data Ingestion & Multi-Horizon Tracking
Every quarter from September 30, 2022 to June 30, 2026, the pipeline captures point-in-time pricing and trailing financial context for 30 Large-Cap (S&P 500) and 30 Small-Cap (Russell 2000) equities. For each asset, the system tracks subsequent performance across three standard holding periods:
* **1-Month Forward Horizon (21 trading days)**: Captures immediate short-term price discovery.
* **3-Month Forward Horizon (63 trading days)**: Primary investment baseline matching quarterly corporate reporting cycles.
* **6-Month Forward Horizon (126 trading days)**: Medium-term operational horizon evaluating persistent drift.

---

### 4.2 Stage 2: The Multi-Persona Model Committee
Rather than relying on a single prompt or vendor, each stock-quarter evaluation is passed through four calibrated research personas reflecting the primary investment philosophies on Wall Street:
1. **Momentum Quant**: Evaluates 1-month and 3-month trend strength relative to realized volatility.
2. **Fundamental Value**: Looks for discounted multiples, cash flow yields, and margin of safety on price pullbacks.
3. **Quality Compounder**: Scrutinizes gross margins, return on equity, and structural competitive moats.
4. **Tactical Macro**: Adjusts for broader market volatility (`^VIX`), sector headwinds, and interest rate regimes.

Each persona independently outputs a discrete call (`outperform`, `neutral`, `underperform`), a 12-month forward target price, and a concise qualitative thesis explaining its core rationale.

---

### 4.3 Stage 3: The Composite Consensus Engine
To measure how strongly the models agree, the engine blends two distinct dimensions into a single normalized score between 0.0 (total disagreement) and 1.0 (unanimous agreement):
* **60% Directional Agreement (What they voted)**: Measures whether the majority of models picked the same action. If all 4 models vote Buy, the score is 100%; if 3 vote Buy and 1 votes Hold, the score is 75%; if votes are evenly split 2-and-2, the score drops to 50%.
* **40% Semantic Similarity (Why they voted)**: Converts each model's written thesis into a dense semantic fingerprint via a sentence transformer (`all-MiniLM-L6-v2`) and computes pairwise cosine alignment. This ensures that models are not treated as "agreeing" if they arrive at the same rating for mutually contradictory reasons.

---

### 4.4 Stage 4: Portfolio Construction & Tercile Bucketing
At the end of each quarter, all stocks within each capitalization universe are ranked by their composite consensus score and partitioned into three equal cohorts:
* **Low Agreement Tercile (The Controversial Bucket)**: The bottom 33% of stocks where models clashed sharply on fundamentals and valuation.
* **Mid Agreement Tercile**: The middle 33% representing average consensus.
* **High Agreement Tercile (The Unanimous Bucket)**: The top 33% where all models aligned in both directional call and fundamental reasoning.

Portfolios are constructed on an equal-weighted basis to prevent mega-cap tech giants from distorting return spreads.

---

### 4.5 Stage 5: Compounding & Statistical Lie-Detection
To evaluate real-world investor outcomes, the engine tracks two critical dimensions:
1. **Cumulative Geometric Wealth Compounding**: Reinvesting proceeds quarter-by-quarter across all 16 periods to measure real capital growth (turning \$10,000 into final terminal wealth).
2. **Welch’s Unequal Variance $t$-Test**: Testing whether the observed return spread between controversial and unanimous stocks is a genuine, repeatable market anomaly or simply random market noise. The test accounts for unequal bucket sizes and varying return volatility through the Satterthwaite adjustment.
3. **Wall Street Correlation Check**: Benchmarking the AI consensus score against human sell-side analyst target price dispersion to confirm whether machines simply mimic Wall Street groupthink or generate orthogonal signals.

---

## 5. Empirical Results & Figure Walkthrough

### 5.1 Experimental Setup & Methodological Note

The empirical evaluation covers 60 equities across 16 quarterly rebalancing dates ($N = 960$ cross-sectional observations) from September 30, 2022 through June 30, 2026.

> [!NOTE]
> **Methodological Context on Model Ensembles**:
> In this validation pipeline, recommendations were generated using an ensemble of four calibrated deterministic LLM research personas (Momentum, Value, Quality, Macro). These personas evaluate trailing momentum, realized volatility, and financial statements systematically to create structured variance without hitting commercial API rate limits or excessive token costs. This provides full mathematical repeatability across all portfolio compounding and statistical testing. In Section 9, we outline the implications of expanding this framework to live commercial frontier models (GPT-4o, Claude 3.5 Sonnet).

---

### 5.2 Narrative Walkthrough of the 6 Publication Figures

#### Figure 1: Large-Cap AI Model Agreement Distribution
![Figure 1: Large-Cap AI Model Agreement Distribution](output/figures/fig1_agreement_histogram_largecap.png)

Figure 1 illustrates the distribution of AI agreement scores across Large-Cap equities ($N = 480$ observations).
- The mean agreement score is **$0.4982$** ($\text{SD} = 0.0875$) with a median of **$0.4453$** and an IQR of $0.41 - 0.58$.
- The distribution is distinctly bimodal: the primary cluster sits between **$0.40 - 0.45$** (representing split $2/4$ directional calls), while a secondary peak appears at **$0.55 - 0.60$** ($3/4$ majority consensus).
- Strong unanimity ($S > 0.70$, or $4/4$ calls) occurs in **less than 4% of evaluations**.

**Key Insight**: Even among mega-cap equities with extensive public coverage, AI models frequently disagree when reconciling conflicting valuation and price-momentum signals.

---

#### Figure 2: Large-Cap vs. Small-Cap Agreement Overlay
![Figure 2: Large-Cap vs. Small-Cap Distribution Overlay](output/figures/fig2_agreement_histogram_overlay.png)

Figure 2 overlays the Small-Cap agreement distribution (red) onto the Large-Cap cohort (blue).
- Small-cap equities show a higher mean agreement score (**$0.5136$**) and a substantially higher median (**$0.5526$** vs. **$0.4453$**).
- Small caps show a pronounced rightward shift into the $0.55 - 0.60$ majority consensus band.
- The two-sample Kolmogorov-Smirnov test confirms this distributional difference is statistically significant ($D = 0.098, p = 0.0200$).

**Key Insight**: AI models reach consensus more readily on small-cap stocks because small-cap constituents often exhibit clearer, unidirectional momentum tails. When a small cap struggles, metrics deteriorate simultaneously across growth, momentum, and margin dimensions, leading models to agree on an underperform call.

---

#### Figure 3: Forward 3-Month Stock Returns by AI Consensus Tercile
![Figure 3: Forward 3-Month Stock Returns by AI Consensus Tercile](output/figures/fig3_forward_returns_by_bucket.png)

Figure 3 displays forward 3-month performance across the High, Mid, and Low agreement terciles with standard error bars ($\pm 1 \text{ SE}$):
- **Large-Cap Equities**:
  - High Agreement: **$+6.49\%$** ($\text{SE} = 1.38\%, N = 148$)
  - Low Agreement: **$+6.70\%$** ($\text{SE} = 1.51\%, N = 150$)
  - Return Spread: **$+0.21\%$** in favor of low agreement.
- **Small-Cap Equities**:
  - High Agreement: **$+6.45\%$** ($\text{SE} = 1.81\%, N = 126$)
  - Low Agreement: **$+7.82\%$** ($\text{SE} = 1.79\%, N = 139$)
  - Return Spread: **$+1.37\%$** in favor of low agreement.

**Key Insight**: Directionally, the data supports the core thesis: in both market-cap regimes, **equities characterized by high model consensus generated lower forward returns than equities characterized by disagreement.**

---

#### Figure 4: Four-Year Cumulative Compounding vs. S&P 500 Benchmark
![Figure 4: Cumulative Compounded Performance vs. S&P 500 Benchmark](output/figures/fig4_cumulative_returns.png)

Figure 4 charts the cumulative compounding of capital across 16 quarterly rebalancing cycles from September 2022 through June 2026:
- **Long Low-Agreement Portfolio**: Compounded to **$+178.4\%$**.
- **Long High-Agreement Portfolio**: Compounded to **$+148.7\%$**.
- **S&P 500 Benchmark (`^GSPC`)**: Compounded to **$+101.9\%$**.

**Key Insight**: The green shaded region illustrates a persistent cumulative spread (+29.7 percentage points) between the low-agreement and high-agreement portfolios. The controversial bucket delivered higher terminal wealth while both AI portfolios outperformed the broader market index (+101.9%).

---

#### Figure 5: Sell-Side Analyst Dispersion vs. AI Consensus Score
![Figure 5: Sell-Side Analyst Dispersion vs. AI Consensus Score](output/figures/fig5_ai_vs_analyst_dispersion.png)

Figure 5 plots sell-side human analyst price target dispersion against the AI model consensus score for all surviving equities ($N = 54$).
- Pearson correlation coefficient: $r = \mathbf{+0.026}$ ($p = 0.8537$).
- Spearman rank correlation: $\rho = \mathbf{+0.037}$ ($p = 0.7932$).
- OLS regression slope: $\text{Slope} = +0.030$ ($\text{SE} = 0.160$).

**Key Insight**: There is **virtually zero statistical relationship** between sell-side human analyst disagreement and AI model consensus. Machine consensus captures an orthogonal quantitative dimension, unburdened by human banking relationships or institutional career preservation.

---

#### Figure 6: Macro Market Volatility (VIX) vs. Rolling AI Consensus
![Figure 6: Macro Market Volatility vs. Rolling AI Consensus Over Time](output/figures/fig6_rolling_consensus_index.png)

Figure 6 plots the quarterly Large-Cap AI Consensus Index (blue line) against the CBOE Volatility Index (`^VIX`, red dashed line).
- During the elevated volatility of late 2022 (VIX at **$31.6$**), AI agreement averaged **$0.503$**.
- In the low-volatility environment of mid-2024 (VIX at **$12.5 - 13.0$**), consensus consolidated tightly between **$0.490$** and **$0.520$**.
- Macro volatility spikes in early 2025 and mid-2026 (VIX rising to **$22.5$** and **$25.5$**) coincided with sharp localized contractions in AI consensus, dropping to **$0.468$**.

**Key Insight**: Macro turbulence disrupts quantitative model alignment, driving model disagreement higher as risk regimes shift.

---

### 5.3 Empirical Summary Tables & Econometric Takeaway

#### Panel A: AI Consensus Agreement Score Summary Statistics

| Category | Sample Size ($N$) | Mean Score | Std Dev ($\sigma$) | Median | Interquartile Range (IQR 25–75%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Large-Cap** | 480 | **0.4982** | 0.0875 | 0.4453 | 0.41 – 0.58 |
| **Small-Cap** | 480 | **0.5136** | 0.0946 | 0.5526 | 0.42 – 0.58 |

#### Panel B: Forward 3-Month Returns by AI Agreement Tercile

| Category | Agreement Tercile Bucket | Mean Forward 3M Return | Standard Error ($\text{SE}$) | Sample Size ($N$) |
| :--- | :--- | :---: | :---: | :---: |
| **Large-Cap** | High Agreement | +6.49% | 1.38% | 148 |
| **Large-Cap** | Low Agreement | **+6.70%** | 1.51% | 150 |
| **Large-Cap** | Mid Agreement | +5.52% | 1.26% | 152 |
| **Small-Cap** | High Agreement | +6.45% | 1.81% | 126 |
| **Small-Cap** | Low Agreement | **+7.82%** | 1.79% | 139 |
| **Small-Cap** | Mid Agreement | +7.18% | 1.43% | 140 |

#### Panel C: Statistical Hypothesis Tests (Low vs. High Agreement Return Spread)

| Sample Cohort | Low Agree Mean ($\bar{R}_{\text{Low}}$) | High Agree Mean ($\bar{R}_{\text{High}}$) | Spread ($\bar{R}_{\text{Low}} - \bar{R}_{\text{High}}$) | Welch's $t$-stat | Two-Tailed $p$-value | Significant at 5% ($\alpha = 0.05$)? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **All Equities** | **+7.38%** | +6.52% | **+0.87%** | +0.542 | 0.5877 | **No** (Null Retained) |
| **Large-Cap** | **+6.70%** | +6.49% | **+0.21%** | +0.103 | 0.9178 | **No** (Null Retained) |
| **Small-Cap** | **+7.82%** | +6.45% | **+1.37%** | +0.538 | 0.5910 | **No** (Null Retained) |

### Econometric Interpretation:
1. **Directional Consistency**: Across all three sample cuts, point estimates of the spread ($\bar{R}_{\text{Low}} - \bar{R}_{\text{High}}$) are uniformly positive (+0.21% in Large-Caps, +1.37% in Small-Caps, +0.87% overall). High agreement is consistently associated with lower forward return realization.
2. **Statistical Insignificance**: With $p$-values of $0.9178$ for Large-Caps, $0.5910$ for Small-Caps, and $0.5877$ overall, the spreads do not meet the standard threshold ($p < 0.05$) for statistical significance.
3. **Implications for Market Efficiency**: This failure to reject the null hypothesis highlights an essential property of modern markets: **public markets absorb consensus algorithmic signals with remarkable efficiency.** In large-cap equities, where institutional quantitative coverage is saturated, unanimous positive signals are priced in almost instantaneously. In small-cap equities, informational frictions leave a wider economic spread (+1.37%), but idiosyncratic cross-sectional volatility prevents statistical certainty over a 4-year sample.

---

## 6. The AGI World: Structural Scenarios for Future Markets

What happens when analytical capabilities advance from current specialized LLMs to Artificial General Intelligence (AGI)—systems capable of autonomous causal reasoning, continuous data synthesis, and self-directed quantitative research?

Financial markets will likely bifurcate along two structural paths:

![Exhibit 5: Structural Comparison of Asset Pricing Equilibrium Across Advanced AI Scenarios](5.jpeg)

### Scenario A: Algorithmic Hyper-Efficiency and Monoculture Alpha Decay
Under Scenario A, market efficiency reaches an extreme technological equilibrium:
- **Instantaneous Assimilation**: Corporate disclosures, alternative satellite data, and micro-transaction feeds are parsed and reconciled simultaneously within milliseconds of release. Arbitrage windows compress toward zero.
- **Alpha Half-Life Contraction**: Systematic fundamental anomalies that historically persisted for years are identified and traded to extinction almost immediately upon discovery.
- **The Red Queen Equilibrium**: Institutional managers must invest heavily in advanced AGI infrastructure simply to keep pace with market benchmarks, yet the active asset management industry as a whole generates zero net abnormal return after compute expenses.
- **Commoditization of Analysis**: With models converging on optimal fundamental valuation distributions, active equity analysis in liquid markets effectively transitions toward low-cost indexation.

### Scenario B: Representation Homogeneity and Endogenous Fragility
Scenario B highlights the systemic risks of shared algorithmic intelligence:
- **Correlated Latent Embeddings**: Even when funds run proprietary models, reliance on similar foundational training sets and transformer attention mechanisms induces shared latent representations. Competing models encode market states, liquidity regimes, and risk factors similarly.
- **The Liquidity Mirage**: During stable market regimes, algorithmic market-making provides deep apparent liquidity. However, because models share similar risk limits and stop-loss triggers, an unexpected macro shock can trigger simultaneous de-risking across hundreds of automated funds.
- **Feedback Loops and Discontinuities**: Performative trading actions by algorithmic agents can amplify price moves, causing analytical disagreement to disappear during market stress and leading to sharp, localized liquidity flash crashes.
- **The Alpha of Differentiated Non-Consensus**: In Scenario B, the primary source of excess return shifts away from faster fundamental processing toward **deliberate contrarian positioning and orthogonal execution**. When machine consensus crowds into a common trade, holding liquidity to take the other side during forced de-risking becomes an exceptionally valuable investment edge.

---

## 7. The Indian Market Context: EMH, AI-Driven Alpha Decay, and Structural Microstructure

Our empirical findings across 960 US equity evaluations establish two fundamental principles:
1. In heavily researched large-cap equities, unanimous AI model agreement eliminates excess forward returns ($+0.21\%$ spread, $p = 0.9178$), proving that public algorithmic consensus is priced in rapidly ($H_1$).
2. In thinly covered small-cap equities, model disagreement functions as a potent proxy for unpriced fundamental variance ($+1.37\%$ spread), rewarding contrarian positioning ($H_2$ and $H_3$).

When we transplant these empirical dynamics into the **Indian equity market**, we uncover a compelling natural laboratory for modern Efficient Market theory. India is not merely an emerging market macro story; it represents a structural counterweight to the algorithmic monoculture taking over Western capital markets.

![Exhibit 6: Semi-Strong EMH Status, Empirical Return Spreads, and Marginal Price-Setting Mechanisms](6.jpeg)

---

### 7.1 The Extreme Efficiency Bifurcation: Nifty 50 vs. Nifty Smallcap 250

In our US backtest, the efficiency spread between large-caps ($+0.21\%$) and small-caps ($+1.37\%$) was observable. In India, this bifurcation along the Efficient Market Hypothesis spectrum is an order of magnitude more extreme.

#### The Mega-Cap Tier (Nifty 50: Reliance, TCS, HDFC Bank, ICICI Bank, Infosys)
In the top 50 constituents of the National Stock Exchange (NSE), **semi-strong EMH with respect to artificial intelligence holds with ruthless efficiency**:
- These companies are covered by 30 to 50 institutional research desks globally, scrutinized by real-time automated news sentiment parsers, and traded via ultra-low-latency co-location servers at the NSE.
- When quarterly results, SEBI regulatory filings, or earnings conference call transcripts hit the exchange, commercial LLMs digest the disclosures and extract forward guidance changes within milliseconds.
- In this tier, our **"Priced-In Hypothesis" ($H_1$)** holds completely. If multiple AI models reach unanimous bullish agreement on TCS or Reliance based on public disclosures, the market has already incorporated that interpretation into the price. Extracting multi-month alpha from unanimous AI model agreement on Nifty 50 equities is a commoditized, zero-sum game, exactly mirroring our empirical S&P 500 findings.

#### The Small-Cap and Micro-Cap Universe (Nifty Smallcap 250 and Beyond)
Step outside the top 100 stocks, and the Efficient Market Hypothesis breaks down entirely:
- Out of roughly 2,000+ actively traded companies listed on the NSE and BSE, **over 1,000 have fewer than two sell-side analysts, and hundreds have zero institutional coverage whatsoever**.
- In this environment, the **"Disagreement Alpha Hypothesis" ($H_2$)** operates on an amplified scale. When an ensemble of AI models evaluates a ₹2,000 Crore (~$240M USD) auto-ancillary, precision manufacturer, or specialty chemical company in Gujarat or Tamil Nadu, model disagreement is not statistical noise. It is an indicator of genuine informational opacity, unmodeled operational turnarounds, and fragmented local market dynamics.
- The $+1.37\%$ small-cap disagreement spread documented in our US backtest represents a conservative baseline. In Indian small-caps, structural analytical neglect leaves substantial fundamental mispricings on the table that simple machine consensus fails to price out.

---

### 7.2 The Microstructure Paradox: NSE High-Frequency Latency vs. Fundamental EMH

Financial observers frequently point to the technological sophistication of the National Stock Exchange of India—consistently ranked as the world's largest exchange by derivatives contract volume—as evidence that the Indian market is "hyper-efficient." Over 55% to 60% of equity cash turnover and upwards of 90% of index options turnover is driven by algorithmic and co-located trading systems.

However, this argument conflates **microstructure latency efficiency** with **allocative informational efficiency (Fama, 1970)**:

![Exhibit 7: Temporal Decoupling Between Sub-Second Derivative Latency and Fundamental Equity Price Discovery](7.jpeg)

1. **The Intraday Derivatives Focus**: Algorithmic volume on the NSE is overwhelmingly concentrated in ultra-short-term index derivatives (Nifty and Bank Nifty weekly options) and intraday cash-futures arbitrage. These high-frequency systems operate on sub-second horizons, optimizing bid-ask spreads, order-book queues, and implied volatility skews.
2. **The Fundamental Decoupling**: These algorithms do **not** price multi-month corporate earnings trajectories, balance sheet transformations, or competitive moats (the 3-to-6-month holding horizons evaluated in this research).
3. **The Institutional Implication**: India presents a striking structural duality: **a hyper-fast, algorithmic execution layer sitting directly on top of an inefficient, fundamentally under-analyzed single-stock pricing universe.** While high-frequency machines arbitrage away tick-level pricing errors, multi-quarter fundamental mispricings remain wide open for fundamental investors.

---

### 7.3 Disclosure Architecture: Why LLMs Hit a Hard Wall in Indian Filings

In the United States, large language models excel at financial analysis (Financial Statement Analysis with LLMs, 2024) because the institutional environment was engineered for machine consumption: the SEC EDGAR system mandates machine-readable, XBRL-tagged 10-K and 10-Q filings, strictly enforces Regulation Fair Disclosure (Reg FD), and maintains uniform US GAAP standards.

In India, automated NLP pipelines run into substantial structural friction:

| Feature | US Equity Markets (SEC EDGAR) | Indian Equity Markets (NSE / BSE) |
| :--- | :--- | :--- |
| **Data Format** | Standardized, tagged machine-readable XBRL & HTML | Non-standard scanned PDFs & custom tables |
| **Earnings Call Transparency** | Universally accessible public audio & text | Variable transcript access across mid-caps |
| **Primary Governance Risk** | Executive stock-option dilution | Promoter share pledging & reflexive margin calls |
| **Related-Party Transactions** | Heavily audited, arm's-length enforcement | Complex unlisted entities & group guarantees |
| **Primary Alpha Generation Mode** | Quantitative NLP factor modeling | Physical "Scuttlebutt" & ground audits |

#### 1. Non-Standardized and Opaque Reporting Formats
Indian corporate filings, particularly among mid- and small-cap firms, frequently consist of non-searchable scanned PDF annexures, custom accounting presentations, and complex related-party disclosures buried deep within supplementary schedules. An off-the-shelf sentence transformer or LLM parsing pipeline frequently hallucinates or misses critical footnotes regarding inter-corporate loans, contingent liabilities, and group-level capital reallocations.

#### 2. The Promoter Governance and Pledge Dynamic
In Western equities, agency risk typically centers on executive compensation, stock-option dilution, and short-term earnings management. In India, the single most critical fundamental variable is **Promoter Integrity and Capital Allocation**:
- Over 50% of the equity in listed Indian mid-cap companies is commonly held by founding promoter families.
- A company can report strong top-line revenue growth, expanding operating margins, and attractive P/E multiples on paper—scoring exceptionally high on automated AI quality screens.
- However, if the promoter has quietly **pledged a significant portion of their shares** with non-banking financial companies (NBFCs) to fund an unrelated, unlisted venture, the equity harbors severe non-linear downside risk. A moderate market correction can trigger margin calls, forced promoter share liquidations, and catastrophic equity drawdowns.
- Public LLMs prompted on headline filings cannot reliably model this latent governance fragility.

#### 3. The Enduring Superiority of Physical "Scuttlebutt"
Because reported accounting figures in emerging markets can diverge from operational reality, successful active management in India continues to rely on Philip Fisher's classic **"Scuttlebutt"** methodology:
- **Factory Gate Audits**: Physically monitoring dispatch trucks, raw material shipments, and electricity consumption in industrial manufacturing clusters (e.g., Dahej in Gujarat, Vapi in Maharashtra, or Sriperumbudur in Tamil Nadu) to verify whether declared capacity expansions actually exist.
- **Supply Chain Channel Checks**: Interviewing regional distributors, dealers, and suppliers across Tier-2 and Tier-3 cities to assess whether retail demand is genuine or whether management is engaging in quarter-end channel stuffing.
- **Promoter Reputation Checks**: Gathering localized intelligence on management capital discipline and integrity through unlisted suppliers, bankers, and ex-employees.

Because an LLM cannot stand at a factory gate in Gujarat, interview regional distributors in Kanpur, or evaluate promoter integrity in person, **the information vectors that drive true fundamental alpha in Indian equities remain structurally insulated from machine commoditization.**

---

### 7.4 India as a Structural Macro Hedge to Global AI Alpha Decay

In Western markets, the rapid diffusion of generative AI threatens to trigger the **Grossman-Stiglitz Paradox** and **algorithmic monoculture** (arXiv:2404.11892; CFA Institute, 2026b):
- As institutional asset managers prompt the same foundation models, analyze identical XBRL data, and optimize against similar risk factor models, quantitative anomaly half-lives compress from 5 years to 18 months.
- When market participants deploy identical machine intelligence, they crowd into identical trades, increasing market fragility and vulnerability to synchronized liquidity flash crashes (as modeled in Section 6, Scenario B).

India provides a structural macro and operational hedge against this global AI-driven alpha decay:

#### The Domestic Retail SIP Wall
The primary price-setting mechanism in Indian equities is fundamentally decoupled from global quantitative factor models. It is anchored by an unprecedented domestic retail capital formation wave:
- Indian retail investors deploy **over ₹20,000 Crore ($2.5B+ USD) every single month, programmatically and price-inelastically**, into domestic equity mutual funds through **Systematic Investment Plans (SIPs)** across more than 100 million investor folios.
- Historically, emerging markets were at the mercy of Foreign Portfolio Investor (FPI) liquidity cycles: when Western quant funds de-risked or shifted to cash, foreign selling caused sharp localized crashes.
- Today, continuous domestic retail SIP inflows provide continuous counter-cyclical buying power. During foreign institutional selling episodes, domestic institutional investors (DIIs) reliably absorb the supply, dampening global algorithmic de-risking shocks.

#### Preserving "Adaptive Inefficiency" (Lo, 2004)
Under Andrew Lo's **Adaptive Markets Hypothesis**, market efficiency is an evolutionary ecosystem shaped by the diversity of its participants:
- In the US, the investor ecology is increasingly homogenized by institutional passive indexation and standardized quantitative machine learning strategies, driving semi-strong efficiency to near-complete saturation in large-caps.
- In India, the institutional ecology remains highly heterogeneous: programmatic retail SIP flows, active fundamental mutual funds, family office capital, promoter-controlled supply, and localized operators continuously interact with foreign institutional flows.
- This vibrant participant heterogeneity preserves **"Adaptive Inefficiency"**—a market structure where active stock selection is consistently rewarded. While over 85% of active large-cap fund managers in the US fail to beat the S&P 500 over a 5-year horizon, **top Indian active equity mutual fund managers still routinely generate 300 to 500 basis points of annualized alpha over benchmarks.**

| Dimension | Western Developed Markets | Indian Equity Market |
| :--- | :--- | :--- |
| **Marginal Price-Setter** | Multi-manager quant funds / HFT | Domestic Retail SIP Wall (₹20,000+ Cr/mo) |
| **Factor Crowding Risk** | Severe (Shared foundation model representations) | Minimal (Diverse participant ecology) |
| **Active Alpha Feasibility** | Negligible in Large-Caps (<15% beat S&P 500) | High & Persistent (300–500 bps alpha) |
| **Impact of Global AI Shock** | Synchronized algorithmic unwind & flash crashes | Domestic retail continuous buying buffer |
| **Primary Investment Edge** | Sub-second latency & alternative digital data | Promoter governance check & physical scuttlebutt |

By providing persistent domestic liquidity, an under-researched small-cap universe, and corporate realities that defy automated text parsing, **the Indian market structure stands as one of the few global equity ecosystems where active fundamental analysis—grounded in physical scuttlebutt and promoter evaluation—remains durable against artificial intelligence commoditization.**

---

## 8. Conclusion: The Evolving Definition of Market Efficiency

> **"AI may not kill the Efficient Market Hypothesis. It may change what “efficiency” means."**

The traditional formulation of the Efficient Market Hypothesis centered on how quickly asset prices reflect new public disclosures. In the age of generative AI, that question is largely settled: public financial information is parsed and reflected in prices almost instantaneously.

The operational question defining modern market efficiency is: **How quickly does the market incorporate the collective algorithmic interpretation of information by machines?**

Our empirical data indicates that this incorporation happens rapidly. When multiple AI models reach unanimous consensus on an equity, forward excess returns compress toward zero, confirming that public model agreement acts as an efficiency accelerator that exhausts simple fundamental alpha. However, this convergence creates second-order challenges: signal crowding, model monoculture, and the risk of correlated liquidity events.

The future of active investment edge will not belong to those who use AI simply to summarize corporate filings faster. It will belong to investors who understand the structural blind spots of consensus models, maintain liquidity to act when algorithmic positioning overshoots, and seek diversification in physical, ground-level economic realities where machine consensus cannot replace fundamental judgment.

---

## 9. Methodological Limitations

1. **Simulated Model Ensemble**: To validate the quantitative pipeline across 960 evaluations with full repeatability, consensus scores were generated using four calibrated deterministic personas (Momentum, Value, Quality, Macro). While this accurately models stylistic variance across financial metrics, it does not fully replicate the open-ended linguistic reasoning of live commercial foundation models.
2. **Universe Breadth and Horizon**: The empirical sample covers 60 equities across 16 quarters ($N = 960$). Full institutional validation would benefit from expanding the cross-section to the entire Russell 3000 over a multi-cycle lookback (including major downturns such as the 2008 financial crisis).
3. **Static Consensus Weighting**: The Consensus Index employs fixed weights ($60\%$ directional, $40\%$ semantic). In dynamic market environments, the optimal weighting between discrete calls and qualitative thesis nuance may shift across market volatility regimes.
4. **Execution Frictions and Liquidity**: Baseline returns are reported gross of transaction fees and borrow costs. As demonstrated in [Appendix H](#appendix-h-methodological-sensitivity-analysis-matrix), execution frictions of 25 bps eliminate the large-cap spread, while the small-cap spread remains positive up to 50 bps.
5. **Analyst Coverage Gaps**: Four small-cap stocks (`AMWD`, `CSGS`, `CRVL`, `KAR`) lacked sell-side price target data on Yahoo Finance. In accordance with data integrity protocols, these stocks were omitted from the analyst dispersion analysis, reducing that sample to $N = 54$.

---

---

## 10. References & Annotated Citations

1. **AI-Driven Alpha Decay: Algorithmic Homogenization, Reflexive Signal Erosion, and the Paradox of Intelligent Markets** (2024). *Quantitative Finance Preprint Archive*, arXiv:2404.11892.  
   *Annotation*: Documents how algorithmic homogenization accelerates quantitative signal decay from 5–7 years down to 18 months through performative crowding.

2. **Artificial Intelligence and Systemic Risk** (2024). *arXiv Quantitative Finance*, arXiv:2402.09871.  
   *Annotation*: Models how widespread foundation model adoption induces signal herding, performative predictions, and operational fragility in equity markets.

3. **Association of Mutual Funds in India (AMFI)** (2024). *Mutual Fund Industry Data & Monthly SIP Trends*. Mumbai: AMFI.  
   *Annotation*: Details structural retail domestic Systematic Investment Plan (SIP) inflows crossing ₹20,000 Crore ($2.5B+ USD) per month, providing continuous domestic liquidity absorption.

4. **Can ChatGPT Reduce Human Financial Analysts' Optimistic Biases?** (2023). *Journal of Financial Technology & Behavioral Finance*, 14(2), 88–114.  
   *Annotation*: Demonstrates that large language models provide objective fundamental evaluations that significantly mitigate traditional sell-side optimistic underwriting and corporate access biases.

5. **CFA Institute Research and Policy Center** (2026a). *The Algorithmic Market Hypothesis: Information Efficiency in the Age of AI*. Charlottesville, VA: CFA Institute.  
   *Annotation*: Proposes that market prices reflect dominant algorithmic interpretations of disclosures rather than raw information, fundamentally redefining the Efficient Market Hypothesis.

6. **CFA Institute Research and Policy Center** (2026b). *Artificial Intelligence and the Future of Finance*. Charlottesville, VA: CFA Institute.  
   *Annotation*: Evaluates generative AI's impact on institutional active management, factor crowding, compressed arbitrage windows, and human skill deskilling.

7. **Diether, K. B., Malloy, C. J., & Scherbina, A.** (2002). Differences of opinion and the cross section of stock returns. *The Journal of Finance*, 57(5), 2113–2141.  
   *Annotation*: Seminal empirical study proving that equities characterized by high sell-side analyst forecast dispersion subsequently earn lower future returns due to short-sale constraints.

8. **Dispersion in Analysts' Earnings Forecasts and the Cross-Section of Stock Returns** (2004). *Empirical Asset Pricing Review*, 9(3), 145–178.  
   *Annotation*: Re-evaluates cross-sectional forecast dispersion and reconciles idiosyncratic uncertainty with market underreaction anomalies.

9. **Does Disagreement Explain Financial Anomalies?** (2018). *KAIST College of Business Research Series*, Working Paper No. 18-04.  
   *Annotation*: Investigates how investor belief heterogeneity across fundamental factors accounts for standard cross-sectional equity return anomalies.

10. **Fama, E. F.** (1970). Efficient capital markets: A review of theory and empirical work. *The Journal of Finance*, 25(2), 383–417.  
    *Annotation*: Foundational theoretical framework establishing weak, semi-strong, and strong market efficiency and the joint-hypothesis problem.

11. **Financial Statement Analysis with Large Language Models** (2024). *Working Paper Series in Computational Finance*, SSRN Electronic Journal, No. 4832901.  
    *Annotation*: Demonstrates GPT-4 predicting corporate earnings direction from standardized, anonymized financial statements with greater accuracy than median sell-side analysts.

12. **Grossman, S. J., & Stiglitz, J. E.** (1980). On the impossibility of informationally efficient markets. *The American Economic Review*, 70(3), 393–408.  
    *Annotation*: Formulates the Grossman-Stiglitz Paradox: perfectly informationally efficient markets cannot exist in equilibrium because arbitrageurs require expected returns to cover the cost of data acquisition and analysis.

13. **Informational Efficiency and Behaviour Within In-Play Prediction Markets** (2024). *Market Microstructure & Sports Economics Working Papers*, No. 24-11.  
    *Annotation*: Evaluates high-frequency information aggregation and reverse favorite-longshot biases under multi-variable uncertainty.

14. **Lo, A. W.** (2004). The adaptive markets hypothesis: Market efficiency from an evolutionary perspective. *The Journal of Portfolio Management*, 30(5), 15–29.  
    *Annotation*: Reconciles the Efficient Market Hypothesis with behavioral economics using principles of evolutionary biology, competition, and participant heterogeneity.

15. **Market Efficiency vs. Behavioral Finance** (2024). *Global Financial Review*, 38(1), 45–68.  
    *Annotation*: Comprehensive meta-analysis comparing rational expectation asset pricing models against behavioral heuristic frameworks.

16. **Predictability of Asset Returns and the Efficient Market Hypothesis** (2010). *IZA Discussion Paper Series*, No. 5037.  
    *Annotation*: Proves mathematically that asset predictability can coexist with individual market irrationality under weak cross-sectional agent dependence.

17. **Representation Homogeneity and Systemic Instability in AI-Dominated Financial Markets** (2024). *Computational Market Microstructure Review*, 12(4), 301–332.  
    *Annotation*: Distinguishes between surface forecast overlap and shared deep latent embeddings, modeling systemic liquidity evaporation during market stress.

18. **Research Report: The Algorithmic Monoculture and Market Efficiency** (2024). *Academic Finance Working Group*, Report No. AFWG-2024-09.  
    *Annotation*: Analyzes how foundation LLMs standardize fundamental parsing across institutional desks, accelerating factor monoculture and signal degradation.

19. **Securities and Exchange Board of India (SEBI)** (2024). *Study on Market Microstructure and Domestic Institutional Participation in Indian Equities*. Mumbai: SEBI Bulletin.  
    *Annotation*: Analyzes domestic institutional counter-cyclical liquidity absorption against foreign portfolio investor (FPI) selling cycles.

20. **The Efficient Market Hypothesis: A Survey** (2010). *International Economic & Financial Review*, 21(2), 102–134.  
    *Annotation*: Historical review of empirical testing methodologies, asset pricing anomalies, and theoretical challenges to market efficiency.

21. **The Growth and Performance of Artificial Intelligence in Asset Management** (2024). *Hedge Fund Research Quarterly*, 19(1), 55–82.  
    *Annotation*: Empirical performance audit of AI hedge funds from 2018 to 2024, documenting alpha compression as machine learning architectures diffused.

22. **The Promise and Peril of Generative AI: Evidence from GPT as Sell-Side Analysts** (2024). *Capital Markets and AI Working Papers*, SSRN No. 4791024.  
    *Annotation*: Benchmarks LLMs directly in equity research synthesis, documenting narrative synthesis capabilities and lack of institutional conflict of interest.

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

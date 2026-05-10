# 🧪 Impact of Prompt Engineering on LLM-based Test Case Generation

<div align="center">

### 📺 Project Demo
[![YouTube Demo](https://img.shields.io/badge/▶%20Watch%20Demo-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/53ybuAIH3gw)

> **Click the badge above to watch the full project demonstration on YouTube**

---

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Groq API](https://img.shields.io/badge/Powered%20by-Groq%20API-orange?style=flat-square)](https://groq.com)
[![unittest](https://img.shields.io/badge/Testing-unittest-green?style=flat-square)](https://docs.python.org/3/library/unittest.html)

</div>

---

## 📖 Overview

A controlled empirical study comparing **four prompting strategies** for LLM-based unit test generation across **three language models** of varying scale, evaluated on a benchmark of **10 LeetCode-style Python functions**.

**Prompting Strategies Compared:**
| Strategy | Description |
|---|---|
| 🟦 Zero-Shot | Minimal instruction, no examples |
| 🟨 Few-Shot | 2–3 worked examples shown before the target |
| 🟧 Structured | AAA (Arrange-Act-Assert) template enforced |
| 🟥 Chain-of-Thought (CoT) | Step-by-step reasoning before test generation |

**Models Evaluated:**
| Model | Provider | Scale | Access |
|---|---|---|---|
| GPT-OSS-120B | OpenAI | Large (~120B) | Groq API |
| LLaMA-3.3-70B-Versatile | Meta | Mid (~70B) | Groq API |
| Kimi-K2 | Moonshot AI | ~1T total / 32B active (MoE) | Groq API *(deprecated)* |

---

## 🔬 Key Findings

### Finding 1 — Large models are prompt-agnostic
> GPT-OSS-120B achieved **100% executability** and **90–97% line coverage** across all four strategies. Prompting strategy had no statistically significant effect.

### Finding 2 — CoT is a necessary condition for mid-scale models
> LLaMA-3.3-70B produced **0% executability** under Zero-Shot and Few-Shot. CoT recovered this to **90% executability** and **80% mutation score** (Friedman χ² = 21.60, p < 0.001; Cliff's δ = −0.90).

### Finding 3 — Mutation score and pass rate can dangerously dissociate
> LLaMA-3.3-70B CoT achieved **80% mutation score** with only **10% pass rate** — tests killed mutants while failing against correct implementations. **Never rely on mutation score alone.**

### Finding 4 — Linked list functions are a systematic failure mode
> The `partition_list` function (linked list manipulation) resisted mutation killing across **all models and all strategies**, due to difficulty instantiating custom `ListNode` objects.

### Finding 5 — LLM test redundancy is negligible
> Redundancy rate remained **≤ 0.85%** across all conditions, a practically useful property for test suite maintainability.

---

## 📊 Results Summary

```
Model            Strategy     Exec.   Pass    Mut.    Line    Branch
─────────────────────────────────────────────────────────────────────
GPT-OSS-120B     Zero-Shot    100%    50%     80%     96.1%   92.2%
                 Few-Shot     100%    50%     70%     92.9%   89.2%
                 Structured   100%    40%     80%     90.4%   88.3%
                 CoT          100%    30%     80%     97.1%   95.0%
─────────────────────────────────────────────────────────────────────
LLaMA-3.3-70B    Zero-Shot      0%     0%      0%      N/A     N/A
                 Few-Shot       0%     0%      0%      N/A     N/A
                 Structured    30%    10%     40%     23.8%   23.1%
                 CoT           90%    10%     80%     84.2%   81.7%
─────────────────────────────────────────────────────────────────────
Kimi-K2*         Zero-Shot    100%    50%     80%     96.3%   92.5%
                 Few-Shot       0%     0%      0%      N/A     N/A
                 Structured    90%    30%     80%     89.6%   85.8%
                 CoT†          83%     0%     67%     77.1%   70.8%
─────────────────────────────────────────────────────────────────────
* Kimi-K2 deprecated during study — descriptive only, excluded from inferential analysis
† CoT data available for 6 of 10 functions only
```

---

## 🗂️ Repository Structure

```
├── functions/                          # 10 LeetCode-style Python SUTs (Systems Under Test)
│   ├── __init__.py
│   ├── candy_distribution.py
│   ├── dota2_senate.py
│   ├── frog_jump.py
│   ├── letter_combination_of_phones.py
│   ├── longest_palindrome_subsequence.py
│   ├── partition_list.py
│   ├── pascal_triangle.py
│   ├── predict_the_winner.py
│   ├── search_a_2D_matrix.py
│   └── word_break.py
│
├── prompts/                            # Prompt templates for each strategy
│   ├── cot.txt
│   ├── few_shot.txt
│   ├── structured.txt
│   └── zero_shot.txt
│
├── generated_tests/                    # LLM-generated test suites (per model)
│   ├── llama-3.3-70b-versatile/
│   ├── moonshotai-kimi-k2-instruct/
│   └── openai-gpt-oss-120b/
│
├── mutants/                            # 1 LLM-generated mutant per function
│   ├── __init__.py
│   ├── __init__mutant.py
│   └── can_cross_mutant.py
│   └── ...
│
├── results/                            # All evaluation outputs
│   ├── Final_Test/                     # ✅ Final production run results
│   │   ├── figures/                    # Generated plots and visualizations
│   │   ├── results/                    # Per-function metric breakdowns
│   │   └── results.json               # Aggregated results (main data file)
│   ├── First_Tests/                    # 🧪 Exploratory run (not used in paper)
│   ├── Second_Tests/                   # 🧪 Exploratory run (not used in paper)
│   ├── Third_Tests/                    # 🧪 Exploratory run (not used in paper)
│   ├── Fourth_Tests/                   # 🧪 Exploratory run (not used in paper)
│   └── Fifth_Tests/                    # 🧪 Exploratory run (not used in paper)
│
├── scripts/                            # All pipeline scripts
│   ├── gt_groq_new.py                  # ✅ FINAL — Test generation via Groq API
│   ├── evaluator_new.py                # ✅ FINAL — Full evaluation pipeline
│   ├── gen_figures.py                  # Figure generation from results
│   ├── statistical_analysis.py         # Friedman, Wilcoxon, Cliff's delta
│   ├── evaluator.py                    # 🧪 Earlier evaluator draft
│   ├── generate_tests.py               # 🧪 Earlier generation draft
│   ├── groq_models.py                  # 🧪 Model exploration script
│   ├── gt_deep.py                      # 🧪 DeepSeek generation experiment
│   ├── gt_groq.py                      # 🧪 Earlier Groq generation draft
│   ├── result_checker.py               # 🧪 Ad-hoc result inspection utility
│   ├── run_metrics.py                  # 🧪 Standalone metrics runner draft
│   └── temp_test.py                    # 🧪 Throwaway scratch file
│
├── .coverage                           # Coverage measurement artifact
├── .gitignore
└── README.md
```

> **Note:** Only `gt_groq_new.py` and `evaluator_new.py` were used for the final experimental run reported in the paper. All other scripts under `scripts/` are earlier drafts or exploratory utilities kept for transparency.

---

## ⚙️ Setup & Usage

### Prerequisites

```bash
pip install groq coverage scipy numpy matplotlib
```

### Environment Variables

```bash
export GROQ_API_KEY=your_groq_api_key_here
```

### Step 1 — Generate Tests

Uses `gt_groq_new.py` (the final generation script) to call the Groq API for all model–strategy–function combinations.

```bash
python scripts/gt_groq_new.py
```

Generated test suites are saved under `generated_tests/` organized by model name.

### Step 2 — Run Evaluation Pipeline

Uses `evaluator_new.py` (the final evaluator) to compute all five metrics: executability, pass rate, mutation score, line coverage, and branch coverage.

```bash
python scripts/evaluator_new.py
```

Results are written to `results/Final_Test/results.json` and per-function breakdowns are saved under `results/Final_Test/results/`.

### Step 3 — Generate Figures

```bash
python scripts/gen_figures.py
```

Plots are saved to `results/Final_Test/figures/`.

### Step 4 — Statistical Analysis

Runs the full 3-stage pipeline: Friedman test → Wilcoxon signed-rank with Bonferroni correction → Cliff's delta effect sizes.

```bash
python scripts/statistical_analysis.py
```

---

## 📐 Evaluation Metrics

| Metric | Description | Tool |
|---|---|---|
| **Executability** | Test suite runs without manual intervention | `unittest` runner |
| **Pass Rate** | Fraction of tests passing against correct implementation | `unittest` |
| **Mutation Score** | Fraction of artificial mutants detected | Custom mutant runner |
| **Line Coverage** | % of source lines executed by tests | `coverage.py` |
| **Branch Coverage** | % of conditional branches executed | `coverage.py` |
| **Redundancy Rate** | Structurally duplicate test methods (AST matching) | Custom AST comparator |

---

## 📋 Statistical Methods

Analysis used a **3-stage non-parametric pipeline** appropriate for bounded, non-normal, small-n within-subjects designs:

1. **Descriptive Statistics** — Mean, SD, median, min, max per model–strategy cell
2. **Friedman Test** — Non-parametric repeated-measures ANOVA equivalent (H₀: all strategies equivalent)
3. **Wilcoxon Signed-Rank + Bonferroni + Cliff's δ** — Pairwise post-hoc with family-wise error control and effect size

Effect size thresholds (Cliff's δ): `< 0.147` negligible · `< 0.330` small · `< 0.474` medium · `≥ 0.474` large

---

## 💡 Practical Recommendations

| Scenario | Recommendation |
|---|---|
| **Large frontier model (≥ 100B params)** | Any strategy is acceptable. Zero-Shot is most token-efficient. |
| **Mid-scale model (50–100B params)** | Use **CoT exclusively**. Zero-Shot and Few-Shot are unreliable. |
| **Evaluating test quality** | Always report **both mutation score and pass rate**. Either alone is misleading. |
| **Complex data structures** | Supplement generated tests with **manually written tests** for linked lists, trees, and graphs. |

---

## 🧬 Systems Under Test

| # | Function | Problem Type | Challenge |
|---|---|---|---|
| 1 | `candy_distribution` | Greedy / constraint logic | Non-trivial expected outputs |
| 2 | `dota2_senate` | Simulation / queue-based | Order-dependent stateful logic |
| 3 | `frog_jump` | Dynamic programming | Complex path exploration |
| 4 | `letter_combinations` | Combinatorics | Set/list output validation |
| 5 | `longest_palindrome_subsequence` | Dynamic programming | Hard oracle generation |
| 6 | `partition_list` | Linked list manipulation | Custom node instantiation |
| 7 | `pascal_triangle` | Mathematical pattern | Multi-row output generation |
| 8 | `predict_the_winner` | Game theory / recursion | Non-obvious decision outputs |
| 9 | `search_2d_matrix` | Binary search / matrix | Boundary condition testing |
| 10 | `word_break` | DP / string segmentation | Multiple valid paths |

---

## 📄 Citation

If you use this work, please cite:

```bibtex
@article{shawon2025prompt,
  title     = {Impact of Prompt Engineering on LLM-based Test Case Generation},
  author    = {Saha Shawon, Swapnil},
  year      = {2025},
  school    = {North South University},
  note      = {Student ID: 2616035650}
}
```

---

## 🔗 Links

| Resource | Link |
|---|---|
| 📺 Video Demo | https://youtu.be/53ybuAIH3gw |
| 📦 Repository | https://github.com/shawonsaha15/LLM-based-Test-Case-Generation-Research |

---

<div align="center">
  <sub>Built at North South University · swapnil.shawon.261@northsouth.edu</sub>
</div>
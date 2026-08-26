# Surveys, Reviews, Tutorials, and Position Papers

This page tracks surveys that can help us build the literature map for an AI4AI review. They are grouped by subfield because AI4AI currently spans several previously separate communities.

## 1. AutoML / Automated Data Science

- **AutoML: A Survey of the State-of-the-Art** (2020) — broad AutoML taxonomy covering data preparation, feature engineering, model generation, and HPO. https://arxiv.org/abs/1908.00709
- **Automated Machine Learning: State-of-the-Art and Open Challenges** (2020) — overview of AutoML techniques and open problems. https://arxiv.org/abs/1906.02287
- **Automated Machine Learning: Methods, Systems, Challenges** (2019) — foundational AutoML book edited by Hutter, Kotthoff, and Vanschoren. https://www.automl.org/book/
- **A Literature Review on Automated Machine Learning** (2025/2026) — systematic review connecting algorithm selection, meta-learning, HPO, transfer learning, and pipeline design. https://doi.org/10.1007/s10462-025-11397-2

## 2. Hyperparameter Optimization / Bayesian Optimization

- **Algorithms for Hyper-Parameter Optimization** (2011) — classic HPO foundation. https://proceedings.neurips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html
- **Taking the Human Out of the Loop: A Review of Bayesian Optimization** (2016) — influential BO review. https://ieeexplore.ieee.org/document/7352306
- **Hyperparameter Optimization in Machine Learning** (survey background) — useful family of review papers around Bayesian optimization, evolutionary search, bandits, and multi-fidelity methods.

## 3. Neural Architecture Search

- **Neural Architecture Search: A Survey** (2019) — classic NAS survey organized around search space, search strategy, and performance estimation. https://arxiv.org/abs/1808.05377
- **A Comprehensive Survey of Neural Architecture Search: Challenges and Solutions** (2020) — broad NAS review. https://arxiv.org/abs/2006.02903
- **Neural Architecture Search Survey: A Hardware Perspective** (2022) — hardware-aware NAS and deployment constraints. https://doi.org/10.1145/3524500
- **Neural Architecture Search Benchmarks: Insights and Survey** (2023) — survey specifically focused on NAS benchmark design. https://doi.org/10.1109/ACCESS.2023.3253818
- **Neural Architecture Search Survey: A Computer Vision Perspective** (2023) — CV-oriented NAS review. https://doi.org/10.3390/s23031713
- **Neural Architecture Search from a Natural Language Processing Perspective: A Survey** (2026) — NLP-oriented NAS review. https://doi.org/10.1007/s10462-026-11550-5
- **Toward Automated Deep Learning: Advances and Challenges in Neural Architecture Search** (2026) — recent review spanning search space, optimization, HPO, and evaluation. https://doi.org/10.1002/widm.70091

## 4. Meta-Learning / Learning to Learn

- **Learning to Learn: Gradient Descent by Gradient Descent** and related learned-optimizer work form an important precursor to self-improving AI4AI.
- **Meta-Learning in Neural Networks: A Survey** (2020/2021) — broad taxonomy of optimization-based, model-based, and metric-based meta-learning. https://arxiv.org/abs/2004.05439
- **A Survey of Deep Meta-Learning** (2019) — useful historical map of deep meta-learning methods. https://arxiv.org/abs/1810.03548

## 5. Automated Algorithm Design / Program Synthesis

Relevant surveys are spread across evolutionary computation, genetic programming, program synthesis, and automated algorithm configuration rather than labeled AI4AI.

- **Automated Algorithm Configuration and Design** literature — ParamILS, SMAC, irace, genetic programming, hyper-heuristics.
- **Program Synthesis** surveys — important for understanding the transition from choosing parameters to generating executable algorithms.
- **Genetic Programming / Hyper-Heuristics** surveys — background for FunSearch, AlphaEvolve, and evolutionary coding agents.

## 6. LLMs as Optimizers / Search Operators

- **Large Language Models as Optimizers: A Survey of Direct vs. Tool-Augmented Approaches and Their Performance Frontiers** (2026) — organizes LLM optimization into direct, tool-augmented, and tool-creating paradigms. https://arxiv.org/abs/2606.15577
- Broader LLM-agent surveys are also relevant where they cover planning, tool use, reflection, memory, and self-improvement, but we should distinguish generic agents from agents that explicitly optimize AI systems or conduct AI research.

## 7. AI Scientists / Autonomous Research Agents

- **From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery** (2025) — domain-oriented survey of autonomous scientific discovery across life sciences, chemistry, materials, and physics. https://arxiv.org/abs/2508.14111
- **Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap** (2026) — focuses on AI-scientist systems and the gap between producing research artifacts and verifying scientific claims. https://arxiv.org/abs/2608.05179
- Surveys on **LLM agents for scientific discovery**, **AI for Science**, and **scientific agents** should be tracked here even when their scope includes domains outside AI research, because they provide lifecycle and autonomy taxonomies.

## 8. Self-Improving / Evolutionary Agents

This subfield is emerging rapidly and currently has fewer mature surveys. Relevant adjacent literatures include:

- self-refining / reflective LLM agents;
- open-ended learning;
- quality-diversity and evolutionary computation;
- population-based training;
- automated curriculum generation;
- meta-learning and learned optimizers;
- self-referential / self-modifying agent systems;
- world models for planning;
- process supervision and trajectory-level learning.

A key opportunity for our survey is to connect these traditions to **AI R&D automation**, rather than reviewing them as generic agent techniques.

## 9. Benchmark Surveys

- **Neural Architecture Search Benchmarks: Insights and Survey** (2023) — benchmark taxonomy for NAS. https://doi.org/10.1109/ACCESS.2023.3253818
- The AutoML literature contains benchmark methodology and framework-comparison work such as AMLB.
- Modern AI-R&D benchmark papers (MLAgentBench, MLE-bench, RE-Bench, PaperBench) are themselves currently more informative than any single benchmark survey because this area is very recent.

## Survey gap we can target

Existing reviews usually stop at one of these boundaries:

1. **AutoML surveys** stop at automated pipelines / NAS / HPO.
2. **NAS surveys** focus on architecture search and efficiency.
3. **LLM-agent surveys** are broad but not specific to AI R&D.
4. **AI-for-Science surveys** focus on scientific domains rather than AI improving AI.
5. **AI-scientist surveys** emphasize end-to-end scientific workflows but generally do not trace the methodological lineage back through AutoML, meta-learning, program search, and learned optimization.

Our potential niche is therefore:

> **A unified history and taxonomy of AI systems that improve the process of building AI itself — from fixed-space AutoML to open-ended, agentic, and self-improving AI research.**

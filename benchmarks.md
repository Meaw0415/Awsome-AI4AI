# AI4AI Benchmarks

This page collects benchmarks that evaluate the different layers of AI4AI: hyperparameter/architecture search, AutoML systems, optimization agents, ML engineering agents, AI-R&D agents, and research replication.

## 1. Hyperparameter Optimization / AutoML

- **HPOBench** (2021) — A Collection of Reproducible Multi-Fidelity Benchmark Problems for HPO. Benchmark collection for HPO algorithms. https://arxiv.org/abs/2109.06716
- **YAHPO Gym** (2021/2022) — An Efficient Multi-Objective Multi-Fidelity Benchmark for Hyperparameter Optimization. 700+ surrogate HPO problems. https://arxiv.org/abs/2109.03670
- **AMLB: an AutoML Benchmark** (2022) — Benchmark of end-to-end AutoML frameworks across classification and regression tasks. https://arxiv.org/abs/2207.12560
- **OpenML Benchmarking Suites** (2021) — Standardized reusable ML benchmark suites including OpenML-CC18. https://openreview.net/forum?id=OCrD8ycKjG
- **AutoML Benchmark** (2019) — Early systematic framework for benchmarking AutoML systems. https://www.automl.org/wp-content/uploads/2019/06/automlws2019_Paper45.pdf

## 2. Neural Architecture Search Benchmarks

- **NAS-Bench-101** (2019) — 423k unique CNN architectures; one of the foundational tabular NAS benchmarks. https://arxiv.org/abs/1902.09635
- **NAS-Bench-201** (2020) — Unified 15,625-architecture benchmark evaluated on multiple datasets. https://arxiv.org/abs/2001.00326
- **NAS-Bench-301** (2020) — Surrogate NAS benchmark for the DARTS search space. https://arxiv.org/abs/2008.09777
- **NAS-Bench-NLP** (2020) — NAS benchmark for recurrent architectures / NLP. https://arxiv.org/abs/2006.07116
- **NATS-Bench** (2020/2021) — Benchmarking NAS algorithms for architecture topology and size. https://arxiv.org/abs/2009.00437
- **HW-NAS-Bench** (2021) — Hardware-aware NAS benchmark with measured hardware costs. https://arxiv.org/abs/2103.10584
- **TransNAS-Bench-101** (2021) — Transferable NAS benchmark across tasks. https://arxiv.org/abs/2105.11871
- **NAS-Bench-Suite** (2022) — A benchmark suite intended to reduce overfitting to a single NAS search space. https://arxiv.org/abs/2201.13396

## 3. Black-Box / Algorithm Optimization Benchmarks

- **BBOB / COCO** — Long-running black-box optimization benchmark ecosystem, important background for automated algorithm design. https://coco-platform.org/
- **Nevergrad** — Optimization benchmark/platform spanning gradient-free optimization and algorithm configuration. https://github.com/facebookresearch/nevergrad
- **MetaBox** (2023) — Benchmark/platform for meta-black-box optimization and learned optimizers. https://arxiv.org/abs/2305.16605

## 4. Code & Software Engineering Precursors

These are not AI4AI-specific, but they provide the execution substrate and evaluation ideas later reused by ML/R&D agents.

- **HumanEval** (2021) — Functional correctness of code generation. https://arxiv.org/abs/2107.03374
- **SWE-bench** (2023/2024) — Repository-level software engineering benchmark based on real GitHub issues. https://arxiv.org/abs/2310.06770
- **SWE-bench Verified** (2024) — Human-validated subset of SWE-bench. https://www.swebench.com/
- **SWE-Lancer** (2025) — Real-world freelance software engineering tasks. https://openai.com/index/swe-lancer/

## 5. Machine Learning Experimentation & Engineering Agents

- **MLAgentBench** (2023) — 13 end-to-end ML experimentation tasks where agents modify files, run code, inspect results, and iterate. https://arxiv.org/abs/2310.03302
- **MLE-bench** (2024) — 75 Kaggle competitions used to evaluate autonomous machine-learning engineering agents. https://arxiv.org/abs/2410.07095
- **RE-Bench** (2024/2025) — 7 open-ended frontier AI research-engineering environments with human expert baselines and long time budgets. https://arxiv.org/abs/2411.15114

## 6. Research Replication / Full Research Benchmarks

- **PaperBench** (2025) — Replicate 20 ICML 2024 Spotlight/Oral papers from scratch; 8,316 rubric items. https://openai.com/index/paperbench/
- **PaperBench Code-Dev** (2025) — Code-development-focused slice of PaperBench. https://github.com/openai/preparedness/tree/main/project/paperbench
- **JudgeEval** (2025) — Auxiliary evaluation introduced with PaperBench to evaluate automated judges for research replication. https://openai.com/index/paperbench/

## 7. Scientific Discovery / Research-Agent Evaluation

This area is still much less standardized than AutoML or code benchmarks. We should track benchmarks along multiple axes rather than treating a single score as sufficient:

- hypothesis quality / novelty;
- literature-grounding accuracy;
- experimental design quality;
- ability to execute experiments;
- scientific correctness;
- reproducibility;
- claim verification;
- long-horizon progress under compute/time budgets;
- information gain / uncertainty reduction;
- ability to revise beliefs after negative or contradictory evidence.

## Benchmark progression

A useful difficulty ladder for the survey is:

> **fixed black-box objective**  
> HPOBench / YAHPO  
> ↓  
> **architecture / program search**  
> NAS-Bench family  
> ↓  
> **end-to-end AutoML**  
> AMLB  
> ↓  
> **ML experimentation**  
> MLAgentBench  
> ↓  
> **realistic ML engineering**  
> MLE-bench  
> ↓  
> **frontier research engineering**  
> RE-Bench  
> ↓  
> **paper-level replication**  
> PaperBench  
> ↓  
> **open-ended scientific research**  
> still an open evaluation problem.

## Evaluation gap

Most existing benchmarks still reward an **artifact outcome**: final score, working code, replicated result, or rubric completion. A stronger benchmark for research-level AI4AI should additionally measure whether the agent:

1. forms useful hypotheses;
2. chooses informative experiments;
3. updates beliefs appropriately after evidence;
4. avoids repeatedly testing already-refuted ideas;
5. transfers learned research strategies across problems;
6. can justify why the next experiment is valuable before running it.

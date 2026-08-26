# Awesome AI4AI

A curated list of papers, benchmarks, surveys, and resources on **AI for AI (AI4AI)** — using AI to automate or improve the design, training, evaluation, engineering, and research of AI systems.

## Contents

- [Evolution of AI4AI](#evolution-of-ai4ai)
- [1. AutoML & Hyperparameter Optimization](#1-automl--hyperparameter-optimization)
- [2. Neural Architecture Search](#2-neural-architecture-search)
- [3. Meta-Learning & Learned Optimization](#3-meta-learning--learned-optimization)
- [4. Automated Algorithm & Program Discovery](#4-automated-algorithm--program-discovery)
- [5. LLMs as Optimizers](#5-llms-as-optimizers)
- [6. Autonomous ML Engineering Agents](#6-autonomous-ml-engineering-agents)
- [7. AI Research Agents / AI Scientists](#7-ai-research-agents--ai-scientists)
- [8. Self-Improving / Open-Ended AI4AI](#8-self-improving--open-ended-ai4ai)
- [Benchmarks](benchmarks.md)
- [Surveys](surveys.md)
- [Full Paper Library](papers.md)
- [Survey Writing Notes](writing.md)

## Evolution of AI4AI

```text
Algorithm Selection / HPO
        ↓
AutoML / Pipeline Search
        ↓
Neural Architecture Search
        ↓
Meta-Learning / Learned Optimizers
        ↓
Automated Algorithm & Program Discovery
        ↓
LLM-based Optimization / Code Search
        ↓
Autonomous ML Engineering Agents
        ↓
AI Research Agents / AI Scientists
        ↓
Self-Improving / Open-Ended AI4AI
```

The scope of automation has gradually expanded from selecting parameters inside a human-defined search space to modifying code, running experiments, proposing research ideas, and potentially improving the research process itself.

---

## 1. AutoML & Hyperparameter Optimization

Early AI4AI focuses on automating model selection, hyperparameter tuning, and complete ML pipelines.

- **2011** — [Algorithms for Hyper-Parameter Optimization](https://proceedings.neurips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html) — TPE / modern HPO.
- **2012** — [Random Search for Hyper-Parameter Optimization](https://jmlr.org/papers/v13/bergstra12a.html).
- **2013** — [Auto-WEKA: Combined Selection and Hyperparameter Optimization of Classification Algorithms](https://arxiv.org/abs/1208.3719).
- **2015** — [Efficient and Robust Automated Machine Learning](https://proceedings.neurips.cc/paper/2015/hash/11d0e6287202fced83f79975ec59a3a6-Abstract.html) — auto-sklearn.
- **2016** — [TPOT: A Tree-based Pipeline Optimization Tool for Automating Machine Learning](https://proceedings.mlr.press/v64/olson_tpot_2016.html).
- **2016** — [Hyperband](https://arxiv.org/abs/1603.06560).
- **2017** — [BOHB](https://arxiv.org/abs/1807.01774).
- **2017** — [Google Vizier](https://dl.acm.org/doi/10.1145/3097983.3098043).
- **2020** — [AutoGluon-Tabular](https://arxiv.org/abs/2003.06505).
- **2020** — [Auto-Sklearn 2.0](https://arxiv.org/abs/2007.04074).
- **2021** — [FLAML](https://arxiv.org/abs/1911.04706).

More: [`papers.md`](papers.md)

## 2. Neural Architecture Search

Automation moves from choosing hyperparameters to designing neural structures.

- **2016/2017** — [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578).
- **2017** — [Designing Neural Network Architectures using Reinforcement Learning](https://arxiv.org/abs/1611.02167).
- **2017** — [Large-Scale Evolution of Image Classifiers](https://arxiv.org/abs/1703.01041).
- **2017** — [NASNet](https://arxiv.org/abs/1707.07012).
- **2018** — [ENAS](https://arxiv.org/abs/1802.03268).
- **2018** — [DARTS](https://arxiv.org/abs/1806.09055).
- **2018** — [ProxylessNAS](https://arxiv.org/abs/1812.00332).
- **2019** — [MnasNet](https://arxiv.org/abs/1807.11626).
- **2019** — [Once-for-All](https://arxiv.org/abs/1908.09791).
- **2020** — [NAS-Bench-201](https://arxiv.org/abs/2001.00326).

## 3. Meta-Learning & Learned Optimization

The optimizer/search procedure itself begins to learn from prior tasks and optimization trajectories.

- **2016** — [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474).
- **2017** — [MAML](https://arxiv.org/abs/1703.03400).
- **2017** — [Population Based Training of Neural Networks](https://arxiv.org/abs/1711.09846).
- **2018** — [Reptile](https://arxiv.org/abs/1803.02999).
- **2020** — [Meta-Learning in Neural Networks: A Survey](https://arxiv.org/abs/2004.05439).
- **2022** — [VeLO: Training Versatile Learned Optimizers by Scaling Up](https://arxiv.org/abs/2211.09760).

## 4. Automated Algorithm & Program Discovery

Search expands beyond architectures toward executable learning rules, programs, heuristics, and algorithms.

- **2018** — [Neural Optimizer Search with Reinforcement Learning](https://arxiv.org/abs/1709.07417).
- **2019** — [AutoAugment](https://arxiv.org/abs/1805.09501).
- **2020** — [AutoML-Zero: Evolving Machine Learning Algorithms From Scratch](https://arxiv.org/abs/2003.03384).
- **2023** — [FunSearch: Mathematical Discoveries from Program Search with Large Language Models](https://www.nature.com/articles/s41586-023-06924-6).
- **2025** — [AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery](https://arxiv.org/abs/2506.13131).

## 5. LLMs as Optimizers

Foundation models become proposal operators that optimize prompts, code, reward functions, and algorithms.

- **2022** — [Large Language Models Are Human-Level Prompt Engineers](https://arxiv.org/abs/2211.01910) — APE.
- **2023** — [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) — OPRO.
- **2023** — [Promptbreeder](https://arxiv.org/abs/2309.16797).
- **2023** — [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931).
- **2024** — [TextGrad: Automatic Differentiation via Text](https://arxiv.org/abs/2406.07496).
- **2024** — [DSPy](https://arxiv.org/abs/2310.03714).
- **2025** — [AlphaEvolve](https://arxiv.org/abs/2506.13131).

## 6. Autonomous ML Engineering Agents

Agents now interact with actual codebases, datasets, terminals, experiment logs, and evaluation metrics.

- **2023** — [MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://arxiv.org/abs/2310.03302).
- **2024** — [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://arxiv.org/abs/2410.07095).
- **2024** — [AIDE: AI-Driven Exploration in the Space of Code](https://github.com/WecoAI/aideml).
- **2024/2025** — [RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts](https://arxiv.org/abs/2411.15114).

See also: [`benchmarks.md`](benchmarks.md)

## 7. AI Research Agents / AI Scientists

Automation extends from engineering tasks to research ideation, literature use, experimentation, interpretation, and paper generation.

- **2024** — [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](https://arxiv.org/abs/2404.07738).
- **2024** — [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292).
- **2025** — [Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227).
- **2025** — [Towards an AI Co-Scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/).
- **2025** — [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://openai.com/index/paperbench/).

## 8. Self-Improving / Open-Ended AI4AI

The newest line studies systems that accumulate skills, evolve solutions, modify their own agent machinery, or improve components used by later iterations.

- **2017** — [Population Based Training](https://arxiv.org/abs/1711.09846).
- **2019** — [POET](https://arxiv.org/abs/1901.01753).
- **2021** — [Open-Ended Learning Leads to Generally Capable Agents](https://arxiv.org/abs/2107.12808).
- **2023** — [Voyager](https://arxiv.org/abs/2305.16291).
- **2023** — [Promptbreeder](https://arxiv.org/abs/2309.16797).
- **2023** — [FunSearch](https://www.nature.com/articles/s41586-023-06924-6).
- **2025** — [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954).
- **2025** — [AlphaEvolve](https://arxiv.org/abs/2506.13131).

---

## Benchmarks

See [`benchmarks.md`](benchmarks.md) for:

- HPOBench / YAHPO Gym / AMLB
- NAS-Bench-101 / 201 / 301 / NATS-Bench
- MLAgentBench
- MLE-bench
- RE-Bench
- PaperBench
- related software-engineering benchmarks

## Surveys

See [`surveys.md`](surveys.md) for surveys on:

- AutoML
- HPO / Bayesian optimization
- NAS
- meta-learning
- program synthesis / automated algorithm design
- LLM optimizers
- autonomous research agents / AI Scientists
- self-improving agents
- AI for Science / agentic science

## Contributing

This is a living list. New papers, benchmarks, surveys, and corrections are welcome.

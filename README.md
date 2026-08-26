<div align="center">

# 🤖 Awesome AI4AI

### AI Agents for Automating, Optimizing, and Advancing AI Research

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Focus](https://img.shields.io/badge/Focus-Agent4AI-blue)
![Papers](https://img.shields.io/badge/Agentic%20Papers-160%2B-brightgreen)
![Years](https://img.shields.io/badge/Agentic%20Focus-2024--2026-orange)

**AI4AI** studies how AI can improve the development of AI itself — from AutoML and algorithm discovery to autonomous **ML engineering agents, data-analytic agents, AI research agents, AI scientists, and recursively self-improving AI systems**.

**Current focus: Agent4AI — agents that autonomously perform, evaluate, optimize, and learn from AI/ML engineering and research.**

[Agent4AI Papers](agentic_ai4ai_2024_2026.md) · [Recent Additions](agentic_ai4ai_recent_additions.md) · [Benchmarks](benchmarks.md) · [Surveys](surveys.md) · [Full Library](papers.md) · [Writing Notes](writing.md)

</div>

---

## 🔥 Agent4AI: The Emerging Core of AI4AI

```text
AutoML / NAS
    ↓
LLM as Optimizer
    ↓
Agent edits code + runs experiments
    ↓
MLE / Data-Analytic Agent searches over solution trajectories
    ↓
Execution-grounded learning + memory + post-training
    ↓
AI Research Agent forms hypotheses + interprets evidence
    ↓
AI Scientist automates the research lifecycle
    ↓
AI4AI toward recursive self-improvement
```

The key transition is from optimizing a **model configuration** to optimizing the **entire AI R&D process**, including code, experiments, hypotheses, experience, agent policies, and even the harness itself.

### ⭐ Representative Agent4AI Systems

| Year | System / Paper | What is automated? | Main mechanism | Evaluation / environment |
|:---:|---|---|---|---|
| 2023/24 | [MLAgentBench](https://arxiv.org/abs/2310.03302) | ML experimentation | language agent + experiment feedback | ML research tasks |
| 2024 | [DS-Agent](https://arxiv.org/abs/2402.17453) | Data science | case-based reasoning from prior competitions | Kaggle tasks |
| 2024 | [SELA](https://arxiv.org/abs/2410.17238) | AutoML | tree-search enhanced LLM agent | tabular ML |
| 2024 | [MLE-bench](https://arxiv.org/abs/2410.07095) | ML engineering | executable competition environments | 75 Kaggle competitions |
| 2024 | [The AI Scientist](https://arxiv.org/abs/2408.06292) | Research lifecycle | idea → experiment → paper → review | automated ML research |
| 2024/25 | [RE-Bench](https://arxiv.org/abs/2411.15114) | AI R&D | long-horizon agentic R&D evaluation | frontier AI research engineering |
| 2025 | [AIDE](https://arxiv.org/abs/2502.13138) | ML engineering | solution-tree search over code | MLE / competitions |
| 2025 | [I-MCTS](https://arxiv.org/abs/2502.14693) | AutoML / MLE | introspective MCTS | ML tasks |
| 2025 | [ML-Agent](https://arxiv.org/abs/2505.23723) | ML engineering | reinforcement learning for MLE agents | MLE tasks |
| 2025 | [R&D-Agent](https://arxiv.org/abs/2505.14738) | AI solution R&D | research + development + evolution | data-driven AI tasks |
| 2025 | [MLE-STAR](https://arxiv.org/abs/2506.15692) | ML engineering | search + targeted refinement | MLE-bench |
| 2025 | [ML-Master](https://arxiv.org/abs/2506.16499) | ML engineering | exploration + reasoning + adaptive memory | MLE-bench |
| 2025 | [AutoMind](https://arxiv.org/abs/2506.10974) | Data science | expert knowledge + adaptive search | Kaggle / MLE |
| 2025/26 | [DataMind: Scaling Generalist Data-Analytic Agents](https://arxiv.org/abs/2509.25084) | General data analysis | synthetic trajectories + SFT/RL + code rollout | multi-benchmark data analysis |
| 2026 | [DSGym](https://arxiv.org/abs/2601.16344) | Data-science agent training/eval | standardized executable environments + verified data synthesis | DS tasks + DSBio + DSPredict |
| 2026 | [FOREAGENT](https://arxiv.org/abs/2601.05930) | MLE search | predict-then-verify / world-model-like execution prior | data-centric MLE tasks |
| 2026 | [AIBuildAI-2](https://arxiv.org/abs/2605.27873) | AI model building | evolving external knowledge + experience distillation | MLE-Bench |
| 2026 | [ML-Master 2.0](https://arxiv.org/abs/2601.10402) | long-horizon AI research | exploration + persistent experience | long-horizon research |
| 2026 | [Reasoning as Gradient](https://arxiv.org/abs/2603.01692) | ML engineering | reasoning feedback beyond tree search | MLE tasks |
| 2026 | [Frontis-MA1 / OpenRSI](https://arxiv.org/abs/2607.28568) | AI4AI / MLE self-improvement | execution-grounded SFT+RL + Draft/Improve/Debug/Crossover + evolutionary search | MLE-Bench Lite, NatureBench Lite |

> 📚 Full table: [`agentic_ai4ai_2024_2026.md`](agentic_ai4ai_2024_2026.md)  
> 🆕 Newer papers and citation-neighborhood additions: [`agentic_ai4ai_recent_additions.md`](agentic_ai4ai_recent_additions.md)

---

## 🧭 Agent4AI Landscape

| Track | Core question | Representative systems / ideas |
|---|---|---|
| **MLE Agents** | Can an agent autonomously build and improve ML solutions? | AIDE, MLE-STAR, ML-Master, R&D-Agent, AIBuildAI-2 |
| **Data-Analytic Agents** | Can a generalist agent perform long-horizon executable analysis? | DataMind, DSGym, DatawiseAgent, DataSciBench |
| **Search & Planning** | How should the agent explore code / experiment space? | tree search, MCTS, evolution, reasoning-as-gradient |
| **Execution Prediction / World Models** | Can expensive experiments be predicted before execution? | FOREAGENT, learned execution priors, research world models |
| **Agent Learning** | Can the research policy itself be trained? | MLE-Dojo, ML-Agent, AceGRPO, execution-grounded SFT/RL |
| **Experience & Memory** | How does past research alter future decisions? | ML-Master, AIBuildAI-2, case-based reasoning, trajectory distillation |
| **Workflow / Harness Optimization** | Can the agent architecture itself improve? | workflow search, topology optimization, automated harness design |
| **AI Research Agents** | Can agents move from engineering to research decisions? | MLGym, AIRA, ResearchAgent, Agent Laboratory |
| **AI Scientists** | Can a larger fraction of the research lifecycle be automated? | AI Scientist, AI Scientist-v2, AI Co-Scientist |
| **Recursive Self-Improvement** | Can AI improve the process of building AI itself? | OpenRSI / Frontis-MA1, Darwin Gödel Machine, AlphaEvolve |
| **Evaluation** | How do we measure autonomous AI R&D? | MLE-bench, RE-Bench, MLR-Bench, PaperBench, NatureBench, RSIBench-Data |

---

<details open>
<summary><h2>🛠️ MLE Agents & Automated AI Engineering</h2></summary>

These systems directly edit code, train models, inspect metrics, debug failures, and iterate on AI/ML solutions.

| Year | Paper / System | Key idea |
|:---:|---|---|
| 2024 | [DS-Agent](https://arxiv.org/abs/2402.17453) | case-based reasoning from prior data-science tasks |
| 2024 | [SELA](https://arxiv.org/abs/2410.17238) | tree-search enhanced AutoML agent |
| 2025 | [AIDE](https://arxiv.org/abs/2502.13138) | code-space solution tree search |
| 2025 | [I-MCTS](https://arxiv.org/abs/2502.14693) | introspective MCTS for agentic AutoML |
| 2025 | [ML-Agent](https://arxiv.org/abs/2505.23723) | RL-trained autonomous MLE agent |
| 2025 | [R&D-Agent](https://arxiv.org/abs/2505.14738) | automated research, development, and evolution |
| 2025 | [MLE-STAR](https://arxiv.org/abs/2506.15692) | search + targeted code-block refinement |
| 2025 | [ML-Master](https://arxiv.org/abs/2506.16499) | exploration + reasoning + adaptive memory |
| 2025 | [AutoMind](https://arxiv.org/abs/2506.10974) | expert knowledge + adaptive search |
| 2026 | [AIBuildAI-2](https://arxiv.org/abs/2605.27873) | evolving knowledge system learned from completed MLE runs |
| 2026 | [Reasoning as Gradient](https://arxiv.org/abs/2603.01692) | iterative reasoning signals guide MLE improvement |

</details>

<details open>
<summary><h2>📈 Generalist Data-Analytic Agents</h2></summary>

This branch sits between data science automation and AI research automation: agents must inspect heterogeneous data, write code, execute analyses, reason over results, and generalize across tasks.

| Year | Paper | Focus |
|:---:|---|---|
| 2025/26 | [Scaling Generalist Data-Analytic Agents (DataMind)](https://arxiv.org/abs/2509.25084) | scalable trajectory synthesis, SFT/RL, long-horizon code rollout |
| 2025 | [DataSciBench](https://arxiv.org/abs/2502.13897) | benchmark for data-science agents |
| 2025 | [DatawiseAgent](https://aclanthology.org/2025.emnlp-main.58/) | long-horizon executable data-science agent |
| 2026 | [DSGym](https://arxiv.org/abs/2601.16344) | unified executable evaluation and training framework |
| 2026 | [RSIBench-Data](https://arxiv.org/abs/2607.25886) | executable benchmark for self-improvement / generalist data-agent capability |
| 2026 | [FOREAGENT](https://arxiv.org/abs/2601.05930) | predict solution quality before expensive execution |

</details>

<details open>
<summary><h2>🧠 Execution-Grounded Learning, Memory & World Models</h2></summary>

A central Agent4AI direction is learning not only from final scores, but from **research trajectories and execution evidence**.

- [FOREAGENT](https://arxiv.org/abs/2601.05930) — learns execution priors for a **Predict-then-Verify** loop.
- [AIBuildAI-2](https://arxiv.org/abs/2605.27873) — distills completed AI-building runs into an evolving external knowledge system.
- [ML-Master](https://arxiv.org/abs/2506.16499) / [ML-Master 2.0](https://arxiv.org/abs/2601.10402) — reusable research experience and adaptive memory.
- [MLE-Dojo](https://arxiv.org/abs/2505.07782) — executable MLE environment for training and evaluating research agents.
- [DSGym](https://arxiv.org/abs/2601.16344) — execution-verified data synthesis for agent training.
- **Adjacent directions:** execution-grounded post-training, agent memory, trajectory-level credit assignment, learned research dynamics, research world models.

</details>

<details open>
<summary><h2>♻️ AI4AI toward Recursive Self-Improvement (RSI)</h2></summary>

This is the most direct realization of the repository's AI4AI theme: **AI systems that improve the process of building better AI systems**.

### OpenRSI / Frontis-MA1

[Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering](https://arxiv.org/abs/2607.28568)

OpenRSI treats MLE as an executable RSI testbed and builds a full stack:

```text
OpenMLE-Gym     → executable AI4AI environments
OpenMLE-RL      → execution-grounded operator learning
OpenMLE-Evo     → long-horizon evolutionary search
Frontis-MA1     → post-trained AI4AI meta-evolution agent
```

The system aligns training and inference around four program-evolution operators:

**Draft · Improve · Debug · Crossover**

Related lines:

- [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) — open-ended evolution of self-improving agents.
- [AlphaEvolve](https://arxiv.org/abs/2506.13131) — evolutionary coding agent for algorithm discovery.
- [EvoAgentX](https://arxiv.org/abs/2507.03616) — evolving agentic workflows.
- self-evolving agents, meta-evolution, execution-grounded post-training, and harness optimization.

</details>

<details open>
<summary><h2>🔬 AI Research Agents & AI Scientists</h2></summary>

| Year | Paper / System | Scope |
|:---:|---|---|
| 2024 | [ResearchAgent](https://arxiv.org/abs/2404.07738) | iterative literature-grounded research ideation |
| 2024 | [The AI Scientist](https://arxiv.org/abs/2408.06292) | idea → experiment → paper → review |
| 2025 | [Agent Laboratory](https://arxiv.org/abs/2501.04227) | multi-agent research workflow |
| 2025 | [AI Co-Scientist](https://arxiv.org/abs/2502.18864) | generate / debate / evolve scientific hypotheses |
| 2025 | [AI Scientist-v2](https://arxiv.org/abs/2504.08066) | agentic tree-search scientific discovery |
| 2025 | [MLGym](https://arxiv.org/abs/2502.14499) | interactive environment for AI research agents |
| 2025 | [MLR-Bench](https://arxiv.org/abs/2505.19955) | open-ended ML research benchmark |
| 2026 | [AIRA_2](https://arxiv.org/abs/2603.26499) | improved AI research-agent harness |
| 2026 | [FML-bench](https://arxiv.org/abs/2605.17373) | process-level evaluation of research search dynamics |

</details>

---

## 📊 Agent4AI Benchmarks

The benchmark unit is evolving from a **single ML metric** to a **complete research process**.

```text
Data analysis
    ↓
ML experimentation
    ↓
Competition-scale ML engineering
    ↓
Long-horizon AI R&D
    ↓
Open-ended ML research
    ↓
Paper reproduction / SOTA reproduction
    ↓
Executable AI4AI / self-improvement
```

| Benchmark | Year | What it measures |
|---|:---:|---|
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023/24 | iterative ML experimentation |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | 2024 | competition-scale ML engineering |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | 2024/25 | long-horizon frontier AI R&D |
| [ScienceAgentBench](https://arxiv.org/abs/2410.05080) | 2025 | data-driven scientific discovery |
| [DataSciBench](https://arxiv.org/abs/2502.13897) | 2025 | general data-science agents |
| [MLGym](https://arxiv.org/abs/2502.14499) | 2025 | interactive AI research |
| [PaperBench](https://arxiv.org/abs/2504.01848) | 2025 | reproducing AI research papers |
| [MLE-Dojo](https://arxiv.org/abs/2505.07782) | 2025 | training/evaluating MLE agents |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | 2025 | open-ended ML research |
| ResearchCodeBench | 2025 | implementing methods from recent research papers |
| EXP-Bench | 2025/26 | complete research experiments |
| [DSGym](https://arxiv.org/abs/2601.16344) | 2026 | executable data-science evaluation and training |
| [FML-bench](https://arxiv.org/abs/2605.17373) | 2026 | research search dynamics |
| NatureBench | 2026 | matching published SOTA from Nature-family papers |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | executable data-agent / self-improvement capability |

More → [`benchmarks.md`](benchmarks.md)

---

## 📚 Resource Map

| Resource | Description |
|---|---|
| [`agentic_ai4ai_2024_2026.md`](agentic_ai4ai_2024_2026.md) | master Agent4AI paper table |
| [`agentic_ai4ai_recent_additions.md`](agentic_ai4ai_recent_additions.md) | newest additions from EMNLP / NeurIPS / ICLR / arXiv and citation neighborhoods |
| [`benchmarks.md`](benchmarks.md) | AI4AI benchmark landscape |
| [`surveys.md`](surveys.md) | surveys / tutorials / position papers |
| [`papers.md`](papers.md) | full AI4AI bibliography including classical foundations |
| [`reading_priority.md`](reading_priority.md) | compact reading path |
| [`writing.md`](writing.md) | survey-writing ideas, taxonomy, and research gaps |

---

<details>
<summary><h2>📜 Classical AI4AI Foundations — AutoML, NAS, Meta-Learning & Algorithm Discovery</h2></summary>

These directions remain part of AI4AI, but the repository's current emphasis is **Agent4AI**.

### AutoML & Hyperparameter Optimization
- [Algorithms for Hyper-Parameter Optimization](https://proceedings.neurips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html)
- [Random Search for Hyper-Parameter Optimization](https://jmlr.org/papers/v13/bergstra12a.html)
- [Auto-WEKA](https://arxiv.org/abs/1208.3719)
- [auto-sklearn](https://proceedings.neurips.cc/paper/2015/hash/11d0e6287202fced83f79975ec59a3a6-Abstract.html)
- [TPOT](https://proceedings.mlr.press/v64/olson_tpot_2016.html)
- [Hyperband](https://arxiv.org/abs/1603.06560)
- [BOHB](https://arxiv.org/abs/1807.01774)
- [AutoGluon-Tabular](https://arxiv.org/abs/2003.06505)
- [FLAML](https://arxiv.org/abs/1911.04706)

### Neural Architecture Search
- [NAS with Reinforcement Learning](https://arxiv.org/abs/1611.01578)
- [NASNet](https://arxiv.org/abs/1707.07012)
- [ENAS](https://arxiv.org/abs/1802.03268)
- [DARTS](https://arxiv.org/abs/1806.09055)
- [ProxylessNAS](https://arxiv.org/abs/1812.00332)
- [Once-for-All](https://arxiv.org/abs/1908.09791)

### Meta-Learning & Learned Optimization
- [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474)
- [MAML](https://arxiv.org/abs/1703.03400)
- [Population Based Training](https://arxiv.org/abs/1711.09846)
- [VeLO](https://arxiv.org/abs/2211.09760)

### Automated Algorithm & Program Discovery
- [Neural Optimizer Search](https://arxiv.org/abs/1709.07417)
- [AutoAugment](https://arxiv.org/abs/1805.09501)
- [AutoML-Zero](https://arxiv.org/abs/2003.03384)
- [FunSearch](https://www.nature.com/articles/s41586-023-06924-6)
- [AlphaEvolve](https://arxiv.org/abs/2506.13131)

### LLMs as Optimizers
- [APE](https://arxiv.org/abs/2211.01910)
- [OPRO](https://arxiv.org/abs/2309.03409)
- [Promptbreeder](https://arxiv.org/abs/2309.16797)
- [Eureka](https://arxiv.org/abs/2310.12931)
- [TextGrad](https://arxiv.org/abs/2406.07496)

More → [`papers.md`](papers.md)

</details>

<details>
<summary><h2>🌱 Open-Ended & Self-Improving Foundations</h2></summary>

- [POET](https://arxiv.org/abs/1901.01753)
- [Open-Ended Learning Leads to Generally Capable Agents](https://arxiv.org/abs/2107.12808)
- [Voyager](https://arxiv.org/abs/2305.16291)
- [Promptbreeder](https://arxiv.org/abs/2309.16797)
- [FunSearch](https://www.nature.com/articles/s41586-023-06924-6)
- [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)
- [AlphaEvolve](https://arxiv.org/abs/2506.13131)

</details>

---

## ⭐ Scope

We use **AI4AI** as the umbrella term. The repository particularly tracks **Agent4AI**: autonomous agents that improve AI systems or automate the AI research-and-development process. General-purpose agents are included only when their optimization mechanism is directly relevant to AI R&D agents.

Contributions, missing papers, benchmark updates, and corrections are welcome.

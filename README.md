<div align="center">

# 🤖 Awesome AI4AI

### AI Agents for Automating, Optimizing, and Advancing AI Research

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Focus](https://img.shields.io/badge/Focus-Agent4AI-blue)
![Coverage](https://img.shields.io/badge/Coverage-2024--2026-orange)
![Papers](https://img.shields.io/badge/Agent4AI-160%2B%20papers-brightgreen)

**AI4AI** studies how AI can improve the development of AI itself — from AutoML and algorithm discovery to autonomous **ML engineering agents, data-analytic agents, AI research agents, AI scientists, and recursively self-improving AI systems**.

**Current focus: Agent4AI — agents that perform, evaluate, optimize, and learn from AI/ML engineering and research.**

[Agent4AI Hub](agent4ai/README.md) · [Agent4AI Papers](agent4ai/papers.md) · [Benchmarks](agent4ai/benchmarks.md) · [Surveys](agent4ai/surveys.md) · [Foundations](foundations/papers.md) · [Writing Notes](writing/notes.md)

</div>

---

## 🧭 AI4AI in One View

```text
Classical AutoML / NAS / Meta-Learning
                ↓
       LLMs as Optimizers
                ↓
      MLE / Data Agents
                ↓
Execution-Grounded Search & Learning
                ↓
 Experience / Memory / World Models
                ↓
      AI Research Agents
                ↓
         AI Scientists
                ↓
 Recursive / Self-Improving AI4AI
```

The repository is organized around this transition: from optimizing a fixed model configuration to optimizing the **entire AI R&D process** — code, experiments, hypotheses, trajectories, memory, agent policies, and eventually the research machinery itself.

---

## 🔥 Representative Agent4AI Systems

| Year | System / Paper | What is automated? | Main mechanism | Evaluation / environment |
|:---:|---|---|---|---|
| 2023/24 | [MLAgentBench](https://arxiv.org/abs/2310.03302) | ML experimentation | language agent + experiment feedback | ML research tasks |
| 2024 | [DS-Agent](https://arxiv.org/abs/2402.17453) | Data science | case-based reasoning | Kaggle tasks |
| 2024 | [SELA](https://arxiv.org/abs/2410.17238) | AutoML | tree-search enhanced LLM agent | tabular ML |
| 2024 | [MLE-bench](https://arxiv.org/abs/2410.07095) | ML engineering | executable competition environments | 75 Kaggle competitions |
| 2024 | [The AI Scientist](https://arxiv.org/abs/2408.06292) | research lifecycle | idea → experiment → paper → review | automated ML research |
| 2024/25 | [RE-Bench](https://arxiv.org/abs/2411.15114) | AI R&D | long-horizon executable research tasks | frontier AI R&D |
| 2025 | [AIDE](https://arxiv.org/abs/2502.13138) | ML engineering | solution-tree search over code | MLE tasks |
| 2025 | [I-MCTS](https://arxiv.org/abs/2502.14693) | AutoML / MLE | introspective MCTS | ML tasks |
| 2025 | [ML-Agent](https://arxiv.org/abs/2505.23723) | ML engineering | reinforcement learning | MLE tasks |
| 2025 | [R&D-Agent](https://arxiv.org/abs/2505.14738) | AI solution R&D | research + development + evolution | data-driven AI tasks |
| 2025 | [MLE-STAR](https://arxiv.org/abs/2506.15692) | ML engineering | search + targeted refinement | MLE-bench |
| 2025 | [ML-Master](https://arxiv.org/abs/2506.16499) | ML engineering | exploration + reasoning + adaptive memory | MLE-bench |
| 2025 | [AutoMind](https://arxiv.org/abs/2506.10974) | Data science | expert knowledge + adaptive search | Kaggle / MLE |
| 2025/26 | [DataMind](https://arxiv.org/abs/2509.25084) | general data analysis | synthetic trajectories + SFT/RL + code rollout | data-analysis benchmarks |
| 2026 | [DSGym](https://arxiv.org/abs/2601.16344) | DS agent training/eval | executable environments + verified synthesis | DS tasks |
| 2026 | [FOREAGENT](https://arxiv.org/abs/2601.05930) | MLE search | predict-then-verify execution prior | data-centric MLE |
| 2026 | [AIBuildAI-2](https://arxiv.org/abs/2605.27873) | AI model building | evolving knowledge + experience distillation | MLE-Bench |
| 2026 | [ML-Master 2.0](https://arxiv.org/abs/2601.10402) | long-horizon AI research | persistent exploration + experience | long-horizon research |
| 2026 | [Reasoning as Gradient](https://arxiv.org/abs/2603.01692) | ML engineering | reasoning feedback beyond tree search | MLE tasks |
| 2026 | [Frontis-MA1 / OpenRSI](https://arxiv.org/abs/2607.28568) | AI4AI / self-improvement | execution-grounded SFT/RL + program evolution | MLE-Bench Lite / NatureBench Lite |

More → [`agent4ai/papers.md`](agent4ai/papers.md)

---

## 🧩 Agent4AI Landscape

| Track | Core question | Representative directions |
|---|---|---|
| **MLE Agents** | Can an agent autonomously build and improve ML systems? | AIDE, MLE-STAR, ML-Master, R&D-Agent, AIBuildAI-2 |
| **Data-Analytic Agents** | Can a generalist agent perform long-horizon executable analysis? | DataMind, DSGym, DatawiseAgent |
| **Search & Planning** | How should the agent explore code / experiment space? | tree search, MCTS, evolution, reasoning-as-gradient |
| **Execution Prediction / World Models** | Can expensive experiments be predicted before execution? | FOREAGENT, learned execution priors |
| **Agent Learning** | Can the research policy itself be trained? | MLE-Dojo, ML-Agent, AceGRPO, execution-grounded RL |
| **Experience & Memory** | How should past experiments alter future decisions? | ML-Master, AIBuildAI-2, case-based reasoning, trajectory distillation |
| **Workflow / Harness Optimization** | Can the agent architecture itself improve? | workflow search, topology optimization, automated harness design |
| **AI Research Agents** | Can agents move beyond engineering into research decisions? | MLGym, AIRA, ResearchAgent, Agent Laboratory |
| **AI Scientists** | Can the research lifecycle be automated? | AI Scientist, AI Scientist-v2, AI Co-Scientist |
| **Recursive Self-Improvement** | Can AI improve the process of building AI itself? | OpenRSI / Frontis-MA1, Darwin Gödel Machine, AlphaEvolve |
| **Evaluation** | What counts as autonomous AI R&D progress? | MLE-bench, RE-Bench, MLR-Bench, PaperBench, NatureBench, RSIBench-Data |

---

<details open>
<summary><h2>📊 Agent4AI Benchmarks</h2></summary>

| Benchmark | Year | Main capability |
|---|:---:|---|
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023/24 | iterative ML experimentation |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | 2024 | competition-scale ML engineering |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | 2024/25 | long-horizon AI R&D |
| [ScienceAgentBench](https://arxiv.org/abs/2410.05080) | 2025 | data-driven scientific discovery |
| [MLGym](https://arxiv.org/abs/2502.14499) | 2025 | interactive AI research |
| [DataSciBench](https://arxiv.org/abs/2502.13897) | 2025 | data-science agents |
| [PaperBench](https://arxiv.org/abs/2504.01848) | 2025 | reproducing AI research papers |
| [MLE-Dojo](https://arxiv.org/abs/2505.07782) | 2025 | training/evaluating MLE agents |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | 2025 | open-ended ML research |
| [ResearchCodeBench](https://arxiv.org/abs/2506.02314) | 2025 | implementing methods from research papers |
| [EXP-Bench](https://arxiv.org/abs/2505.24785) | 2025/26 | complete AI research experiments |
| [DSGym](https://arxiv.org/abs/2601.16344) | 2026 | executable DS-agent training/eval |
| [FML-bench](https://arxiv.org/abs/2605.17373) | 2026 | research search dynamics |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | recursive-improvement-oriented data-agent evaluation |

Full benchmark map → [`agent4ai/benchmarks.md`](agent4ai/benchmarks.md)

</details>

<details>
<summary><h2>🧠 Execution-Grounded Learning, Memory & Self-Improvement</h2></summary>

This branch is especially important for the transition from ordinary MLE agents to systems that **learn how to do AI R&D better over time**.

Representative themes:

- execution-grounded post-training;
- experiment prediction / learned execution priors;
- trajectory reuse and experience distillation;
- persistent research memory;
- harness / workflow optimization;
- evolutionary program improvement;
- recursive self-improvement in executable AI tasks.

Representative systems include **FOREAGENT, ML-Master, AIBuildAI-2, OpenRSI / Frontis-MA1, Darwin Gödel Machine, AlphaEvolve**, plus adjacent work on self-evolving workflows and agent RL.

</details>

<details>
<summary><h2>🔬 AI Research Agents & AI Scientists</h2></summary>

- **2024** — [ResearchAgent](https://arxiv.org/abs/2404.07738)
- **2024** — [The AI Scientist](https://arxiv.org/abs/2408.06292)
- **2025** — [Agent Laboratory](https://arxiv.org/abs/2501.04227)
- **2025** — [AI Co-Scientist](https://arxiv.org/abs/2502.18864)
- **2025** — [AI Scientist-v2](https://arxiv.org/abs/2504.08066)
- **2025** — [MLGym](https://arxiv.org/abs/2502.14499)
- **2025** — [MLR-Bench](https://arxiv.org/abs/2505.19955)
- **2026** — [AIRA_2](https://arxiv.org/abs/2603.26499)
- **2026** — [FML-bench](https://arxiv.org/abs/2605.17373)

</details>

<details>
<summary><h2>📜 Classical AI4AI Foundations</h2></summary>

The repository keeps the historical lineage, but these foundations are separated from the current Agent4AI focus.

### AutoML / HPO
Auto-WEKA · auto-sklearn · TPOT · Hyperband · BOHB · AutoGluon · FLAML

### NAS
NAS with RL · NASNet · ENAS · DARTS · ProxylessNAS · Once-for-All

### Meta-Learning / Learned Optimization
Learning to Learn by Gradient Descent · MAML · Population-Based Training · VeLO

### Automated Algorithm / Program Discovery
Neural Optimizer Search · AutoAugment · AutoML-Zero · FunSearch · AlphaEvolve

### LLMs as Optimizers
APE · OPRO · Promptbreeder · Eureka · TextGrad

Full foundation bibliography → [`foundations/papers.md`](foundations/papers.md)

</details>

---

## 🗂 Repository Structure

```text
Awesome-AI4AI/
├── README.md
├── agent4ai/
│   ├── README.md          # Agent4AI navigation / taxonomy
│   ├── papers.md          # main 2024–2026 Agent4AI paper table
│   ├── recent.md          # staging area for newly found papers
│   ├── benchmarks.md      # benchmark landscape
│   └── surveys.md         # related surveys / reviews
├── foundations/
│   └── papers.md          # AutoML / NAS / meta-learning / algorithm discovery
└── writing/
    ├── notes.md           # survey thesis, taxonomy, gaps, writing ideas
    └── reading-list.md    # prioritized reading path
```

### Maintenance convention

New papers first go to `agent4ai/recent.md`. After verification and deduplication, they are merged into `agent4ai/papers.md`. This keeps the master table clean while still letting us collect fast-moving 2026 work.

---

## ⭐ Scope

We use **AI4AI** as the umbrella term. The repository particularly tracks **Agent4AI**: autonomous agents that improve AI systems or automate the AI research-and-development process. General-purpose agents are included only when their optimization mechanism is directly relevant to AI R&D agents.

Contributions, missing papers, benchmark updates, and corrections are welcome.

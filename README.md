<div align="center">

# 🤖 Awesome AI4AI

### AI Agents for Improving AI

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Focus](https://img.shields.io/badge/Focus-Agent4AI-blue)
![Coverage](https://img.shields.io/badge/Coverage-2024--2026-orange)
![Papers](https://img.shields.io/badge/Agent4AI-160%2B%20papers-brightgreen)

**AI4AI** asks a simple question: **how can AI improve AI?**

This repository focuses on **Agent4AI** — AI agents that build, train, evaluate, optimize, redesign, or research AI systems. The scope includes **MLE agents, data-analytic agents, LLM training/post-training agents, algorithm discovery, agent-system optimization, AI research agents, and self-improving AI systems**.

[🚀 Start Here](agent4ai/getting-started.md) · [🧭 Taxonomy](agent4ai/README.md) · [📚 Papers](agent4ai/papers.md) · [🧪 Benchmarks](agent4ai/benchmarks.md) · [🆕 Recent](agent4ai/recent.md) · [📖 Surveys](agent4ai/surveys.md)

</div>

---

## 🧭 From Agentic MLE to Self-Improving AI

```text
Build / modify AI systems
          ↓
Execute / train / evaluate
          ↓
Learn from feedback and experience
          ↓
Search or learn better actions
          ↓
Improve the agent / workflow itself
          ↓
Repeat with increasing autonomy
```

Agent4AI broadens the optimization target from a **model or pipeline** to the **entire process used to improve AI**.

### What can an Agent4AI system improve?

| Area | Optimization target | Representative work |
|---|---|---|
| **ML Engineering** | pipelines, features, models, code, experiments | AIDE, MLE-STAR, ML-Master, AIBuildAI-2 |
| **Data Analytics for AI** | executable analysis and modeling workflows | DS-Agent, DataMind, DSGym, DatawiseAgent |
| **Model Training & Post-Training** | data, fine-tuning, alignment, training recipes | AutoTrainess, PostTrainBench, ANDES |
| **Algorithms & Programs** | algorithms, optimizers, executable programs | FunSearch, AlphaEvolve, MLEvolve, AdaEvolve |
| **Agent Systems** | prompts, tools, context, workflows, harnesses | ADAS, EvoAgentX, Meta-Harness, Self-Harness |
| **AI Research & Reproduction** | ideas, implementations, experiments, papers | AI Scientist, AIRA, ResearchCodeBench, ResearchGym |
| **Self-Improvement** | the agent or improver used to build future AI | Frontis-MA1 / OpenRSI, meta-evolution systems |

---

# 🔥 Method Taxonomy

We organize Agent4AI by **which part of the AI-improvement process is being optimized**, rather than generic agent components such as planning, tools, or multi-agent coordination.

| Branch | Core problem | Representative work |
|---|---|---|
| **B1 · Search & Candidate Improvement** | generate, explore, refine, and select better AI solutions | SELA, AIDE, I-MCTS, MLE-STAR, R&D-Agent |
| **B2 · Execution & Evaluation** | obtain reliable executable feedback and attribute gains/failures | MLE-bench, MLE-Dojo, executable graders and verifiers |
| **B3 · Experience & Knowledge Accumulation** | turn previous runs into transferable skills, lessons, and reusable knowledge | DS-Agent, ML-Master, AIBuildAI-2, MLEvolve |
| **B4 · Adaptive Decision Making** | use current results and accumulated state to choose the next high-value action | I-MCTS, Reasoning as Gradient, FOREAGENT, hypothesis-tree methods |
| **B5 · Learning from Execution** | internalize AI-building experience into the agent/model policy | ML-Agent, MLE-RL, AceGRPO, Frontis-MA1 |
| **B6 · Agent & Harness Optimization** | improve prompts, tools, context, memory implementation, topology, and orchestration | ADAS, EvoAgentX, Meta-Harness, Self-Harness, SwarmAgentic |
| **B7 · Program & Algorithm Evolution** | evolve populations of executable programs, algorithms, or agents | FunSearch, AlphaEvolve, AdaEvolve, OpenMLE-Evo |
| **B8 · Improver Learning & Meta-Evolution** | improve the mechanism that performs AI improvement | Frontis-MA1 / OpenRSI, self-improving evolutionary systems |
| **B9 · Full-Cycle AI Development** | automate increasingly complete AI-development workflows | AI Scientist, AIRA, AlphaLab, AutoTrainess, ResearchGym |

> The branches are not mutually exclusive. A system such as **Frontis-MA1** combines executable environments, policy learning, evolutionary search, and improver learning; **MLEvolve** combines search, evolution, and accumulated experience.

Detailed method map → [`agent4ai/README.md`](agent4ai/README.md)

---

## ⭐ Representative Systems

| Year | Paper / System | Area | Main idea |
|:---:|---|---|---|
| 2023/24 | [MLAgentBench](https://arxiv.org/abs/2310.03302) | MLE | iterative ML experimentation benchmark |
| 2024 | [DS-Agent](https://arxiv.org/abs/2402.17453) | Data / MLE | case-based reuse of data-science experience |
| 2024 | [The AI Scientist](https://arxiv.org/abs/2408.06292) | AI Research | idea → experiment → paper → review |
| 2024 | [MLE-bench](https://arxiv.org/abs/2410.07095) | Evaluation | end-to-end competition-scale MLE |
| 2024 | [SELA](https://arxiv.org/abs/2410.17238) | MLE | tree-search-enhanced LLM AutoML |
| 2025 | [AIDE](https://arxiv.org/abs/2502.13138) | MLE | solution-tree search in code space |
| 2025 | [MLE-Dojo](https://arxiv.org/abs/2505.07782) | Training / Eval | executable environments for MLE agents |
| 2025 | [ML-Agent](https://arxiv.org/abs/2505.23723) | Agent Learning | RL for autonomous MLE |
| 2025 | [R&D-Agent](https://arxiv.org/abs/2505.14738) | AI Development | research + development + evolution |
| 2025 | [MLE-STAR](https://arxiv.org/abs/2506.15692) | MLE | search + targeted refinement |
| 2025 | [ML-Master](https://arxiv.org/abs/2506.16499) | MLE | exploration + reasoning + adaptive memory |
| 2025 | [AlphaEvolve](https://arxiv.org/abs/2506.13131) | Algorithm Discovery | LLM-guided evolutionary coding |
| 2025/26 | [DataMind](https://arxiv.org/abs/2509.25084) | Data Agent | scaling generalist executable data-analytic agents |
| 2026 | [FOREAGENT](https://arxiv.org/abs/2601.05930) | MLE | predict-then-verify candidate execution |
| 2026 | [DSGym](https://arxiv.org/abs/2601.16344) | Data Agent | executable training/evaluation environments |
| 2026 | [Meta-Harness](https://arxiv.org/abs/2603.28052) | Agent System | optimize harness source code from traces and scores |
| 2026 | [AIBuildAI-2](https://arxiv.org/abs/2605.27873) | MLE | evolving knowledge distilled from completed runs |
| 2026 | [Self-Harness](https://arxiv.org/abs/2606.09498) | Agent System | agent improves its own harness |
| 2026 | [MLEvolve](https://arxiv.org/abs/2606.06473) | MLE / Evolution | progressive graph search + retrospective memory |
| 2026 | [AutoTrainess](https://arxiv.org/abs/2606.31551) | Post-Training | autonomous LM post-training agent |
| 2026 | [Frontis-MA1 / OpenRSI](https://arxiv.org/abs/2607.28568) | Self-Improvement | execution-grounded learning + evolutionary AI4AI loop |

Full bibliography → [`agent4ai/papers.md`](agent4ai/papers.md) · [`agent4ai/recent.md`](agent4ai/recent.md)

---

## 🧪 Benchmark Landscape

Agent4AI benchmarks increasingly move from isolated coding tasks toward complete, executable AI-development loops.

| Benchmark | Year | What it tests |
|---|:---:|---|
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023/24 | iterative ML experimentation |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | 2024 | competition-scale ML engineering |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | 2024/25 | long-horizon AI R&D |
| [PaperBench](https://arxiv.org/abs/2504.01848) | 2025 | AI paper reproduction |
| [MLE-Dojo](https://arxiv.org/abs/2505.07782) | 2025 | executable MLE training/evaluation |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | 2025 | open-ended ML improvement/research |
| [ResearchCodeBench](https://arxiv.org/abs/2506.02314) | 2025 | implementing novel methods from ML papers |
| [EXP-Bench](https://arxiv.org/abs/2505.24785) | 2025/26 | complete executable AI experiments |
| [DSGym](https://arxiv.org/abs/2601.16344) | 2026 | generalist data-agent training/evaluation |
| [ResearchGym](https://arxiv.org/abs/2602.15112) | 2026 | real-world closed-loop AI projects |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | 2026 | autonomous LLM post-training |
| [MLS-Bench](https://arxiv.org/abs/2605.08678) | 2026 | AI improvements that generalize across settings/scales |
| [NatureBench](https://arxiv.org/abs/2606.24530) | 2026 | reproducing published code/results |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | recursive-improvement-oriented data agents |

Full benchmark map → [`agent4ai/benchmarks.md`](agent4ai/benchmarks.md)

---

## 🚀 Getting Started

A compact path through the field:

```text
MLE-bench
   ↓
AIDE / MLE-STAR / ML-Master
   ↓
MLE-Dojo / ML-Agent
   ↓
AIBuildAI-2 / MLEvolve
   ↓
Meta-Harness / Self-Harness
   ↓
Frontis-MA1 / OpenRSI
```

Then branch by the AI system you want to improve:

- **ML engineering:** AIDE → MLE-STAR → ML-Master → MLEvolve
- **data agents:** DS-Agent → DataMind → DSGym
- **model/post-training:** PostTrainBench → AutoTrainess → ANDES
- **agent learning:** MLE-Dojo → ML-Agent → Frontis-MA1
- **agent-system optimization:** ADAS → Meta-Harness → Self-Harness
- **algorithm discovery:** FunSearch → AlphaEvolve → AdaEvolve
- **AI research/reproduction:** AI Scientist → ResearchCodeBench → ResearchGym

For reproducible starting projects and concrete research questions → **[Getting Started with Agent4AI](agent4ai/getting-started.md)**.

---

<details>
<summary><h2>📜 Classical AI4AI Background</h2></summary>

AutoML, HPO, NAS, meta-learning, learned optimizers, and LLM-as-optimizer methods provide historical context. They are background rather than the main focus here.

**AutoML / HPO:** Auto-WEKA · auto-sklearn · TPOT · Hyperband · BOHB  
**NAS:** NASNet · ENAS · DARTS · Once-for-All  
**Meta-learning / learned optimization:** MAML · Population Based Training · VeLO  
**Algorithm discovery / LLM optimization:** AutoML-Zero · OPRO · TextGrad

→ [`foundations/papers.md`](foundations/papers.md)

</details>

---

## Repository Structure

```text
Awesome-AI4AI/
├── README.md
├── agent4ai/
│   ├── README.md          # detailed taxonomy
│   ├── getting-started.md # newcomer → research path
│   ├── papers.md          # main bibliography
│   ├── recent.md          # newly discovered papers
│   ├── benchmarks.md      # benchmark landscape
│   └── surveys.md         # related surveys
├── foundations/
│   └── papers.md          # brief historical background
└── writing/
    ├── notes.md           # survey ideas / gaps
    └── reading-list.md    # prioritized reading list
```

## Scope

> **Core criterion:** does the agent make AI better at building, training, evaluating, optimizing, redesigning, or researching AI?

Generic agent techniques are included only when they directly contribute to this AI-improvement objective.

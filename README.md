<div align="center">

# 🤖 Awesome AI4AI

### AI Agents for Improving AI

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Focus](https://img.shields.io/badge/Focus-Agent4AI-blue)
![Coverage](https://img.shields.io/badge/Coverage-2024--2026-orange)
![Papers](https://img.shields.io/badge/Agent4AI-160%2B%20papers-brightgreen)

**AI4AI** asks a simple question: **how can AI improve AI?**

This repository focuses on **Agent4AI** — AI agents that build, train, evaluate, optimize, redesign, or research AI systems. This includes **MLE agents, data-analytic agents, LLM post-training agents, algorithm/program discovery, agent-system optimization, AI research agents, and self-improving AI systems**.

[🚀 Start Here](agent4ai/getting-started.md) · [🧭 Agent4AI Taxonomy](agent4ai/README.md) · [📚 Papers](agent4ai/papers.md) · [🧪 Benchmarks](agent4ai/benchmarks.md) · [🆕 Recent Papers](agent4ai/recent.md) · [📖 Surveys](agent4ai/surveys.md)

</div>

---

## What does Agent4AI do?

The common pattern is an **AI improvement loop**:

```text
Goal: build / improve an AI system
              ↓
     Propose candidate changes
              ↓
      Build / Train / Execute
              ↓
       Evaluate / Verify
              ↓
 Interpret outcome / assign credit
              ↓
 Update experience / decision state
              ↓
      Select the next action
              ↓
Learn the policy / redesign the agent
              ↓
             Repeat
```

The target can be a model, data pipeline, training recipe, algorithm, agent harness, or complete AI-development workflow.

---

## Main Agent4AI application families

| Family | What the agent improves | Representative work |
|---|---|---|
| **MLE / AutoML Agents** | ML pipelines, features, models, code, experiments | MLAgentBench, AIDE, MLE-STAR, ML-Master, AIBuildAI-2 |
| **Data-Analytic Agents for AI** | executable data analysis and modeling workflows | DS-Agent, DataMind, DSGym, DatawiseAgent |
| **LLM Training / Post-Training Agents** | data synthesis, fine-tuning, alignment, post-training recipes | AutoTrainess, PostTrainBench, ANDES |
| **Algorithm / Program Discovery** | algorithms, optimizers, executable programs | FunSearch, AlphaEvolve, MLEvolve, AdaEvolve |
| **Agent-System Optimization** | prompts, tools, memory, topology, orchestration, harness source | ADAS, EvoAgentX, SwarmAgentic, Meta-Harness, Self-Harness |
| **AI Research / Reproduction Agents** | research ideas, experiments, implementations, papers | AI Scientist, AIRA, Agent Laboratory, ResearchCodeBench, ResearchGym |
| **Self-Improving AI Systems** | the agent or improver used to build future AI | Frontis-MA1 / OpenRSI, meta-evolution systems |

> These are **application families**. Our method taxonomy separately asks **how** the agent improves AI.

---

# 🔥 Agent4AI Method Map

Rather than use a generic agent taxonomy such as *planning / memory / tools / multi-agent*, we organize methods by **which part of the AI-improvement loop becomes better**.

| Branch | What improves? | Representative work |
|---|---|---|
| **B1. Candidate Generation & Search** | code, models, pipelines, algorithms, candidate experiments | SELA, AIDE, I-MCTS, MLE-STAR, R&D-Agent |
| **B2. Execution, Evaluation & Credit** | quality of executable feedback and attribution | MLE-bench, MLE-Dojo, executable graders / verifiers |
| **B3. Experience → Reusable Knowledge** | transferable lessons, skills, failure modes | ML-Master, AIBuildAI-2, MLEvolve |
| **B4. State Update & Next-Action Selection** | search state, uncertainty, value estimates, hypotheses | I-MCTS, Reasoning as Gradient, FOREAGENT, hypothesis-tree methods |
| **B5. Policy Learning from Experience** | model / agent weights | ML-Agent, MLE-RL, AceGRPO, Frontis-MA1 |
| **B6. Harness / Workflow Optimization** | prompts, tools, memory implementation, context, topology | ADAS, Meta-Harness, Self-Harness, SwarmAgentic |
| **B7. Program / Algorithm Evolution** | populations of programs, algorithms, agents | FunSearch, AlphaEvolve, AdaEvolve, OpenMLE-Evo |
| **B8. Improver Learning / Meta-Evolution** | the improvement mechanism itself | Frontis-MA1 / OpenRSI, self-improving evolutionary systems |
| **B9. Full-Cycle AI Development** | complete AI-development or research workflows | AI Scientist, AIRA, AlphaLab, ResearchGym |

Detailed taxonomy → [`agent4ai/README.md`](agent4ai/README.md)

---

## Where does memory fit?

**Memory itself is not automatically AI4AI.** It belongs here when stored experience directly improves future AI-building decisions.

```text
M1  Trajectory memory
    remember runs, code, metrics, failures
           ↓
M2  Experience / knowledge
    extract reusable skills, lessons, failure conditions
           ↓
M3  Structured decision state
    maintain confidence, evidence, promising directions,
    unresolved questions, or values of candidate actions
```

The important problem is therefore not merely *how to retrieve memory*, but **how experience is written, credited, abstracted, revised, forgotten, and converted into better future AI-development actions**.

Examples include **ML-Master, AIBuildAI-2, MLEvolve**, and hypothesis/evidence-state approaches.

---

## Where do world models / predictive models fit?

They are **not a standalone top-level Agent4AI direction**.

They are one possible mechanism in **B4: State Update & Next-Action Selection**. Because full training runs and experiments are expensive, an agent may estimate candidate value before execution:

```text
candidate actions
      ↓
heuristic / MCTS value / uncertainty / learned critic / predictor
      ↓
prioritize
      ↓
execute selectively
      ↓
update state
```

[FOREAGENT](https://arxiv.org/abs/2601.05930) is one example of predict-then-verify. Other systems can solve the same decision problem with search values, bandits, cheap proxy runs, uncertainty, or learned critics.

---

## ⭐ Representative Agent4AI systems

| Year | Paper / System | Family | Main idea |
|:---:|---|---|---|
| 2023/24 | [MLAgentBench](https://arxiv.org/abs/2310.03302) | MLE | iterative ML experimentation benchmark |
| 2024 | [DS-Agent](https://arxiv.org/abs/2402.17453) | Data / MLE | case-based reuse of data-science experience |
| 2024 | [The AI Scientist](https://arxiv.org/abs/2408.06292) | AutoResearch | idea → experiment → paper → review |
| 2024 | [MLE-bench](https://arxiv.org/abs/2410.07095) | Benchmark | 75 Kaggle competitions for end-to-end MLE |
| 2024 | [SELA](https://arxiv.org/abs/2410.17238) | MLE | tree-search-enhanced LLM AutoML |
| 2025 | [AIDE](https://arxiv.org/abs/2502.13138) | MLE | solution-tree search in code space |
| 2025 | [MLE-Dojo](https://arxiv.org/abs/2505.07782) | Training / Benchmark | executable environments for MLE agents |
| 2025 | [ML-Agent](https://arxiv.org/abs/2505.23723) | Policy Learning | RL for autonomous MLE |
| 2025 | [R&D-Agent](https://arxiv.org/abs/2505.14738) | MLE / AI R&D | research + development + evolution |
| 2025 | [MLE-STAR](https://arxiv.org/abs/2506.15692) | MLE | search + targeted refinement |
| 2025 | [ML-Master](https://arxiv.org/abs/2506.16499) | MLE / Memory | exploration + reasoning + adaptive memory |
| 2025/26 | [DataMind](https://arxiv.org/abs/2509.25084) | Data Agent | scaling generalist executable data-analytic agents |
| 2025 | [AlphaEvolve](https://arxiv.org/abs/2506.13131) | Algorithm Discovery | LLM-guided evolutionary coding |
| 2026 | [DSGym](https://arxiv.org/abs/2601.16344) | Data Agent | executable training/evaluation environments |
| 2026 | [FOREAGENT](https://arxiv.org/abs/2601.05930) | Decision / MLE | predict-then-verify candidate execution |
| 2026 | [AIBuildAI-2](https://arxiv.org/abs/2605.27873) | MLE / Knowledge | evolving knowledge distilled from completed MLE runs |
| 2026 | [MLEvolve](https://arxiv.org/abs/2606.06473) | MLE / Evolution | progressive graph search + retrospective memory |
| 2026 | [Meta-Harness](https://arxiv.org/abs/2603.28052) | Harness | optimize harness source code using traces and scores |
| 2026 | [Self-Harness](https://arxiv.org/abs/2606.09498) | Harness | agent improves its own harness |
| 2026 | [AutoTrainess](https://arxiv.org/abs/2606.31551) | Post-Training | autonomous LM post-training agent |
| 2026 | [Frontis-MA1 / OpenRSI](https://arxiv.org/abs/2607.28568) | Self-Improvement | execution-grounded learning + evolutionary AI4AI loop |

Full bibliography → [`agent4ai/papers.md`](agent4ai/papers.md) and [`agent4ai/recent.md`](agent4ai/recent.md)

---

## 🧪 Benchmark map

| Benchmark | What it tests |
|---|---|
| [MLE-bench](https://arxiv.org/abs/2410.07095) | competition-scale ML engineering |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | long-horizon AI R&D |
| [MLE-Dojo](https://arxiv.org/abs/2505.07782) | executable MLE training/evaluation |
| [PaperBench](https://arxiv.org/abs/2504.01848) | AI paper reproduction |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | open-ended ML research |
| [ResearchCodeBench](https://arxiv.org/abs/2506.02314) | implementing novel methods from ML papers |
| [EXP-Bench](https://arxiv.org/abs/2505.24785) | complete AI research experiments |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | autonomous LLM post-training |
| [ResearchGym](https://arxiv.org/abs/2602.15112) | real-world closed-loop AI projects |
| [MLS-Bench](https://arxiv.org/abs/2605.08678) | building AI improvements that generalize across settings/scales |
| [NatureBench](https://arxiv.org/abs/2606.24530) | reproducing / matching published scientific code results |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | recursive-improvement-oriented data agents |

Full map → [`agent4ai/benchmarks.md`](agent4ai/benchmarks.md)

---

## 🚀 New to the field?

A practical reading path is:

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

Then branch based on your interest:

- **MLE / search:** AIDE, MLE-STAR, ML-Master;
- **learning agents:** MLE-Dojo, ML-Agent, Frontis-MA1;
- **memory / experience:** AIBuildAI-2, MLEvolve;
- **post-training:** AutoTrainess, PostTrainBench, ANDES;
- **agent-system optimization:** ADAS, Meta-Harness, Self-Harness;
- **algorithm discovery:** AlphaEvolve, MLEvolve, AdaEvolve;
- **AI research:** AI Scientist, AIRA, ResearchGym.

For reproducible starting projects, benchmark choices, and concrete research questions, see **[Getting Started with Agent4AI Research](agent4ai/getting-started.md)**.

---

<details>
<summary><h2>📜 Classical AI4AI Background</h2></summary>

AutoML, HPO, NAS, meta-learning, learned optimizers, and LLM-as-optimizer methods provide historical context for AI4AI. They are kept as background rather than the main focus of this repository.

Examples: Auto-WEKA · auto-sklearn · TPOT · Hyperband · DARTS · MAML · AutoML-Zero · OPRO · TextGrad.

Full background bibliography → [`foundations/papers.md`](foundations/papers.md)

</details>

---

## Repository structure

```text
Awesome-AI4AI/
├── README.md
├── agent4ai/
│   ├── README.md          # detailed method taxonomy
│   ├── getting-started.md # newcomer → reproducible research path
│   ├── papers.md          # main Agent4AI bibliography
│   ├── recent.md          # newly discovered papers
│   ├── benchmarks.md      # benchmark landscape
│   └── surveys.md         # related surveys
├── foundations/
│   └── papers.md          # classical AI4AI background
└── writing/
    ├── notes.md           # survey ideas / gaps
    └── reading-list.md    # prioritized reading list
```

---

## Scope

The core criterion is:

> **Does this method make AI better at building, training, evaluating, optimizing, redesigning, or researching AI?**

If not, it is probably a generic agent method rather than a core Agent4AI paper.

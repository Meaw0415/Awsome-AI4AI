<div align="center">

# 🤖 Awesome AI4AI

### From AutoML to Agent4AI and Recursive Self-Improvement

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Focus](https://img.shields.io/badge/Focus-Agent4AI-blue)
![Coverage](https://img.shields.io/badge/Coverage-2024--2026-orange)
![Papers](https://img.shields.io/badge/Agent4AI-160%2B%20papers-brightgreen)

**AI4AI** studies how AI can improve the development of AI itself. This repository emphasizes **Agent4AI**: agents that build models, run experiments, learn from execution, optimize research strategies, and increasingly improve the machinery used to build future AI.

[Agent4AI Hub](agent4ai/README.md) · [Paper Table](agent4ai/papers.md) · [Recent Papers](agent4ai/recent.md) · [Benchmarks](agent4ai/benchmarks.md) · [Surveys](agent4ai/surveys.md) · [Foundations](foundations/papers.md) · [Writing Notes](writing/notes.md)

</div>

---

## 🧭 AI4AI Evolution

```text
AutoML / HPO / NAS
        ↓
LLMs as Optimizers & Program Search
        ↓
MLE Agents: code → execute → metric → revise
        ↓
Long-horizon Search + Memory + Experience
        ↓
Execution-grounded SFT / RL
        ↓
World Models / Research Judgment
        ↓
Harness & Improver Optimization
        ↓
AI Research Agents / AI Scientists
        ↓
Meta-Evolution / Recursive Self-Improvement
```

The central shift is from **optimizing a solution** to **optimizing the process that generates future solutions**.

---

# 🔥 Agent4AI Method Paradigms

A useful way to organize modern Agent4AI is by **where the improvement lives**. This taxonomy follows the structure emerging from recent MLE/AutoResearch work, especially OpenRSI / Frontis-MA1, while separating several increasingly important branches.

| Paradigm | What changes? | Feedback / state | Representative papers |
|---|---|---|---|
| **P1. Inference-Time Search & Scaffolds** | candidate code / experiment trajectory | execution score, logs, search tree | SELA, AIDE, I-MCTS, MLE-STAR, AIRA, AutoMLGen |
| **P2. Execution-Grounded Agent Learning** | model policy / operator behavior | executable rewards, SFT/RL trajectories | ML-Agent, MLE-RL, AceGRPO, OpenMLE-ERL / Frontis-MA1 |
| **P3. Experience & Memory Augmentation** | retrieved experience / persistent state | successful + failed experiments, cross-task knowledge | ML-Master, MLEvolve, AIBuildAI-2, hypothesis-tree refinement |
| **P4. Predictive World Models & Research Judgment** | predicted value of future experiments | learned execution priors, uncertainty, research-value signals | FOREAGENT; emerging AI4AI world-model / research-taste direction |
| **P5. Harness / Workflow Optimization** | prompts, tools, orchestration, memory code, agent topology | traces + downstream task scores | Automated Design of Agentic Systems, EvoAgentX, Meta-Harness, SwarmAgentic |
| **P6. Evolutionary / Program-Discovery Systems** | programs, algorithms, populations | executable fitness + recombination / mutation | FunSearch, AlphaEvolve, MLEvolve, AdaEvolve, OpenMLE-Evo |
| **P7. Trainable Improvers / Meta-Evolution** | the improver itself | search experience returns to training, then back to search | Frontis-MA1 / OpenRSI, MLE-RL, test-time learning, self-improving agents |
| **P8. Full AutoResearch / AI Scientists** | hypotheses, experiments, evidence, papers, research state | scientific evidence, reviewer / benchmark / artifact feedback | AI Scientist, AI Scientist-v2, Agent Laboratory, AIRA_2, Arbor |

### A second axis: what is the optimization target?

```text
solution parameters
      ↓
program / model code
      ↓
experiment trajectory
      ↓
agent policy
      ↓
experience / memory
      ↓
harness / workflow
      ↓
research strategy
      ↓
the improver itself
```

This distinction matters because two systems may use the same LLM but represent very different levels of AI4AI: **AIDE searches candidate solutions**, **ML-Agent changes the agent policy**, **Meta-Harness changes the harness**, and **OpenRSI explicitly couples search experience back into training of the improver**.

---

<details open>
<summary><h2>🌲 P1 · Inference-Time Search & Scaffolds</h2></summary>

Keep the underlying model mostly fixed and spend additional inference compute on structured exploration, branching, selection, refinement, or multi-agent decomposition.

| Year | Paper | Main mechanism |
|:---:|---|---|
| 2024 | [SELA](https://arxiv.org/abs/2410.17238) | tree-search enhanced LLM AutoML |
| 2025 | [AIDE](https://arxiv.org/abs/2502.13138) | solution-tree exploration in code space |
| 2025 | [I-MCTS](https://arxiv.org/abs/2502.14693) | introspective Monte Carlo tree search |
| 2025 | [MLE-STAR](https://arxiv.org/abs/2506.15692) | search + targeted code-block refinement |
| 2025 | [AI Research Agents for Machine Learning](https://arxiv.org/abs/2507.02554) | search / exploration policies on MLE-Bench |
| 2025 | [AutoMLGen](https://arxiv.org/abs/2510.08511) | fine-grained optimization for coding agents |
| 2026 | [Reasoning as Gradient](https://arxiv.org/abs/2603.01692) | iterative reasoning feedback beyond conventional tree search |

**Core idea:** improvement remains largely in an **external scaffold**. The model proposes; the harness allocates compute and decides what to try next.

</details>

<details open>
<summary><h2>🎯 P2 · Execution-Grounded Agent Learning</h2></summary>

Instead of keeping all improvement logic outside the model, these methods **internalize executable experience** through SFT, RL, preference optimization, or other post-training.

| Year | Paper | Main mechanism |
|:---:|---|---|
| 2025 | [ML-Agent](https://arxiv.org/abs/2505.23723) | reinforcement learning for autonomous MLE |
| 2025 | [MLE-RL](https://openreview.net/forum?id=nElqyHPHAz) | RL for self-improvement in machine-learning agents |
| 2025 | [MLE-Dojo](https://arxiv.org/abs/2505.07782) | interactive executable environments for training MLE agents |
| 2026 | [AceGRPO](https://arxiv.org/abs/2602.07906) | curriculum-enhanced GRPO for autonomous MLE |
| 2026 | [Frontis-MA1 / OpenMLE-ERL](https://arxiv.org/abs/2607.28568) | execution-grounded SFT + RL over Draft / Improve / Debug / Crossover operators |

**Core idea:** the result of an experiment is not only used to select a branch; it becomes a **training signal for future behavior**.

</details>

<details open>
<summary><h2>🧠 P3 · Experience, Memory & Persistent Research State</h2></summary>

These systems explicitly preserve what happened before so that later decisions do not restart from scratch.

| Year | Paper | Experience mechanism |
|:---:|---|---|
| 2024 | [DS-Agent](https://arxiv.org/abs/2402.17453) | case-based reasoning from prior data-science tasks |
| 2025 | [ML-Master](https://arxiv.org/abs/2506.16499) | adaptive memory integrated with exploration / reasoning |
| 2025 | [AutoMind](https://arxiv.org/abs/2506.10974) | external expert knowledge + adaptive retrieval |
| 2026 | [AIBuildAI-2](https://arxiv.org/abs/2605.27873) | evolving hierarchical knowledge base + experience distillation |
| 2026 | [MLEvolve](https://arxiv.org/abs/2606.06473) | retrospective memory + graph-based cross-branch information flow |
| 2026 | [Toward Generalist Autonomous Research via Hypothesis-Tree Refinement](https://arxiv.org/abs/2606.11926) | persistent hypotheses, artifacts, evidence, and reusable insights |
| 2026 | [Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering](https://arxiv.org/abs/2606.30911) | cross-task skill accumulation |

**Core idea:** optimization state grows from `code + score` into **trajectory / knowledge / hypothesis / evidence state**.

</details>

<details open>
<summary><h2>🔮 P4 · Predictive World Models & Research Judgment</h2></summary>

Execution is expensive. A stronger Agent4AI system should learn to estimate **what will happen** and **which experiment is worth running** before spending compute.

| Year | Paper / direction | Main idea |
|:---:|---|---|
| 2026 | [FOREAGENT: Can We Predict Before Executing Machine Learning Agents?](https://arxiv.org/abs/2601.05930) | Predict-then-Verify with learned execution priors |
| 2026 | [OpenRSI / Frontis-MA1](https://arxiv.org/abs/2607.28568) | explicitly identifies richer research objectives, AI4AI world models, and research judgment as a next step |
| Emerging | **Research world models / research taste** | predict improvement, information gain, robustness, generalization, or value-of-compute rather than only final metric |

**Core idea:** move from a purely reactive loop

`generate → execute → observe`

toward

`predict → prioritize → execute selectively → update belief`.

</details>

<details open>
<summary><h2>🧰 P5 · Harness & Workflow Optimization</h2></summary>

The optimization target is no longer the task solution alone — it becomes the **agent system itself**: context management, memory, tools, prompts, roles, topology, and orchestration.

| Year | Paper | What is optimized? |
|:---:|---|---|
| 2024 | [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) | agentic system design |
| 2025 | [EvoAgentX](https://arxiv.org/abs/2507.03616) | evolving agentic workflows |
| 2025 | [SwarmAgentic](https://aclanthology.org/2025.emnlp-main.93/) | swarm-based automated agent-system generation |
| 2026 | [Meta-Harness](https://arxiv.org/abs/2603.28052) | harness source code using prior source, traces, and scores |
| 2026 | [Better Harnesses, Smaller Models](https://arxiv.org/abs/2607.08938) | automated adaptation of instructions, tools, and orchestration |

**Core idea:** instead of asking “what code should the agent write?”, ask **“what agent should we build to solve future tasks?”**

</details>

<details open>
<summary><h2>🧬 P6–P7 · Evolution, Self-Evolution & Meta-Evolution</h2></summary>

Evolutionary Agent4AI treats executable programs or agents as a population. The more ambitious step is to make the **variation mechanism / improver** itself learn from prior evolution.

| Year | Paper | Level |
|:---:|---|---|
| 2023/24 | [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) | LLM-guided program evolution |
| 2025 | [AlphaEvolve](https://arxiv.org/abs/2506.13131) | evolutionary coding for algorithms / scientific discovery |
| 2025 | [Self-Improving Language Models for Evolutionary Program Synthesis](https://arxiv.org/abs/2507.14172) | search experience returned through hindsight fine-tuning |
| 2025 | [ShinkaEvolve](https://arxiv.org/abs/2509.19349) | open-ended, sample-efficient program evolution |
| 2026 | [AdaEvolve](https://arxiv.org/abs/2602.20133) | adaptive LLM-driven zeroth-order optimization |
| 2026 | [MLEvolve](https://arxiv.org/abs/2606.06473) | self-evolving MLE search + memory |
| 2026 | [Frontis-MA1 / OpenRSI](https://arxiv.org/abs/2607.28568) | **meta-evolution:** search generates executable experience that trains the same operators used in future search |
| 2026 | [Self-Improving Agents in the Era of Experience](https://openreview.net/forum?id=IUltZSgLMm) | survey framing self-evolution → meta-evolution → RSI |

### The RSI ladder

```text
Evolution
  candidate solutions improve
        ↓
Self-Evolution
  agent/system modifies itself
        ↓
Meta-Evolution
  the improver learns how to improve
        ↓
Recursive Self-Improvement
  improved improvers accelerate future improvement
```

OpenRSI is especially useful conceptually because it couples **environment → execution → experience → training → evolutionary search** in one reproducible loop rather than treating search and learning as separate components.

</details>

<details open>
<summary><h2>🔬 P8 · AutoResearch, AI Research Agents & AI Scientists</h2></summary>

Here the unit of optimization grows beyond a competition score into a research process: **hypothesis → experiment → evidence → interpretation → artifact**.

| Year | Paper | Research scope |
|:---:|---|---|
| 2024 | [ResearchAgent](https://arxiv.org/abs/2404.07738) | literature-grounded iterative ideation |
| 2024 | [The AI Scientist](https://arxiv.org/abs/2408.06292) | idea → experiments → paper → review |
| 2025 | [Agent Laboratory](https://arxiv.org/abs/2501.04227) | multi-agent literature / experimentation / writing |
| 2025 | [AI Scientist-v2](https://arxiv.org/abs/2504.08066) | agentic tree-search scientific discovery |
| 2025 | [AI Research Agents for Machine Learning](https://arxiv.org/abs/2507.02554) | MLE search, exploration, generalization |
| 2026 | [AIRA_2](https://arxiv.org/abs/2603.26499) | improved AI-research-agent search / harness |
| 2026 | [Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018) | persistent long-horizon ML research engineering |
| 2026 | [Toward Generalist Autonomous Research via Hypothesis-Tree Refinement](https://arxiv.org/abs/2606.11926) | hypothesis / evidence state across long-horizon research |

</details>

---

## 📊 Benchmarks: What Part of AI R&D Is Being Tested?

| Benchmark | Year | Evaluation target |
|---|:---:|---|
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023/24 | iterative ML experimentation |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | 2024 | end-to-end Kaggle-style MLE |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | 2024/25 | long-horizon frontier AI R&D |
| [MLE-Dojo](https://arxiv.org/abs/2505.07782) | 2025 | executable environments for MLE training/eval |
| [PaperBench](https://arxiv.org/abs/2504.01848) | 2025 | replication of AI research papers |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | 2025 | open-ended ML research |
| [ResearchCodeBench](https://arxiv.org/abs/2506.02314) | 2025 | implementing novel ML research methods |
| [EXP-Bench](https://arxiv.org/abs/2505.24785) | 2025/26 | complete AI research experiments |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | 2026 | autonomous LLM post-training |
| [ResearchGym](https://arxiv.org/abs/2602.15112) | 2026 | real-world AI research projects |
| [AIRS-Bench](https://arxiv.org/abs/2602.06855) | 2026 | frontier AI research science agents |
| [MLS-Bench](https://arxiv.org/abs/2605.08678) | 2026 | inventing generalizable / scalable ML methods |
| [NatureBench](https://arxiv.org/abs/2606.24530) | 2026 | matching or surpassing published scientific SOTA |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | RSI-oriented data-agent evaluation |

Full map → [`agent4ai/benchmarks.md`](agent4ai/benchmarks.md)

---

<details>
<summary><h2>📜 Classical AI4AI Foundations</h2></summary>

These are retained as the historical substrate of Agent4AI.

**AutoML / HPO:** Auto-WEKA · auto-sklearn · TPOT · Hyperband · BOHB · AutoGluon · FLAML  
**NAS:** NAS with RL · NASNet · ENAS · DARTS · ProxylessNAS · Once-for-All  
**Meta-Learning / Learned Optimization:** Learning to Learn by Gradient Descent · MAML · Population-Based Training · VeLO  
**Algorithm / Program Discovery:** Neural Optimizer Search · AutoML-Zero · FunSearch · AlphaEvolve  
**LLMs as Optimizers:** APE · OPRO · Promptbreeder · Eureka · TextGrad

Full foundation bibliography → [`foundations/papers.md`](foundations/papers.md)

</details>

---

## 🗂 Repository Structure

```text
Awesome-AI4AI/
├── README.md
├── agent4ai/
│   ├── README.md          # detailed taxonomy / navigation
│   ├── papers.md          # master Agent4AI paper table
│   ├── recent.md          # newly verified papers before merge
│   ├── benchmarks.md      # evaluation landscape
│   └── surveys.md         # surveys / reviews
├── foundations/
│   └── papers.md          # AutoML / NAS / meta-learning / algorithm discovery
└── writing/
    ├── notes.md           # survey thesis / gaps / writing ideas
    └── reading-list.md    # prioritized reading path
```

**Maintenance rule:** new papers → `agent4ai/recent.md` → verify / deduplicate / classify → merge into `agent4ai/papers.md`.

---

## ⭐ Scope

We use **AI4AI** as the umbrella term. The repository particularly tracks **Agent4AI**: systems that improve AI artifacts, AI-development policies, agent workflows, or the research process itself. General-purpose agents are included only when their method directly informs AI R&D automation.

Contributions, missing papers, benchmark updates, and corrections are welcome.

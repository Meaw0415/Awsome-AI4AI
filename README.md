<div align="center">

# 🤖 Awesome AI4AI

### From AutoML and NAS to Autonomous and Self-Improving AI Research

**AI4AI** studies AI systems that improve **AI artifacts or the processes that create AI**: data, hyperparameters, pipelines, architectures, optimizers, objectives, algorithms, programs, model training, experiments, agent workflows, harnesses, and eventually the improver itself.

[📚 Full AI4AI Library](foundations/papers.md) · [🤖 Agentic AI4AI](agent4ai/README.md) · [🧪 Benchmarks](agent4ai/benchmarks.md) · [📖 Related Surveys](agent4ai/surveys.md) · [✍️ Survey Notes](writing/notes.md)

</div>

---

## 🧭 Scope: AI Improving AI, Across Generations of Methods

This repository is **not limited to MLE agents or Agent4AI**. We treat recent agents as the newest part of a much longer AI4AI lineage:

```text
Algorithm selection / HPO
        ↓
Classical AutoML and pipeline search
        ↓
Neural Architecture Search
        ↓
Meta-learning and learned optimizers
        ↓
Algorithm / objective / program discovery
        ↓
LLMs as general-purpose optimization operators
        ↓
Agentic ML engineering and model training
        ↓
Autonomous AI research
        ↓
Agent / workflow / harness optimization
        ↓
Self-improving and recursive AI4AI
```

The common thread is an expanding **object of improvement** and an increasingly capable **improver**.

---

# 🔥 Six-Block AI4AI Map

## I. Automated Optimization — HPO, Algorithm Selection & AutoML

**What is improved:** hyperparameters, algorithms, features, pipelines.  
**Typical feedback:** validation performance and resource cost.  
**Representative lineage:** Rice → ParamILS / SMAC / TPE → Auto-WEKA → auto-sklearn → TPOT → Hyperband / BOHB → AutoGluon / FLAML.

This era establishes the canonical AI4AI loop:

`propose → evaluate → update`

but the search space, objective, and workflow remain mostly human-defined.

## II. Automated Design & Learning to Improve — NAS, Meta-Learning, Learned Optimization

**What is improved:** model structures and the optimization procedure itself.  
**Representative lineage:** NASNet / evolution → ENAS → DARTS → Once-for-All; MAML / RL² → learned optimizers → PBT → VeLO.

The key transition is from **choosing configurations** to **designing structures and learning reusable improvement rules**.

## III. Open-Ended Artifact Discovery — Objectives, Rewards, Data, Algorithms & Programs

**What is improved:** executable learning procedures, rewards, data policies, algorithms, and programs.  
**Representative lineage:** AutoAugment → AutoML-Zero → Eureka → FunSearch → AlphaEvolve → modern program-evolution systems.

This stage greatly expands the search representation from vectors and graphs to **programs and executable artifacts**.

## IV. Foundation Models as AI Improvement Operators

LLMs make natural language and code a general proposal space for AI4AI.

Representative directions include:
- prompt / instruction optimization: APE, ProTeGi, OPRO, Promptbreeder;
- textual / pipeline optimization: DSPy, TextGrad, GEPA;
- reward and objective generation;
- code and algorithm evolution;
- data and training-recipe generation.

The important shift is not merely “using an LLM,” but using a foundation model as a **semantic search, synthesis, and revision operator over heterogeneous AI artifacts**.

## V. Agentic AI Development & Autonomous AI Research

**What is improved:** complete ML systems and increasingly complete research loops.  
**State now includes:** repositories, datasets, environments, code, logs, checkpoints, metrics, literature, hypotheses, and experiment histories.

Major branches:
- autonomous ML engineering and data science;
- data curation and model post-training;
- algorithm discovery through execution;
- AI research agents and AI scientists;
- research reproduction and experiment automation.

Representative systems and benchmarks include MLAgentBench, MLE-bench, AIDE, MLE-STAR, ML-Master, MLEvolve, PostTrainBench, ResearchGym, PaperBench, EXP-Bench, and AI Scientist-style systems.

Detailed modern-agent map → [`agent4ai/`](agent4ai/README.md)

## VI. Improving the Improver — Workflow, Harness, Self-Evolution & Recursive AI4AI

The optimization target moves from the artifact produced by AI to **the mechanism that produces improvements**.

```text
fixed workflow
   ↓
optimized prompt / workflow / agent architecture
   ↓
adaptive or externally optimized harness
   ↓
self-modifying agent / harness
   ↓
model–harness / optimizer–target co-evolution
   ↓
recursive improvement of the improvement process
```

Representative directions include ADAS, Meta-Harness, Self-Harness, Darwin Gödel Machine, Frontis-MA1 / OpenRSI, HarnessX, Recursive Harness Self-Improvement, MetaSkill-Evolve, Escher-Loop, and bilevel autoresearch.

---

# 🧩 A Unified Design Space

Rather than treating AutoML, NAS, agents, and self-improvement as unrelated fields, we compare them along shared dimensions:

| Dimension | Historical progression |
|---|---|
| **Improvement target** | hyperparameter → pipeline → architecture → optimizer / algorithm → program → model-training process → experiment → research process → harness / improver |
| **Representation** | vector → graph → program → language / code → repository → trajectory → research state |
| **Proposal mechanism** | BO / bandit → gradient / RL → evolution → learned optimizer → LLM → tree search / multi-agent → learned or evolving improver |
| **Feedback** | validation metric → multi-fidelity signal → execution → verifier / judge → experiment evidence |
| **Experience reuse** | none → warm start → meta-learning → archive / memory → trajectory learning → continual self-modification |
| **Human scaffolding** | fixed search space → configurable pipeline → fixed agent loop → adaptive harness → self-authored improvement mechanism |
| **Evaluation horizon** | single evaluation → training run → experiment → ML project → research project → multi-generation improvement |
| **Open-endedness** | closed → compositional → programmatic → open code → open research / self-improvement |

This design space is intended to connect the classical and agentic eras of AI4AI rather than privilege either one.

---

## 📚 Repository Structure

```text
Awesome-AI4AI/
├── README.md
├── foundations/
│   ├── papers.md                    # comprehensive AI4AI lineage: AutoML → RSI
│   └── preprint-2026082108-additions.md
├── agent4ai/
│   ├── README.md                    # detailed modern Agent4AI taxonomy
│   ├── papers.md                    # agentic AI4AI bibliography
│   ├── benchmarks.md
│   ├── recent.md
│   └── surveys.md
└── writing/
    ├── notes.md                     # survey framing and conceptual synthesis
    ├── reading-list.md
    └── preprint-2026082108.md       # comparison with the Aug-2026 AI4AI survey
```

## Inclusion Rule

A work is core AI4AI when AI is used to improve an **AI artifact** or the **process/mechanism that builds or improves AI**. Generic agents, memory, planning, world models, or tool-use methods are included only when they materially contribute to that objective.

---

## Survey Thesis

> **AI4AI is evolving from machines that optimize human-defined choices into systems that can design, execute, evaluate, and increasingly redesign the process of AI improvement itself.**

The historical question is therefore not simply “AutoML versus agents.” It is how the **target, state, feedback, and improver** expand from bounded optimization to open-ended and potentially self-improving AI research.

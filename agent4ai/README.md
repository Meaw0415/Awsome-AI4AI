# Agent4AI Hub

This directory covers **Agent4AI: AI agents for improving AI**.

The scope includes machine-learning engineering, data curation, model training/post-training, algorithm discovery, agent-system optimization, AI research/reproduction, and self-improving AI systems.

> **Scope rule.** Agent4AI is not a generic LLM-agent survey. Planning, memory, tools, multi-agent coordination, RL, or predictive models are included only when they directly improve **AI models or the process used to build, train, evaluate, optimize, redesign, or reproduce them**.

[Start here](getting-started.md) · [Papers](papers.md) · [Recent](recent.md) · [Benchmarks](benchmarks.md) · [Surveys](surveys.md)

---

# 1. Two-Axis View of Agent4AI

A clean way to understand the field is to separate:

1. **What part of AI is being improved?** — the task/object axis.
2. **How does the agent improve it?** — the mechanism axis.

This avoids mixing task categories such as *post-training* with methods such as *MCTS* or *RL*.

## Axis A — What is being improved?

| Task family | Optimization object | Representative work |
|---|---|---|
| **T1 · ML Engineering & Model Building** | features, pipelines, model code, experiments | AIDE, MLE-STAR, ML-Master, AIBuildAI-2, MLEvolve |
| **T2 · Training Data & Data Engineering** | data selection, synthesis, filtering, curriculum | Curation-Bench, Autonomous Agentic Data Engineering, ANDES, CurateEvo |
| **T3 · Model Training & Post-Training** | fine-tuning, SFT/RL recipes, checkpoints, alignment | FT-Dojo, PostTrainBench, Agent² RL-Bench, AutoTrainess |
| **T4 · Algorithm & Program Discovery** | algorithms, optimizers, executable programs | FunSearch, AlphaEvolve, AdaEvolve, OpenMLE-Evo |
| **T5 · Agent-System Improvement** | prompts, tools, context, workflow, topology, harness code | ADAS, EvoAgentX, Meta-Harness, Self-Harness, RHO |
| **T6 · AI Research & Reproduction** | implementations, experiments, research artifacts | AI Scientist, AIRA, ResearchCodeBench, ResearchGym, NatureBench |
| **T7 · Improver / Self-Improvement** | the agent or mechanism that improves future AI | Frontis-MA1 / OpenRSI, meta-evolution systems |

## Axis B — How is improvement achieved?

| Mechanism | Core question | Representative work |
|---|---|---|
| **M1 · Search & Refinement** | How are better candidate solutions generated, explored, and selected? | SELA, AIDE, I-MCTS, MLE-STAR, R&D-Agent |
| **M2 · Executable Feedback & Verification** | How is progress grounded in real training/execution and reliably evaluated? | MLE-bench, MLE-Dojo, PostTrainBench, executable graders |
| **M3 · Experience Accumulation & Transfer** | How are previous runs converted into reusable skills, knowledge, or priors? | DS-Agent, ML-Master, AIBuildAI-2, MLEvolve |
| **M4 · Adaptive Decision Making** | Given current results, what should be tried next and how should compute be allocated? | I-MCTS, Reasoning as Gradient, FOREAGENT, value/uncertainty-based selection |
| **M5 · Policy / Model Learning from Experience** | Can execution-generated experience be internalized into stronger weights? | ML-Agent, MLE-RL, AceGRPO, Frontis-MA1 |
| **M6 · Harness / Workflow Optimization** | Can the AI system around the model be automatically redesigned? | ADAS, Meta-Harness, Self-Harness, RHO, SwarmAgentic |
| **M7 · Evolutionary Improvement** | Can executable mutation/recombination drive program, algorithm, or agent improvement? | FunSearch, AlphaEvolve, AdaEvolve, MLEvolve, OpenMLE-Evo |
| **M8 · Meta-Improvement** | Can the improvement mechanism itself learn and become a better improver? | Frontis-MA1 / OpenRSI, search→training→search loops |

A paper may occupy several cells. For example:

- **MLEvolve**: `T1 + T4` and `M1 + M3 + M7`.
- **AutoTrainess**: `T3` and `M2 + M3 + M4`.
- **Frontis-MA1**: `T1 + T7` and `M2 + M5 + M7 + M8`.
- **Meta-Harness**: `T5` and `M3 + M6`.

This two-axis representation should be the main taxonomy for the survey and repository.

---

# 2. The Common AI-Improvement Loop

Most Agent4AI systems can be mapped onto the same loop:

```text
Target AI system
      ↓
Generate / modify candidates
      ↓
Build / train / execute
      ↓
Evaluate / verify
      ↓
Use feedback to update strategy, experience, or weights
      ↓
Choose or generate the next improvement
      ↓
optionally improve the agent / harness / improver itself
      ↓
Repeat
```

Different papers mainly differ in **what object they improve**, **what feedback they receive**, **what persists across iterations**, and **whether the improvement process itself changes**.

---

# 3. Key Method Families

<details open>
<summary><b>M1 · Search & Refinement</b></summary>

Search remains the dominant inference-time paradigm for MLE agents.

Representative lines:

- **SELA** — tree-search-enhanced agentic AutoML.
- **AIDE** — solution-tree search over executable ML code.
- **I-MCTS** — introspective Monte Carlo tree search.
- **AI Research Agents for Machine Learning** — compares Greedy, MCTS, and evolutionary policies with different operators on MLE-bench.
- **MLE-STAR** — search plus targeted code-block refinement.
- **Reasoning as Gradient** — uses iterative reasoning feedback rather than conventional branch-only search.

A useful research question is whether gains come from **better candidate operators**, **better exploration policies**, or simply **more execution budget**.

</details>

<details open>
<summary><b>M2 · Executable Feedback & Verification</b></summary>

Agent4AI is unusually dependent on external grounding because candidate AI improvements can often be executed and measured.

Important environments include:

- **MLE-bench / MLE-Dojo** for ML engineering;
- **Curation-Bench** for training-data policies;
- **FT-Dojo / PostTrainBench / Agent² RL-Bench** for model fine-tuning and post-training;
- **ResearchCodeBench / EXP-Bench / ResearchGym** for larger AI-development tasks.

The central methodological issues are evaluation leakage, reward hacking, noisy metrics, reproducibility, and credit assignment across long trajectories.

</details>

<details open>
<summary><b>M3 · Experience Accumulation & Transfer</b></summary>

The important question is not whether an agent has a generic memory module, but whether **past AI-improvement attempts change future performance**.

Representative approaches:

- **DS-Agent** — reuse prior competition experience.
- **ML-Master** — adaptive memory for exploration and reasoning.
- **AIBuildAI-2** — distill completed MLE runs into an evolving knowledge hierarchy.
- **MLEvolve** — retrospective memory and cross-branch information flow.
- **Hierarchical Skill Accumulation** — transfer reusable MLE skills across tasks.

Promising research problems include credit assignment, abstraction from trajectories into reusable skills, conflict/revision of stored experience, and measuring cross-task transfer rather than within-run gains only.

</details>

<details open>
<summary><b>M4 · Adaptive Decision Making</b></summary>

After each execution, the agent must decide **what is worth trying next**. This includes search-tree values, uncertainty, heuristics, learned critics, cheap proxy evaluations, or predictors.

- **I-MCTS** uses tree-search values.
- **FOREAGENT** uses predict-then-verify execution priors.
- **Reasoning as Gradient** uses structured reasoning feedback to redirect iteration.

Predictive/world-model-style techniques belong here as one implementation option rather than a standalone AI4AI branch.

</details>

<details open>
<summary><b>M5 · Policy / Model Learning from Experience</b></summary>

These systems move improvement from an external inference-time loop into model weights.

- **ML-Agent** — RL for autonomous MLE.
- **MLE-RL** — execution-grounded RL for ML agents.
- **AceGRPO** — curriculum-enhanced GRPO for MLE.
- **Frontis-MA1** — trains Draft / Improve / Debug / Crossover operators with execution-grounded SFT and RL before composing them in search.

A central question is when expensive search trajectories should be used merely as context versus converted into training data.

</details>

<details open>
<summary><b>M6 · Harness / Workflow Optimization</b></summary>

Here the object of improvement is the **agent system around the base model**.

- **ADAS** — automated design of agentic systems.
- **EvoAgentX / SwarmAgentic** — automatic workflow/agent-system evolution.
- **Meta-Harness** — outer-loop search directly over harness source code.
- **Self-Harness** — an agent identifies its weaknesses and validates self-generated harness edits.
- **Retrospective Harness Optimization (RHO)** — improves a harness from historical trajectories without external labels.

This branch is important because capability gains can come from the **model**, the **harness**, or their interaction. Agent4AI should track these separately.

</details>

<details open>
<summary><b>M7–M8 · Evolution and Meta-Improvement</b></summary>

Evolutionary methods optimize executable populations through variation and selection. Meta-improvement closes an additional loop by improving the mechanism that performs future improvements.

```text
candidate evolution
      ↓
better solutions
      ↓
experience from evolution
      ↓
train / adapt the improver
      ↓
better future evolution
```

Representative work: **FunSearch, AlphaEvolve, AdaEvolve, MLEvolve, OpenMLE-Evo, Frontis-MA1 / OpenRSI**.

The strongest claim to test is not just whether outputs improve, but whether the **rate or efficiency of future improvement** increases.

</details>

---

# 4. Fast-Growing Task Frontiers

## Agentic Training-Data Optimization

This is now a distinct Agent4AI task family rather than generic data analysis.

- [Can Generalist Agents Automate Data Curation? / Curation-Bench](https://arxiv.org/abs/2606.04261)
- [Exploring Autonomous Agentic Data Engineering for Model Specialization](https://arxiv.org/abs/2605.30407)
- [ANDES](https://arxiv.org/abs/2606.01279)
- [CurateEvo](https://arxiv.org/abs/2607.06140)

These methods treat **training data itself as the artifact an agent iteratively improves using downstream model performance**.

## Autonomous Model Training & Post-Training

- [FT-Dojo](https://arxiv.org/abs/2603.01712)
- [PostTrainBench](https://arxiv.org/abs/2603.08640)
- [Agent² RL-Bench](https://arxiv.org/abs/2604.10547)
- [AutoTrainess](https://arxiv.org/abs/2606.31551)

This frontier is especially central to AI4AI because agents directly improve the capabilities of other models.

## Agent-System Improvement

- ADAS
- Meta-Harness
- Self-Harness
- Retrospective Harness Optimization
- EvoAgentX / SwarmAgentic

This asks whether AI can automatically engineer the **software system that turns a base model into an effective agent**.

---

# 5. Comparison Dimensions

For each paper, useful columns are:

`Year | Task Family (T1–T7) | Mechanism (M1–M8) | Optimization Object | Feedback | Persistent Experience? | Weight Update? | Harness Update? | Execution Budget | Transfer? | Self-Reference? | Benchmark`

Important evaluation questions:

- Is feedback externally executable/verifiable?
- Does the method improve only within one task or transfer across tasks/models?
- Are gains caused by more inference compute or a genuinely better improvement policy?
- What persists: search state, reusable experience, weights, or harness changes?
- Can failure trajectories improve later behavior?
- Does the system improve AI artifacts only, or does it eventually improve its own improvement machinery?

---

# 6. Positioning

Classical AutoML / HPO / NAS are historical context, not the focus here. Modern Agent4AI is distinguished by agents operating over **open-ended, executable AI-development actions** such as code edits, training runs, data policies, post-training recipes, agent-harness modifications, algorithm changes, and research implementations.

A rough progression is:

```text
agent searches for better AI artifacts
        ↓
agent learns from executable feedback
        ↓
experience transfers across improvement attempts
        ↓
model or harness itself is updated
        ↓
improvement mechanism becomes an optimization target
        ↓
self-improving AI-development systems
```

For a practical entry path, see [`getting-started.md`](getting-started.md).

# AI4AI Survey — Paradigm-Driven Writing Outline

## Working title

**AI for AI: From Automated Machine Learning to Autonomous and Self-Improving AI Research**

Alternative:

**AI Improving AI: The Evolution from Automated Optimization to Self-Improving Research Systems**

---

# 0. Central thesis and narrative

The review should not be organized as a catalogue of AutoML, NAS, agents, and self-improvement systems. Instead, it should tell a continuous story about how the meaning of **AI4AI** expands over time.

The central idea is that the two “AI”s in **AI for AI** evolve together.

## 0.1 The second AI: what is being improved?

The target of improvement becomes progressively more expressive:

```text
hyperparameter / algorithm choice
        ↓
pipeline
        ↓
architecture
        ↓
optimizer / learning rule
        ↓
objective / reward / data policy
        ↓
algorithm / executable program
        ↓
model-training process
        ↓
complete ML system
        ↓
experiment / research project
        ↓
agent / workflow / harness
        ↓
the improver itself
```

Early AI4AI optimizes a small object inside a human-designed system. Modern AI4AI increasingly treats the **entire process that creates AI** as an optimization target.

## 0.2 The first AI: what performs the improvement?

The improvement mechanism also evolves:

```text
rules / random search
        ↓
Bayesian optimization / bandits
        ↓
RL / evolutionary search / gradients
        ↓
meta-learning / learned optimizers
        ↓
program search and synthesis
        ↓
foundation models as semantic/code optimizers
        ↓
tool-using agents
        ↓
research agents
        ↓
self-modifying / evolving improvers
```

This gives the core historical thesis:

> **AI4AI evolves through the simultaneous expansion of the object being improved and the intelligence of the mechanism performing the improvement.**

A third supporting axis is the feedback signal:

```text
validation score
   → resource-aware / multi-fidelity signal
   → execution result
   → structured verifier / judge
   → experiment history
   → scientific evidence
   → retention / transfer / future research value
```

---

# 1. Introduction — From Using AI to Building Better AI with AI

## 1.1 Motivation

Start from the conventional human AI-development loop:

`problem → design → implement → train → evaluate → diagnose → revise`

AI4AI progressively moves AI into more stages of this loop.

## 1.2 Scope and definition

Define AI4AI broadly:

> AI4AI studies computational systems in which AI is used to improve an AI artifact, an AI-development process, or the mechanism responsible for future AI improvement.

Core targets include data, features, hyperparameters, pipelines, architectures, optimizers, objectives, algorithms, programs, model weights, training recipes, experiments, research processes, prompts, workflows, harnesses, evaluators, and improvers.

Explicitly distinguish AI4AI from generic AI agents or generic AI-for-Science.

## 1.3 Why a new review is needed

Existing literatures are fragmented:

- AutoML reviews focus on pipeline/configuration automation;
- NAS reviews focus on architecture search;
- meta-learning reviews focus on adaptation and learning-to-learn;
- program-search literature focuses on generated algorithms/programs;
- LLM-agent surveys focus on generic planning/tool use;
- AI-scientist surveys focus on recent autonomous research;
- self-improvement surveys focus mostly on modern agent systems.

Our contribution is the **genealogy connecting all these generations as successive AI4AI paradigms**.

## 1.4 Preview of the dual evolution

Introduce Figure 1:

- x-axis: time;
- upper trajectory: **what AI improves**;
- lower trajectory: **how AI performs the improvement**;
- representative systems and venues distributed along the timeline.

---

# 2. Paradigm I — Automated Search over Human-Defined AI Choices

### Representative period
1970s–early 2020s, with major modern AutoML development from 2009 onward.

### The second AI
Algorithm choice, hyperparameters, features, and pipeline components.

### The first AI
Rules, black-box optimizers, Bayesian optimization, bandits, evolutionary search, meta-features.

## 2.1 Problem setting

Formalize classical AutoML/HPO as:

`x* = argmax_x f(x)`

where the human defines:

- search variables;
- valid search space;
- objective;
- train/validation protocol.

AI controls candidate selection, but not the semantics of the task.

## 2.2 Benchmark and evaluation setting

Discuss:

- algorithm-selection benchmarks;
- OpenML / AutoML benchmark suites;
- tabular classification/regression;
- fixed datasets and validation metrics;
- wall-clock/resource constraints.

Metrics:

- validation/test performance;
- time to best solution;
- sample efficiency;
- computational budget.

## 2.3 Method evolution

### Algorithm selection and configuration
Rice → ParamILS → SMAC → TPE / BO.

### Joint model and hyperparameter selection
Auto-WEKA → auto-sklearn.

### Pipeline construction
TPOT → AutoGluon / FLAML / modern AutoML systems.

### Cost-aware search
Hyperband → BOHB → resource-aware optimization.

## 2.4 What changed in AI4AI?

The first important abstraction appears:

`propose → evaluate → update`

but both the candidate representation and objective remain human-authored.

## 2.5 Limitation and transition

The central limitation is **closed search-space dependence**.

This motivates the next question:

> Instead of selecting values inside a human-defined model, can AI design the model structure itself?

---

# 3. Paradigm II — Automated Design of AI Structures

### The second AI
Model architecture and computational graph.

### The first AI
RL controllers, evolutionary algorithms, gradient-based architecture optimizers, weight-sharing search.

## 3.1 Problem and benchmark setting

Search over architecture graphs rather than scalar configurations.

Discuss benchmark evolution:

- CIFAR/ImageNet evaluation;
- mobile/latency-aware NAS;
- NAS-Bench families;
- architecture ranking and reproducibility.

Evaluation now becomes expensive because every candidate may require training.

## 3.2 Method evolution

### RL-based NAS
Neural Architecture Search → NASNet.

### Evolutionary NAS
Large-Scale Evolution → AmoebaNet.

### Weight sharing
ENAS and one-shot methods.

### Differentiable NAS
DARTS → PC-DARTS / DrNAS.

### Hardware-aware / efficient NAS
MnasNet → ProxylessNAS → Once-for-All.

### LLM-assisted architecture design
Later works such as design-principle transfer and LM-Searcher can be used to show that the same target survives while the first AI becomes more capable.

## 3.3 Conceptual transition

The target evolves:

`configuration vector → structured computation graph`

AI is no longer only selecting parameters; it is designing a component of AI itself.

## 3.4 Limitation

The architecture grammar, search operators, and training objective are still mostly fixed by humans.

Transition question:

> Can the system learn not only what architecture to choose, but how improvement itself should be performed?

---

# 4. Paradigm III — Learning How to Improve

### The second AI
Adaptation rule, optimizer, initialization, training dynamics.

### The first AI
Meta-learning systems, learned optimizers, recurrent learners, population-based adaptation.

This chapter is important because it introduces a qualitatively different idea: **the improver itself is learned from previous tasks**.

## 4.1 Benchmark / task setting

Unlike HPO/NAS, evaluation is explicitly cross-task.

Typical structure:

`meta-train tasks → learn improvement mechanism → meta-test on unseen tasks`

Discuss:

- few-shot classification;
- meta-RL;
- optimizer generalization;
- cross-task adaptation;
- task distributions instead of one fixed dataset.

## 4.2 Method evolution

### Learning-to-learn
Learning to Learn by Gradient Descent by Gradient Descent.

### Fast adaptation
MAML, Reptile, RL².

### Learned optimizers
Neural optimizer search → VeLO.

### Population adaptation
Population Based Training and related population-based methods.

## 4.3 Conceptual advance

Previous paradigms ask:

> What model/configuration is best?

This paradigm asks:

> What **improvement rule** produces good future models?

This is the first clear bridge toward later experience-learning and self-improving agents.

## 4.4 Limitation and transition

The learned improvement mechanisms generally operate inside tightly specified parameterizations and training loops.

Next step:

> Can AI create entirely new learning objectives, algorithms, or executable programs rather than optimize a fixed formal object?

---

# 5. Paradigm IV — Automated Discovery of Objectives, Algorithms, Data Policies, and Programs

### The second AI
Learning objective, reward function, augmentation/data policy, optimizer, algorithm, executable program.

### The first AI
RL, evolutionary search, program synthesis, LLM-guided mutation and selection.

## 5.1 Benchmark / problem setting

The candidate is now executable.

General loop:

`generate program → execute/train → evaluate → select/refine`

Benchmarks therefore require:

- executable environments;
- deterministic or reproducible evaluation;
- resource constraints;
- increasingly open candidate spaces.

## 5.2 Method evolution

### Data and augmentation policy search
AutoAugment → Population Based Augmentation → modern agentic data curation.

### Learned objectives and rewards
Learned losses → Eureka → DrEureka → RF-Agent.

### Learning-algorithm discovery
AutoML-Zero.

### LLM-guided program search
FunSearch → AlphaEvolve → ShinkaEvolve / AdaEvolve / MLEvolve.

### Joint AI-component improvement
Use ASI-Evolve as a modern example where data, architecture, and learning algorithm become parts of one larger optimization space.

## 5.3 Key transition

The representation evolves:

`vector → graph → executable program`

This substantially increases open-endedness.

## 5.4 Limitation

These systems can explore expressive program spaces, but usually rely on strongly engineered evaluators and task-specific outer loops.

Next question:

> Is there a general-purpose model that can propose, reason about, and revise heterogeneous AI artifacts using one common interface?

---

# 6. Paradigm V — Foundation Models as General-Purpose AI Improvement Operators

### The second AI
Prompt, context, program, reward, data generator, pipeline, algorithm, workflow.

### The first AI
Large language models acting as semantic proposal, critique, synthesis, and optimization operators.

## 6.1 Why foundation models change AI4AI

Earlier search methods require artifact-specific representations and operators.

LLMs can manipulate:

- natural language;
- code;
- prompts;
- configurations;
- algorithms;
- reward functions;
- experiment plans.

The first AI therefore becomes substantially more general.

## 6.2 Benchmark / evaluation setting

Discuss prompt optimization benchmarks, program evaluation, downstream task accuracy, code execution, and evaluator-model feedback.

## 6.3 Method evolution

### Prompt search
APE → ProTeGi → OPRO.

### Self-referential prompt evolution
Promptbreeder.

### Optimizable LM pipelines
DSPy.

### Textual gradients and reflective optimization
TextGrad → GEPA.

### Agent/workflow generation as a bridge
GPTSwarm, ADAS, AFlow, ScoreFlow.

## 6.4 Conceptual transition

The first AI changes from a specialized mathematical optimizer into a **general semantic optimizer**.

However, most systems still optimize one artifact using an outer loop provided by humans.

Next step:

> Can AI execute the entire build–train–evaluate–repair cycle itself?

---

# 7. Paradigm VI — Agentic Closed-Loop AI Development

### The second AI
Complete ML system: data, code, model, training pipeline, experiments, post-training recipe.

### The first AI
Tool-using LLM agents with planning, execution, memory, search, reflection, and increasingly policy learning.

This is where AI4AI changes from **candidate optimization** to **process automation**.

## 7.1 Benchmark and environment evolution

Explain why modern AI4AI requires executable environments.

Key benchmarks/settings:

- MLAgentBench — iterative ML experimentation;
- MLE-bench — Kaggle-scale ML engineering;
- MLE-Dojo — executable RL environment;
- DSGym — data-science agent evaluation/training;
- PostTrainBench / Agent² RL-Bench — autonomous model post-training.

Benchmark unit evolves from one candidate evaluation to an entire development episode.

## 7.2 Method evolution by next-experiment mechanism

### Sequential execution and reflection
Early ML/data agents, DS-Agent.

### Tree search
SELA, I-MCTS.

### Code-space search
AIDE.

### Targeted refinement
MLE-STAR.

### Reasoning + exploration + memory
ML-Master.

### Research/development co-optimization
R&D-Agent.

### Predict-before-execute / value-guided search
FOREAGENT.

### Experience and graph evolution
AIBuildAI-2, MLEvolve.

### Policy learning
ML-Agent, AceGRPO and RL-trained MLE agents.

## 7.3 Model/data/post-training as targets

Discuss:

- FT-Dojo;
- DataEnvGym / Autodata;
- autonomous data curation;
- AutoTrainess;
- agentic RL post-training.

This subsection shows that the second AI now includes **model weights and training process**, not just external pipelines.

## 7.4 Limitation and transition

Most MLE agents still receive a concrete optimization objective from humans.

Research introduces a qualitatively different state:

- competing hypotheses;
- uncertain evidence;
- literature;
- novelty;
- negative results;
- experiment selection.

Transition:

> AI4AI moves from improving a model to improving the **research process that discovers better AI**.

---

# 8. Paradigm VII — Autonomous AI Research

### The second AI
Research project and AI-discovery process.

### The first AI
Research agents / AI scientists capable of literature retrieval, ideation, implementation, experimentation, interpretation, and writing.

## 8.1 What makes research different from MLE?

MLE often has a relatively clear scalar objective.

Research additionally requires:

- novelty;
- hypothesis quality;
- evidence gathering;
- uncertainty reduction;
- scientific validity;
- reproducibility;
- deciding what experiment is worth running.

## 8.2 Benchmark evolution

Discuss the progression:

- RE-Bench — frontier AI R&D against humans;
- PaperBench — paper replication;
- MLR-Bench — open-ended ML research;
- EXP-Bench — research experiments;
- ResearchCodeBench — novel method implementation;
- ResearchGym — closed-loop real-world projects;
- NatureBench — reproduction of published SOTA;
- MLS-Bench — whether improvements generalize rather than overfit one setting.

Emphasize the shift in evaluation horizon:

`experiment → project → paper/research contribution`

## 8.3 Method evolution

### Research assistance
Literature / ideation agents.

### End-to-end research pipelines
AI Scientist → Agent Laboratory.

### Search over scientific ideas
AI Scientist-v2 and hypothesis-tree systems.

### Long-horizon autonomous research
AIRA/AIRA_2, AutoSOTA, DeepScientist, AlphaLab, related systems.

## 8.4 Artifact state versus epistemic state

Introduce an original synthesis here.

Artifact state:

- code;
- model;
- data;
- metrics;
- experiment outputs.

Epistemic state:

- hypotheses;
- confidence;
- uncertainty;
- supporting/contradicting evidence;
- unresolved questions.

Classical optimization mainly tracks artifact state.

Research requires:

`experiment → evidence → belief update → changed value of future experiments`

This provides the bridge to research world models / value-of-information perspectives.

## 8.5 Limitation and transition

Even autonomous research agents are usually built inside a human-designed harness.

The next question becomes:

> If the agent can improve AI, who improves the agent and its improvement process?

---

# 9. Paradigm VIII — Improving the Improver

### The second AI
Agent architecture, prompts, memory, context, tools, workflow, harness, evaluator, and eventually the improvement mechanism itself.

### The first AI
Outer-loop optimizers, meta-agents, self-modifying agents, co-evolutionary systems.

This chapter closes the historical loop: **the first AI itself becomes the second AI.**

## 9.1 Agent and workflow optimization

Progression:

- prompt optimization;
- GPTSwarm / graph optimization;
- ADAS;
- AFlow;
- ScoreFlow;
- EvoAgentX / multi-agent topology optimization.

## 9.2 Harness optimization

Explain harness as the executable system surrounding the model:

- instructions/context;
- tools;
- memory;
- orchestration;
- runtime policies;
- source code.

Method progression:

Meta-Harness → HarnessX → Self-Harness → Continual Harness → Recursive Harness Self-Improvement / Harness-R1.

Useful hierarchy:

1. fixed human-authored harness;
2. externally optimized harness;
3. self-modifying harness;
4. model–harness / optimizer–target co-evolution.

## 9.3 Persistent self-improvement

Distinguish carefully:

### Self-refinement
Only the current answer/artifact changes.

### Persistent self-improvement
The system carries modifications into future episodes through weights, memory, skills, prompts, workflow, or source code.

### Recursive/meta-improvement
The mechanism that generates/selects/evaluates future improvements is itself improved.

## 9.4 Meta-evolution and recursive systems

Historical anchor:

- Gödel Machines;
- STOP;
- Gödel Agent;
- Darwin Gödel Machine.

Modern systems:

- Group-Evolving Agents;
- Hyperagents;
- Red Queen Gödel Machine;
- Frontis-MA1 / OpenRSI;
- Bilevel Autoresearch;
- MetaSkill-Evolve;
- Escher-Loop.

## 9.5 New evaluation problem

Performance on one task is no longer enough.

Need to measure:

- improvement gain;
- retention;
- held-out transfer;
- regression;
- compounding across generations;
- evaluator drift;
- cost;
- reliability.

Bring in the complementary concepts from Wu et al. (2026): stage ownership, signal grounding, composition gap, retention and transfer.

---

# 10. Unified Design Space of AI4AI

After the historical paradigms, synthesize the field with one common table.

| Dimension | Evolution |
|---|---|
| **Second AI: improvement target** | hyperparameter → pipeline → architecture → optimizer → objective/data → program → ML system → research process → agent/harness → improver |
| **First AI: improvement mechanism** | rule/random → BO/bandit → RL/evolution/gradient → meta-learner → program search → LLM → agent → research agent → meta/self-improver |
| Representation | vector → graph → program → language/code → repository → research state → editable improver |
| Feedback | validation score → cost-aware signal → execution → verifier/judge → experimental evidence → retention/transfer |
| Experience reuse | none → warm-start → meta-learning → archive → memory → learned policy → persistent self-modification |
| Human scaffolding | fixed search space → grammar → fixed workflow → fixed harness → adaptive harness → self-authored improvement mechanism |
| Evaluation horizon | evaluation → training run → experiment → ML project → research project → multi-generation improvement |
| Open-endedness | closed → structured → programmatic → open code → open research → meta-level improvement |

The key synthesis should be:

> The history of AI4AI is not simply a sequence of applications. It is a progressive relaxation of what humans must specify in the AI-improvement loop.

---

# 11. Benchmark Evolution — What Does It Mean to Measure AI Improving AI?

This should be a cross-cutting chapter, not just a list of benchmarks.

## 11.1 Benchmark unit becomes larger

```text
configuration
   ↓
architecture
   ↓
pipeline
   ↓
training / adaptation task
   ↓
ML experiment
   ↓
competition-scale ML engineering
   ↓
AI R&D project
   ↓
paper reproduction / open-ended research
   ↓
multi-generation self-improvement
```

## 11.2 Evaluation dimensions

- final performance;
- sample/compute efficiency;
- wall-clock cost;
- robustness;
- generalization;
- reproducibility;
- novelty;
- scientific validity;
- retention;
- transfer;
- reliability across repeated trials;
- contamination/leakage;
- human comparison.

## 11.3 Composition gap

Component success does not imply reliable end-to-end improvement.

Examples:

- good planning + good coding + good memory ≠ reliable research agent;
- a successful harness edit on one benchmark ≠ persistent transferable improvement.

This is an important modern evaluation challenge.

---

# 12. Open Challenges and Future Directions

Do not organize this as generic “agent challenges.” Tie each challenge to AI4AI specifically.

## 12.1 From performance optimization to scientific progress

How should research-level AI4AI value experiments that reduce uncertainty but do not immediately increase benchmark score?

## 12.2 Learning research dynamics

Research world models / transition models that predict:

`current state + proposed experiment → result + belief update + future research value`

## 12.3 Long-horizon credit assignment

Which earlier decisions caused eventual gains or failures?

## 12.4 Learning from negative results

Failures should update future experiment selection rather than disappear into raw trajectory memory.

## 12.5 Evaluator reliability and reward hacking

As the target becomes more open-ended, evaluation becomes the bottleneck.

## 12.6 Generalization and transfer of improvements

A true AI4AI advance should not merely exploit a single benchmark or repository.

## 12.7 Retention and compounding

Do improvements persist across tasks and generations, or do new changes erase old capabilities?

## 12.8 Cost-aware autonomous experimentation

Research agents need to reason about information value per unit compute/time.

## 12.9 Human–AI division of scientific responsibility

Which parts should remain human-owned: problem choice, evaluator, final claims, deployment?

## 12.10 Safety and auditability of self-modifying AI4AI

The more of the improvement process is exposed to optimization, the more important provenance, regression testing, rollback, and independent evaluation become.

---

# 13. Outlook

End by returning to the two-AI framing.

### Evolution of the second AI

`parameter → model → algorithm → system → research process → improver`

### Evolution of the first AI

`search → learning → generation → agency → self-improvement`

Closing message:

> AI4AI has evolved from machines that optimize a few human-defined choices into systems that can increasingly design, execute, evaluate, and redesign the processes by which better AI is produced. The defining frontier is no longer whether AI can improve an artifact, but how much of the improvement loop itself can become adaptive, generalizable, reliable, and eventually self-improving.

---

# Recommended figures / tables

## Figure 1 — Dual evolution of AI4AI

Timeline with two rising trajectories:

- **Second AI:** parameter → architecture → algorithm → ML system → research → improver.
- **First AI:** BO/search → RL/evolution → meta-learning → LLM → agent → self-improver.

Place representative papers + venue abbreviations along the trajectory.

## Figure 2 — Expansion of the AI-improvement loop

Show which stages are automated under each paradigm:

`design → implement → train → evaluate → diagnose → hypothesize → experiment → update improver`

## Figure 3 — Artifact space and epistemic space

Contrast classical optimization with research-level AI4AI.

## Table 1 — Paradigm comparison

Columns:

- paradigm;
- improved object;
- improvement mechanism;
- representation;
- feedback;
- benchmark unit;
- representative methods;
- major limitation.

## Table 2 — Benchmark evolution

Benchmark, year, target, episode horizon, execution access, feedback, human baseline, transfer setting.

## Table 3 — Self-improvement levels

Self-refinement vs persistent improvement vs harness improvement vs recursive/meta-improvement, with representative systems and required evidence.

---

# Writing rule for every paradigm chapter

To keep the whole review coherent, every paradigm chapter should follow the same seven-step template:

1. **What is the second AI?** — define the object being improved.
2. **What is the first AI?** — define the improvement mechanism.
3. **What is the problem/benchmark setting?** — search space, environment, available feedback, evaluation horizon.
4. **How did methods evolve?** — explain 3–5 meaningful methodological transitions rather than listing papers.
5. **What new capability did the paradigm introduce?** — identify the conceptual advance.
6. **What remained human-defined or unsolved?** — expose the bottleneck.
7. **Why did the next paradigm emerge?** — end with a transition sentence that naturally opens the next chapter.

This repeated structure should make the review read as one continuous argument rather than a sequence of disconnected mini-surveys.
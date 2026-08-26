# Writing Notes for the AI4AI Survey

This file contains the evolving **survey framing, taxonomy, research gaps, and writing ideas**. The public-facing README should stay focused on resources and field evolution.

## 1. Candidate survey titles

- **AI4AI: From Automated Machine Learning to Autonomous and Self-Improving AI Research Agents**
- **From AutoML to AI Scientists: A Survey of AI for Automating AI Research and Development**
- **On the Road to AI4AI: Search, Agents, and Self-Improving Research Systems**

## 2. Core narrative

A useful historical transition is:

> **Search over human-defined choices → search over programs → agentic experimentation → research-loop automation → learned research / epistemic dynamics.**

The field evolves along at least four dimensions:

1. **Automation target** — hyperparameters → architectures → programs → code → experiments → hypotheses → complete research loops.
2. **Search/state representation** — vectors/configurations → graphs → programs → repositories → research state.
3. **Feedback** — validation metric → execution result → judge/reward → experimental evidence.
4. **Adaptation** — per-task optimization → cross-task meta-learning → memory → self-modification / learned research dynamics.

## 3. Proposed taxonomy

### A. Foundations: AutoML, HPO, algorithm selection, pipelines
The first generation of AI4AI automates choices inside a mostly human-designed search space.

### B. Neural Architecture Search & Algorithm Discovery
Automation moves from tuning parameters to creating structures, programs, optimizers, and learning algorithms.

### C. Meta-Learning & Learned Optimization
Experience across tasks changes the optimizer/search procedure itself.

### D. LLMs as Optimizers, Program Synthesizers & Design Operators
Foundation models make the candidate space much more open-ended: natural language, code, reward functions, algorithms, and hypotheses.

### E. Autonomous ML Engineering Agents
Agents interact with repositories, data, compute, logs, and metrics to perform long-horizon iterative ML engineering.

### F. AI Research Agents / AI Scientists
Automation expands from engineering to literature grounding, ideation, hypothesis formation, experimental design, execution, interpretation, writing, and review.

### G. Benchmarks & Evaluation for AI R&D
Evaluation evolves from a scalar validation metric to long-horizon engineering, paper reproduction, novelty, scientific correctness, and research progress.

### H. Self-Improving / Open-Ended / World-Model-Based AI4AI
Systems improve their own search or agent machinery, maintain evolving populations/archives, learn from research trajectories, or model how actions and evidence change future research state.

## 4. Taxonomy by next-action mechanism

| Paradigm | State | Feedback | Typical next-action mechanism |
|---|---|---|---|
| Classical AutoML | configuration | validation metric | Bayesian/evolutionary/bandit search |
| NAS / program search | architecture/program | execution + score | RL/evolution/gradient/search |
| LLM optimizer | text/code candidate + history | evaluator/reward | prompted proposal/refinement |
| ML engineering agent | repository + experiment history | logs + metric | planner/reasoner + tools |
| Evolutionary coding agent | population/archive of programs | evaluator fitness | selection + LLM mutation/crossover |
| Research agent | literature + hypotheses + experiments | evidence + reviewer/metric signals | planning + tool use + memory |
| Research world model | artifact state + epistemic state | evidence + predicted information/value | learned transition/value model |

## 5. Key survey questions

1. **What is being automated?** Hyperparameters, architectures, code, experiments, hypotheses, evidence updates, or the whole research loop?
2. **What is the search state?** Configuration, program, codebase, experiment history, research hypothesis, or internal belief/world model?
3. **What provides feedback?** Validation score, reward, execution result, benchmark score, reviewer feedback, evidence, or a learned model?
4. **How is experience reused?** Warm starts, meta-learning, memory, retrieval, trajectory archives, evolutionary populations, learned dynamics, or self-modification?
5. **How open-ended is the task?** Fixed search space → open code space → open research problem space.
6. **How strong is human scaffolding?** Hard-coded pipeline → configurable harness → adaptive/self-authored/self-improving harness.
7. **What counts as success?** Final metric, efficiency, novelty, reproducibility, scientific validity, information gain, or long-horizon research progress?

## 6. Dual-space view

A potentially useful original framing is to distinguish:

### Artifact space

- code;
- models;
- datasets;
- experiment configurations;
- outputs;
- metrics;
- papers / reports.

### Epistemic space

- hypotheses;
- uncertainty;
- causal beliefs;
- supporting / contradicting evidence;
- unresolved questions;
- confidence.

Most existing AutoML and ML-agent systems primarily optimize in **artifact space**. Research-level agents should also model how experiments change **epistemic state**.

The core transition can be written as:

> **hyperparameter state + scalar score**  
> → **program/code state + execution feedback**  
> → **research state + experimental evidence**  
> → **artifact + epistemic state + learned information/value dynamics**.

## 7. Research-world-model idea

A research world model could learn a transition of the form:

```text
(current research state, proposed experiment)
                ↓
(predicted result, belief update, future research value)
```

A richer version could explicitly model:

```text
S_t = {artifact state, epistemic state}
A_t = proposed experiment / code change / analysis
O_t = experimental observation
S_{t+1} = updated artifact + belief state
```

The key difference from a conventional RL world model is that the goal is not merely predicting the next environment observation. The system should predict **how evidence changes what the researcher should believe and what experiments become valuable afterward**.

## 8. Potential research gap

Current AI4AI systems often fall into three broad paradigms:

### Hard-coded harness

The designer specifies the workflow:

```text
idea → code → run → inspect metric → revise
```

The LLM chooses content inside fixed stages, but the research process itself is largely hand-authored.

### Reward / evaluator-driven search

Examples include AutoML, evolutionary code search, OPRO, FunSearch, AlphaEvolve, and MLE-style agents.

The main signal is:

```text
candidate → evaluator → scalar/structured reward → next candidate
```

This can find strong artifacts but does not necessarily represent why an experiment was informative.

### Learned research dynamics / world-model paradigm

The system learns from past research trajectories how experiments affect later knowledge and decisions.

The target is closer to:

```text
experiment → evidence → belief change → changed future experiment value
```

This may be a useful direction for moving from **optimization agents** toward **research agents**.

## 9. Benchmark interpretation

The benchmark unit itself shows the evolution of AI4AI:

```text
single function evaluation
        ↓
architecture evaluation
        ↓
complete AutoML pipeline
        ↓
ML experimentation task
        ↓
Kaggle-scale ML engineering
        ↓
frontier AI R&D task
        ↓
paper-level replication
        ↓
open-ended research
```

A useful survey point is that the final stage is still poorly benchmarked.

## 10. Candidate quantitative table

Eventually annotate every method paper with:

| Field | Example values |
|---|---|
| Year | 2013 / 2024 / 2026 |
| Automation target | HPO / NAS / algorithm / code / experiment / hypothesis / full research |
| Search representation | vector / graph / program / language / repository / research state |
| Proposal mechanism | BO / RL / evolution / gradient / LLM / multi-agent / world model |
| Feedback | validation metric / execution / judge / evidence |
| Memory | none / archive / meta-features / trajectory memory / learned state |
| Adaptation | per-task / cross-task / continual / self-modifying |
| Human scaffolding | fixed / configurable / agent-authored |
| Evaluation horizon | evaluation / episode / competition / research session / paper |
| Open-endedness | closed / partially open / open-ended |

This table could become one of the main figures or supplementary resources of the survey.

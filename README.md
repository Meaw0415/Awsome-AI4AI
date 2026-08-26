# Awesome AI4AI

A curated bibliography and survey scaffold for **AI for AI (AI4AI)**: AI systems that automate, accelerate, improve, evaluate, or recursively enhance the research and engineering process of artificial intelligence itself.

> **Scope.** AutoML, hyperparameter/architecture/algorithm search, meta-learning and learned optimization, LLM-driven optimization and program discovery, autonomous ML engineering agents, AI research agents / AI scientists, AI-R&D benchmarks, and self-improving / world-model-based research systems.

## The survey story

We organize AI4AI by **what part of the AI-development loop is automated** and by **what state/feedback the automation system reasons over**:

1. **Configuration automation** — algorithms, features, hyperparameters, pipelines.
2. **Structure discovery** — architectures, programs, training rules, algorithms.
3. **Learning to search** — meta-learning, learned optimizers, population-based adaptation.
4. **Foundation-model-guided search** — LLMs propose prompts, rewards, code, algorithms, and experimental modifications.
5. **Autonomous ML engineering** — agents edit code, run experiments, debug, inspect metrics, and iterate.
6. **AI research agents / AI scientists** — literature, ideation, hypothesis formation, experimental design, execution, interpretation, writing, and review.
7. **Self-improving AI4AI** — systems that improve their own search/agent machinery, evolve algorithms, accumulate reusable research experience, or learn models of research dynamics.

A useful historical transition is:

> **Search over human-defined choices → search over programs → agentic experimentation → research-loop automation → learned research / epistemic dynamics.**

## Repository map

- [`papers.md`](papers.md) — main paper library, grouped by topic and labeled by year.
- [`survey_outline.md`](survey_outline.md) — proposed survey structure and narrative.
- [`reading_priority.md`](reading_priority.md) — compact reading path through the field.

## Taxonomy

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
Automation expands from engineering to literature grounding, ideation, experimental design, interpretation, and scientific communication.

### G. Benchmarks & Evaluation for AI R&D
Evaluation evolves from a scalar validation metric to long-horizon engineering, paper reproduction, novelty, scientific correctness, and research progress.

### H. Self-Improving / Open-Ended / World-Model-Based AI4AI
Systems improve their own search or agent machinery, maintain evolving populations/archives, learn from research trajectories, or model how actions and evidence change future research state.

## A second taxonomy: what drives the next action?

This is useful for comparing modern agent harnesses:

| Paradigm | State | Feedback | Typical next-action mechanism |
|---|---|---|---|
| Classical AutoML | configuration | validation metric | Bayesian/evolutionary/bandit search |
| NAS / program search | architecture/program | execution + score | RL/evolution/gradient/search |
| LLM optimizer | text/code candidate + history | evaluator/reward | prompted proposal/refinement |
| ML engineering agent | repository + experiment history | logs + metric | planner/reasoner + tools |
| Evolutionary coding agent | population/archive of programs | evaluator fitness | selection + LLM mutation/crossover |
| Research agent | literature + hypotheses + experiments | evidence + reviewer/metric signals | planning + tool use + memory |
| Research world model (emerging) | artifact state + epistemic state | evidence + predicted information/value | learned transition/value model |

## Key survey questions

1. **What is being automated?** Hyperparameters, architectures, code, experiments, hypotheses, evidence updates, or the whole research loop?
2. **What is the search state?** Configuration, program, codebase, experiment history, research hypothesis, or internal belief/world model?
3. **What provides feedback?** Validation score, reward, execution result, benchmark score, reviewer feedback, evidence, or a learned model?
4. **How is experience reused?** Warm starts, meta-learning, memory, retrieval, trajectory archives, evolutionary populations, learned dynamics, or self-modification?
5. **How open-ended is the task?** Fixed search space → open code space → open research problem space.
6. **How strong is human scaffolding?** Hard-coded pipeline → agent harness → adaptive/self-authored/self-improving harness.
7. **What counts as success?** Final metric, efficiency, novelty, reproducibility, scientific validity, information gain, or long-horizon research progress?

## Proposed survey thesis

A central change in AI4AI is the transition in both **state representation** and **feedback**:

> **hyperparameter state + scalar score**  
> → **program/code state + execution feedback**  
> → **research state + experimental evidence**  
> → potentially **artifact + epistemic state + learned information/value dynamics**.

This motivates a useful **dual-space view** for future AI-research agents:

- **Artifact space:** code, models, datasets, experiment configurations, outputs, metrics.
- **Epistemic space:** hypotheses, uncertainty, causal beliefs, evidence, unresolved questions, confidence.

The next experiment should not only be selected for immediate metric gain; it can also be selected because it is expected to change the epistemic state in a way that improves future research decisions.

## Candidate survey titles

- **AI4AI: From Automated Machine Learning to Autonomous and Self-Improving AI Research Agents**
- **From AutoML to AI Scientists: A Survey of AI for Automating AI Research and Development**
- **On the Road to AI4AI: Search, Agents, and Self-Improving Research Systems**

## Status

Living bibliography. The goal is not to enumerate every application-specific AutoML paper, but to capture the conceptual path from **optimization over a fixed space** to **autonomous, open-ended and potentially self-improving AI R&D**.

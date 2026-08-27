# AI4AI Review — Working Outline

**Working title:** *AI for AI: From Automated Machine Learning to Autonomous and Self-Improving AI Research*

**Initial format:** IEEE journal (`IEEEtran`, journal mode)

**Target options:** TPAMI-style systematic survey first; the same material can later be rewritten into a more conceptual Nature Reviews / Nature Machine Intelligence narrative.

---

## Core narrative

The paper should not read as a catalogue of agent papers. The main historical transition is:

> **Search over human-defined choices → search over structures/programs → learning how to optimize → language-mediated open-ended optimization → agentic experimentation → research-loop automation → improving the improver.**

Across this history, four questions remain constant:

1. **What is being automated?**
2. **What representation/search state is manipulated?**
3. **What feedback drives improvement?**
4. **How does accumulated experience change future decisions?**

A second, more original conceptual thread is:

> **Artifact optimization → joint artifact + epistemic optimization.**

Classical AI4AI primarily searches for better artifacts. Research-level AI must also model hypotheses, uncertainty, evidence, belief changes, and the future value of experiments.

---

# 1. Introduction — When AI enters the AI development loop

### Main question
What does it mean for AI to improve AI, and why should AutoML, MLE agents, AI scientists, and self-improving systems be viewed as one historical trajectory?

### Key points
- Human AI-development loop: problem → design → implementation → experiment → evaluation → interpretation → revision.
- AI4AI progressively automates larger portions of this loop.
- Define AI4AI broadly enough to include classical AutoML and modern Agent4AI.
- Introduce the four survey questions.
- State the central thesis: the field is moving from optimizing artifacts toward learning the process/dynamics of AI improvement.

---

# 2. Foundations: Automating Model Development

## 2.1 Hyperparameter optimization and algorithm configuration

### Representative work
- Random Search
- Bayesian optimization / SMAC / TPE
- Hyperband / BOHB

### Core idea
Establish the canonical loop:

`propose → train → evaluate → update`

### Limitation
Humans still define both the optimization objective and almost the entire search space.

## 2.2 Automated machine learning

### Representative work
- Auto-WEKA
- auto-sklearn
- TPOT
- AutoGluon / FLAML as later systems

### Core transition
`hyperparameter → pipeline`

### Main argument
AutoML expands the *automation boundary*, but remains largely search inside human-authored spaces.

---

# 3. From Tuning Models to Discovering Them

## 3.1 Neural architecture search

### Representative work
- NAS with RL
- evolutionary NAS
- ENAS
- DARTS
- Once-for-All

### Core transition
`configuration vector → architecture graph`

### Discussion
- search space design
- evaluation cost
- weight sharing
- differentiable relaxation
- human priors remain substantial

## 3.2 Program and algorithm discovery

### Representative work
- learned optimizer search
- AutoML-Zero
- FunSearch
- AlphaEvolve

### Core transition
`architecture → executable program/algorithm`

### Main argument
Program space is qualitatively more expressive and open-ended than conventional AutoML/NAS spaces.

---

# 4. Learning to Improve AI

## 4.1 Meta-learning

### Representative work
- learning-to-learn lineage
- MAML
- meta-features / warm-start AutoML

### Main argument
Experience across tasks starts to change the *improvement process itself*.

## 4.2 Learned optimizers and population-based adaptation

### Representative work
- Learning to Learn by Gradient Descent by Gradient Descent
- PBT
- VeLO

### Core transition
`optimize the model → learn part of the optimizer`

### Connection to modern Agent4AI
Modern agent memory, RL, and self-improvement can be interpreted as a new form of meta-learning over richer research trajectories.

---

# 5. Foundation Models as General-Purpose Improvement Operators

## 5.1 LLMs as optimizers

### Representative work
- APE / prompt optimization
- OPRO
- Promptbreeder / ProTeGi
- TextGrad
- DSPy

### Main pattern
`context + candidate + feedback → improved candidate`

### Main argument
Semantic priors enable optimization over objects that cannot easily be represented as numerical vectors.

## 5.2 LLMs as program/search operators

### Representative work
- FunSearch
- reward generation / Eureka-like systems
- AlphaEvolve

### Core transition
`closed enumerable search → open-ended generative search`

---

# 6. Agentic AI4AI: Autonomous Machine-Learning Engineering

## 6.1 From generation to iterative experimentation

### Representative work / benchmarks
- MLAgentBench
- MLE-bench
- MLE-Dojo

### Main state
`repository + data + code + experiment history + logs + metrics + memory`

### Main argument
Execution becomes first-class: a proposed solution matters only if it runs and improves the target system.

## 6.2 Search and candidate improvement

### Representative work
- SELA
- AIDE
- MLE-STAR
- ML-Master
- R&D-Agent
- MLEvolve

### Organize methods by *next-action mechanism*, not merely agent architecture
- sequential proposal/refinement
- tree/MCTS search
- evolutionary population search
- targeted component refinement
- predict-then-execute / value-guided experimentation

### Central question
Given current evidence and budget, **what should the agent try next?**

---

# 7. Learning from AI-Development Experience

## 7.1 Memory and experience reuse

### Representative work
- DS-Agent
- ML-Master
- AIBuildAI-2
- MLEvolve

### Important distinction
`raw trace → retrievable case → abstracted lesson → reusable skill/knowledge`

Storing trajectories is not the same as learning transferable research knowledge.

## 7.2 Policy learning from execution

### Representative work
- MLE-Dojo
- ML-Agent
- MLE-RL / execution-grounded RL systems
- Frontis-MA1/OpenRSI lineage

### Main argument
AI-building experience begins to be internalized in model parameters rather than existing only in prompts/memory.

---

# 8. Beyond Engineering: Automating the AI Research Loop

## 8.1 Literature grounding and problem formulation

Research adds goals that are weak or absent in AutoML:
- novelty
- relevance
- prior-art grounding
- unresolved-question identification

## 8.2 Hypothesis and idea generation

### Candidate object changes
`configuration/code → explanation/hypothesis/mechanism/research idea`

## 8.3 Experimental design and execution

### Representative systems
- AI Scientist
- AIRA / Agent Laboratory-style systems
- R&D-Agent
- ResearchGym-style systems

### Loop
`hypothesis → code → experiment → observation`

## 8.4 Interpretation and revision

A research result may:
- improve a metric
- falsify a hypothesis
- reveal a confounder
- eliminate a direction
- motivate a new experiment

This is why research cannot be reduced to scalar-reward optimization alone.

---

# 9. From Artifact Optimization to Epistemic Optimization

**This should be one of the paper's main conceptual contributions.**

## 9.1 Artifact space

Contains:
- code
- architectures/models
- data
- configurations
- experiment outputs
- metrics
- papers/reports

Most AutoML, NAS, program-search, and MLE systems live primarily here.

## 9.2 Epistemic space

Contains:
- hypotheses
- uncertainty
- causal/mechanistic beliefs
- supporting evidence
- contradicting evidence
- unresolved questions

## 9.3 Dual transition

`(artifact state, epistemic state) + experiment → observation → updated artifact + updated beliefs`

### Central argument
An experiment can be valuable even when it does not immediately increase performance, because it can reduce uncertainty and alter the value of future experiments.

### Contrast
**Optimization loop:**

`candidate → execute → scalar reward → next candidate`

**Research loop:**

`experiment → evidence → belief update → changed future experiment value`

---

# 10. Improving the Improver

## 10.1 Agent and harness optimization

### Optimization targets
- prompts
- context construction
- tool sets
- memory
- workflow
- multi-agent topology
- harness/source code

### Representative work
- ADAS
- EvoAgentX
- Meta-Harness
- Self-Harness

## 10.2 Recursive/self-improving AI4AI

### Proposed hierarchy
- **Level 0:** artifact improvement
- **Level 1:** process/workflow improvement
- **Level 2:** improver/agent improvement
- **Level 3:** recursive improvement, where the improved improver contributes to its own future improvement

### Representative frontier
- Frontis-MA1 / OpenRSI
- meta-evolution / self-evolving systems

---

# 11. Evaluating AI That Builds AI

## 11.1 Evolution of the evaluation unit

`function → model → AutoML pipeline → experiment → Kaggle-scale engineering → AI R&D → paper reproduction → open-ended research`

## 11.2 MLE benchmarks

- MLAgentBench
- MLE-bench
- MLE-Dojo

## 11.3 Research and reproduction benchmarks

- RE-Bench
- PaperBench
- MLR-Bench
- ResearchCodeBench
- EXP-Bench
- ResearchGym
- NatureBench
- PostTrainBench / MLS-Bench where relevant

## 11.4 What should count as success?

Not just final score:
- performance
- compute efficiency
- robustness
- generalization
- reproducibility
- novelty
- experimental validity
- information gain
- long-term research progress

---

# 12. Unified Design Space / Systematic Taxonomy

This is where the repository's detailed taxonomy should appear in the paper.

Every method can be annotated by:

| Dimension | Values / progression |
|---|---|
| Automation target | HPO → architecture → algorithm → code → experiment → hypothesis → full research → improver |
| Search representation | vector → graph → program → language → repository → research state |
| Proposal mechanism | BO / bandit / RL / gradient / evolution / LLM / tree search / multi-agent / world model |
| Feedback | validation metric / execution / verifier / judge / evidence |
| Experience | none / warm-start / archive / memory / abstracted knowledge / learned policy |
| Adaptation | per-task / cross-task / continual / self-modifying |
| Human scaffolding | fixed / configurable / adaptive / agent-authored / self-improving |
| Evaluation horizon | evaluation / experiment / competition / research project / multi-project |
| Open-endedness | closed / partially open / open-ended |

### Relation to repository B1–B9 branches
The B1–B9 taxonomy is useful as a **method-level systematic map**, but should not control the main narrative of the paper.

---

# 13. Open Challenges and Future Directions

## 13.1 Reliable and non-gameable evaluators
- reward hacking
- benchmark overfitting
- contamination
- model-as-judge circularity

## 13.2 Generalization
- across datasets
- modalities
- codebases
- model scales
- research domains

## 13.3 Long-horizon credit assignment
Research progress can depend on experiments many steps earlier.

## 13.4 Learning from negative results
Need to preserve failed hypotheses and contradictions, not only best candidates.

## 13.5 Cost-aware experimentation
Optimize expected research value per compute/time/resource budget.

## 13.6 Research world models
Potential formulation:

`(current artifact state, epistemic state, proposed experiment)`

→

`(predicted result, predicted belief update, future research value)`

The key is **epistemic transition**, not merely predicting the next environment observation.

## 13.7 Open-endedness versus verifiability
Closed spaces are easier to score; open research spaces are more creative but harder to verify.

## 13.8 Safety of self-improving systems
- objective preservation
- evaluator manipulation
- auditability
- compute/resource control
- independent verification

---

# 14. Outlook

Final progression:

`AutoML`
→ `NAS / algorithm discovery`
→ `meta-learning / learned optimization`
→ `LLM optimization`
→ `MLE agents`
→ `AI research agents`
→ `self-improving AI4AI`

### Closing thesis
The frontier is shifting from **automating optimization** toward **automating the acquisition and use of knowledge required for optimization**.

A mature autonomous AI researcher must repeatedly answer:

> **What should we learn next about how to build better AI, what experiment would teach us that, and how should the resulting evidence change what we do afterward?**

---

## Immediate writing tasks

1. Expand Sections 2--5 with classical AutoML/NAS/meta-learning references from `foundations/papers.md`.
2. Expand Sections 6--10 using all Agent4AI papers from `agent4ai/papers.md`.
3. Build the systematic method table using the dimensions in Section 12.
4. Build a benchmark table with task unit, horizon, environment, metric, human baseline, and contamination controls.
5. Verify every BibTeX entry against the original paper/project page before submission.
6. Only after the text stabilizes, design figures around the historical progression and artifact/epistemic dual-space view.

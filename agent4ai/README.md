# Agent4AI Hub

This directory contains the fast-moving **Agent4AI** part of Awesome AI4AI: agents that improve AI/ML systems or automate and improve the AI R&D process itself.

> **Scope rule.** Agent4AI is **not** a generic LLM-agent survey. Planning, memory, tool use, multi-agent coordination, or RL are included only when they directly improve **AI/ML engineering, model development, experimentation, research, or the improver itself**. Generic agent-memory/tool papers are background mechanisms, not core Agent4AI papers.

## Structure

| File | Purpose |
|---|---|
| [`papers.md`](papers.md) | Main verified paper table for 2024–2026 Agent4AI |
| [`recent.md`](recent.md) | Newly verified papers before deduplication / merge |
| [`benchmarks.md`](benchmarks.md) | MLE, data-agent, AI-research, post-training, and RSI benchmarks |
| [`surveys.md`](surveys.md) | Related surveys, reviews, and position papers |

## Our main taxonomy: **where does the AI-improvement state update?**

Rather than using a generic agent taxonomy such as *planning / memory / tools / multi-agent*, we organize Agent4AI by **which state in the AI R&D loop is being improved and retained**.

```text
Solution State
   ↓
Experiment / Search State
   ↓
Experience State
   ↓
Belief / Research State
   ↓
Policy State
   ↓
Harness State
   ↓
Improver State
   ↓
Research-System State
```

| Branch | State being updated | Core question | Representative work |
|---|---|---|---|
| **A1. Solution-Space Search** | candidate code / model / algorithm | How do we find a better AI solution with a mostly fixed agent? | SELA, AIDE, I-MCTS, MLE-STAR, AutoMLGen |
| **A2. Experiment-State Optimization** | search tree / experiment portfolio / resource allocation | Which experiment should run next, and how should compute be allocated? | AIDE, I-MCTS, R&D-Agent, Reasoning as Gradient |
| **A3. Experience → Knowledge** | reusable successful/failed trajectories, skills, lessons | How does an agent accumulate transferable AI-engineering experience? | DS-Agent, ML-Master, AIBuildAI-2, MLEvolve |
| **A4. Evidence → Belief / Research State** | hypotheses, evidence, uncertainty, research conclusions | How should experimental evidence change what the agent believes and what it tries next? | Hypothesis-Tree Refinement / Arbor; emerging research-state methods |
| **A5. Predictive Research Judgment** | predicted experiment outcome / value / information gain | Can the agent predict which expensive experiment is worth executing? | FOREAGENT; emerging AI4AI world models / research taste |
| **A6. Policy Learning from Execution** | model / agent policy | Can executable AI-R&D experience be internalized into weights? | ML-Agent, MLE-RL, MLE-Dojo, AceGRPO, Frontis-MA1 |
| **A7. Harness / Workflow Self-Optimization** | prompts, tools, context, memory implementation, topology, orchestration | Can AI redesign the machinery around the base model? | ADAS, EvoAgentX, SwarmAgentic, Meta-Harness, Self-Harness |
| **A8. Improver Learning / Meta-Evolution** | the mechanism that performs improvement | Can the improver learn from previous improvement attempts? | OpenRSI / Frontis-MA1, self-improving evolutionary systems |
| **A9. Full AutoResearch** | whole hypothesis → experiment → evidence → artifact loop | Can the system autonomously conduct increasingly complete AI research? | AI Scientist, AI Scientist-v2, AIRA_2, Agent Laboratory, AlphaLab |

### Why this is different from a standard agent taxonomy

A standard agent survey might ask whether a system has **planning, memory, tools, reflection, or multiple agents**. For Agent4AI, those are implementation components. The more important question is:

> **What persistent state changes after an AI experiment, and can that state make the next AI-improvement cycle better?**

This lets us distinguish systems that otherwise all look like `LLM + code execution`.

---

## Memory in Agent4AI: when does it actually count?

**Memory alone is not AI4AI.** It becomes an Agent4AI contribution when it stores or transforms information that directly improves future AI R&D.

We propose three increasingly strong levels:

### M1. Trajectory Memory — *remember what happened*

Store raw or lightly processed research traces:

```text
(task, code, config, command, metric, error, log, action sequence)
```

Typical update:

```text
new experiment → append trajectory / failure / score
```

Use case: retrieve a similar previous task or avoid repeating a failed implementation.

Examples: **DS-Agent**, basic episodic memory in MLE agents.

### M2. Experience / Knowledge Memory — *extract what was learned*

Compress trajectories into reusable lessons, skills, strategies, and failure conditions:

```text
trajectory
   ↓ reflection / summarization / verifier
lesson / skill / rule / reusable code pattern
   ↓ deduplicate + merge + confidence update
knowledge memory
```

A useful memory item might look like:

```text
Context:
  tabular classification with severe class imbalance

Action:
  stratified split + class-weighted LightGBM

Evidence:
  +0.037 validation AUC across 4 seeds

Failure boundary:
  SMOTE degraded calibration

Confidence:
  medium-high

Provenance:
  tasks X, Y, Z
```

Examples: **ML-Master**, **AIBuildAI-2**, **MLEvolve**, hierarchical skill accumulation.

This is much more relevant to AI4AI than generic conversation memory because the stored object is **research experience**.

### M3. Belief / Epistemic State — *update what the agent thinks is true*

The strongest form is not just remembering actions but updating hypotheses and uncertainty from evidence:

```text
Hypothesis H
   ↓ experiment E
Observation / metric / artifact
   ↓ evidence interpretation
Support(H) ↑ / ↓
Uncertainty(H) ↑ / ↓
New hypothesis H'
   ↓
next experiment
```

Possible state:

```text
Hypothesis: augmentation improves low-data robustness
Evidence_for: E12, E19
Evidence_against: E23
Confidence: 0.62
Known boundary: gain disappears above 50k samples
Open question: interaction with pretrained encoder scale
Next discriminating experiment: ...
```

Examples / early signals: **Toward Generalist Autonomous Research via Hypothesis-Tree Refinement (Arbor)** and research-agent systems that explicitly link hypotheses, artifacts, evidence, and distilled insights.

This **epistemic memory** is especially important for moving from MLE agents to genuine AI research agents.

### A practical memory update loop

For Agent4AI, a good memory system should not simply `append()` everything. A stronger loop is:

```text
Execute experiment
      ↓
Capture trace + result + artifacts
      ↓
Evaluate reliability / provenance
      ↓
Reflect: what actually changed?
      ↓
Extract candidate lesson / evidence
      ↓
Compare with existing memory
   ↙          ↓          ↘
merge      revise      create
   ↓          ↓          ↓
update confidence / scope / provenance
      ↓
Retrieve only when relevant to next research decision
```

Important operations are therefore:

- **Write:** what information is worth retaining?
- **Credit assignment:** which action actually caused the gain/loss?
- **Abstraction:** convert one trajectory into a reusable lesson.
- **Deduplication:** merge semantically equivalent lessons.
- **Revision:** new experiments can weaken or invalidate old memory.
- **Scope estimation:** record where a lesson is known to work.
- **Confidence update:** accumulate supporting / contradicting evidence.
- **Retrieval:** condition on task, model, dataset, stage, and current hypothesis.
- **Forgetting:** remove stale or consistently contradicted knowledge.

For the survey, generic agent-memory papers should appear only briefly as mechanism background. The core table should focus on papers where memory is tied to **ML experiments, research trajectories, transferable AI skills, or epistemic state**.

---

## Two orthogonal axes for comparing Agent4AI

The **A1–A9 taxonomy** describes *where improvement happens*. A second axis describes *how closed and recursive the loop is*.

Represent one improvement pass as:

```text
goal → plan → execute → feedback → state update → next pass
```

| Dimension | Question |
|---|---|
| **Improvement state** | solution / experiment / experience / belief / policy / harness / improver |
| **Feedback** | metric / logs / verifier / evidence / learned predictor / reviewer |
| **Closure** | which stages are system-owned rather than human-specified? |
| **Self-reference** | is the system being improved also doing the improving? |
| **Grounding** | how externally verifiable is the improvement signal? |
| **Persistence** | does the gain survive the current run? |
| **Transfer** | does it help new tasks / datasets / model scales? |
| **Compounding** | does the improved system become a better improver? |

This gives us a more distinctive survey framework than simply grouping papers by agent modules.

---

## Reliability: the composition gap

Agent4AI is inherently long-horizon: success depends on preserving and validating consequences across repeated plan–execute–feedback–state-update cycles. Planning, coding, tool use, evaluation, and repair may each look strong separately while the coupled end-to-end research loop remains unreliable.

For our survey, evaluate not only final score but also:

- **reliable horizon** — how long a coupled trajectory remains on-goal;
- **state quality** — whether experiment outcomes are converted into correct experience / belief updates;
- **error propagation** — whether local mistakes corrupt later research state;
- **verification quality** — whether feedback measures genuine progress rather than proxy exploitation;
- **persistent gain** — whether improvement survives new tasks or settings;
- **compounding** — whether improved systems become better improvers.

---

## Positioning relative to existing AI4AI surveys

A nearby 2026 survey, **On the Eve of AI4AI: From Long-Horizon Agents to Recursive Self-Improvement**, focuses strongly on **long-horizon reliability, closure, model-vs-harness routes, self-reference, and RSI**.

Our intended review is narrower in object but finer in mechanism:

| Our planned review | Nearby long-horizon / RSI survey |
|---|---|
| primary subject is **AI agents improving AI / AI research** | starts from general long-horizon agents and builds toward AI4AI / RSI |
| AutoML / NAS are **brief historical lineage only** | not centered on AutoML lineage |
| detailed taxonomy of **where AI-improvement state updates** | taxonomy emphasizes **closure / self-reference / compounding** |
| separates **experience memory** from **epistemic / belief-state updating** | treats memory mainly as part of the long-horizon reliability stack |
| emphasizes **MLE agents, post-training agents, research agents, executable AI R&D** | emphasizes the broader road to recursively self-improving agents |
| highlights **world models / research judgment / experimental belief update** as an emerging research gap | highlights reliable execution, self-reference, and compounding |

So the main story should remain:

```text
AI Agent for AI
      ↓
search better AI solutions
      ↓
learn from AI experiments
      ↓
accumulate transferable AI-R&D experience
      ↓
update research beliefs from evidence
      ↓
predict which AI experiments are worth running
      ↓
learn / redesign the agent and harness
      ↓
improve the improver
      ↓
full autonomous AI research / recursive improvement
```

## Recommended survey-table columns

For each core Agent4AI paper, use columns such as:

`Year | Paper | AI-R&D Task | Improvement State | Search/Policy Mechanism | Execution Feedback | Memory Level (M0–M3) | Weight Update? | Harness Update? | Closure | Self-Reference | Benchmark`

This should make differences between superficially similar MLE agents much easier to see.

## Maintenance

`recent.md` is intentionally temporary. New papers are collected there quickly, then periodically verified, deduplicated, categorized, and merged into `papers.md`. Generic memory/tool/agent papers stay out of the core table unless they directly improve AI R&D.

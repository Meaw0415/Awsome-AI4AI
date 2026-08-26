# Agent4AI Hub

This directory covers **Agent4AI: AI agents for improving AI**. The scope includes machine-learning engineering, model building, data analysis for AI, post-training, algorithm/program discovery, agent-system optimization, AI research automation, and self-improving AI systems.

> **Scope rule.** Agent4AI is **not** a generic LLM-agent survey. Planning, memory, tools, multi-agent coordination, RL, or world models are included only when they directly improve **AI models, AI engineering, AI training, AI evaluation, AI experimentation, AI research, or the agent/improver used to build AI**.

[Start here](getting-started.md) · [Papers](papers.md) · [Recent](recent.md) · [Benchmarks](benchmarks.md) · [Surveys](surveys.md)

---

## What is Agent4AI?

A useful abstraction is an **AI improvement loop**:

```text
Goal: improve an AI system / pipeline / agent
                 ↓
        Propose candidate changes
                 ↓
       Build / Train / Execute
                 ↓
        Evaluate / Verify
                 ↓
     Interpret outcome / assign credit
                 ↓
     Update reusable state / experience
                 ↓
         Select the next action
                 ↓
 Learn the policy / redesign the harness
                 ↓
              Repeat
```

The task can be Kaggle-style MLE, LLM post-training, architecture or algorithm discovery, agent-system optimization, paper reproduction, or open-ended AI research. The common object is **AI improving AI**.

---

# A finer taxonomy: where does improvement happen?

Instead of grouping papers by generic agent components such as *planning / memory / tools / multi-agent*, we organize Agent4AI by **which part of the AI-improvement loop becomes better**.

| Branch | Optimization object | Core question | Representative work |
|---|---|---|---|
| **B1. Candidate Generation & Search** | code, model, pipeline, algorithm, hypothesis | How are promising AI improvements proposed and explored? | SELA, AIDE, I-MCTS, MLE-STAR, R&D-Agent, AutoMLGen |
| **B2. Execution, Evaluation & Credit** | experiments, training runs, scores, traces | How do we obtain trustworthy feedback and identify what caused the gain or failure? | MLE-bench, MLE-Dojo, executable graders, ablation/verifier loops |
| **B3. Experience → Reusable Knowledge** | trajectories, skills, lessons, failure modes | How does an agent retain and transfer useful AI-building experience? | DS-Agent, ML-Master, AIBuildAI-2, MLEvolve, skill accumulation |
| **B4. State Updating & Next-Action Selection** | search state, uncertainty, beliefs, value estimates | Given what happened, what should the agent try next? | I-MCTS, Reasoning as Gradient, FOREAGENT, hypothesis/evidence-state methods |
| **B5. Policy Learning from AI-Building Experience** | agent/model weights | Can execution traces and rewards be internalized into a stronger AI-building policy? | ML-Agent, MLE-RL, AceGRPO, Frontis-MA1, post-training agents |
| **B6. Harness / Workflow Optimization** | prompts, tools, context, memory implementation, topology, orchestration | Can AI improve the system around the base model? | ADAS, EvoAgentX, SwarmAgentic, Meta-Harness, Self-Harness |
| **B7. Program / Algorithm Evolution** | populations of programs, algorithms, agents | Can executable evolution discover better AI methods or systems? | FunSearch, AlphaEvolve, AdaEvolve, MLEvolve, OpenMLE-Evo |
| **B8. Improver Learning & Meta-Evolution** | the improvement mechanism itself | Can the mechanism that generates improvements learn from previous improvement cycles? | OpenRSI / Frontis-MA1, self-improving evolutionary systems |
| **B9. Full-Cycle AI Development / AutoResearch** | end-to-end AI project lifecycle | Can agents own increasingly complete AI-development tasks? | AI Scientist, AIRA, Agent Laboratory, AlphaLab, ResearchGym |

### Why this taxonomy is useful

The same system may use planning, memory, tools, and RL simultaneously. Those are implementation choices. For AI4AI, the more revealing questions are:

- **What is being improved?** solution, policy, harness, algorithm, improver, or full AI-development process;
- **What feedback closes the loop?** metric, logs, verifier, execution result, evidence, reviewer, or learned value;
- **What persists across iterations?** nothing, search state, memory, weights, harness changes, or an improved improver;
- **Does improvement transfer or compound?** across tasks, models, datasets, or generations.

---

## Memory in Agent4AI

**Memory is not a standalone Agent4AI branch by default.** It matters when it changes future AI-building decisions.

We use three levels:

### M1. Trajectory Memory — remember what happened

```text
(task, code, config, command, metric, error, log, action sequence)
```

Useful for retrieving similar runs, avoiding repeated failures, and continuing long-horizon tasks.

Examples: DS-Agent and episodic memories used in MLE agents.

### M2. Experience / Knowledge Memory — extract what was learned

```text
trajectory
   ↓ reflection / attribution
lesson / skill / rule / reusable pattern
   ↓ merge + scope + confidence
knowledge memory
```

Examples: ML-Master, AIBuildAI-2, MLEvolve, hierarchical skill accumulation.

The important question is not simply whether a system stores memory, but **how it updates memory**:

- write only information that changes future decisions;
- assign credit to the action that caused a gain or failure;
- abstract specific trajectories into reusable skills or rules;
- merge duplicates and contradictions;
- record scope, provenance, and confidence;
- revise or forget knowledge after new evidence;
- retrieve conditional on task, model, dataset, stage, and current objective.

### M3. Structured Decision State — maintain what the system currently thinks should be done

For open-ended optimization or research, the state may include hypotheses, supporting/contradicting evidence, uncertainty, unresolved questions, or expected value of candidate actions.

```text
Current belief / state
        ↓
candidate actions
        ↓
expected value / uncertainty / evidence
        ↓
select next action
        ↓
execute and update state
```

Hypothesis-tree methods are one example, but this idea is broader than research: the state can also encode which model families, data transformations, post-training recipes, or agent modifications are currently promising.

---

## Where do predictive models / world models fit?

They are **not a separate top-level branch**. They are one mechanism inside **B4: State Updating & Next-Action Selection**.

The problem is simple: executing every candidate AI experiment is expensive. An agent may therefore estimate which action is worth trying before full execution.

```text
candidate changes
      ↓
heuristic / tree value / uncertainty / learned critic / predictor
      ↓
prioritize candidates
      ↓
execute only the most promising ones
      ↓
update the decision state
```

`FOREAGENT` is an example of a learned predict-then-verify mechanism. Similar decision-making can be implemented with MCTS values, bandits, uncertainty, cheap proxy experiments, learned critics, or expected value-of-compute. Therefore **world models are a technique for experiment/action selection, not the central story of Agent4AI**.

---

## A second axis: how closed is the improvement loop?

Two methods in the same branch can differ greatly in autonomy and self-improvement.

| Dimension | Question |
|---|---|
| **Feedback grounding** | Is progress externally executable/verifiable? |
| **Loop closure** | Which stages are system-owned rather than human-specified? |
| **Persistence** | Does improvement survive the current run? |
| **Transfer** | Does it help unseen tasks, datasets, models, or scales? |
| **Weight update** | Does experience change the model policy? |
| **Harness update** | Can tools/prompts/memory/orchestration change? |
| **Self-reference** | Is the improving system also the object being improved? |
| **Compounding** | Does the improved system become a better improver? |

This axis complements B1–B9 and is especially useful for comparing ordinary MLE agents with OpenRSI-style systems.

---

## Main application families inside Agent4AI

These are **tasks**, not method paradigms:

| Application family | Examples |
|---|---|
| **MLE / AutoML Agents** | AIDE, MLE-STAR, ML-Master, AIBuildAI-2 |
| **Data-Analytic Agents for AI** | DataMind, DSGym, DatawiseAgent |
| **LLM Training / Post-Training Agents** | AutoTrainess, PostTrainBench, ANDES |
| **Algorithm / Program Discovery** | FunSearch, AlphaEvolve, MLEvolve |
| **Agent-System Optimization** | ADAS, Meta-Harness, Self-Harness, SwarmAgentic |
| **AI Research / Reproduction Agents** | AI Scientist, AIRA, Agent Laboratory, ResearchGym, PaperBench |
| **Self-Improving AI Systems** | Frontis-MA1 / OpenRSI, meta-evolution systems |

This separation is important: **application family tells us what task the agent solves; B1–B9 tells us how the AI-improvement mechanism works.**

---

## Recommended survey-table columns

For each core paper:

`Year | Paper | Application Family | B1–B9 Mechanism | Optimization Object | Feedback | Memory Level | Weight Update? | Harness Update? | Transfer? | Self-Reference? | Benchmark`

This should let a newcomer quickly see both **what a system does** and **how it improves AI**.

---

## Positioning

Classical AutoML / HPO / NAS remain useful historical context, but they are not the focus of this directory. The main review should concentrate on **AI agents that operate over open-ended AI-development actions**: code, experiments, training recipes, data pipelines, model policies, agent systems, algorithms, and research workflows.

The progression is roughly:

```text
fixed search spaces
      ↓
agentic open-ended solution search
      ↓
execution-grounded feedback
      ↓
experience accumulation and state updating
      ↓
policy / harness / algorithm improvement
      ↓
improver improvement
      ↓
full-cycle and self-improving AI development
```

For a practical entry path, see [`getting-started.md`](getting-started.md).

# Agent4AI Hub

This directory contains the fast-moving **Agent4AI** part of Awesome AI4AI: agents that autonomously perform, optimize, evaluate, or learn from AI/ML engineering and research.

## Structure

| File | Purpose |
|---|---|
| [`papers.md`](papers.md) | Main verified paper table for 2024–2026 Agent4AI |
| [`recent.md`](recent.md) | Newly verified papers before deduplication / merge |
| [`benchmarks.md`](benchmarks.md) | MLE, data-agent, AI-research, post-training, and RSI benchmarks |
| [`surveys.md`](surveys.md) | Related surveys, reviews, and position papers |

## Method taxonomy: where does the improvement live?

| Branch | Optimization target | Typical feedback | Representative work |
|---|---|---|---|
| **P1 Search / Scaffold** | candidate programs and experiment paths | runtime metrics, logs, search state | SELA, AIDE, I-MCTS, MLE-STAR |
| **P2 Execution-Grounded Learning** | agent/model policy | executable reward, SFT/RL trajectories | ML-Agent, MLE-RL, AceGRPO, Frontis-MA1, AutoTrainess |
| **P3 Experience / Memory** | persistent knowledge and research state | prior successes, failures, trajectories | ML-Master, AIBuildAI-2, MLEvolve, Arbor |
| **P4 World Model / Research Judgment** | predicted experiment value | execution priors, uncertainty, value-of-compute | FOREAGENT, emerging AI4AI world models |
| **P5 Harness / Workflow Optimization** | tools, prompts, context, orchestration, topology | downstream traces and scores | ADAS, EvoAgentX, Meta-Harness, Self-Harness, SwarmAgentic |
| **P6 Program Evolution** | populations of programs / algorithms | executable fitness | FunSearch, AlphaEvolve, AdaEvolve, OpenMLE-Evo |
| **P7 Trainable Improver / Meta-Evolution** | the improvement mechanism itself | search experience returned to training | OpenRSI / Frontis-MA1, self-improving agents |
| **P8 AutoResearch / AI Scientist** | hypothesis → experiment → evidence → artifact | scientific evidence and research outcomes | AI Scientist, AIRA_2, Agent Laboratory, hypothesis-tree refinement |

### Relationship between the branches

```text
Executable Environment
        ↓
Search / Scaffold ────────────────┐
        ↓                         │
Execution Trajectories            │
   ↙        ↓        ↘            │
Memory   Policy RL   World Model  │
   ↘        ↓        ↙            │
    Better Research Decisions     │
              ↓                   │
     Harness / Improver Update ───┘
              ↓
        Meta-Evolution
              ↓
      Recursive Improvement
```

The useful distinction is **external versus internal improvement**. Search-based methods improve outputs while leaving the base policy mostly fixed. Execution-grounded learning internalizes task feedback into weights. Memory systems externalize reusable experience. World-model methods try to predict expensive outcomes. Harness optimization changes the machinery around the model. Meta-evolution closes the loop by using search-generated experience to improve the improver that controls later search.

## A complementary axis: where does the loop close?

Our P1–P8 taxonomy answers **what is being improved and by what mechanism**. A complementary view, emphasized by the 2026 survey *On the Eve of AI4AI*, is **how much of the improvement loop is actually autonomous**.

Represent an improvement pass as:

```text
goal → plan → execute → feedback → repair → next pass
```

Then compare systems along five orthogonal dimensions:

| Dimension | Question |
|---|---|
| **Target** | What may the system change: solution, model, data, harness, training recipe, or improver? |
| **Closure** | Which of plan / execute / feedback / repair are system-owned rather than human-specified? |
| **Self-reference** | Is the system being improved also the system doing the improving? |
| **Grounding** | How constrained and externally verifiable is the improvement signal? |
| **Compounding** | Do improvements transfer, accumulate, or make later improvement more effective? |

This prevents overloading the term **recursive self-improvement**. A search scaffold can improve outputs without changing itself; ADAS / Meta-Harness use an outer improver to redesign an agent or harness; Self-Harness removes the stronger external improver but still uses a fixed evaluator; Frontis-MA1 moves further by feeding execution-grounded experience back into the improver used by later search. True RSI would additionally require reliable compounding improvement in the improvement process itself.

## Reliability: the composition gap

Agent4AI is inherently long-horizon: success depends on preserving and validating consequences across repeated plan–execute–feedback–repair cycles. A useful failure mode is the **composition gap**: planning, coding, tool use, evaluation, and repair may each look strong separately, while the coupled end-to-end research loop remains unreliable.

For our survey, this suggests evaluating not only final score, but also:

- **reliable horizon:** how long a coupled trajectory remains on-goal;
- **closure:** which stages are actually autonomous;
- **error propagation:** whether early local mistakes corrupt later research state;
- **verification quality:** whether feedback measures genuine progress rather than proxy exploitation;
- **persistent gain:** whether an improvement survives new tasks, scales, or future generations;
- **compounding:** whether improved systems become better improvers.

## Recommended comparison dimensions

For survey tables, classify each Agent4AI method by:

- **Optimization object:** solution / code / experiment / model policy / memory / harness / research strategy / improver.
- **Feedback source:** scalar metric / execution logs / verifier / evidence / learned predictor / human or reviewer signal.
- **Adaptation location:** frozen model + scaffold / external memory / test-time learning / SFT / RL / self-modifying harness.
- **Search structure:** linear refinement / tree / MCTS / graph / population / multi-agent / learned policy.
- **Experience reuse:** none / in-task memory / cross-task retrieval / distilled knowledge / weight update.
- **Horizon:** single solution / multi-experiment / project-level / research lifecycle / cross-generation self-improvement.
- **Closure:** which of plan / execute / feedback / repair are system-owned.
- **Self-reference:** outer improver / self-modifying system / same improver and improved system.
- **Compounding evidence:** none / retained artifact / cross-task transfer / persistent policy gain / improved future improver.

## Positioning relative to existing AI4AI surveys

A nearby 2026 survey, **On the Eve of AI4AI: From Long-Horizon Agents to Recursive Self-Improvement**, is organized primarily around **long-horizon reliability, closure, model-vs-harness routes, self-reference, and RSI**. Our intended scope is complementary:

| This repository / planned review | On the Eve of AI4AI |
|---|---|
| traces the historical lineage from **AutoML / NAS / learned optimization → Agent4AI** | starts from **long-horizon agents → AI4AI → RSI** |
| emphasizes **MLE agents, executable AI research, data agents, AutoResearch** | emphasizes **reliable horizon and autonomy closure** |
| organizes modern work by **P1–P8 method paradigms** | organizes systems by **target / closure / self-reference / grounding / compounding** |
| treats **world models / research judgment / epistemic state** as a distinct emerging branch | emphasizes the broader **composition gap and reliable execution stack** |
| keeps a large bibliography and benchmark map for writing a full survey | audits a smaller set of representative systems in depth |

The strongest survey structure is therefore to use **P1–P8 as the main methodological taxonomy**, and use **closure / self-reference / compounding as cross-cutting evaluation axes**.

## Core trajectory

```text
Fixed-space AutoML
      ↓
Open code-space search
      ↓
Execution-grounded MLE agents
      ↓
Experience + memory + learned policies
      ↓
World models / research judgment
      ↓
Harness and improver optimization
      ↓
AutoResearch / AI Scientists
      ↓
Meta-Evolution / RSI
```

## Maintenance

`recent.md` is intentionally temporary. New papers are collected there quickly, then periodically verified, deduplicated, categorized, and merged into `papers.md`. Benchmark papers should additionally be reflected in `benchmarks.md`.

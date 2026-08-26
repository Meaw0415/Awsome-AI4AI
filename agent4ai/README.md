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
| **P2 Execution-Grounded Learning** | agent/model policy | executable reward, SFT/RL trajectories | ML-Agent, MLE-RL, AceGRPO, Frontis-MA1 |
| **P3 Experience / Memory** | persistent knowledge and research state | prior successes, failures, trajectories | ML-Master, AIBuildAI-2, MLEvolve, Arbor |
| **P4 World Model / Research Judgment** | predicted experiment value | execution priors, uncertainty, value-of-compute | FOREAGENT, emerging AI4AI world models |
| **P5 Harness / Workflow Optimization** | tools, prompts, context, orchestration, topology | downstream traces and scores | ADAS, EvoAgentX, Meta-Harness, SwarmAgentic |
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

## Recommended comparison dimensions

For survey tables, classify each Agent4AI method by:

- **Optimization object:** solution / code / experiment / model policy / memory / harness / research strategy / improver.
- **Feedback source:** scalar metric / execution logs / verifier / evidence / learned predictor / human or reviewer signal.
- **Adaptation location:** frozen model + scaffold / external memory / test-time learning / SFT / RL / self-modifying harness.
- **Search structure:** linear refinement / tree / MCTS / graph / population / multi-agent / learned policy.
- **Experience reuse:** none / in-task memory / cross-task retrieval / distilled knowledge / weight update.
- **Horizon:** single solution / multi-experiment / project-level / research lifecycle / cross-generation self-improvement.

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

# Agent4AI Hub

This directory contains the fast-moving **Agent4AI** part of Awesome AI4AI: agents that autonomously perform, optimize, evaluate, or learn from AI/ML engineering and research.

## Structure

| File | Purpose |
|---|---|
| [`papers.md`](papers.md) | Main verified paper table for 2024–2026 Agent4AI |
| [`recent.md`](recent.md) | Staging area for newly discovered papers before deduplication / merge |
| [`benchmarks.md`](benchmarks.md) | Benchmarks for MLE agents, AI research agents, data agents, and AI R&D |
| [`surveys.md`](surveys.md) | Related surveys, reviews, and position papers |

## Taxonomy

1. **MLE Agents & Automated AI Engineering** — code, models, experiments, debugging, iterative optimization.
2. **Generalist Data-Analytic Agents** — executable analysis over heterogeneous datasets.
3. **Search & Planning** — tree search, MCTS, evolutionary search, reasoning-as-gradient.
4. **Execution Prediction / World Models** — predicting experiment outcomes and reducing expensive execution.
5. **Agent Learning** — SFT, RL, preference optimization, execution-grounded post-training.
6. **Experience & Memory** — reusable trajectories, case-based reasoning, persistent research memory.
7. **Workflow / Harness Optimization** — optimizing prompts, topology, orchestration, and the agent harness itself.
8. **AI Research Agents** — literature, ideation, hypothesis formation, experiments, evidence interpretation.
9. **AI Scientists** — broader automation of the research lifecycle.
10. **Recursive / Self-Improving AI4AI** — agents that improve the process or machinery used to build better AI.

## Core trajectory

```text
MLE Agent
   ↓
Execution-grounded search
   ↓
Learn from trajectories
   ↓
Memory / world model / post-training
   ↓
Research-agent policy improves
   ↓
AI Research Agent / AI Scientist
   ↓
Recursive Self-Improvement
```

## Maintenance

`recent.md` is intentionally temporary. New papers are collected there quickly, then periodically verified, deduplicated, categorized, and merged into `papers.md`. Benchmark papers should additionally be reflected in `benchmarks.md`.

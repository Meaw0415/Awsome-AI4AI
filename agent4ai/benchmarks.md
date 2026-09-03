# Agent4AI Benchmarks

This page focuses on benchmarks for **AI agents that improve AI**. Classical HPO/NAS benchmarks are historical background and are kept separately in [`../foundations/papers.md`](../foundations/papers.md).

## 1. ML Engineering & Model Building

| Benchmark | Year | What it tests |
|---|:---:|---|
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023/24 | iterative ML experimentation |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | 2024 | end-to-end Kaggle-style ML engineering across 75 competitions |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | 2024/25 | long-horizon frontier AI R&D under substantial time budgets |
| [MLE-Dojo](https://arxiv.org/abs/2505.07782) | 2025 | executable environments for training/evaluating MLE agents |
| [MLS-Bench](https://arxiv.org/abs/2605.08678) | 2026 | whether proposed ML improvements generalize across settings and scales |

## 2. Data Curation & Data Engineering for Model Improvement

| Benchmark / Environment | Year | What it tests |
|---|:---:|---|
| [Curation-Bench](https://arxiv.org/abs/2606.04261) | 2026 | closed-loop agentic data selection/curation where agents revise policies after model-training feedback |
| [Autonomous Agentic Data Engineering](https://arxiv.org/abs/2605.30407) | 2026 | end-to-end data generation and curriculum optimization for model specialization |
| [DSGym](https://arxiv.org/abs/2601.16344) | 2026 | executable data-science agent training/evaluation across heterogeneous tasks |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | data-agent capability in a recursive-improvement-oriented setting |

## 3. LLM Fine-Tuning & Post-Training

| Benchmark / Environment | Year | What it tests |
|---|:---:|---|
| [FT-Dojo](https://arxiv.org/abs/2603.01712) | 2026 | autonomous end-to-end LLM fine-tuning across data, training, evaluation, and diagnosis |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | 2026 | autonomous post-training of base LMs under bounded compute |
| [Agent^2 RL-Bench](https://arxiv.org/abs/2604.10547) | 2026 | whether agents can design, implement, debug, and run complete agentic RL post-training loops |

This branch is especially important for AI4AI because the **object being improved is the model itself**, rather than a downstream application built with the model.

## 4. Research Implementation, Reproduction & Full AI Projects

| Benchmark | Year | What it tests |
|---|:---:|---|
| [PaperBench](https://arxiv.org/abs/2504.01848) | 2025 | reproducing AI research papers from scratch |
| [ResearchCodeBench](https://arxiv.org/abs/2506.02314) | 2025 | implementing novel ML methods from recent papers |
| [LMR-BENCH](https://aclanthology.org/2025.emnlp-main.314/) | 2025 | reproducing language-modeling research |
| [EXP-Bench](https://arxiv.org/abs/2505.24785) | 2025/26 | complete executable AI experiments: design → implementation → execution → analysis |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | 2025 | open-ended ML research tasks |
| [ResearchGym](https://arxiv.org/abs/2602.15112) | 2026 | real-world closed-loop AI projects |
| [AIRS-Bench](https://arxiv.org/abs/2602.06855) | 2026 | frontier AI-research-agent tasks from state-of-the-art ML work |
| [NatureBench](https://arxiv.org/abs/2606.24530) | 2026 | matching/reproducing published scientific coding results |

## 5. Agent-System / Harness Improvement

Harness work often evaluates on general coding/agent benchmarks rather than a single dedicated AI4AI benchmark. Relevant evaluation settings include:

- **Meta-Harness** — outer-loop optimization of harness source code using execution traces and held-out performance.
- **Self-Harness** — self-modification of an agent harness with regression validation.
- **Retrospective Harness Optimization (RHO)** — self-supervised harness improvement from past trajectories.
- **ADAS / EvoAgentX / SwarmAgentic** — automatic generation or optimization of agentic systems/workflows.
- **[SkillMisevo-Bench / Practice Makes Unsafe](https://arxiv.org/abs/2608.12851)** — tests whether persistent skill evolution propagates unsafe procedures into later clean sessions and separates authoring, retrieval, and execution failures.

This deserves separate tracking because the **optimization object is the AI agent system itself**, not merely the task solution.

## 6. Self-Improvement / Meta-Evolution

| Benchmark / Stack | Year | What it tests |
|---|:---:|---|
| [AI4AI-Bench](https://arxiv.org/abs/2608.20318) | 2026 | whether agents can redesign training algorithms across frozen AI research repositories under a fixed compute budget |
| [OpenMLE / Frontis-MA1](https://arxiv.org/abs/2607.28568) | 2026 | execution-grounded operator learning + long-horizon evolutionary MLE search, with transfer to held-out AI tasks |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | recursive-improvement-oriented data-agent evaluation |
| [Do Self-Evolving Agents Forget?](https://arxiv.org/abs/2605.09315) | 2026 | retention and capability erosion across workflow, skill, model, and memory evolution |

The central evaluation question here is no longer only **“did the final artifact improve?”** but also **“did the system become a better improver?”** and **“did it preserve what it had already learned?”**

## 7. Benchmark validity & evaluation methodology

A growing issue is whether agent benchmarks actually measure the claimed capability rather than artifacts of the protocol, harness, evaluator, or budget.

| Paper | Year | Why it matters |
|---|:---:|---|
| [Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368) | 2026 | separates measured score from protocol validity and highlights how evaluation design can change capability conclusions |
| [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](https://arxiv.org/abs/2607.12790) | 2026 | makes the evaluator itself an evolving object and therefore forces independent validation of a learned/evolved metric |

---

## Capability Progression

```text
single ML experiment
      ↓
competition-scale MLE
      ↓
data / training-recipe optimization
      ↓
model fine-tuning and post-training
      ↓
research implementation / reproduction
      ↓
full AI-development projects
      ↓
agent / harness optimization
      ↓
meta-improvement: improve the improver
```

## What should an Agent4AI benchmark measure?

Final score alone is increasingly insufficient. Useful dimensions include:

- **execution grounding** — are improvements measured by real runs rather than self-evaluation only?
- **credit assignment** — can the system identify which change caused the improvement or failure?
- **iteration efficiency** — improvement per unit of compute, time, or number of executions;
- **transfer** — do strategies learned on one task/model help unseen ones?
- **persistence** — are gains stored in reusable knowledge, weights, or harness changes?
- **retention** — do later improvements preserve capabilities acquired earlier?
- **evaluator validity** — if the judge/metric evolves, is it independently validated rather than self-certifying?
- **robustness** — does the method avoid overfitting a benchmark/task?
- **loop closure** — how much of propose → execute → evaluate → revise is agent-owned?
- **self-improvement** — does an improved agent/harness become better at future AI-improvement tasks?

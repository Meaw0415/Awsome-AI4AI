# Getting Started with Agent4AI Research

This page is for readers who are new to **AI4AI / Agent4AI** and want to understand the field quickly, reproduce a baseline, and identify a research problem.

## 1. What is Agent4AI?

Agent4AI studies agents that improve **AI systems or the AI R&D process itself**. A typical loop is:

```text
propose a model / code / hypothesis
        ↓
execute an experiment
        ↓
observe metrics, logs, artifacts, failures
        ↓
interpret what the evidence means
        ↓
update search state / experience / belief
        ↓
choose the next experiment
        ↓
adapt the policy, memory, harness, or improver
        ↓
repeat
```

The key difference from a generic coding agent is that the object being improved is **AI/ML engineering or AI research**.

## 2. Read these papers first

### Stage 1 — understand executable MLE agents

1. [MLAgentBench](https://arxiv.org/abs/2310.03302) — early benchmark for iterative ML experimentation.
2. [MLE-bench](https://arxiv.org/abs/2410.07095) — establishes Kaggle-scale machine-learning engineering as an executable agent benchmark.
3. [AIDE](https://arxiv.org/abs/2502.13138) — solution-tree search over code.
4. [MLE-STAR](https://arxiv.org/abs/2506.15692) — search plus targeted refinement.
5. [ML-Master](https://arxiv.org/abs/2506.16499) — combines exploration, reasoning, and adaptive memory.

### Stage 2 — understand learning from execution

6. [MLE-Dojo](https://arxiv.org/abs/2505.07782) — executable training/evaluation environment for MLE agents.
7. [ML-Agent](https://arxiv.org/abs/2505.23723) — reinforcement learning for autonomous MLE.
8. [Frontis-MA1 / OpenRSI](https://arxiv.org/abs/2607.28568) — execution-grounded SFT/RL plus long-horizon evolutionary search in one AI4AI stack.
9. [AIBuildAI-2](https://arxiv.org/abs/2605.27873) — distills completed MLE runs into an evolving external knowledge system.

### Stage 3 — understand research-level agents

10. [The AI Scientist](https://arxiv.org/abs/2408.06292) — idea → experiment → paper → review.
11. [MLGym](https://arxiv.org/abs/2502.14499) — interactive environment for AI research agents.
12. [MLR-Bench](https://arxiv.org/abs/2505.19955) — open-ended machine-learning research benchmark.
13. [EXP-Bench](https://arxiv.org/abs/2505.24785) — complete AI research experiments.
14. [ResearchGym](https://arxiv.org/abs/2602.15112) — real-world closed-loop AI research projects.
15. [Toward Generalist Autonomous Research via Hypothesis-Tree Refinement](https://arxiv.org/abs/2606.11926) — persistent hypotheses, evidence, artifacts, and research state.

### Stage 4 — understand self-improvement of the agent system

16. [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) — automatically search agent-system designs.
17. [Meta-Harness](https://arxiv.org/abs/2603.28052) — optimize harness source code using traces and scores.
18. [Self-Harness](https://arxiv.org/abs/2606.09498) — an agent improves its own harness using weakness mining, proposals, and regression tests.
19. [AutoTrainess](https://arxiv.org/abs/2606.31551) — an agent autonomously performs LM post-training using a training-specialized interface.
20. [AlphaEvolve](https://arxiv.org/abs/2506.13131) — evolutionary coding for algorithmic and scientific discovery.

## 3. Understand the research loop, not just the agent modules

A useful Agent4AI taxonomy asks **where the improvement occurs after an experiment**.

| Research-loop stage | Typical research question | Representative methods |
|---|---|---|
| **Generate** | How do we propose better code, hypotheses, or experiments? | tree search, MCTS, evolutionary search, multi-agent ideation |
| **Execute & Verify** | How do we obtain reliable external feedback? | executable environments, graders, reproducible evaluators |
| **Interpret & Credit** | Which action or hypothesis caused the observed gain/loss? | reflection, ablation, verifier, credit assignment |
| **Update Research State** | What reusable knowledge or belief should change? | trajectory memory, distilled skills, hypothesis/evidence state |
| **Choose Next Experiment** | What is the best use of the next unit of compute? | search value, uncertainty, predicted outcome, value-of-information |
| **Internalize** | Can the agent learn from previous AI-R&D experience? | SFT, RL, preference learning, continual learning |
| **Redesign the Agent** | Can prompts, tools, memory, orchestration, or topology improve? | ADAS, Meta-Harness, Self-Harness |
| **Improve the Improver** | Can the mechanism generating improvements itself get better? | OpenRSI / meta-evolution, self-improving systems |
| **Close the Research Loop** | Can the agent own increasingly complete research projects? | AI Scientist, AIRA, AlphaLab, ResearchGym |

`World models` are therefore **not a standalone required branch**. They are one possible mechanism for **choosing the next experiment**: predict outcomes or research value before paying for expensive execution. Other mechanisms include tree-search value estimates, uncertainty, bandits, heuristics, learned critics, and explicit information-gain objectives.

## 4. Benchmarks: choose one before proposing a method

| Goal | Good starting benchmark |
|---|---|
| ML engineering / Kaggle-style optimization | [MLE-bench](https://arxiv.org/abs/2410.07095) |
| train an MLE policy | [MLE-Dojo](https://arxiv.org/abs/2505.07782) |
| open-ended ML research | [MLR-Bench](https://arxiv.org/abs/2505.19955) |
| implement methods from papers | [ResearchCodeBench](https://arxiv.org/abs/2506.02314) |
| complete AI research experiments | [EXP-Bench](https://arxiv.org/abs/2505.24785) |
| real-world research projects | [ResearchGym](https://arxiv.org/abs/2602.15112) |
| autonomous LM post-training | [PostTrainBench](https://arxiv.org/abs/2603.08640) |
| transfer to scientific research code | [NatureBench](https://arxiv.org/abs/2606.24530) |
| building better AI across settings/scales | [MLS-Bench](https://arxiv.org/abs/2605.08678) |

## 5. Practical research entry points

Good starter projects should modify **one part of the loop** while keeping the rest controlled.

### R1. Better experiment selection

Baseline: AIDE / MLE-STAR / MLE-bench.

Question: can the agent rank candidate experiments better before executing all of them?

Possible signals: uncertainty, historical transfer, cheap proxy runs, learned critic, expected information gain, expected score improvement per GPU-minute.

### R2. Experience that actually transfers

Baseline: ML-Master / AIBuildAI-2.

Question: when should an old experiment become a reusable lesson, and when should that lesson be revised or forgotten?

Measure: cross-task transfer, negative transfer, memory precision, compute saved, performance gain.

### R3. Evidence-aware research state

Baseline: hypothesis-tree / AutoResearch systems.

Question: can the agent explicitly maintain hypotheses, evidence-for/evidence-against, uncertainty, and unresolved questions?

Measure: better next-experiment choices, fewer redundant experiments, better hypothesis discrimination.

### R4. Learn from trajectories rather than only search harder

Baseline: MLE-Dojo / ML-Agent / Frontis-MA1.

Question: what parts of successful and failed MLE trajectories are useful for SFT/RL? How should long-horizon credit be assigned?

### R5. Optimize the harness

Baseline: ADAS / Meta-Harness / Self-Harness.

Question: which harness components should be mutable—prompt, memory policy, tool interface, context management, branching strategy, verification, or scheduling?

Important evaluation: transfer the optimized harness to unseen tasks and, ideally, different base models.

### R6. From one-shot gains to compounding improvement

Baseline: OpenRSI / evolutionary AI4AI.

Question: does an improved agent become a **better improver**, or does it merely produce a better one-off solution?

Measure improvement across generations, transfer, self-reference, and rate-of-improvement rather than only final task score.

## 6. A useful experimental template

For a first Agent4AI project:

```text
1. Pick one executable benchmark.
2. Reproduce a strong open baseline.
3. Identify one bottleneck in the closed loop.
4. Change only that component.
5. Log full trajectories, artifacts, compute, and failures.
6. Evaluate final quality AND process quality.
7. Test transfer on unseen tasks.
8. Run ablations that separate model strength from harness/method gains.
```

Recommended process metrics include:

- best score vs. compute;
- number of executed experiments;
- duplicated / wasted experiments;
- error recovery rate;
- useful-memory retrieval precision;
- transfer to unseen tasks;
- robustness across base models;
- research-horizon completion rate;
- persistent or compounding gain across iterations.

## 7. What to avoid

A project is usually too generic for this survey if it is merely:

- a new generic memory module tested only on QA/chat;
- a tool-use agent with no AI/ML R&D task;
- a multi-agent workflow without measurable improvement to AI development;
- prompt optimization with no connection to AI engineering/research;
- a coding benchmark that never trains, evaluates, or improves an AI system.

The core question should stay:

> **How does this method make AI better at building, evaluating, researching, or improving AI?**

## 8. Repository navigation

- [`README.md`](README.md): Agent4AI taxonomy and conceptual map.
- [`papers.md`](papers.md): main paper table.
- [`recent.md`](recent.md): newly discovered papers.
- [`benchmarks.md`](benchmarks.md): benchmark landscape.
- [`surveys.md`](surveys.md): related surveys and position papers.

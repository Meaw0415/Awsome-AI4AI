# Additions from Preprints.org 202608.2108

Source survey: **AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement—Definitions, Reliable Horizons, and Open Problems** (Wu et al., 2026), Preprints.org manuscript 202608.2108.

This file is a staging list of references and conceptual links worth merging into the comprehensive AI4AI library. The goal is **not** to copy the survey bibliography wholesale. We prioritize papers that fill a missing transition in our historical AI4AI narrative or sharpen the late-stage self-improvement taxonomy.

## A. Survey anchor

- **2026** — ★ *AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement—Definitions, Reliable Horizons, and Open Problems* — Wu et al. https://www.preprints.org/manuscript/202608.2108
  - Useful for: stage ownership, signal grounding, reliable horizon, composition gap, retention/transfer evidence.
  - Scope difference from our review: it centers the intersection of **long-horizon agents and AI-driven improvement**, whereas our review traces the full AI4AI lineage from HPO/AutoML and NAS onward.

## B. Weight-layer AI4AI: data, architecture, learning algorithms

- **2026** — ★ *ASI-Evolve: AI Accelerates AI*. https://arxiv.org/abs/2603.29640
  - Unified AI-for-AI framework across **pretraining-data curation, neural architecture design, and RL-algorithm design**.
  - Important bridge between classical automated design and modern agentic closed-loop research.

- **2026** — ★ *Autodata: An Agentic Data Scientist to Create High Quality Synthetic Data*. https://arxiv.org/abs/2606.25996
  - Agent creates training/evaluation data and meta-optimizes the data-creation process itself.
  - Useful for the transition `data generation → data-policy improvement → improving the data improver`.

### Already strongly covered in our library, but emphasized by the survey

- **2025** — *AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery*. https://arxiv.org/abs/2506.13131
- **2026** — *PostTrainBench: Can LLM Agents Automate LLM Post-Training?*. https://arxiv.org/abs/2603.08640
- **2026** — *Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering*. https://arxiv.org/abs/2607.28568

These should be discussed as modern descendants of earlier NAS / learned-optimizer / program-search ideas, rather than as an isolated agent-only literature.

## C. Harness optimization and self-modification

- **2026** — ★ *HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry*. https://arxiv.org/abs/2606.14249
  - Treats prompts, tools, memory, and control flow as a composable optimization object.
  - Particularly useful for separating **model improvement** from **runtime/harness improvement**.

- **2026** — ★ *Recursive Harness Self-Improvement*. https://arxiv.org/abs/2607.15524
  - Iteratively refines a prompt-level harness specification from pairwise feedback over its own revision history.
  - Explicitly motivates **harness-in-the-loop learning**, where improved traces can later train improved models.

- **2026** — *Meta-Harness: End-to-End Optimization of Model Harnesses*. https://arxiv.org/abs/2603.28052
  - Already covered; retain as the key example of **external optimization of harness source code**.

- **2026** — *Self-Harness: Harnesses That Improve Themselves*. https://arxiv.org/abs/2606.09498
  - Already covered; retain as the key transition from external harness search to **self-modifying harnesses**.

## D. Improving the improvement process

- **2026** — ★ *MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution*. https://arxiv.org/abs/2607.05297
  - Fast loop improves task skills; slow loop improves the **meta-skill that performs improvement**.
  - A clean example of the distinction between `improving what the agent does` and `improving how the agent improves`.

- **2026** — ★ *Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization*. https://arxiv.org/abs/2604.23472
  - Co-evolves task agents and optimizer agents; task performance becomes evidence for improving the optimizer population.
  - Useful for our final transition from **artifact evolution** to **improver evolution**.

- **2026** — ★ *Bilevel Autoresearch: Meta-Autoresearching Itself*. https://arxiv.org/abs/2603.23420
  - Outer research loop modifies the mechanisms used by an inner research loop.
  - Important as a minimal, conceptually clear bilevel form of `research about how to research`.

## E. Evaluation concepts worth importing, without adopting their whole taxonomy

The preprint proposes five dimensions for AI4AI claims:

1. **Target** — what is improved.
2. **Self-reference** — whether the acting system is itself a target.
3. **Stage ownership** — who controls goal, plan, execution, feedback, and repair.
4. **Signal grounding** — executable verifier, held-out metric, learned judge, self-judgment, etc.
5. **Improvement evidence** — measured gain, retention, matched-human comparison, held-out transfer.

For our comprehensive historical review, these are best used as an **evaluation overlay** across eras rather than as the narrative skeleton.

Example:

| Era | Typical target | Self-reference | Human ownership | Feedback |
|---|---|---|---|---|
| HPO / classical AutoML | configuration / pipeline | no | objective + search space | validation metric |
| NAS | architecture | no | search grammar + metric | trained-model performance |
| learned optimizer / meta-learning | optimizer / adaptation rule | partial | task family + meta-objective | cross-task performance |
| program / algorithm discovery | executable algorithm | no/partial | evaluator + edit surface | execution / formal score |
| agentic AI development | code / data / experiments / model | sometimes | goal + evaluator often human-fixed | execution + benchmark |
| harness / improver evolution | workflow / harness / improver | yes | evaluator usually still fixed | execution + regression / transfer |

## F. Main takeaway for our review

The strongest citation-level contribution of this preprint is its evidence discipline around **closure, ownership, reliability, retention, and transfer**. Our review should absorb those evaluation questions while retaining a broader historical thesis:

> **AI4AI did not begin with long-horizon agents. It evolves from automated search over human-defined AI choices, through automated design and learned optimization, toward open-ended agentic research and finally the optimization of the improver itself.**

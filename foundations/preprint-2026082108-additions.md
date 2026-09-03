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

## G. References recovered by the post-survey gap audit

The companion survey/catalog is useful for discovering late-stage references that were not yet represented in our repository. The following are especially relevant because they change the **optimized object** rather than merely adding a generic agent capability.

### Skills, context, memory, and harnesses as learnable AI artifacts

- **2026** — ★ *Meta Context Engineering via Agentic Skill Evolution*. https://arxiv.org/abs/2601.21557
  - A bi-level loop evolves context-engineering skills while a base agent optimizes context artifacts.
- **2026** — *MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents*. https://arxiv.org/abs/2602.02474
  - Makes memory operations themselves selectable and evolvable skills.
- **2026** — ★ *SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning*. https://arxiv.org/abs/2602.08234
  - Couples persistent skill discovery with recursive policy improvement.
- **2026** — ★ *Memento-Skills: Let Agents Design Agents*. https://arxiv.org/abs/2603.18743
  - A generalist agent constructs and adapts task-specific agents using persistent prompts, skills, and memory.
- **2026** — *SkillOS: Learning Skill Curation for Self-Evolving Agents*. https://arxiv.org/abs/2605.06614
  - Makes skill selection/curation an adaptive component rather than a hand-coded library operation.
- **2026** — ★ *SkillOpt: Executive Strategy for Self-Evolving Agent Skills*. https://arxiv.org/abs/2605.23904
  - Treats natural-language skills as trainable external state optimized through rollout and validation.
- **2026** — *MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation*. https://arxiv.org/abs/2605.27366
  - Treats skills as long-lived assets with creation, reuse, testing, refinement, and transfer.
- **2026** — *You Live More Than Once: Towards Hierarchical Skill Meta-Evolving*. https://arxiv.org/abs/2605.28390
  - Moves from isolated skills toward hierarchical skill/meta-skill evolution.
- **2026** — *SkillOpt-Lite: Better and Faster Agent Self-evolution via One Line of Vibe*. https://arxiv.org/abs/2607.03451
  - Studies the minimal optimization machinery necessary for skill evolution.
- **2026** — ★ *Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents*. https://arxiv.org/abs/2607.12790
  - Particularly important because the **evaluator** becomes part of the evolutionary loop instead of remaining fixed.

### Retention and safety of persistent self-improvement

- **2026** — ★ *Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation*. https://arxiv.org/abs/2605.09315
  - Shows that improvement can be non-monotonic across workflow, skill, model, and memory evolution; motivates explicit retention tests.
- **2026** — *The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory*. https://arxiv.org/abs/2606.31121
  - Selective-update control for persistent memory evolution.

### AI-research and MLE loops missing from the earlier staging list

- **2026** — ★ *Towards Execution-Grounded Automated AI Research*. https://arxiv.org/abs/2601.14525
  - Converts LLM pre-training and post-training research into executable search environments and learns from measured experimental outcomes.
- **2026** — *Learning to Ideate for Machine Learning Engineering Agents*. https://arxiv.org/abs/2601.17596
  - Explicitly optimizes the ideation process that proposes ML-engineering improvements.
- **2026** — *TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration*. https://arxiv.org/abs/2604.14116
  - Adds an agent-driven exploration loop over the fine-tuning lifecycle.
- **2026** — *EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management*. https://arxiv.org/abs/2606.03841
  - Connects data-science automation with persistent skill learning and context adaptation.

## H. Post-survey August 2026 additions

These papers appeared after the survey/catalog freeze or after its initial bibliography was assembled, so they are especially important for keeping our review current.

- **2026-08** — ★ *AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses*. https://arxiv.org/abs/2608.12307
  - A strong model improves a weaker frozen model by **building its inference harness**, creating a test-time AI-for-AI transfer axis distinct from weight distillation.
- **2026-08** — ★ *Agent Lightning v1.0: Towards Harnessed Agentic RL*. https://arxiv.org/abs/2608.17528
  - Bridges harness design and model post-training by explicitly treating the deployment harness as part of the RL training interface.
- **2026-08** — ★ *AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement*. https://arxiv.org/abs/2608.20318
  - Direct benchmark of training-algorithm redesign; highly aligned with our definition of recursive AI4AI.
- **2026-08** — ★ *Prime Agent: A Self-Improving RLM Harness*. https://arxiv.org/abs/2608.23552
  - Persistent long-horizon harness with recursive subagents and reusable histories, skills, prompts, and computation.
- **2026-08** — ★ *Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents*. https://arxiv.org/abs/2608.15071
  - Compiles execution experience into reusable harness skills around a frozen model.
- **2026-08** — *Self-Evolving Embodied Agents via Skill-Harness Evolution*. https://arxiv.org/abs/2608.11350
  - Embodied setting, but useful evidence that skill+harness co-evolution transfers beyond coding/research agents.
- **2026-08** — ★ *Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents*. https://arxiv.org/abs/2608.12851
  - Makes persistent-adaptation safety a first-class evaluation issue: a successful but unsafe trajectory can become reusable future policy.

### Adjacent harness foundation worth tracking separately

- **2026-08** — *Context as an Environment: Programmatic Context Management for Long-Horizon Agents*. https://arxiv.org/abs/2608.21690
  - Not core AI4AI by itself, but important as a programmable context substrate on which self-improving harnesses can operate.

## I. Updated narrative implication

The missing-paper audit strengthens a more precise late-stage progression:

`prompt/workflow optimization → harness optimization → persistent skill optimization → skill/harness co-evolution → evaluator/retention co-evolution → model–harness joint improvement → algorithm-level recursive AI4AI`.

This is useful for distinguishing our comprehensive review from an agent-only survey: the modern harness/skill literature is the newest stage of a much longer trajectory that begins with algorithm selection, HPO, AutoML, NAS, meta-learning, and program search.

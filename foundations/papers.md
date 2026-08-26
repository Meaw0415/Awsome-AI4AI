# AI4AI Paper Library

A living paper list for **AI for AI (AI4AI)**. The emphasis is conceptual coverage rather than exhaustive application-specific AutoML.

Legend: **★** = especially important for the survey narrative.

---

# 1. Algorithm Selection, Configuration & Early AutoML

## Foundations

- **1976** — *The Algorithm Selection Problem* — Rice. Foundational formulation of choosing algorithms based on problem characteristics.
- **1998** — *Sequential Model-Based Optimization for General Algorithm Configuration* precursors / algorithm configuration literature.
- **2003** — *Metalearning: Applications to Data Mining* — early meta-learning / algorithm recommendation lineage.
- **2009** — *ParamILS: An Automatic Algorithm Configuration Framework* — Hutter et al. Automated configuration of algorithm parameters. https://www.cs.ubc.ca/labs/algorithms/Projects/ParamILS/
- **2011** — ★ *Algorithms for Hyper-Parameter Optimization* — Bergstra et al. TPE and modern HPO framing. https://proceedings.neurips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html
- **2011** — *Sequential Model-Based Optimization for General Algorithm Configuration (SMAC)* — Hutter et al. Core model-based configuration method. https://www.cs.ubc.ca/labs/algorithms/Projects/SMAC/
- **2012** — *Random Search for Hyper-Parameter Optimization* — Bergstra & Bengio. https://jmlr.org/papers/v13/bergstra12a.html
- **2013** — ★ *Auto-WEKA: Combined Selection and Hyperparameter Optimization of Classification Algorithms* — Thornton et al. CASH formulation. https://arxiv.org/abs/1208.3719
- **2015** — ★ *Efficient and Robust Automated Machine Learning* — auto-sklearn. Feurer et al. Meta-learning + Bayesian optimization + ensembles. https://proceedings.neurips.cc/paper/2015/hash/11d0e6287202fced83f79975ec59a3a6-Abstract.html
- **2016** — *TPOT: A Tree-based Pipeline Optimization Tool for Automating Machine Learning* — Olson et al. Genetic programming for ML pipelines. https://proceedings.mlr.press/v64/olson_tpot_2016.html
- **2016** — *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization* — Li et al. Multi-fidelity resource allocation. https://arxiv.org/abs/1603.06560
- **2016** — *Taking the Human Out of the Loop: A Review of Bayesian Optimization* — Shahriari et al. https://ieeexplore.ieee.org/document/7352306
- **2017** — *BOHB: Robust and Efficient Hyperparameter Optimization at Scale* — Falkner et al. Bayesian optimization + Hyperband. https://arxiv.org/abs/1807.01774
- **2017** — *Google Vizier: A Service for Black-Box Optimization* — Golovin et al. Industrial-scale optimization service. https://dl.acm.org/doi/10.1145/3097983.3098043
- **2018** — *Auto-Keras: Efficient Neural Architecture Search with Network Morphism* — Jin et al. https://arxiv.org/abs/1806.10282
- **2019** — ★ *Automated Machine Learning: Methods, Systems, Challenges* — Hutter, Kotthoff, Vanschoren (eds.). https://www.automl.org/book/
- **2020** — *AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data* — Erickson et al. https://arxiv.org/abs/2003.06505
- **2020** — *Auto-Sklearn 2.0: Hands-free AutoML via Meta-Learning* — Feurer et al. https://arxiv.org/abs/2007.04074
- **2021** — *FLAML: A Fast and Lightweight AutoML Library* — Wang et al. Cost-effective AutoML. https://arxiv.org/abs/1911.04706

# 2. Neural Architecture Search (NAS)

## Reinforcement learning / evolutionary NAS

- **2016/2017** — ★ *Neural Architecture Search with Reinforcement Learning* — Zoph & Le. https://arxiv.org/abs/1611.01578
- **2017** — *Designing Neural Network Architectures using Reinforcement Learning* — Baker et al. https://arxiv.org/abs/1611.02167
- **2017** — *Large-Scale Evolution of Image Classifiers* — Real et al. Evolutionary architecture search. https://arxiv.org/abs/1703.01041
- **2017** — *Learning Transferable Architectures for Scalable Image Recognition* — NASNet. https://arxiv.org/abs/1707.07012
- **2018** — *Regularized Evolution for Image Classifier Architecture Search* — AmoebaNet. https://arxiv.org/abs/1802.01548
- **2018** — *Efficient Neural Architecture Search via Parameter Sharing* — ENAS. https://arxiv.org/abs/1802.03268

## Differentiable / efficient NAS

- **2018** — ★ *DARTS: Differentiable Architecture Search* — Liu et al. https://arxiv.org/abs/1806.09055
- **2018** — *ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware* — Cai et al. https://arxiv.org/abs/1812.00332
- **2019** — *MnasNet: Platform-Aware Neural Architecture Search for Mobile* — Tan et al. https://arxiv.org/abs/1807.11626
- **2019** — *FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable NAS* — Wu et al. https://arxiv.org/abs/1812.03443
- **2019** — *Once-for-All: Train One Network and Specialize it for Efficient Deployment* — Cai et al. https://arxiv.org/abs/1908.09791
- **2019** — *Single Path One-Shot Neural Architecture Search with Uniform Sampling* — Guo et al. https://arxiv.org/abs/1904.00420
- **2020** — *PC-DARTS: Partial Channel Connections for Memory-Efficient Architecture Search* — Xu et al. https://arxiv.org/abs/1907.05737
- **2020** — *DrNAS: Dirichlet Neural Architecture Search* — Chen et al. https://arxiv.org/abs/2006.10355

## NAS foundations / analysis

- **2019** — *Neural Architecture Search: A Survey* — Elsken et al. https://arxiv.org/abs/1808.05377
- **2020** — *Understanding Architectures Learnt by Cell-based Neural Architecture Search* and related NAS-analysis work.
- **2020** — *NAS-Bench-201: Extending the Scope of Reproducible NAS* — Dong & Yang. https://arxiv.org/abs/2001.00326

# 3. Automated Algorithm Discovery, Program Search & Training-Rule Discovery

- **2017** — *Learning to Optimize Neural Nets* / learned optimizer family — optimizer itself becomes learned.
- **2018** — *Neural Optimizer Search with Reinforcement Learning* — automated optimizer discovery. https://arxiv.org/abs/1709.07417
- **2018** — *Learning to Teach with Dynamic Loss Functions* — automated learning objective design lineage.
- **2019** — *AutoAugment: Learning Augmentation Policies from Data* — Cubuk et al. https://arxiv.org/abs/1805.09501
- **2019** — *Population Based Augmentation* — Ho et al. https://arxiv.org/abs/1905.05393
- **2020** — ★ *AutoML-Zero: Evolving Machine Learning Algorithms From Scratch* — Real et al. Searches complete ML algorithms expressed as programs. https://arxiv.org/abs/2003.03384
- **2020** — *Discovering Neural Nets with Low Kolmogorov Complexity* / program-search approaches to architecture discovery.
- **2021** — *Symbolic Discovery of Optimization Algorithms* and related program-synthesis approaches to learned optimizers.
- **2022** — *VeLO: Training Versatile Learned Optimizers by Scaling Up* — Metz et al. https://arxiv.org/abs/2211.09760
- **2023** — ★ *FunSearch: Mathematical Discoveries from Program Search with Large Language Models* — Romera-Paredes et al. LLM-guided evolutionary program search. https://www.nature.com/articles/s41586-023-06924-6
- **2025** — ★ *AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery* — LLM-driven evolutionary code search, including improvements to computing infrastructure and algorithms. https://arxiv.org/abs/2506.13131

# 4. Meta-Learning, Learned Optimization & Population-Based Adaptation

- **1991–2000s** — early learning-to-learn / meta-learning literature.
- **2016** — ★ *Learning to Learn by Gradient Descent by Gradient Descent* — Andrychowicz et al. https://arxiv.org/abs/1606.04474
- **2016** — *RL²: Fast Reinforcement Learning via Slow Reinforcement Learning* — Duan et al. https://arxiv.org/abs/1611.02779
- **2017** — ★ *Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks (MAML)* — Finn et al. https://arxiv.org/abs/1703.03400
- **2017** — *Population Based Training of Neural Networks* — Jaderberg et al. Online adaptation of parameters and hyperparameters. https://arxiv.org/abs/1711.09846
- **2018** — *Reptile: A Scalable Metalearning Algorithm* — Nichol et al. https://arxiv.org/abs/1803.02999
- **2018** — *Learning to Reinforcement Learn* — meta-RL lineage.
- **2019** — *Meta-Learning with Implicit Gradients* / scalable gradient-based meta-learning.
- **2020** — *Meta-Learning in Neural Networks: A Survey*. https://arxiv.org/abs/2004.05439
- **2022** — ★ *VeLO: Training Versatile Learned Optimizers by Scaling Up*. https://arxiv.org/abs/2211.09760

# 5. LLMs as Optimizers, Search Operators & Prompt/Reward Designers

## Prompt optimization

- **2022** — *Large Language Models Are Human-Level Prompt Engineers* — APE / Automatic Prompt Engineer. https://arxiv.org/abs/2211.01910
- **2023** — ★ *Large Language Models as Optimizers (OPRO)* — Yang et al. Natural-language optimization loop. https://arxiv.org/abs/2309.03409
- **2023** — *Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution* — Fernando et al. https://arxiv.org/abs/2309.16797
- **2023** — *Automatic Prompt Optimization with Gradient Descent and Beam Search* / ProTeGi. https://arxiv.org/abs/2305.03495
- **2024** — *TextGrad: Automatic Differentiation via Text* — textual feedback as gradients for optimization. https://arxiv.org/abs/2406.07496
- **2024** — *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines* — automated LM program optimization. https://arxiv.org/abs/2310.03714

## Reward / objective discovery

- **2023** — ★ *Eureka: Human-Level Reward Design via Coding Large Language Models* — Ma et al. Evolutionary reward-function generation. https://arxiv.org/abs/2310.12931
- **2024** — *DrEureka: Language Model Guided Sim-to-Real Transfer* — automatic reward/domain randomization design. https://arxiv.org/abs/2406.01967
- **2024** — *Language to Rewards for Robotic Skill Synthesis* and related LLM reward-generation work.

## Algorithm / heuristic discovery

- **2023** — ★ *FunSearch*. https://www.nature.com/articles/s41586-023-06924-6
- **2024** — *Evolution through Large Models* / LLM-guided evolutionary algorithm-design lineage.
- **2025** — ★ *AlphaEvolve*. https://arxiv.org/abs/2506.13131
- **2026** — *Large Language Models as Optimizers: A Survey of Direct vs. Tool-Augmented Approaches and Their Performance Frontiers*. https://arxiv.org/abs/2606.15577

# 6. General Agent Foundations Relevant to AI4AI

These are not specifically AI4AI, but provide mechanisms heavily reused by research agents.

- **2022** — ★ *ReAct: Synergizing Reasoning and Acting in Language Models* — Yao et al. https://arxiv.org/abs/2210.03629
- **2023** — *Reflexion: Language Agents with Verbal Reinforcement Learning* — Shinn et al. https://arxiv.org/abs/2303.11366
- **2023** — *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* — Yao et al. https://arxiv.org/abs/2305.10601
- **2023** — *Voyager: An Open-Ended Embodied Agent with Large Language Models* — lifelong skill library and automatic curriculum. https://arxiv.org/abs/2305.16291
- **2023** — *Generative Agents: Interactive Simulacra of Human Behavior* — memory/reflection/planning architecture. https://arxiv.org/abs/2304.03442
- **2023** — *Toolformer: Language Models Can Teach Themselves to Use Tools* — Schick et al. https://arxiv.org/abs/2302.04761
- **2024** — *Self-Discover: Large Language Models Self-Compose Reasoning Structures* — adaptive reasoning structures. https://arxiv.org/abs/2402.03620

# 7. Autonomous ML Engineering Agents

- **2023** — ★ *MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation* — Huang et al. Agent reads/writes files, runs experiments, observes metrics, iterates. https://arxiv.org/abs/2310.03302
- **2024** — ★ *MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering* — 75 Kaggle competitions. https://arxiv.org/abs/2410.07095
- **2024** — ★ *AIDE: AI-Driven Exploration in the Space of Code* — tree-search-like iterative code generation/evaluation scaffold used strongly on MLE-bench. https://github.com/WecoAI/aideml
- **2024/2025** — ★ *RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts* — realistic open-ended AI R&D environments. https://arxiv.org/abs/2411.15114
- **2025–2026** — MLE-bench agent systems and harnesses including increasingly explicit experiment memory, candidate populations, code-evolution, planning, and resource allocation; track leaderboard systems separately from peer-reviewed methodology.

# 8. AI Research Agents / AI Scientists

## Literature, ideation and research planning

- **2023** — *ResearchRabbit / Semantic Scholar-style retrieval agents* are useful tooling precursors but not autonomous researchers.
- **2024** — ★ *ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models* — literature-grounded research ideation. https://arxiv.org/abs/2404.07738
- **2024** — *SciMON: Scientific Inspiration Machines Optimized for Novelty* — scientific idea generation / novelty-oriented systems lineage.
- **2024** — *MOOSE: A Multi-Agent Framework for Open-Ended Scientific Discovery* and related hypothesis-generation agents.

## End-to-end AI scientist systems

- **2024** — ★ *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery* — Lu et al., Sakana AI. Idea generation, coding, experiments, paper writing, automated review. https://arxiv.org/abs/2408.06292
- **2024/2025** — ★ *Agent Laboratory: Using LLM Agents as Research Assistants* — multi-agent research workflow spanning literature review, experimentation and writing. https://arxiv.org/abs/2501.04227
- **2025** — ★ *Towards an AI Co-Scientist* — multi-agent scientific reasoning and hypothesis generation system. https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/
- **2025** — *AI-Researcher / Scientist-agent systems* — a growing family of systems automating ideation → experiment → writing loops.
- **2025** — ★ *PaperBench: Evaluating AI's Ability to Replicate AI Research* — although a benchmark, it strongly shapes the definition of end-to-end research capability. https://openai.com/index/paperbench/

# 9. Self-Improving, Evolutionary & Open-Ended Agents

- **2017** — ★ *Population Based Training of Neural Networks* — population-level continual adaptation. https://arxiv.org/abs/1711.09846
- **2019** — *POET: Paired Open-Ended Trailblazer* — co-evolution of environments and agents; important open-endedness precursor. https://arxiv.org/abs/1901.01753
- **2021** — *Open-Ended Learning Leads to Generally Capable Agents* — DeepMind XLand. https://arxiv.org/abs/2107.12808
- **2023** — ★ *Promptbreeder* — prompt-level self-referential evolution. https://arxiv.org/abs/2309.16797
- **2023** — *Voyager* — curriculum + skill-library accumulation. https://arxiv.org/abs/2305.16291
- **2023** — ★ *FunSearch* — evolutionary population + LLM code generation + evaluator. https://www.nature.com/articles/s41586-023-06924-6
- **2025** — ★ *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents* — self-modifying agents where modifications are validated empirically. https://arxiv.org/abs/2505.22954
- **2025** — ★ *AlphaEvolve* — evolutionary coding agent that can improve algorithms and parts of AI infrastructure. https://arxiv.org/abs/2506.13131

# 10. World Models, Experience Models & Learned Research Dynamics

This is the most speculative but potentially most important bridge to the next generation of AI4AI.

## World-model foundations

- **2018** — ★ *World Models* — Ha & Schmidhuber. Learn compact predictive dynamics for planning/control. https://arxiv.org/abs/1803.10122
- **2020** — *Dreamer: Reinforcement Learning with Latent Dynamics Models* — model-based planning via learned latent dynamics. https://arxiv.org/abs/1912.01603
- **2023** — *Mastering Diverse Domains through World Models (DreamerV3)* — Hafner et al. https://arxiv.org/abs/2301.04104

## Agent / research world models

- **2025–2026** — emerging work on **agent world models**, **experience models**, and learned predictions of action outcomes for long-horizon agents.
- **AAWM / Agent-Aware World Model** — track as relevant to learned agent-environment dynamics and research-action prediction.

The key AI4AI question is not only whether we can predict an environment observation, but whether we can learn:

> `research_state + proposed_experiment -> result + belief_change + future_research_value`.

This differs from conventional world models because the latent state must include both **artifacts** and **epistemic beliefs**.

# 11. Scientific Discovery Agents Outside AI Research

These are useful because they often solve harder evidence-grounding problems than current AI-research agents.

- **2023–2026** — autonomous chemistry laboratories / self-driving labs.
- **2023–2026** — LLM agents for materials discovery.
- **2024–2026** — biomedical hypothesis generation and experimental agents.
- **2025** — *From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery*. https://arxiv.org/abs/2508.14111

For this survey, these should be used primarily as **methodological analogues** for experimental planning, physical feedback, uncertainty, and evidence-based iteration rather than treated as the main scope.

# 12. Evaluation, Verification & Scientific Reliability

- **2024** — *MLE-bench* — performance-oriented ML engineering evaluation. https://arxiv.org/abs/2410.07095
- **2024/2025** — *RE-Bench* — AI-R&D progress under realistic time budgets, with expert comparison. https://arxiv.org/abs/2411.15114
- **2025** — *PaperBench* — research replication and rubric-based grading. https://openai.com/index/paperbench/
- **2026** — *Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap* — argues that producing research artifacts and verifying claims are different capabilities. https://arxiv.org/abs/2608.05179

# 13. Candidate conceptual families for the survey

Rather than grouping only by chronology, we should eventually code every paper with the following columns:

| Field | Meaning |
|---|---|
| Year | publication/preprint year |
| Automation target | HPO / architecture / algorithm / code / experiment / hypothesis / full research |
| Search representation | vector / graph / program / natural language / repository / research state |
| Proposal mechanism | BO / RL / evolution / gradient / LLM / multi-agent / world model |
| Feedback | validation metric / runtime / execution / judge / experimental evidence |
| Memory | none / archive / meta-features / trajectory memory / learned state |
| Adaptation level | per-task / cross-task / continual / self-modifying |
| Human scaffolding | fixed pipeline / configurable harness / agent-authored |
| Evaluation horizon | single evaluation / episode / competition / multi-hour research / paper |
| Reproducibility | code / data / traces / seeds / complete artifacts |

This coding scheme can later become the central quantitative table/figure of the survey.

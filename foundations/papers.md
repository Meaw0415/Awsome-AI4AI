# AI4AI Paper Library

A living bibliography for **AI for AI (AI4AI)**: AI systems that **improve, construct, train, optimize, evaluate, redesign, or evolve another AI system — or themselves**.

This definition is intentionally broader than any one application label. **AutoML, NAS, MLE agents, AI-research agents, post-training agents, harness optimizers, and self-evolving agents are downstream manifestations of the same AI4AI idea**, not mutually exclusive top-level fields.

**Inclusion rule.** A paper is core AI4AI when the optimized object is an AI artifact or the process that creates/improves AI: data, features, architecture, hyperparameters, optimizer, objective/reward, algorithm/program, training recipe, model weights, prompt, workflow, agent harness, evaluator, or the improvement mechanism itself.

**Scope cleanup in this revision.**

- Generic **world-model** papers are removed: predictive environment modeling is not AI4AI unless it is explicitly used to improve an AI system or its improver.
- Generic agent foundations such as ReAct / Tree-of-Thoughts / generic tool-use are not listed merely because later AI4AI agents use them.
- **Research agent** and **MLE agent** are not used as primary taxonomy branches. A research agent stays only when it automates or improves AI/ML research/development; an MLE agent stays because ML engineering is one AI4AI target.
- The organization below follows the **developmental paradigms of AI4AI**, from fixed search spaces to recursive/meta-evolution.

Legend: **★** = especially important for the survey narrative / timeline figure.

---

# 0. Survey anchors used to check coverage

These surveys/books are useful for checking whether the paper list is missing important lineages.

## AutoML / NAS / ML workflow automation

- **2019** — ★ *Automated Machine Learning: Methods, Systems, Challenges* — Hutter, Kotthoff, Vanschoren (eds.). https://www.automl.org/book/
- **2019** — *Neural Architecture Search: A Survey* — Elsken et al. https://arxiv.org/abs/1808.05377
- **2023** — ★ *AutoML in the Age of Large Language Models: Current Challenges, Future Opportunities and Risks*. https://arxiv.org/abs/2306.08107
- **2024** — *Automated Machine Learning: Past, Present and Future*. https://link.springer.com/article/10.1007/s10462-024-10726-1
- **2024** — *Advances in Neural Architecture Search*. https://academic.oup.com/nsr/article/11/8/nwae282/7740455
- **2024** — ★ *Large Language Models for Constructing and Optimizing Machine Learning Workflows: A Survey*. https://arxiv.org/abs/2411.10478
- **2025** — *Systematic Review on Neural Architecture Search*. https://link.springer.com/article/10.1007/s10462-024-11058-w
- **2025/26** — *A Literature Review on Automated Machine Learning*. https://link.springer.com/article/10.1007/s10462-025-11397-2

## Evolutionary / self-improving AI

- **2024** — *Evolutionary Computation in the Era of Large Language Model: Survey and Roadmap*. https://arxiv.org/abs/2401.10034
- **2026** — ★ *A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence* — TMLR. https://arxiv.org/abs/2507.21046
- **2026** — ★ *Self-Improving Agents in the Era of Experience: A Survey of Self- to Meta-Evolution*. https://openreview.net/forum?id=IUltZSgLMm
- **2026** — *Self-Improvements in Modern Agentic Systems: A Survey*. https://arxiv.org/abs/2607.13104
- **2026** — *Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops*. https://arxiv.org/abs/2607.07663
- **2026** — *Automated Design of Agentic Systems: A Survey of Algorithms for Searching, Optimizing, and Evolving LLM Agents, Workflows, and Prompts*. https://www.preprints.org/manuscript/202606.0238

---

# 1. Paradigm I — Search over explicit configurations: Algorithm Selection, HPO & Classical AutoML

**Core idea:** define a human-specified search/configuration space and let an optimizer choose a better ML configuration.

- **1976** — ★ *The Algorithm Selection Problem* — Rice. Foundational algorithm-selection formulation.
- **2009** — *ParamILS: An Automatic Algorithm Configuration Framework*. https://www.cs.ubc.ca/labs/algorithms/Projects/ParamILS/
- **2011** — ★ *Algorithms for Hyper-Parameter Optimization* — TPE. https://proceedings.neurips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html
- **2011** — *Sequential Model-Based Optimization for General Algorithm Configuration (SMAC)*. https://www.cs.ubc.ca/labs/algorithms/Projects/SMAC/
- **2012** — *Random Search for Hyper-Parameter Optimization*. https://jmlr.org/papers/v13/bergstra12a.html
- **2013** — ★ *Auto-WEKA: Combined Selection and Hyperparameter Optimization of Classification Algorithms*. https://arxiv.org/abs/1208.3719
- **2015** — ★ *Efficient and Robust Automated Machine Learning* — auto-sklearn. https://proceedings.neurips.cc/paper/2015/hash/11d0e6287202fced83f79975ec59a3a6-Abstract.html
- **2016** — *TPOT: A Tree-based Pipeline Optimization Tool for Automating Machine Learning*. https://proceedings.mlr.press/v64/olson_tpot_2016.html
- **2016** — *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*. https://arxiv.org/abs/1603.06560
- **2017** — *BOHB: Robust and Efficient Hyperparameter Optimization at Scale*. https://arxiv.org/abs/1807.01774
- **2017** — *Google Vizier: A Service for Black-Box Optimization*. https://dl.acm.org/doi/10.1145/3097983.3098043
- **2020** — *AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data*. https://arxiv.org/abs/2003.06505
- **2020** — *Auto-Sklearn 2.0: Hands-free AutoML via Meta-Learning*. https://arxiv.org/abs/2007.04074
- **2021** — *FLAML: A Fast and Lightweight AutoML Library*. https://arxiv.org/abs/1911.04706

**Paradigm shift:** optimization moves from choosing among hand-designed configurations to **designing the structures and learning rules themselves**.

---

# 2. Paradigm II — Search over structures: NAS, Pipelines & Architecture Construction

**Core idea:** expand the optimization target from hyperparameters to the structure of the AI model or pipeline.

## RL / evolutionary NAS

- **2016/17** — ★ *Neural Architecture Search with Reinforcement Learning* — Zoph & Le. https://arxiv.org/abs/1611.01578
- **2017** — *Designing Neural Network Architectures using Reinforcement Learning*. https://arxiv.org/abs/1611.02167
- **2017** — *Large-Scale Evolution of Image Classifiers*. https://arxiv.org/abs/1703.01041
- **2017** — *Learning Transferable Architectures for Scalable Image Recognition* — NASNet. https://arxiv.org/abs/1707.07012
- **2018** — *Regularized Evolution for Image Classifier Architecture Search* — AmoebaNet. https://arxiv.org/abs/1802.01548
- **2018** — *Efficient Neural Architecture Search via Parameter Sharing* — ENAS. https://arxiv.org/abs/1802.03268

## Differentiable / efficient NAS

- **2018** — ★ *DARTS: Differentiable Architecture Search*. https://arxiv.org/abs/1806.09055
- **2018** — *ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware*. https://arxiv.org/abs/1812.00332
- **2019** — *MnasNet: Platform-Aware Neural Architecture Search for Mobile*. https://arxiv.org/abs/1807.11626
- **2019** — *FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable NAS*. https://arxiv.org/abs/1812.03443
- **2019** — *Once-for-All: Train One Network and Specialize it for Efficient Deployment*. https://arxiv.org/abs/1908.09791
- **2019** — *Single Path One-Shot Neural Architecture Search with Uniform Sampling*. https://arxiv.org/abs/1904.00420
- **2020** — *PC-DARTS: Partial Channel Connections for Memory-Efficient Architecture Search*. https://arxiv.org/abs/1907.05737
- **2020** — *DrNAS: Dirichlet Neural Architecture Search*. https://arxiv.org/abs/2006.10355
- **2020** — *NAS-Bench-201: Extending the Scope of Reproducible NAS*. https://arxiv.org/abs/2001.00326

## LLM-assisted architecture / pipeline search

- **2024** — ★ *AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML*. https://arxiv.org/abs/2410.02958
- **2024** — *AutoM3L: An Automated Multimodal Machine Learning Framework with Large Language Models*. https://arxiv.org/abs/2408.00665
- **2025** — *Design Principle Transfer in Neural Architecture Search via Large Language Models* — AAAI 2025. https://ojs.aaai.org/index.php/AAAI/article/view/34463
- **2025** — *LM-Searcher: Cross-domain Neural Architecture Search with LLMs via Unified Numerical Encoding* — EMNLP 2025. https://aclanthology.org/2025.emnlp-main.478/

**Paradigm shift:** instead of searching only a fixed structure space, AI begins to **learn how to improve AI** and to generate new optimization rules/programs.

---

# 3. Paradigm III — Learning the improver: Meta-Learning, Learned Optimizers & Population Adaptation

**Core idea:** the improvement rule itself becomes learned or adaptive rather than fixed.

- **2016** — ★ *Learning to Learn by Gradient Descent by Gradient Descent*. https://arxiv.org/abs/1606.04474
- **2016** — *RL²: Fast Reinforcement Learning via Slow Reinforcement Learning*. https://arxiv.org/abs/1611.02779
- **2017** — ★ *Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks (MAML)*. https://arxiv.org/abs/1703.03400
- **2017** — ★ *Population Based Training of Neural Networks*. https://arxiv.org/abs/1711.09846
- **2017/18** — *Neural Optimizer Search with Reinforcement Learning*. https://arxiv.org/abs/1709.07417
- **2018** — *Reptile: A Scalable Metalearning Algorithm*. https://arxiv.org/abs/1803.02999
- **2018** — *Learning to Teach with Dynamic Loss Functions* — automated objective design lineage.
- **2020** — *Meta-Learning in Neural Networks: A Survey*. https://arxiv.org/abs/2004.05439
- **2022** — ★ *VeLO: Training Versatile Learned Optimizers by Scaling Up*. https://arxiv.org/abs/2211.09760

**Paradigm shift:** the target expands from parameters/architectures to **algorithms, objectives, rewards, and executable programs**.

---

# 4. Paradigm IV — Automated discovery of algorithms, objectives, data policies & programs

**Core idea:** AI proposes executable artifacts and receives objective feedback; the searched object can be a learning algorithm, reward, augmentation policy, program, or training-data policy.

## Training rules / objectives / data policies

- **2019** — *AutoAugment: Learning Augmentation Policies from Data*. https://arxiv.org/abs/1805.09501
- **2019** — *Population Based Augmentation*. https://arxiv.org/abs/1905.05393
- **2020** — ★ *AutoML-Zero: Evolving Machine Learning Algorithms From Scratch*. https://arxiv.org/abs/2003.03384
- **2023** — ★ *Eureka: Human-Level Reward Design via Coding Large Language Models*. https://arxiv.org/abs/2310.12931
- **2024** — *DrEureka: Language Model Guided Sim-to-Real Transfer*. https://arxiv.org/abs/2406.01967
- **2026** — *RF-Agent: Automated Reward Function Design via Language Agent Tree Search*. https://arxiv.org/abs/2602.23876
- **2026** — *Can Generalist Agents Automate Data Curation?* — closed-loop data policy → train/evaluate → revise. https://arxiv.org/abs/2606.04261
- **2026** — *Exploring Autonomous Agentic Data Engineering for Model Specialization*. https://arxiv.org/abs/2605.30407
- **2026** — *CurateEvo: Data-Curation Evolving for Agentic Post-Training*. https://arxiv.org/abs/2607.06140
- **2026** — *ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment*. https://arxiv.org/abs/2606.01279

## Program / algorithm evolution

- **2023** — ★ *FunSearch: Mathematical Discoveries from Program Search with Large Language Models* — Nature. https://www.nature.com/articles/s41586-023-06924-6
- **2025** — ★ *AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery*. https://arxiv.org/abs/2506.13131
- **2025/26** — ★ *ShinkaEvolve: Towards Open-Ended and Sample-Efficient Program Evolution* — ICLR 2026. https://arxiv.org/abs/2509.19349
- **2026** — *AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization*. https://arxiv.org/abs/2602.20133
- **2026** — ★ *MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery*. https://arxiv.org/abs/2606.06473

**Paradigm shift:** LLMs turn natural language/code generation into a general-purpose **optimization operator** over many AI artifacts.

---

# 5. Paradigm V — Language models as optimizers of prompts, programs & AI workflows

**Core idea:** replace hand-designed local search operators with language-model proposal + feedback loops.

## Prompt / instruction optimization

- **2022** — *Large Language Models Are Human-Level Prompt Engineers* — APE. https://arxiv.org/abs/2211.01910
- **2023** — *Automatic Prompt Optimization with Gradient Descent and Beam Search* — ProTeGi. https://arxiv.org/abs/2305.03495
- **2023** — ★ *Large Language Models as Optimizers (OPRO)*. https://arxiv.org/abs/2309.03409
- **2023** — ★ *Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution*. https://arxiv.org/abs/2309.16797
- **2024** — ★ *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines*. https://arxiv.org/abs/2310.03714
- **2024** — ★ *TextGrad: Automatic Differentiation via Text*. https://arxiv.org/abs/2406.07496
- **2025** — *GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning*. https://arxiv.org/abs/2507.19457

## From prompt optimization to agent-system optimization

- **2024** — ★ *Automated Design of Agentic Systems (ADAS)*. https://arxiv.org/abs/2408.08435
- **2024** — *GPTSwarm: Language Agents as Optimizable Graphs*. https://arxiv.org/abs/2402.16823
- **2024** — *AFlow: Automating Agentic Workflow Generation*. https://arxiv.org/abs/2410.10762
- **2024/25** — ★ *Symbolic Learning Enables Self-Evolving Agents*. https://arxiv.org/abs/2406.18532
- **2025** — *ScoreFlow: Mastering LLM Agent Workflows via Score-Based Preference Optimization*. https://arxiv.org/abs/2502.04306
- **2025** — *Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies*. https://arxiv.org/abs/2502.02533
- **2025** — *MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision*. https://arxiv.org/abs/2505.14996
- **2025** — *EvoAgentX: An Automated Framework for Evolving Agentic Workflows*. https://arxiv.org/abs/2507.03616
- **2025** — *SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence* — EMNLP 2025. https://aclanthology.org/2025.emnlp-main.93/

**Paradigm shift:** the optimization target becomes the **whole AI-development process**, with execution feedback and long-horizon agents closing the loop.

---

# 6. Paradigm VI — Agentic closed-loop AI development: from AutoML to AI4MLE / autonomous AI building

**Core idea:** an agent directly edits data/code/models, runs training/evaluation, reads real execution feedback, and iterates. This is the modern **AI4MLE / Agent4AI** branch.

## Early executable ML/data agents

- **2023/24** — ★ *MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation*. https://arxiv.org/abs/2310.03302
- **2024** — ★ *DS-Agent: Automated Data Science by Empowering LLMs with Case-Based Reasoning*. https://arxiv.org/abs/2402.17453
- **2024** — *Data Interpreter: An LLM Agent for Data Science*. https://arxiv.org/abs/2402.18679
- **2024** — *AutoAgents: Generating Specialized Agents for End-to-End Machine Learning Pipelines*. https://arxiv.org/abs/2410.03521
- **2024** — *AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions*. https://arxiv.org/abs/2410.20424
- **2024** — ★ *SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning*. https://arxiv.org/abs/2410.17238
- **2024** — *AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML*. https://arxiv.org/abs/2410.02958
- **2024** — *LAMBDA: A Large Model Based Data Agent*. https://arxiv.org/abs/2407.17535

## Search / refinement / memory for MLE

- **2025** — ★ *AIDE: AI-Driven Exploration in the Space of Code*. https://arxiv.org/abs/2502.13138
- **2025** — *I-MCTS: Enhancing Agentic AutoML via Introspective Monte Carlo Tree Search*. https://arxiv.org/abs/2502.14693
- **2025** — *MLZero: A Multi-Agent System for End-to-end Machine Learning Automation*. https://arxiv.org/abs/2505.13941
- **2025** — ★ *R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution*. https://arxiv.org/abs/2505.14738
- **2025** — ★ *ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering*. https://arxiv.org/abs/2505.23723
- **2025** — ★ *MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement*. https://arxiv.org/abs/2506.15692
- **2025** — ★ *ML-Master: Towards AI-for-AI via Integration of Exploration and Reasoning*. https://arxiv.org/abs/2506.16499
- **2025** — *AutoMind: Adaptive Knowledgeable Agent for Automated Data Science*. https://arxiv.org/abs/2506.10974
- **2025** — *AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench*. https://arxiv.org/abs/2507.02554
- **2025/26** — ★ *DataMind: Scaling Generalist Executable Data-Analytic Agents*. https://arxiv.org/abs/2509.25084

## 2026 AI4MLE: prediction, knowledge accumulation, self-evolution

- **2026** — *FOREAGENT: Can We Predict Before Executing Machine Learning Agents?* https://arxiv.org/abs/2601.05930
- **2026** — *ML-Master 2.0: Toward Ultra-Long-Horizon Agentic Science*. https://arxiv.org/abs/2601.10402
- **2026** — *Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search*. https://arxiv.org/abs/2603.01692
- **2026** — ★ *AIBuildAI: An AI Agent for Automatically Building AI Models*. https://arxiv.org/abs/2604.14455
- **2026** — ★ *AIBuildAI-2: A Knowledge-Enhanced Agent for Automatically Building AI Models*. https://arxiv.org/abs/2605.27873
- **2026** — *DataMaster: Data-Centric Autonomous AI Research*. https://arxiv.org/abs/2605.10906
- **2026** — ★ *MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery*. https://arxiv.org/abs/2606.06473
- **2026** — *Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering*. https://arxiv.org/abs/2606.30911

## Model training / post-training as an AI4AI target

- **2026** — *FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents*. https://arxiv.org/abs/2603.01712
- **2026** — *AceGRPO: Adaptive Curriculum Enhanced Group Relative Policy Optimization for Autonomous Machine Learning Engineering*. https://arxiv.org/abs/2602.07906
- **2026** — *Agent^2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?* https://arxiv.org/abs/2604.10547
- **2026** — ★ *AutoTrainess: Teaching Language Models to Improve Language Models Autonomously*. https://arxiv.org/abs/2606.31551
- **2026** — *ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment*. https://arxiv.org/abs/2606.01279

## Full-cycle AI research/development (included only when the target is AI/ML improvement)

- **2024** — ★ *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery* — its demonstrated loop includes automated ML research. https://arxiv.org/abs/2408.06292
- **2025** — *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*. https://arxiv.org/abs/2504.08066
- **2026** — *AIRA_2: Overcoming Bottlenecks in AI Research Agents*. https://arxiv.org/abs/2603.26499
- **2026** — *Toward Autonomous Long-Horizon Engineering for ML Research*. https://arxiv.org/abs/2604.13018
- **2026** — *Towards End-to-End Automation of AI Research*. https://arxiv.org/abs/2606.15497
- **2026** — *AlphaLab: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs*. https://arxiv.org/abs/2604.08590

**Paradigm shift:** the agent no longer only improves an external model/pipeline; its **own prompt, memory, tools, workflow, harness, and source code become optimization targets**.

---

# 7. Paradigm VII — AI designs and improves AI agents: Workflow, Harness & Runtime Optimization

**Core idea:** the AI system itself becomes an editable artifact. This is a more direct AI4AI loop than generic agent use.

## Workflow / topology evolution

- **2024** — ★ *Automated Design of Agentic Systems (ADAS)*. https://arxiv.org/abs/2408.08435
- **2024** — *GPTSwarm: Language Agents as Optimizable Graphs*. https://arxiv.org/abs/2402.16823
- **2024** — *AFlow: Automating Agentic Workflow Generation*. https://arxiv.org/abs/2410.10762
- **2024/25** — ★ *Symbolic Learning Enables Self-Evolving Agents*. https://arxiv.org/abs/2406.18532
- **2025** — *ScoreFlow: Mastering LLM Agent Workflows via Score-Based Preference Optimization*. https://arxiv.org/abs/2502.04306
- **2025** — *Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies*. https://arxiv.org/abs/2502.02533
- **2025** — *MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision*. https://arxiv.org/abs/2505.14996
- **2025** — *EvoAgentX: An Automated Framework for Evolving Agentic Workflows*. https://arxiv.org/abs/2507.03616
- **2025** — *SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence*. https://aclanthology.org/2025.emnlp-main.93/

## Harness / runtime as the optimization target

- **2026** — ★ *Meta-Harness: End-to-End Optimization of Model Harnesses*. https://arxiv.org/abs/2603.28052
- **2026** — ★ *Self-Harness: Harnesses That Improve Themselves*. https://arxiv.org/abs/2606.09498
- **2026** — *Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts*. https://arxiv.org/abs/2606.05922
- **2026** — *Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation*. https://arxiv.org/abs/2607.08938
- **2026** — ★ *Continual Harness: Online Adaptation for Self-Improving Foundation Agents*. https://arxiv.org/abs/2605.09998
- **2026** — *Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams*. https://arxiv.org/abs/2606.01770
- **2026** — ★ *MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems*. https://arxiv.org/abs/2605.22794
- **2026** — *JudgeFlow: Agentic Workflow Optimization via Block Judge*. https://arxiv.org/abs/2601.07477
- **2026** — ★ *Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories*. https://arxiv.org/abs/2608.02276
- **2026** — *AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering*. https://arxiv.org/abs/2601.04620

**Paradigm shift:** optimization progresses from improving the task agent to improving the **mechanism that performs improvement**.

---

# 8. Paradigm VIII — Persistent self-improvement, recursive AI & meta-evolution

**Core idea:** improvements persist across rounds; increasingly, the improver, evaluator, or meta-level policy is itself exposed to improvement.

## Early self-evolving / self-referential systems

- **2023** — ★ *Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution*. https://arxiv.org/abs/2309.16797
- **2024/25** — ★ *Symbolic Learning Enables Self-Evolving Agents*. https://arxiv.org/abs/2406.18532
- **2025** — *SICA: A Self-Improving Coding Agent* — ICLR 2025 Workshop on Scaling Self-Improving Foundation Models. https://openreview.net/forum?id=rShJCyLsOr
- **2025** — ★ *Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement* — ACL 2025. https://aclanthology.org/2025.acl-long.1354/
- **2025** — ★ *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents*. https://arxiv.org/abs/2505.22954
- **2025** — *Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine*. https://arxiv.org/abs/2510.21614
- **2025** — *Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?* https://arxiv.org/abs/2511.13646

## 2026: from self-evolution to meta-evolution

- **2026** — ★ *Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing*. https://arxiv.org/abs/2602.04837
- **2026** — ★ *Hyperagents* — self-referential task + meta agent in an editable program. https://arxiv.org/abs/2603.19461
- **2026** — *CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery*. https://arxiv.org/abs/2604.01658
- **2026** — *Recursive Self-Evolving Agents via Held-Out Selection*. https://arxiv.org/abs/2606.28374
- **2026** — ★ *The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators*. https://arxiv.org/abs/2606.26294
- **2026** — ★ *Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering* / OpenRSI. https://arxiv.org/abs/2607.28568
- **2026** — *Recuris: Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses*. https://arxiv.org/abs/2608.24876
- **2026** — *Meta^n: Recursive Self-Improvement through Emergent Depth*. https://arxiv.org/abs/2608.24735

### Useful distinction for the review

- **Self-refinement:** improves the current output, but the system is unchanged next round.
- **Persistent self-improvement:** updates weights, memory, skills, prompts, workflow, harness, or source code and carries the change forward.
- **Recursive / meta-improvement:** the mechanism that proposes/selects/evaluates future improvements is itself an optimization target.

This distinction is more useful for AI4AI than treating every self-reflection or world-model paper as self-improvement.

---

# 9. Paradigm IX — Evaluation environments that close the AI4AI loop

Benchmarks are not methods, but they are critical because modern AI4AI needs **executable feedback**. They change what can be optimized and trained.

## ML engineering / AI building

- **2023/24** — ★ *MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation*. https://arxiv.org/abs/2310.03302
- **2024** — ★ *MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering*. https://arxiv.org/abs/2410.07095
- **2024/25** — *RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts*. https://arxiv.org/abs/2411.15114
- **2025** — *MLGym: A New Framework and Benchmark for Advancing AI Research Agents*. https://arxiv.org/abs/2502.14499
- **2025** — *MLE-Dojo: Interactive RL Environment for Machine Learning Engineering*. https://arxiv.org/abs/2505.07782
- **2025** — *MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research*. https://arxiv.org/abs/2505.19955
- **2025** — *EXP-Bench: Can AI Conduct AI Research Experiments?* https://arxiv.org/abs/2505.24785
- **2025** — *ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code*. https://arxiv.org/abs/2506.02314
- **2025** — *PaperBench: Evaluating AI's Ability to Replicate AI Research*. https://arxiv.org/abs/2504.01848

## 2026: training, generalization & recursive-improvement evaluation

- **2026** — *DSGym: A Holistic Framework for Evaluating and Training Data Science Agents*. https://arxiv.org/abs/2601.16344
- **2026** — *AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents*. https://arxiv.org/abs/2602.06855
- **2026** — *ResearchGym: Evaluating Language Model Agents on Real-World AI Research*. https://arxiv.org/abs/2602.15112
- **2026** — *PostTrainBench: Can LLM Agents Automate LLM Post-Training?* https://arxiv.org/abs/2603.08640
- **2026** — *Agent^2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?* https://arxiv.org/abs/2604.10547
- **2026** — *FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics*. https://arxiv.org/abs/2605.17373
- **2026** — ★ *MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI*. https://arxiv.org/abs/2605.08678
- **2026** — *NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?* https://arxiv.org/abs/2606.24530
- **2026** — *RSIBench-Data* — recursive-improvement-oriented data-agent evaluation. https://arxiv.org/abs/2607.25886

---

# 10. Compact developmental timeline for the review figure

| Stage | Approx. period | What AI optimizes | Representative milestones |
|---|---:|---|---|
| **Configuration search** | 2009–2016 | algorithms, hyperparameters | ParamILS, SMAC, TPE, Auto-WEKA, auto-sklearn, Hyperband |
| **Structure search** | 2016–2020 | architectures, pipelines | NAS, NASNet, ENAS, DARTS, Once-for-All |
| **Learned improvement rules** | 2016–2022 | optimizer / adaptation rule | Learning-to-Learn, MAML, PBT, VeLO |
| **Program & objective discovery** | 2019–2023 | augmentation, algorithms, rewards, programs | AutoAugment, AutoML-Zero, Eureka, FunSearch |
| **LLM as optimizer** | 2022–2024 | prompts, code, workflows | APE, OPRO, Promptbreeder, DSPy, TextGrad, ADAS |
| **Agentic AI development** | 2023–2026 | full ML lifecycle | MLAgentBench, DS-Agent, SELA, AIDE, MLE-STAR, ML-Master, AIBuildAI-2, MLEvolve, AutoTrainess |
| **Agent / harness optimization** | 2024–2026 | prompts + tools + memory + workflow + runtime code | ADAS, AFlow, Meta-Harness, Self-Harness, Continual Harness, MOSS, Harness-R1 |
| **Recursive / meta-evolution** | 2025–2026 | agent + improver + evaluator | Gödel Agent, Darwin Gödel Machine, Hyperagents, Group-Evolving Agents, Red Queen Gödel Machine, Frontis-MA1/OpenRSI |

The high-level trend is therefore not simply **AutoML → research agents**. A cleaner AI4AI narrative is:

```text
fixed search space
      ↓
search model / pipeline structure
      ↓
learn the improvement rule
      ↓
generate programs / objectives
      ↓
LLM becomes a general optimizer
      ↓
agent closes the build–execute–evaluate loop
      ↓
agent optimizes its own workflow / harness
      ↓
recursive and meta-level improvement
```

---

# 11. Suggested coding fields for the review database

To support a future quantitative table/figure, code every paper along mechanism-centric rather than application-centric dimensions:

| Field | Meaning |
|---|---|
| Year | publication / preprint year |
| **AI artifact improved** | data / feature / hyperparameter / architecture / optimizer / objective / algorithm / model / prompt / workflow / harness / evaluator / improver |
| Search representation | vector / architecture graph / program / natural language / repository / executable agent state |
| Proposal mechanism | BO / RL / gradient / evolution / LLM / multi-agent / learned policy |
| Feedback | validation score / runtime / execution / verifier / judge / experiment |
| Persistence | none / archive / memory / weights / source-code change |
| Adaptation level | per-task / cross-task / continual / self-modifying / meta-evolving |
| Loop closure | human-in-loop / bounded autonomous / persistent self-improvement / recursive improvement |
| Human scaffolding | fixed pipeline / configurable harness / agent-authored / self-authored improver |
| Evaluation horizon | single eval / episode / competition / multi-hour training / research project |
| Reproducibility | code / data / traces / seeds / complete artifacts |

This coding scheme should make it easier to construct the review's central taxonomy and the chronological trend figure without conflating **application domain** (MLE, research, coding) with **AI4AI mechanism**.

---

# 12. Additional core AI4AI references surfaced by Wu et al. (2026)

The following papers were added after cross-checking the reference map of *AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement—Definitions, Reliable Horizons, and Open Problems* (Wu et al., 2026). Existing entries above are intentionally preserved; this section only records previously missing works that directly improve an AI artifact, AI-development process, or the improver itself.

## Data, weights & model self-improvement

- **2022** — *STaR: Bootstrapping Reasoning With Reasoning* — successful model-generated rationales become supervision for subsequent training. https://arxiv.org/abs/2203.14465
- **2024** — ★ *SPIN: Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models* — iterative self-play produces training data for improving the model. https://proceedings.mlr.press/v235/chen24j.html
- **2024** — *Self-Rewarding Language Models* — the model generates instructions and preference judgments used to improve later versions. https://arxiv.org/abs/2401.10020
- **2025** — ★ *DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback* — closes a teacher–student loop in which data generation adapts to student-model feedback. https://openreview.net/forum?id=PQHRWzQ5M7
- **2025** — *Self-Adapting Language Models* — persistent model adaptation through model-generated learning signals. NeurIPS 2025.
- **2026** — ★ *Autodata: An Agentic Data Scientist to Create High Quality Synthetic Data* — iteratively revises a data generator using solver comparisons and held-out utility. https://arxiv.org/abs/2606.25996

## Automated AI research & AI infrastructure

- **2025** — *AgentRxiv: Towards Collaborative Autonomous Research* — multi-agent research production with persistent research artifacts. https://arxiv.org/abs/2503.18102
- **2026** — ★ *ASI-Evolve: AI Accelerates AI* — a unified AI4AI system spanning data, model design, and learning-algorithm improvement. https://arxiv.org/abs/2603.29640
- **2026** — ★ *AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery* — paper-to-repository research automation and model optimization across executable AI studies. https://arxiv.org/abs/2604.05550
- **2026** — *DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively* — progressive autonomous scientific discovery with executable feedback. ICLR 2026.
- **2026** — *KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta* — agentic optimization of low-level AI-computing infrastructure under executable verification. ISCA 2026.
- **2026** — ★ *The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?* — evaluates whether agents can construct stronger successor agents under bounded evaluation. https://arxiv.org/abs/2606.04455
- **2026** — *How Far Are We from True Auto-Research?* — analyzes the gap between research artifact generation and genuinely autonomous research. https://arxiv.org/abs/2605.19156

## Harness self-improvement & meta-evolution

- **2007** — ★ *Gödel Machines: Fully Self-Referential Optimal Universal Self-Improvers* — foundational formal framing of a system that can rewrite its own improvement procedure. https://people.idsia.ch/~juergen/goedelmachine.html
- **2024** — ★ *Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation* — an improver rewrites the code of its own improvement procedure. https://arxiv.org/abs/2310.02304
- **2025** — ★ *Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models* — evolves the context/harness state used by future model calls. https://arxiv.org/abs/2510.04618
- **2026** — ★ *HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry* — represents harnesses as composable settings exposed to automated search. https://arxiv.org/abs/2606.14249
- **2026** — ★ *Recursive Harness Self-Improvement* — updates an editable harness specification from pairwise feedback over revision history. https://arxiv.org/abs/2607.15524
- **2026** — ★ *Bilevel Autoresearch: Meta-Autoresearching Itself* — an outer research loop inspects and modifies the search mechanisms used by an inner autoresearch loop. https://arxiv.org/abs/2603.23420
- **2026** — ★ *MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution* — evolves both task-level branches and slower-timescale improvement procedures. https://arxiv.org/abs/2607.05297
- **2026** — ★ *Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization* — jointly optimizes the proposer and the target in a self-referential loop. https://arxiv.org/abs/2604.23472

## Evaluation of persistent and compounding improvement

- **2026** — *Beyond Pass@1: A Reliability Science Framework for Long-Horizon LLM Agents* — motivates repeated-trial reliability rather than isolated successful runs. https://arxiv.org/abs/2603.29231
- **2026** — *Towards a Science of AI Agent Reliability* — formalizes reliability concerns for long-horizon agent systems and integrated evaluation. https://arxiv.org/abs/2602.16666
- **2026** — *Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0* — directly tests whether improvements from agent optimizers compose across continued adaptation. https://arxiv.org/abs/2607.14004
- **2026** — *Rethinking the Evaluation of Harness Evolution for Agents* — studies transfer, evaluation protocol, and attribution issues in harness evolution. https://arxiv.org/abs/2607.12227

## Survey anchor

- **2026** — ★ *AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement—Definitions, Reliable Horizons, and Open Problems* — useful complementary survey centered on stage ownership, signal grounding, retention/transfer evidence, the composition gap, and model–harness co-evolution. https://www.preprints.org/manuscript/202608.2108

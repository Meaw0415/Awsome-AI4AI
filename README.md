<div align="center">

# 🤖 Awesome AI4AI

### AI Agents for Automating, Optimizing, and Advancing AI Research

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Focus](https://img.shields.io/badge/Focus-Agent4AI-blue)
![Papers](https://img.shields.io/badge/Agentic%20Papers-160%2B-brightgreen)
![Years](https://img.shields.io/badge/Agentic%20Focus-2024--2026-orange)

**AI4AI** studies how AI can improve the development of AI itself — from classical AutoML and architecture search to autonomous **ML engineering agents, AI research agents, AI scientists, and self-improving research systems**.

**Current focus: Agent4AI — agents that autonomously perform and optimize AI/ML engineering and research.**

[Agent4AI Papers](agentic_ai4ai_2024_2026.md) · [Benchmarks](benchmarks.md) · [Surveys](surveys.md) · [Full Library](papers.md) · [Writing Notes](writing.md)

</div>

---

## 🔥 Agent4AI: The Emerging Core of AI4AI

The recent shift is from optimizing a **model configuration** to optimizing an entire **AI R&D trajectory**:

```text
AutoML / NAS
    ↓
LLM as Optimizer
    ↓
Agent edits code + runs experiments
    ↓
MLE Agent searches over research trajectories
    ↓
AI Research Agent forms hypotheses + interprets evidence
    ↓
AI Scientist automates larger portions of the research lifecycle
    ↓
Self-improving / learning research agents
```

### Representative Agent4AI Systems

| Year | System / Paper | What is automated? | Main optimization / agent mechanism | Evaluation |
|:---:|---|---|---|---|
| 2023/24 | [MLAgentBench](https://arxiv.org/abs/2310.03302) | ML experimentation | language agent + experiment feedback | ML research tasks |
| 2024 | [DS-Agent](https://arxiv.org/abs/2402.17453) | Data science | case-based reasoning over Kaggle experience | Kaggle tasks |
| 2024 | [SELA](https://arxiv.org/abs/2410.17238) | AutoML | tree-search enhanced LLM agent | tabular ML tasks |
| 2024 | [MLE-bench](https://arxiv.org/abs/2410.07095) | ML engineering | benchmark for end-to-end MLE agents | 75 Kaggle competitions |
| 2024 | [The AI Scientist](https://arxiv.org/abs/2408.06292) | Research lifecycle | idea → experiment → paper → review loop | automated ML research |
| 2024/25 | [RE-Bench](https://arxiv.org/abs/2411.15114) | AI R&D | long-horizon agentic R&D evaluation | AI research engineering |
| 2025 | [AIDE](https://arxiv.org/abs/2502.13138) | ML engineering | solution-tree search over code | MLE-bench / competitions |
| 2025 | [I-MCTS](https://arxiv.org/abs/2502.14693) | AutoML / MLE | introspective Monte Carlo tree search | ML tasks |
| 2025 | [Agent Laboratory](https://arxiv.org/abs/2501.04227) | Research assistance | specialized multi-agent research workflow | research pipeline |
| 2025 | [AI Co-Scientist](https://arxiv.org/abs/2502.18864) | Scientific ideation | multi-agent generate/debate/evolve loop | scientific hypotheses |
| 2025 | [AI Scientist-v2](https://arxiv.org/abs/2504.08066) | Automated research | agentic tree search | workshop-level research |
| 2025 | [PaperBench](https://arxiv.org/abs/2504.01848) | Research replication | benchmark for paper reproduction agents | ICML research replication |
| 2025 | [ML-Agent](https://arxiv.org/abs/2505.23723) | ML engineering | reinforcement learning for MLE agents | MLE tasks |
| 2025 | [R&D-Agent](https://arxiv.org/abs/2505.14738) | AI solution R&D | research + development + evolution | data-driven AI tasks |
| 2025 | [MLE-STAR](https://arxiv.org/abs/2506.15692) | ML engineering | search + targeted refinement | MLE-bench |
| 2025 | [ML-Master](https://arxiv.org/abs/2506.16499) | ML engineering | exploration + reasoning + adaptive memory | MLE-bench |
| 2025 | [AutoMind](https://arxiv.org/abs/2506.10974) | Data science | expert knowledge + adaptive search | Kaggle / MLE tasks |
| 2025 | [MLR-Bench](https://arxiv.org/abs/2505.19955) | Open-ended ML research | research-agent benchmark | 201 ML research tasks |
| 2025 | [MLGym](https://arxiv.org/abs/2502.14499) | AI research | interactive research environment | AI research tasks |
| 2026 | [ML-Master 2.0](https://arxiv.org/abs/2601.10402) | Long-horizon AI research | extended exploration + memory | ultra-long-horizon tasks |
| 2026 | [Reasoning as Gradient](https://arxiv.org/abs/2603.01692) | ML engineering | iterative reasoning feedback beyond tree search | MLE tasks |
| 2026 | [AIRA_2](https://arxiv.org/abs/2603.26499) | AI research | improved research-agent harness | AI research tasks |
| 2026 | [FML-bench](https://arxiv.org/abs/2605.17373) | Research-agent evaluation | process/search-dynamics evaluation | fundamental ML research |

> 📚 **160+ papers from 2024–2026:** see the full [`Agentic AI4AI table`](agentic_ai4ai_2024_2026.md), covering MLE agents, AI research agents, AI scientists, search/planning, workflow optimization, agent RL, memory/tool optimization, self-evolution, and benchmarks.

---

## 🧭 Agent4AI Landscape

| Track | Research question | Representative directions |
|---|---|---|
| **MLE Agents** | Can an agent autonomously build and improve ML solutions? | AIDE, MLE-STAR, ML-Master, R&D-Agent, AutoMind |
| **Search & Planning** | How should an agent explore the experiment/code space? | tree search, MCTS, evolutionary search, reasoning-as-gradient |
| **Agent Learning** | Can the research policy itself be trained? | agentic SFT/RL, MLE-Dojo, ML-Agent, AceGRPO |
| **Memory & Experience** | How should previous experiments influence future ones? | adaptive memory, case-based reasoning, trajectory reuse |
| **Workflow Optimization** | Can the agent architecture/harness itself be optimized? | workflow search, topology optimization, prompt evolution |
| **AI Research Agents** | Can agents move beyond engineering into research decisions? | MLGym, AIRA, ResearchAgent, Agent Laboratory |
| **AI Scientists** | Can the full research loop be automated? | AI Scientist, AI Scientist-v2, AI Co-Scientist |
| **Self-Improving AI4AI** | Can agents improve their own research machinery? | AlphaEvolve, Darwin Gödel Machine, self-evolving workflows |
| **Evaluation** | What does meaningful autonomous AI R&D progress mean? | MLAgentBench, MLE-bench, RE-Bench, MLR-Bench, PaperBench, FML-bench |

---

## 📊 Agent4AI Benchmarks: Increasing Research Difficulty

```text
Data-science coding
      ↓
ML experimentation
      ↓
Kaggle-scale ML engineering
      ↓
Long-horizon AI R&D
      ↓
Open-ended ML research
      ↓
Paper reproduction / scientific research
```

| Benchmark | Year | Main capability |
|---|:---:|---|
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023/24 | iterative ML experimentation |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | 2024 | competition-scale ML engineering |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | 2024/25 | long-horizon frontier AI R&D |
| [ScienceAgentBench](https://arxiv.org/abs/2410.05080) | 2025 | data-driven scientific discovery |
| [MLGym](https://arxiv.org/abs/2502.14499) | 2025 | interactive AI research |
| [DataSciBench](https://arxiv.org/abs/2502.13897) | 2025 | data-science agents |
| [PaperBench](https://arxiv.org/abs/2504.01848) | 2025 | reproducing AI research papers |
| [MLE-Dojo](https://arxiv.org/abs/2505.07782) | 2025 | training/evaluating MLE agents |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | 2025 | open-ended ML research |
| [FML-bench](https://arxiv.org/abs/2605.17373) | 2026 | process-level research search dynamics |

More → [`benchmarks.md`](benchmarks.md)

---

## 📚 Resource Map

| Resource | Description |
|---|---|
| [`agentic_ai4ai_2024_2026.md`](agentic_ai4ai_2024_2026.md) | **160+ Agent4AI papers (2024–2026)** |
| [`benchmarks.md`](benchmarks.md) | AI4AI benchmarks and evaluation |
| [`surveys.md`](surveys.md) | surveys / tutorials / position papers |
| [`papers.md`](papers.md) | full AI4AI bibliography including classical foundations |
| [`reading_priority.md`](reading_priority.md) | compact reading path |
| [`writing.md`](writing.md) | survey-writing ideas, taxonomy, and research gaps |

---

<details>
<summary><h2>📜 Classical AI4AI Foundations — AutoML, NAS, Meta-Learning & Algorithm Discovery</h2></summary>

These directions remain part of AI4AI, but the repository's current emphasis is **Agent4AI**.

### 1. AutoML & Hyperparameter Optimization

- **2011** — [Algorithms for Hyper-Parameter Optimization](https://proceedings.neurips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html)
- **2012** — [Random Search for Hyper-Parameter Optimization](https://jmlr.org/papers/v13/bergstra12a.html)
- **2013** — [Auto-WEKA](https://arxiv.org/abs/1208.3719)
- **2015** — [auto-sklearn](https://proceedings.neurips.cc/paper/2015/hash/11d0e6287202fced83f79975ec59a3a6-Abstract.html)
- **2016** — [TPOT](https://proceedings.mlr.press/v64/olson_tpot_2016.html)
- **2016** — [Hyperband](https://arxiv.org/abs/1603.06560)
- **2017/18** — [BOHB](https://arxiv.org/abs/1807.01774)
- **2020** — [AutoGluon-Tabular](https://arxiv.org/abs/2003.06505)
- **2021** — [FLAML](https://arxiv.org/abs/1911.04706)

### 2. Neural Architecture Search

- **2016/17** — [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578)
- **2017** — [NASNet](https://arxiv.org/abs/1707.07012)
- **2018** — [ENAS](https://arxiv.org/abs/1802.03268)
- **2018** — [DARTS](https://arxiv.org/abs/1806.09055)
- **2018** — [ProxylessNAS](https://arxiv.org/abs/1812.00332)
- **2019** — [Once-for-All](https://arxiv.org/abs/1908.09791)

### 3. Meta-Learning & Learned Optimization

- **2016** — [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474)
- **2017** — [MAML](https://arxiv.org/abs/1703.03400)
- **2017** — [Population Based Training](https://arxiv.org/abs/1711.09846)
- **2022** — [VeLO](https://arxiv.org/abs/2211.09760)

### 4. Automated Algorithm / Program Discovery

- **2018** — [Neural Optimizer Search](https://arxiv.org/abs/1709.07417)
- **2019** — [AutoAugment](https://arxiv.org/abs/1805.09501)
- **2020** — [AutoML-Zero](https://arxiv.org/abs/2003.03384)
- **2023** — [FunSearch](https://www.nature.com/articles/s41586-023-06924-6)
- **2025** — [AlphaEvolve](https://arxiv.org/abs/2506.13131)

### 5. LLMs as Optimizers

- **2022** — [Large Language Models Are Human-Level Prompt Engineers](https://arxiv.org/abs/2211.01910)
- **2023** — [OPRO](https://arxiv.org/abs/2309.03409)
- **2023** — [Promptbreeder](https://arxiv.org/abs/2309.16797)
- **2023** — [Eureka](https://arxiv.org/abs/2310.12931)
- **2024** — [TextGrad](https://arxiv.org/abs/2406.07496)

More foundations → [`papers.md`](papers.md)

</details>

<details>
<summary><h2>🌱 Open-Ended & Self-Improving Foundations</h2></summary>

- **2019** — [POET](https://arxiv.org/abs/1901.01753)
- **2021** — [Open-Ended Learning Leads to Generally Capable Agents](https://arxiv.org/abs/2107.12808)
- **2023** — [Voyager](https://arxiv.org/abs/2305.16291)
- **2023** — [Promptbreeder](https://arxiv.org/abs/2309.16797)
- **2023** — [FunSearch](https://www.nature.com/articles/s41586-023-06924-6)
- **2025** — [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)
- **2025** — [AlphaEvolve](https://arxiv.org/abs/2506.13131)

</details>

---

## ⭐ Scope

We use **AI4AI** as the umbrella term. The repository particularly tracks **Agent4AI**: autonomous agents that improve AI systems or automate the AI research-and-development process. General-purpose agents are included only when their optimization mechanism is directly relevant to AI R&D agents.

Contributions, missing papers, benchmark updates, and corrections are welcome.

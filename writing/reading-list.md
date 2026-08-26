# Priority Reading Path

A compact reading path through the AI4AI literature. The full bibliography is in [`papers.md`](papers.md).

## Tier 1 — Must read for the main survey story

1. **2013 — Auto-WEKA**  
   *Auto-WEKA: Combined Selection and Hyperparameter Optimization of Classification Algorithms*  
   https://arxiv.org/abs/1208.3719

2. **2015 — auto-sklearn**  
   *Efficient and Robust Automated Machine Learning*  
   https://proceedings.neurips.cc/paper/2015/hash/11d0e6287202fced83f79975ec59a3a6-Abstract.html

3. **2016/2017 — NAS with RL**  
   *Neural Architecture Search with Reinforcement Learning*  
   https://arxiv.org/abs/1611.01578

4. **2016 — Learning to Learn by Gradient Descent by Gradient Descent**  
   Learned optimizer as a precursor to AI systems that improve optimization itself.  
   https://arxiv.org/abs/1606.04474

5. **2017 — Population Based Training**  
   Online population-level adaptation of models and hyperparameters.  
   https://arxiv.org/abs/1711.09846

6. **2018 — DARTS**  
   *Differentiable Architecture Search*  
   https://arxiv.org/abs/1806.09055

7. **2020 — AutoML-Zero**  
   *Evolving Machine Learning Algorithms From Scratch*  
   https://arxiv.org/abs/2003.03384

8. **2023 — OPRO**  
   *Large Language Models as Optimizers*  
   https://arxiv.org/abs/2309.03409

9. **2023 — Eureka**  
   *Human-Level Reward Design via Coding Large Language Models*  
   https://arxiv.org/abs/2310.12931

10. **2023 — FunSearch**  
    *Mathematical Discoveries from Program Search with Large Language Models*  
    https://www.nature.com/articles/s41586-023-06924-6

11. **2023 — MLAgentBench**  
    *Evaluating Language Agents on Machine Learning Experimentation*  
    https://arxiv.org/abs/2310.03302

12. **2024 — ResearchAgent**  
    *Iterative Research Idea Generation over Scientific Literature with Large Language Models*  
    https://arxiv.org/abs/2404.07738

13. **2024 — The AI Scientist**  
    *Towards Fully Automated Open-Ended Scientific Discovery*  
    https://arxiv.org/abs/2408.06292

14. **2024 — MLE-bench**  
    *Evaluating Machine Learning Agents on Machine Learning Engineering*  
    https://arxiv.org/abs/2410.07095

15. **2024/2025 — RE-Bench**  
    *Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts*  
    https://arxiv.org/abs/2411.15114

16. **2025 — PaperBench**  
    *Evaluating AI's Ability to Replicate AI Research*  
    https://openai.com/index/paperbench/

17. **2025 — AlphaEvolve**  
    *A Coding Agent for Scientific and Algorithmic Discovery*  
    https://arxiv.org/abs/2506.13131

18. **2025 — Darwin Gödel Machine**  
    *Open-Ended Evolution of Self-Improving Agents*  
    https://arxiv.org/abs/2505.22954

## Tier 2 — Important supporting papers

- Random Search for HPO (2012)
- Hyperband (2016)
- BOHB (2017)
- MAML (2017)
- Regularized Evolution / AmoebaNet (2018)
- ENAS (2018)
- ProxylessNAS (2018)
- AutoAugment (2019)
- Once-for-All (2019)
- NAS-Bench-101 (2019)
- NAS-Bench-201 (2020)
- AutoGluon (2020)
- VeLO (2022)
- ReAct (2022)
- Reflexion (2023)
- Voyager (2023)
- Promptbreeder (2023)
- DSPy (2023/2024)
- TextGrad (2024)
- AIDE (2024)
- Agent Laboratory (2025)
- AI Co-Scientist (2025)

## Suggested reading order

```text
Auto-WEKA / auto-sklearn
          ↓
NAS + DARTS
          ↓
Learned Optimizers + PBT
          ↓
AutoML-Zero
          ↓
OPRO + Eureka
          ↓
FunSearch + AlphaEvolve
          ↓
MLAgentBench + MLE-bench
          ↓
ResearchAgent + AI Scientist
          ↓
RE-Bench + PaperBench
          ↓
Darwin Gödel Machine / research world models
```

This order is designed to reveal the central progression from **searching a fixed configuration space** to **searching programs**, then to **agents performing experiments**, and finally to **systems that operate on or improve the research process itself**.

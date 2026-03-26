# 🤖 RISK TWIN OSS: Models & Baselines Directory

This directory houses the decision-making algorithms and policies that interact with the RISK TWIN simulated environments. The `baselines/` subfolder specifically contains traditional Operations Research (OR) heuristic policies and standard machine learning models. These serve as the performance floor that our advanced Causal Reinforcement Learning (RL) agents must beat.

Below is a breakdown of the baseline implementations in this repository.

---

### `sc_ss_policy.ipynb`
* **What I did:** Implemented a traditional $(s, S)$ inventory control policy (often referred to as a min-max or safety stock policy) to navigate the simulated supply chain environment.
* **Why I did that:** Before training complex, computationally expensive Causal RL agents, it is critical to establish a performance benchmark using standard, highly interpretable industry rules (e.g., "if inventory falls below $s$, order up to $S$"). 
* **So what:** Provides a concrete "control group" for the experiments. By running this baseline through the `era_swap` macro-shocks, we can definitively measure the "value-add" of our Causal RL approach. If the RL agent cannot survive the simulated shocks better than this simple heuristic, we know the RL reward function or causal graph needs refinement.

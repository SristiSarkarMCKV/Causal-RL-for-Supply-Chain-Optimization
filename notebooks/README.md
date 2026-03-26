# 📓 RISK TWIN OSS: Notebooks Directory

This directory contains the core exploratory, modeling, and simulation notebooks that power the RISK TWIN OSS pipeline. The workflow transitions from raw data processing and causal discovery to world modeling and reinforcement learning simulation.

Below is a breakdown of each notebook in this repository.

---

### `Setup.ipynb`
* **What I did:** Configured the base Python environment, handled dependency installations (e.g., `xlrd`, `openpyxl`), and established the initial data retrieval scripts for macroeconomic data (like the NY Fed GSCPI).
* **Why I did that:** To resolve environment inconsistencies and ensure that external datasets and complex libraries load correctly across different machines.
* **So what:** Provides a stable, reproducible foundation so that anyone cloning the repository can run the subsequent modeling tasks without dealing with package conflicts or missing data streams.

### `DataCo Supply Chain EDA.ipynb`
* **What I did:** Conducted Exploratory Data Analysis (EDA) on the DataCo dataset, analyzing late delivery risks, mapping shipping routes, and merging in macro-environmental factors.
* **Why I did that:** To understand baseline variable distributions, identify missing data anomalies, and uncover initial correlations between global pressures and supply chain failures.
* **So what:** Establishes the baseline risk metrics (e.g., the ~54% late delivery rate) and informs the feature selection process necessary for building accurate causal models.

### `causal_graph.ipynb`
* **What I did:** Defined the Directed Acyclic Graphs (DAGs) to map the structural causal models linking macroeconomic shocks (like GSCPI or inflation) to supply chain and retail outcomes.
* **Why I did that:** Traditional machine learning only captures correlations. A formal causal structure is required to accurately simulate interventions and counterfactual scenarios without suffering from confounding bias.
* **So what:** Acts as the mathematical blueprint for the world model, ensuring our simulated macro-shocks respect true, real-world cause-and-effect relationships.

### `world_model.ipynb`
* **What I did:** Trained the environment dynamics model based on the structures defined in the causal graph.
* **Why I did that:** To mathematically represent how the supply chain environment transitions from one state to another under varying external pressures and internal actions.
* **So what:** Unlocks the ability to generate synthetic, counterfactual futures that the Reinforcement Learning agent can use for robust policy training.

### `era_swap.ipynb`
* **What I did:** Implemented the counterfactual logic to inject historical or synthetic macro-shocks (e.g., "COVID_2020_LOGISTICS" or "GFC_2008_MORTGAGE") into the current operational state.
* **Why I did that:** To stress-test how current supply chain policies and baseline risks would hold up under vastly different, extreme macroeconomic regimes.
* **So what:** Powers the core analytical engine of the RISK TWIN dashboard, allowing decision-makers to visualize vulnerability against specific tail-risk events.

### `simulators.ipynb`
* **What I did:** Wrapped the causal world models and era-swapping logic into standardized Reinforcement Learning simulation environments.
* **Why I did that:** RL agents require a strict, standardized interface (states, actions, rewards, and step functions) to interact with and learn from the simulated world.
* **So what:** Successfully bridges the gap between causal inference and reinforcement learning, making the entire system ready for automated policy optimization.

### `risk_twin_pipeline.ipynb`
* **What I did:** Consolidated the individual components—data ingestion, causal graph generation, world modeling, and simulation—into a single, unified execution pipeline.
* **Why I did that:** To automate the end-to-end workflow, allowing the full model to run seamlessly from raw data to final risk metric outputs without executing notebooks piecemeal.
* **So what:** Provides a clean, executable backend architecture that can be directly integrated with the Streamlit dashboard (`dashboard.py`) or deployed to production servers.

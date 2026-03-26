# 🌪️ Causal-RL-for-Supply-Chain-Optimization (RISK TWIN OSS)

Welcome to the **RISK TWIN OSS** repository. This project builds a causally-constrained simulation environment (a "World Model") to train and evaluate Reinforcement Learning (RL) agents for supply chain and retail optimization. By combining Causal Inference with RL, this system can simulate extreme macroeconomic shocks ("Era Swaps") to stress-test logistics and inventory policies.

Below is a breakdown of the repository's architecture and the purpose of each top-level component.

---

### `data/`
* **What I did:** Created a dedicated directory (specifically `data/raw/`) to store the foundational datasets, including the DataCo Supply Chain dataset and the Walmart Recruiting Store Sales data, neatly compressed in `.zip` formats.
* **Why I did that:** To isolate the original, unmodified data from the processing scripts and prevent massive raw `.csv` files from cluttering the repository.
* **So what:** Ensures a single, immutable source of truth. Anyone cloning the repository can run the automated ingestion pipelines and perfectly reproduce the environment setup from scratch.

### `notebooks/`
* **What I did:** Centralized all exploratory data analysis (EDA), causal graph creation, world model training and simulation logic into a series of sequential Jupyter notebooks.
* **Why I did that:** Building a Causal RL pipeline is highly complex. Breaking it down into modular, highly documented notebooks makes the mathematical progression understandable and testable.
* **So what:** Allows researchers and contributors to easily walk through the core logic—from discovering how GSCPI affects late deliveries to simulating counterfactual macroeconomic eras—without getting lost in a monolithic codebase.

### `models/`
* **What I did:** Established a directory exclusively for decision-making algorithms and policies, currently housing traditional Operations Research baselines (like the $(s, S)$ inventory policy).
* **Why I did that:** To strictly separate the "brain" (the policies and RL agents) from the "world" (the simulated supply chain environments). 
* **So what:** Provides a rigorous scientific testing ground. It ensures we have concrete, industry-standard benchmarks ready to prove whether our advanced Causal RL agents actually deliver superior performance during simulated macro-shocks.

### `experiments/`
* **What I did:** Reserved a dedicated folder for tracking model training runs, hyperparameter configurations and simulation output logs.
* **Why I did that:** Reinforcement learning requires running thousands of episodes across various counterfactual scenarios. Mixing these output logs with source code leads to an unmanageable repository.
* **So what:** Keeps the codebase clean while ensuring that the empirical results of our "Era Swap" stress tests are systematically recorded, easily comparable and fully reproducible.

### `dashboard.py`
* **What I did:** Placed the main Streamlit web application script directly at the root of the repository.
* **Why I did that:** To provide a visual, interactive frontend that bridges the complex Python backend with an intuitive user interface, and to adhere to deployment best practices for cloud hosting platforms.
* **So what:** Transforms this repository from a purely academic research project into an accessible, interactive decision-support tool. It allows users to visually inject macro-shocks (like COVID-era logistics pressures) and instantly see the simulated impact on stockout or late delivery risks.

---

**Getting Started:**
To launch the interactive simulator locally, ensure your environment is set up (see `notebooks/Setup.ipynb`), then run the following command from the root directory:
`streamlit run dashboard.py`

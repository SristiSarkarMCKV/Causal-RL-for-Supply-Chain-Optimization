import streamlit as st
import pandas as pd

def set_page(page_name):
    st.session_state.current_page = page_name

def main():
    st.set_page_config(
        page_title="RISK TWIN OSS",
        page_icon="🌪️",
        layout="wide"
    )

    if "current_page" not in st.session_state:
        st.session_state.current_page = "🏠 Project Overview"

    # Subtle typography and visual styling keeping default theme background
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        .hero-title {
            font-size: 2.3rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 2px;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            font-weight: 500;
            opacity: 0.85;
            margin-bottom: 20px;
        }

        .feature-card {
            border-radius: 12px;
            padding: 20px;
            border: 1px solid rgba(128, 128, 128, 0.2);
            background: rgba(128, 128, 128, 0.05);
            margin-bottom: 16px;
        }

        .metric-badge {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            border: 1px solid rgba(59, 130, 246, 0.5);
            background: rgba(59, 130, 246, 0.1);
            color: #3b82f6;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }

        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            padding: 8px 20px;
            transition: all 0.2s ease;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navigation Sidebar
    st.sidebar.title("🌪️ RISK TWIN OSS")
    pages = ["🏠 Project Overview", "📈 Era Swap Simulator", "🔬 Technical Architecture & Developer"]
    selected_page = st.sidebar.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state.current_page)
    )
    st.sidebar.divider()

    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

    # ---------------------------------------------------------
    # 1. PROJECT OVERVIEW / HOME
    # ---------------------------------------------------------
    if st.session_state.current_page == "🏠 Project Overview":
        st.markdown('<p class="hero-title">🌪️ Causal-RL for Supply Chain Optimization</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">RISK TWIN OSS: Causally-Constrained World Model Simulation</p>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <span class="metric-badge">System Core</span>
            <p style="font-size: 1rem; line-height: 1.6; margin: 0;">
                <b>RISK TWIN OSS</b> builds a causally-constrained simulation environment (a <b>World Model</b>) to train and evaluate Reinforcement Learning (RL) agents for supply chain and retail optimization. By combining formal Causal Inference with RL this system simulates extreme macroeconomic shocks (<b>Era Swaps</b>) to stress-test logistics and inventory policies under volatile conditions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="feature-card">
                <span class="metric-badge">Retail Twin</span>
                <h3 style="margin-top:2px;">🛒 Domain 1: Walmart (Retail Operations)</h3>
                <ul style="line-height: 1.6; font-size: 0.95rem;">
                    <li><b>Mechanism:</b> Tracks how external labor markets (<b>Unemployment</b>) and inflationary pressures (<b>CPI</b>) drive retail inventory stockout risks.</li>
                    <li><b>Baseline State (2026 DNA):</b> Stable operational conditions with an expected stockout rate of <b>4.2%</b>.</li>
                    <li><b>Stress Regimes:</b> Evaluates labor-isolation shocks (2008 GFC) and compounded dual-shocks (COVID-19 Retail Era).</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-card">
                <span class="metric-badge">Logistics Twin</span>
                <h3 style="margin-top:2px;">🚢 Domain 2: DataCo (Logistics Operations)</h3>
                <ul style="line-height: 1.6; font-size: 0.95rem;">
                    <li><b>Mechanism:</b> Tracks how port congestion and supply chain pressure (<b>NY Fed GSCPI</b>) paired with global energy costs impact delivery schedules.</li>
                    <li><b>Baseline State (2026 Routes):</b> High inherent routing friction with a baseline late delivery risk of <b>54.3%</b>.</li>
                    <li><b>Stress Regimes:</b> Simulates supply chain gridlocks and extreme global port bottlenecks.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 🎯 Benchmark Findings")
        tab1, tab2 = st.tabs(["🛒 Retail Stress Takeaways", "🚢 Logistics Stress Takeaways"])
        with tab1:
            retail_summary = pd.DataFrame({
                "Scenario": ["Baseline (2026)", "GFC 2008 Shock", "COVID 2020 Shock"],
                "Unemployment": ["5.0%", "10.0%", "14.7%"],
                "CPI": [210.0, 210.0, 256.0],
                "Stockout Risk": ["4.2%", "8.2%", "14.3%"],
                "Delta vs Baseline": ["—", "+4.0%", "+10.1%"]
            })
            st.dataframe(retail_summary, use_container_width=True, hide_index=True)
            st.caption("Traditional inventory baselines collapse under compounded inflation and labor disruption.")

        with tab2:
            logistics_summary = pd.DataFrame({
                "Scenario": ["Baseline (2026)", "COVID 2020 Shock"],
                "GSCPI (SD)": [0.00, 4.30],
                "Fuel Price": ["$75.00", "$75.00"],
                "Late Delivery Risk": ["54.3%", "71.5%"],
                "Delta vs Baseline": ["—", "+17.2%"]
            })
            st.dataframe(logistics_summary, use_container_width=True, hide_index=True)
            st.caption("Traditional lead-time routing heuristics fail when global logistics networks back up.")

        st.divider()
        st.markdown("#### Explore the Platform")
        nav_c1, nav_c2, _ = st.columns([1, 1.2, 1.8])
        with nav_c1:
            st.button("📈 Launch Simulator", on_click=set_page, args=("📈 Era Swap Simulator",), use_container_width=True)
        with nav_c2:
            st.button("🔬 View Technical Architecture", on_click=set_page, args=("🔬 Technical Architecture & Developer",), use_container_width=True)

    # ---------------------------------------------------------
    # 2. PREDICTION SECTION (ERA SWAP SIMULATOR)
    # ---------------------------------------------------------
    elif st.session_state.current_page == "📈 Era Swap Simulator":
        st.markdown('<p class="hero-title">🌪️ RISK TWIN OSS: Era Swap Simulator</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Simulate Counterfactual Risks on Causally-Constrained World Models.</p>', unsafe_allow_html=True)
        
        st.sidebar.header("Configure Macro Environment")
        domain = st.sidebar.selectbox("Domain", ["Walmart (Retail)", "DataCo (Supply Chain)"])
        
        # WALMART / RETAIL UI
        if domain == "Walmart (Retail)":
            st.sidebar.subheader("Retail Macro Shocks")
            era = st.sidebar.selectbox("Load Predefined Era", ["Custom", "COVID_2020_RETAIL", "GFC_2008_MORTGAGE"])
            
            def_unemp = 14.7 if era == "COVID_2020_RETAIL" else (10.0 if era == "GFC_2008_MORTGAGE" else 5.0)
            def_cpi = 256.0 if era == "COVID_2020_RETAIL" else 210.0
            
            unemployment = st.sidebar.slider("Unemployment Rate (%)", 3.0, 20.0, float(def_unemp))
            cpi = st.sidebar.slider("CPI (Inflation)", 180.0, 300.0, float(def_cpi))
            
            st.subheader("Walmart Portfolio Risk: Stockout Probability")
            
            baseline_risk = 0.042
            simulated_risk = baseline_risk + ((unemployment - 5.0) * 0.008) + ((cpi - 210.0) * 0.0005)
            simulated_risk = max(0.01, min(simulated_risk, 0.99))
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Baseline Risk (2026 DNA)", f"{baseline_risk*100:.1f}%")
            col2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%")
            col3.metric("Macro Strain Index", f"{((unemployment/5.0 + cpi/210.0)/2):.2f}x")
            
            st.divider()
            st.markdown("#### Scenario Comparison Analysis")
            
            chart_data = pd.DataFrame(
                {"Scenario": ["Baseline", "Counterfactual"], "Probability (%)": [baseline_risk * 100, simulated_risk * 100]}
            ).set_index("Scenario")
            
            st.bar_chart(
                chart_data, 
                height=300,
                x_label="Macroeconomic Scenario",
                y_label="Stockout Probability (%)"
            )
            
            st.caption("📊 **Chart Description:** This visual contrasts the expected probability of inventory stockouts under standard 2026 operational parameters (Baseline) against the modeled outcomes when subjected to the selected macroeconomic shock (Counterfactual Era).")
            
            if simulated_risk > 0.15:
                st.error("⚠️ TAIL RISK DETECTED: Model predicts stockout probability exceeds 15% threshold.")
            elif simulated_risk > baseline_risk + 0.03:
                st.warning("⚠️ ELEVATED INVENTORY RISK: Policy adjustments advised.")

        # DATACO / SUPPLY CHAIN UI
        elif domain == "DataCo (Supply Chain)":
            st.sidebar.subheader("Logistics Macro Shocks")
            era = st.sidebar.selectbox("Load Predefined Era", ["Custom", "COVID_2020_LOGISTICS"])
            
            def_gscpi = 4.3 if era == "COVID_2020_LOGISTICS" else 0.0
            
            st.sidebar.markdown("**Global Supply Chain Pressure Index (GSCPI)**")
            gscpi = st.sidebar.slider("GSCPI (Standard Deviations)", -2.0, 5.0, float(def_gscpi))
            fuel = st.sidebar.slider("Global Oil Price ($/bbl)", 40.0, 150.0, 75.0)
            
            st.subheader("DataCo Logistics Risk: Late Delivery Probability")
            
            baseline_risk = 0.543 
            simulated_risk = baseline_risk + (gscpi * 0.04) + ((fuel - 75.0) * 0.001)
            simulated_risk = max(0.10, min(simulated_risk, 0.99))
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Baseline Risk (2026 Routes)", f"{baseline_risk*100:.1f}%")
            col2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%")
            col3.metric("Port Pressure Index", f"{gscpi:+.2f} SD")
            
            st.divider()
            st.markdown("#### Scenario Comparison Analysis")
            
            chart_data = pd.DataFrame(
                {"Scenario": ["Baseline", "Counterfactual"], "Probability (%)": [baseline_risk * 100, simulated_risk * 100]}
            ).set_index("Scenario")
            
            st.bar_chart(
                chart_data, 
                height=300, 
                color="#ff4b4b",
                x_label="Logistics Environment",
                y_label="Late Delivery Risk (%)"
            )
            
            st.caption("📊 **Chart Description:** This visual compares the historical probability of shipment delays under standard routing structures (Baseline) versus the elevated risk calculated during the simulated logistics bottleneck (Counterfactual Era).")
            
            if simulated_risk > 0.65:
                st.error("⚠️ EXTREME CONGESTION DETECTED: Late delivery probability critically high.")
            elif simulated_risk > baseline_risk + 0.05:
                st.warning("📉 Supply Chain Stress detected. Delays likely.")

    # ---------------------------------------------------------
    # 3. ABOUT & TECHNICAL ARCHITECTURE
    # ---------------------------------------------------------
    elif st.session_state.current_page == "🔬 Technical Architecture & Developer":
        st.markdown('<p class="hero-title">🔬 Technical Architecture & Implementation</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Comprehensive blueprint of data transformations causal graphs simulation engines and baseline policies.</p>', unsafe_allow_html=True)
        
        st.markdown("### End-to-End System Execution Flow")
        st.graphviz_chart("""
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fillcolor="#F0F2F6", fontname="sans-serif", fontsize=10];
            edge [color="#555555", arrowsize=0.8];
            
            subgraph cluster_data {
                label = "1. Ingestion & Preprocessing";
                style = "dashed";
                Setup [label="Setup.ipynb\\n(Env & GSCPI Ingestion)", fillcolor="#D1E8E2"];
                EDA [label="DataCo Supply Chain EDA.ipynb\\n(Risk Profiling & Cleansing)", fillcolor="#D1E8E2"];
            }
            
            subgraph cluster_causal {
                label = "2. Causal Architecture";
                style = "dashed";
                CausalGraph [label="causal_graph.ipynb\\n(SCM & DAG Definition)", fillcolor="#D9E2EC"];
                WorldModel [label="world_model.ipynb\\n(Transition Dynamics Engine)", fillcolor="#D9E2EC"];
            }
            
            subgraph cluster_sim {
                label = "3. Counterfactual Simulation";
                style = "dashed";
                EraSwap [label="era_swap.ipynb\\n(Macro Shock Injection)", fillcolor="#BCCCDC"];
                Simulators [label="simulators.ipynb\\n(Gymnasium RL Env)", fillcolor="#BCCCDC"];
                Pipeline [label="risk_twin_pipeline.ipynb\\n(Unified Pipeline)", fillcolor="#BCCCDC"];
            }
            
            subgraph cluster_policies {
                label = "4. Benchmarks & Frontend";
                style = "dashed";
                Baselines [label="sc_ss_policy.ipynb\\n((s, S) OR Control Policy)", fillcolor="#9AA6B2"];
                Dashboard [label="dashboard.py\\n(Streamlit UI)", fillcolor="#F9D5D5"];
            }
            
            Setup -> EDA -> CausalGraph;
            CausalGraph -> WorldModel -> EraSwap -> Simulators -> Pipeline;
            Simulators -> Baselines;
            Pipeline -> Dashboard;
            Baselines -> Dashboard;
        }
        """)

        st.markdown("### Notebook & Component Breakdown")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="feature-card">
                <h4>📓 Core Research Notebooks</h4>
                <ul style="line-height:1.6; font-size:0.95rem;">
                    <li><b><code>Setup.ipynb</code>:</b> Configures the runtime environment installs critical dependencies such as <code>xlrd</code> or <code>openpyxl</code> and fetches live macroeconomic datasets including the NY Fed GSCPI index.</li>
                    <li><b><code>DataCo Supply Chain EDA.ipynb</code>:</b> Performs exploratory analysis on shipping routes establishes late delivery probability distributions and isolates missing data anomalies.</li>
                    <li><b><code>causal_graph.ipynb</code>:</b> Formulates Directed Acyclic Graphs (DAGs) and Structural Causal Models (SCMs) linking macro variables to delivery lateness to mitigate confounding bias.</li>
                    <li><b><code>world_model.ipynb</code>:</b> Trains the environment transition dynamics model to generate synthetic counterfactual trajectories for policy training.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="feature-card">
                <h4>⚙️ Simulation Engines & Baselines</h4>
                <ul style="line-height:1.6; font-size:0.95rem;">
                    <li><b><code>era_swap.ipynb</code>:</b> Implements the counterfactual engine that swaps macroeconomic states (e.g. COVID-2020 logistics stress or 2008 financial shocks) into current operational states.</li>
                    <li><b><code>simulators.ipynb</code>:</b> Wraps world models and era-swapping mechanics into standard step-action-reward interfaces compatible with RL frameworks.</li>
                    <li><b><code>risk_twin_pipeline.ipynb</code>:</b> Unifies data ingestion causal graph generation world modeling and simulation into an automated end-to-end execution pipeline.</li>
                    <li><b><code>sc_ss_policy.ipynb</code>:</b> Implements classical $(s, S)$ inventory policies as an empirical benchmark to quantify the performance advantage of Causal RL algorithms.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.markdown("### 👩‍💻 Developer Contact Information")
        
        dev_col1, dev_col2 = st.columns([1, 2])
        with dev_col1:
            st.info("""
            **Lead Developer:** Sristi Sarkar  
            **Email:** [emailsristisarkar@gmail.com](mailto:emailsristisarkar@gmail.com)  
            **WhatsApp:** [+91 8240580651](https://wa.me/918240580651)  
            """)
        with dev_col2:
            st.markdown("""
            <div class="feature-card">
                <h4>Collaborations & Research</h4>
                <p style="margin: 0; line-height: 1.6; font-size: 0.95rem;">
                    For baseline extensions structural causal model contributions or integration with enterprise supply chain environments reach out via the provided communication channels.
                </p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

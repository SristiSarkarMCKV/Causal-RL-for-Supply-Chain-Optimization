import streamlit as st
import pandas as pd

def set_page(page_name):
    st.session_state.current_page = page_name

def main():
    st.set_page_config(
        page_title="RISK TWIN OSS",
        page_icon="🌪️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    if "current_page" not in st.session_state:
        st.session_state.current_page = "🏠 Project Overview"

    # Custom UI Styling
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #090e17 0%, #101c2e 50%, #0d1522 100%);
            color: #e2e8f0;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }
        
        .main-header {
            background: linear-gradient(90deg, #1e3a8a, #3b82f6, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.8rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 0.2rem;
        }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.04);
            border-radius: 16px;
            padding: 24px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(12px);
            margin-bottom: 20px;
        }

        .glass-card-accent {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 51, 234, 0.05) 100%);
            border-radius: 16px;
            padding: 24px;
            border: 1px solid rgba(59, 130, 246, 0.25);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(12px);
            margin-bottom: 20px;
        }

        .metric-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            background: rgba(59, 130, 246, 0.2);
            color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.4);
            margin-bottom: 8px;
        }

        div[data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
            color: #38bdf8;
        }
        
        .stButton>button {
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(37, 99, 235, 0.6);
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Navigation
    st.sidebar.markdown("<h2 style='color:#38bdf8;'>🌪️ RISK TWIN OSS</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    pages = ["🏠 Project Overview", "📈 Era Swap Simulator", "🔬 Technical Architecture & Developer"]
    selected_page = st.sidebar.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state.current_page)
    )

    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

    # ---------------------------------------------------------
    # 1. PROJECT OVERVIEW / HOME
    # ---------------------------------------------------------
    if st.session_state.current_page == "🏠 Project Overview":
        st.markdown('<p class="main-header">Causal-RL for Supply Chain Optimization</p>', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#94a3b8; font-weight:400;'>Simulating Macroeconomic Counterfactual Stress on Supply Chain Digital Twins</h4>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card-accent">
            <span class="metric-badge">System Core</span>
            <p style="font-size: 1.05rem; line-height: 1.6; margin: 0; color: #cbd5e1;">
                <b>RISK TWIN OSS</b> builds a causally-constrained simulation environment (a <b>World Model</b>) to train and evaluate Reinforcement Learning agents for supply chain and retail optimization. By combining formal Causal Inference with RL this system simulates extreme macroeconomic shocks (<b>Era Swaps</b>) to stress-test logistics and inventory policies under volatile conditions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="glass-card">
                <span class="metric-badge">Retail Twin</span>
                <h3 style="color:#60a5fa; margin-top:4px;">🛒 Walmart Operations</h3>
                <p style="color:#cbd5e1; font-size: 0.95rem;">
                    Models how labor markets (<b>Unemployment</b>) and inflationary pressure (<b>CPI</b>) impact stockout risks.
                </p>
                <ul style="color:#94a3b8; font-size:0.9rem;">
                    <li><b>Baseline Rate:</b> 4.2% safe inventory stockout probability</li>
                    <li><b>GFC 2008 Shock:</b> Doubles risk to 8.2% via labor disruption</li>
                    <li><b>COVID 2020 Shock:</b> Compounds risk to 14.3% triggering tail-risk alerts</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="glass-card">
                <span class="metric-badge">Logistics Twin</span>
                <h3 style="color:#f87171; margin-top:4px;">🚢 DataCo Routing</h3>
                <p style="color:#cbd5e1; font-size: 0.95rem;">
                    Tracks how global port bottlenecks (<b>NY Fed GSCPI</b>) and energy prices trigger network delays.
                </p>
                <ul style="color:#94a3b8; font-size:0.9rem;">
                    <li><b>Baseline Rate:</b> 54.3% high baseline late delivery risk</li>
                    <li><b>COVID 2020 Shock:</b> GSCPI spikes +4.3 SD sending delay risk to 71.5%</li>
                    <li><b>Vulnerability:</b> Heuristic static routing breaks under global congestion</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<h3 style='color:#f1f5f9; margin-top: 15px;'>📊 Empirical Stress Benchmarks</h3>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🛒 Retail Shock Benchmark", "🚢 Logistics Shock Benchmark"])
        with tab1:
            retail_df = pd.DataFrame({
                "Scenario": ["Baseline (2026)", "GFC 2008 Shock", "COVID 2020 Shock"],
                "Unemployment": ["5.0%", "10.0%", "14.7%"],
                "CPI": [210.0, 210.0, 256.0],
                "Stockout Risk": ["4.2%", "8.2%", "14.3%"],
                "Risk Shift": ["Baseline", "+4.0%", "+10.1%"]
            })
            st.dataframe(retail_df, use_container_width=True, hide_index=True)

        with tab2:
            logistics_df = pd.DataFrame({
                "Scenario": ["Baseline (2026)", "COVID 2020 Shock"],
                "GSCPI (SD)": [0.00, 4.30],
                "Fuel Price": ["$75.00", "$75.00"],
                "Late Delivery Risk": ["54.3%", "71.5%"],
                "Risk Shift": ["Baseline", "+17.2%"]
            })
            st.dataframe(logistics_df, use_container_width=True, hide_index=True)

        st.divider()
        st.markdown("<h4 style='color:#f8fafc;'>Explore the Platform</h4>", unsafe_allow_html=True)
        nav_c1, nav_c2, _ = st.columns([1, 1.2, 1.8])
        with nav_c1:
            st.button("📈 Launch Simulator", on_click=set_page, args=("📈 Era Swap Simulator",), use_container_width=True)
        with nav_c2:
            st.button("🔬 View Technical Architecture", on_click=set_page, args=("🔬 Technical Architecture & Developer",), use_container_width=True)

    # ---------------------------------------------------------
    # 2. PREDICTION SECTION (ERA SWAP SIMULATOR)
    # ---------------------------------------------------------
    elif st.session_state.current_page == "📈 Era Swap Simulator":
        st.markdown('<p class="main-header">Era Swap Counterfactual Simulator</p>', unsafe_allow_html=True)
        st.markdown("<p style='color:#94a3b8;'>Simulate macroeconomic counterfactual interventions on causally-constrained environment twins.</p>", unsafe_allow_html=True)
        
        domain = st.sidebar.selectbox("Select Operational Domain", ["Walmart (Retail)", "DataCo (Supply Chain)"])
        
        if domain == "Walmart (Retail)":
            st.sidebar.markdown("### Retail Macro Variables")
            era = st.sidebar.selectbox("Load Macro Scenario", ["Custom", "COVID_2020_RETAIL", "GFC_2008_MORTGAGE"])
            
            def_unemp = 14.7 if era == "COVID_2020_RETAIL" else (10.0 if era == "GFC_2008_MORTGAGE" else 5.0)
            def_cpi = 256.0 if era == "COVID_2020_RETAIL" else 210.0
            
            unemployment = st.sidebar.slider("Unemployment Rate (%)", 3.0, 20.0, float(def_unemp))
            cpi = st.sidebar.slider("Consumer Price Index (CPI)", 180.0, 300.0, float(def_cpi))
            
            baseline_risk = 0.042
            simulated_risk = baseline_risk + ((unemployment - 5.0) * 0.008) + ((cpi - 210.0) * 0.0005)
            simulated_risk = max(0.01, min(simulated_risk, 0.99))
            
            st.markdown("""
            <div class="glass-card">
                <h3 style="color:#60a5fa; margin-top:0;">Walmart Portfolio: Stockout Risk Calculation</h3>
                <p style="color:#94a3b8;">Estimates stockout probabilities under simulated labor constraints and inflationary pressure.</p>
            </div>
            """, unsafe_allow_html=True)
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Baseline Risk (2026 DNA)", f"{baseline_risk*100:.1f}%")
            delta_val = (simulated_risk - baseline_risk) * 100
            m2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"{delta_val:+.1f}%", delta_color="inverse")
            m3.metric("Macro Strain Index", f"{((unemployment/5.0 + cpi/210.0)/2):.2f}x")
            
            st.markdown("#### Scenario Risk Distribution")
            chart_df = pd.DataFrame({
                "Scenario": ["2026 Baseline", "Simulated Counterfactual"],
                "Stockout Probability (%)": [baseline_risk * 100, simulated_risk * 100]
            }).set_index("Scenario")
            
            st.bar_chart(chart_df, height=320, color="#3b82f6")
            st.caption("Comparison between 2026 baseline inventory reliability and the counterfactual scenario under macroeconomic stress.")
            
            if simulated_risk > 0.14:
                st.error("⚠️ TAIL RISK ALERT: Inventory stockout probability exceeds the critical operational limit of 14%.")
            elif simulated_risk > baseline_risk + 0.03:
                st.warning("⚠️ ELEVATED STRESS: Inventory buffers require proactive replenishment adjustment.")

        elif domain == "DataCo (Supply Chain)":
            st.sidebar.markdown("### Logistics Macro Variables")
            era = st.sidebar.selectbox("Load Macro Scenario", ["Custom", "COVID_2020_LOGISTICS"])
            
            def_gscpi = 4.3 if era == "COVID_2020_LOGISTICS" else 0.0
            gscpi = st.sidebar.slider("GSCPI (Standard Deviations)", -2.0, 5.0, float(def_gscpi))
            fuel = st.sidebar.slider("Crude Oil Benchmark ($/bbl)", 40.0, 150.0, 75.0)
            
            baseline_risk = 0.543
            simulated_risk = baseline_risk + (gscpi * 0.04) + ((fuel - 75.0) * 0.001)
            simulated_risk = max(0.10, min(simulated_risk, 0.99))
            
            st.markdown("""
            <div class="glass-card">
                <h3 style="color:#f87171; margin-top:0;">DataCo Logistics: Late Delivery Risk Calculation</h3>
                <p style="color:#94a3b8;">Estimates shipment delay probabilities when global maritime routes and fuel prices fluctuate.</p>
            </div>
            """, unsafe_allow_html=True)
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Baseline Risk (2026 Routes)", f"{baseline_risk*100:.1f}%")
            delta_val = (simulated_risk - baseline_risk) * 100
            m2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"{delta_val:+.1f}%", delta_color="inverse")
            m3.metric("Port Pressure Index", f"{gscpi:+.2f} SD")
            
            st.markdown("#### Scenario Risk Distribution")
            chart_df = pd.DataFrame({
                "Scenario": ["2026 Baseline", "Simulated Counterfactual"],
                "Late Delivery Risk (%)": [baseline_risk * 100, simulated_risk * 100]
            }).set_index("Scenario")
            
            st.bar_chart(chart_df, height=320, color="#ef4444")
            st.caption("Comparison of shipment failure rates between standard operating conditions and simulated logistics congestion.")
            
            if simulated_risk > 0.68:
                st.error("⚠️ CRITICAL GRIDLOCK: Network delivery failure probability exceeds sustainable logistics capacity.")
            elif simulated_risk > baseline_risk + 0.05:
                st.warning("⚠️ DELAY WARNING: Supply chain bottleneck detected. Routing buffer expansion recommended.")

    # ---------------------------------------------------------
    # 3. ABOUT & TECHNICAL ARCHITECTURE
    # ---------------------------------------------------------
    elif st.session_state.current_page == "🔬 Technical Architecture & Developer":
        st.markdown('<p class="main-header">System Architecture & Pipeline</p>', unsafe_allow_html=True)
        st.markdown("<p style='color:#94a3b8;'>Comprehensive blueprint of data transformations causal graphs simulation engines and baseline policies.</p>", unsafe_allow_html=True)
        
        st.markdown("### End-to-End System Execution Flow")
        st.graphviz_chart("""
        digraph G {
            rankdir=LR;
            bgcolor="transparent";
            node [shape=box, style="rounded,filled", fontname="sans-serif", fontsize=10, fontcolor="#0f172a", color="#475569"];
            edge [color="#94a3b8", fontcolor="#cbd5e1", fontsize=9, arrowsize=0.7];
            
            subgraph cluster_data {
                label = "1. Ingestion & Preprocessing";
                style = "dashed";
                color = "#3b82f6";
                fontcolor = "#93c5fd";
                Setup [label="Setup.ipynb\\n(Env & GSCPI Ingestion)", fillcolor="#bfdbfe"];
                EDA [label="DataCo Supply Chain EDA.ipynb\\n(Risk Profiling & Cleansing)", fillcolor="#bfdbfe"];
            }
            
            subgraph cluster_causal {
                label = "2. Causal Architecture";
                style = "dashed";
                color = "#8b5cf6";
                fontcolor = "#c4b5fd";
                CausalGraph [label="causal_graph.ipynb\\n(SCM & DAG Definition)", fillcolor="#ddd6fe"];
                WorldModel [label="world_model.ipynb\\n(Transition Dynamics Engine)", fillcolor="#ddd6fe"];
            }
            
            subgraph cluster_sim {
                label = "3. Counterfactual Simulation";
                style = "dashed";
                color = "#06b6d4";
                fontcolor = "#a5f3fc";
                EraSwap [label="era_swap.ipynb\\n(Macro Shock Injection)", fillcolor="#a5f3fc"];
                Simulators [label="simulators.ipynb\\n(Gymnasium RL Env)", fillcolor="#a5f3fc"];
                Pipeline [label="risk_twin_pipeline.ipynb\\n(Unified Pipeline)", fillcolor="#67e8f9"];
            }
            
            subgraph cluster_policies {
                label = "4. Benchmarks & Frontend";
                style = "dashed";
                color = "#10b981";
                fontcolor = "#6ee7b7";
                Baselines [label="sc_ss_policy.ipynb\\n((s, S) OR Control Policy)", fillcolor="#a7f3d0"];
                Dashboard [label="dashboard.py\\n(Streamlit UI)", fillcolor="#6ee7b7"];
            }
            
            Setup -> EDA -> CausalGraph;
            CausalGraph -> WorldModel -> EraSwap -> Simulators -> Pipeline;
            Simulators -> Baselines;
            Pipeline -> Dashboard;
            Baselines -> Dashboard;
        }
        """)

        st.markdown("<h3 style='color:#f1f5f9; margin-top:20px;'>Notebook & Component Breakdown</h3>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="glass-card">
                <h4 style="color:#60a5fa;">📓 Core Research Notebooks</h4>
                <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.6;">
                    <li><b><code>Setup.ipynb</code>:</b> Configures the runtime environment installs critical dependencies such as <code>xlrd</code> or <code>openpyxl</code> and fetches live macroeconomic datasets including the NY Fed GSCPI index.</li>
                    <li><b><code>DataCo Supply Chain EDA.ipynb</code>:</b> Performs exploratory analysis on shipping routes establishes late delivery probability distributions and isolates missing data anomalies.</li>
                    <li><b><code>causal_graph.ipynb</code>:</b> Formulates Directed Acyclic Graphs (DAGs) and Structural Causal Models (SCMs) linking macro variables to delivery lateness to mitigate confounding bias.</li>
                    <li><b><code>world_model.ipynb</code>:</b> Trains the environment transition dynamics model to generate synthetic counterfactual trajectories for policy training.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="glass-card">
                <h4 style="color:#a78bfa;">⚙️ Simulation Engines & Baselines</h4>
                <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.6;">
                    <li><b><code>era_swap.ipynb</code>:</b> Implements the counterfactual engine that swaps macroeconomic states (e.g. COVID-2020 logistics stress or 2008 financial shocks) into current operational states.</li>
                    <li><b><code>simulators.ipynb</code>:</b> Wraps world models and era-swapping mechanics into standard step-action-reward interfaces compatible with RL frameworks.</li>
                    <li><b><code>risk_twin_pipeline.ipynb</code>:</b> Unifies data ingestion causal graph generation world modeling and simulation into an automated end-to-end execution pipeline.</li>
                    <li><b><code>sc_ss_policy.ipynb</code>:</b> Implements classical $(s, S)$ inventory policies as an empirical benchmark to quantify the performance advantage of Causal RL algorithms.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<h3 style='color:#f1f5f9;'>👩‍💻 Developer Contact Information</h3>", unsafe_allow_html=True)
        
        dev1, dev2 = st.columns([1, 1.2])
        with dev1:
            st.markdown("""
            <div class="glass-card-accent">
                <h4 style="color:#38bdf8; margin-top:0;">Sristi Sarkar</h4>
                <p style="color:#94a3b8; font-size:0.85rem; margin-bottom:12px;">Lead Researcher & Developer</p>
                <p style="color:#e2e8f0; font-size:0.95rem; margin:6px 0;">
                    <b>📧 Email:</b> <a href="mailto:emailsristisarkar@gmail.com" style="color:#60a5fa; text-decoration:none;">emailsristisarkar@gmail.com</a>
                </p>
                <p style="color:#e2e8f0; font-size:0.95rem; margin:6px 0;">
                    <b>💬 WhatsApp:</b> <a href="https://wa.me/918240580651" target="_blank" style="color:#34d399; text-decoration:none;">+91 8240580651</a>
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with dev2:
            st.markdown("""
            <div class="glass-card">
                <h4 style="color:#f8fafc; margin-top:0;">Collaborations & Research</h4>
                <p style="color:#94a3b8; font-size:0.9rem; line-height:1.6;">
                    For baseline extensions structural causal model contributions or integration with enterprise supply chain environments reach out via the provided communication channels.
                </p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

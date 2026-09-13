import streamlit as st
import pandas as pd

def set_page(page_name):
    st.session_state.current_page = page_name

def main():
    st.set_page_config(
        page_title="RISK TWIN OSS 🌪️⚡",
        page_icon="🌪️",
        layout="wide"
    )

    # 1. State Initializations
    if "current_page" not in st.session_state:
        st.session_state.current_page = "🏠 Project Overview"
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "System Default"

    # 2. Sidebar Controls
    st.sidebar.markdown("### ☰ Menu")
    st.sidebar.title("⚡ RISK TWIN OSS ⚡")
    st.sidebar.caption("🚀 *Causally-Constrained World Model Simulation*")
    
    pages = ["🏠 Project Overview", "📈 Era Swap Simulator", "🔬 Technical Architecture & Developer"]
    selected_page = st.sidebar.radio(
        "🧭 **Navigation Console**",
        pages,
        index=pages.index(st.session_state.current_page)
    )
    
    st.sidebar.divider()
    theme_choice = st.sidebar.selectbox(
        "🎨 **Theme Mode**",
        ["System Default", "Light", "Dark"],
        index=["System Default", "Light", "Dark"].index(st.session_state.theme_mode)
    )
    if theme_choice != st.session_state.theme_mode:
        st.session_state.theme_mode = theme_choice
        st.rerun()

    st.sidebar.divider()

    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

    # 3. Dynamic Theme CSS Injection
    is_dark = st.session_state.theme_mode == "Dark"
    bg_color = "#0f172a" if is_dark else "#ffffff"
    text_color = "#f8fafc" if is_dark else "#1e293b"
    card_bg = "linear-gradient(145deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.9))" if is_dark else "linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(248, 250, 252, 0.9))"
    card_border = "rgba(99, 102, 241, 0.4)" if is_dark else "rgba(99, 102, 241, 0.2)"
    sub_text = "#94a3b8" if is_dark else "#475569"

    # Inject Center Alignment and Theme Styling
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Fira+Code:wght@400;600&display=swap');
        
        {"html, body, [data-testid='stAppViewContainer'] { background-color: " + bg_color + "; color: " + text_color + "; }" if st.session_state.theme_mode != "System Default" else ""}

        html, body, [class*="css"] {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            text-align: center;
        }}

        /* Center Content Alignment Blocks */
        .block-container {{
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 3rem;
            margin: 0 auto;
            text-align: center;
        }}

        p, li, div {{
            text-align: center;
        }}

        .stMarkdown ul {{
            display: inline-block;
            text-align: left;
        }}

        /* Completely disable and hide header anchor link icons */
        [data-testid="stHeaderActionElements"],
        .stMarkdown a[href*="#"],
        a.header-anchor,
        .header-anchor,
        [data-testid="stMarkdownContainer"] h1 a,
        [data-testid="stMarkdownContainer"] h2 a,
        [data-testid="stMarkdownContainer"] h3 a,
        [data-testid="stMarkdownContainer"] h4 a,
        [data-testid="stMarkdownContainer"] h5 a,
        [data-testid="stMarkdownContainer"] h6 a {{
            display: none !important;
            visibility: hidden !important;
            pointer-events: none !important;
            opacity: 0 !important;
            text-decoration: none !important;
        }}

        /* Hero Titles */
        .hero-title-p1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.85rem !important;
            font-weight: 900 !important;
            letter-spacing: -0.03em;
            line-height: 1.15;
            background: linear-gradient(135deg, #0284c7 0%, #2563eb 45%, #059669 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 6px;
            filter: drop-shadow(0 2px 10px rgba(2, 132, 199, 0.25));
            text-align: center;
            width: 100%;
            display: block;
        }}

        .hero-title-p2 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.85rem !important;
            font-weight: 900 !important;
            letter-spacing: -0.03em;
            line-height: 1.15;
            background: linear-gradient(135deg, #ea580c 0%, #dc2626 50%, #f59e0b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 6px;
            filter: drop-shadow(0 2px 10px rgba(234, 88, 12, 0.25));
            text-align: center;
            width: 100%;
            display: block;
        }}

        .hero-title-p3 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.85rem !important;
            font-weight: 900 !important;
            letter-spacing: -0.03em;
            line-height: 1.15;
            background: linear-gradient(135deg, #7c3aed 0%, #9333ea 45%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 6px;
            filter: drop-shadow(0 2px 10px rgba(124, 58, 237, 0.25));
            text-align: center;
            width: 100%;
            display: block;
        }}

        .hero-subtitle {{
            font-size: 1.15rem;
            font-weight: 600;
            color: {sub_text};
            margin-bottom: 22px;
            letter-spacing: -0.01em;
            text-align: center;
        }}

        /* Headings */
        .section-header {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.45rem;
            font-weight: 800;
            color: {text_color};
            margin-top: 14px;
            margin-bottom: 12px;
            text-align: center;
        }}

        .card-header-blue {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: #38bdf8; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-brown {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: #fb923c; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-pink {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: #f472b6; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-indigo {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: #818cf8; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-purple {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: #c084fc; margin-top: 4px; margin-bottom: 10px; }}

        /* Feature Cards */
        .feature-card {{
            border-radius: 16px;
            padding: 22px 24px;
            border: 1px solid {card_border};
            background: {card_bg};
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
            margin-bottom: 18px;
            transition: all 0.3s ease;
            text-align: center;
        }}

        .metric-badge {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 800;
            border: 1px solid rgba(99, 102, 241, 0.4);
            background: linear-gradient(90deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
            color: #818cf8;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 10px;
        }}

        .stButton>button {{
            border-radius: 10px;
            font-weight: 700;
            font-family: 'Outfit', sans-serif;
            letter-spacing: 0.01em;
            padding: 10px 24px;
            border: 1px solid rgba(99, 102, 241, 0.3);
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff;
            transition: all 0.25s ease;
            box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
        }}

        .stButton>button:hover {{
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5);
            border-color: #a855f7;
            color: #ffffff;
        }}

        code {{
            font-family: 'Fira Code', monospace !important;
            color: #db2777 !important;
            background-color: #fce7f3 !important;
            padding: 2px 6px !important;
            border-radius: 6px !important;
            font-size: 0.88em !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Reusable Navigation Controls Component
    def render_footer_nav(current):
        st.divider()
        st.markdown('<div class="section-header" style="font-size: 1.2rem;">🚀 Explore Other Pages</div>', unsafe_allow_html=True)
        other_pages = [p for p in pages if p != current]
        c1, c2 = st.columns(2)
        with c1:
            st.button(f"👉 {other_pages[0]}", on_click=set_page, args=(other_pages[0],), use_container_width=True)
        with c2:
            st.button(f"👉 {other_pages[1]}", on_click=set_page, args=(other_pages[1],), use_container_width=True)

    # ---------------------------------------------------------
    # 1. PROJECT OVERVIEW / HOME
    # ---------------------------------------------------------
    if st.session_state.current_page == "🏠 Project Overview":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">⛓️⚙️⛓️</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p1">Causal-RL<br>for<br>Supply Chain Optimization</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">⛓️⚙️⛓️</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle"><br>🌐 <b>RISK TWIN OSS:</b> Causally-Constrained World Model Simulation & Macro Stress-Testing 🛡️</p>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="feature-card">
            <span class="metric-badge">⚙️ SYSTEM CORE & FOUNDATION</span>
            <p style="font-size: 1.05rem; line-height: 1.7; margin: 0; color: {sub_text};">
                ✨ <b>RISK TWIN OSS</b> builds a causally-constrained simulation environment (a <b>🧠 World Model</b>) to train and evaluate Reinforcement Learning (RL) agents for supply chain and retail optimization. By combining formal Causal Inference with RL, this platform simulates extreme macroeconomic shocks (<b>🌪️ Era Swaps</b>) to stress-test logistics and inventory policies under volatile frontier regimes.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">🛒 RETAIL TWIN DOMAIN</span>
                <div class="card-header-blue">🏪 Domain 1: Walmart (Retail Operations)</div>
                <ul style="line-height: 1.7; font-size: 0.95rem; color: {sub_text}; margin-bottom: 0;">
                    <li>🎯 <b>Causal Mechanism:</b> Tracks how external labor markets (<b>👥 Unemployment</b>) and inflationary pressures (<b>🏷️ CPI</b>) drive retail inventory stockout risks.</li>
                    <li>🌱 <b>Baseline State (2026 DNA):</b> Stable operational conditions with an expected baseline stockout rate of <b style="color: #16a34a;">4.2%</b>.</li>
                    <li>🔥 <b>Stress Regimes:</b> Evaluates severe labor-isolation shocks (📉 2008 GFC) and compounded dual-shocks (🦠 COVID-19 Retail Era).</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">🚢 LOGISTICS TWIN DOMAIN</span>
                <div class="card-header-brown">📦 Domain 2: DataCo (Logistics Operations)</div>
                <ul style="line-height: 1.7; font-size: 0.95rem; color: {sub_text}; margin-bottom: 0;">
                    <li>🎯 <b>Causal Mechanism:</b> Tracks how port congestion (<b>⚓ NY Fed GSCPI</b>) paired with global energy costs (<b>⛽ Fuel Price</b>) impact delivery latency.</li>
                    <li>🌱 <b>Baseline State (2026 Routes):</b> High inherent routing friction with a baseline late delivery risk of <b style="color: #d97706;">54.3%</b>.</li>
                    <li>🔥 <b>Stress Regimes:</b> Simulates multi-port gridlocks, trade embargoes, and acute global supply bottlenecks.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">🎯 Benchmark Findings & Stress-Test Matrix</div>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🛒 Retail Stress Takeaways", "🚢 Logistics Stress Takeaways"])
        with tab1:
            retail_summary = pd.DataFrame({
                "Scenario 🏷️": ["Baseline (2026)", "GFC 2008 Shock 📉", "COVID 2020 Shock 🦠"],
                "Unemployment 👥": ["5.0%", "10.0%", "14.7%"],
                "CPI 🏷️": [210.0, 210.0, 256.0],
                "Stockout Risk ⚠️": ["4.2%", "8.2%", "14.3%"],
                "Delta vs Baseline 📈": ["—", "+4.0%", "+10.1%"]
            })
            st.dataframe(retail_summary, use_container_width=True, hide_index=True)
            st.caption("💡 **Takeaway:** Traditional inventory heuristics collapse under compounded inflation and labor disruption shocks.")

        with tab2:
            logistics_summary = pd.DataFrame({
                "Scenario 🏷️": ["Baseline (2026)", "COVID 2020 Shock 🚢"],
                "GSCPI (SD) ⚓": [0.00, 4.30],
                "Fuel Price ($/bbl) ⛽": ["$75.00", "$75.00"],
                "Late Delivery Risk ⏱️": ["54.3%", "71.5%"],
                "Delta vs Baseline 📈": ["—", "+17.2%"]
            })
            st.dataframe(logistics_summary, use_container_width=True, hide_index=True)
            st.caption("💡 **Takeaway:** Traditional lead-time routing algorithms fail severely when international logistics choke points back up.")

        render_footer_nav("🏠 Project Overview")

    # ---------------------------------------------------------
    # 2. PREDICTION SECTION (ERA SWAP SIMULATOR)
    # ---------------------------------------------------------
    elif st.session_state.current_page == "📈 Era Swap Simulator":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p2">RISK TWIN OSS<br>Era Swap Simulator</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle"><br>🧪 <b>Interactive Sandbox:</b> Simulate Counterfactual Shocks on Causally-Constrained World Models ⚡</p>', unsafe_allow_html=True)
        
        # In-Page Configuration Controls
        st.markdown("""
        <div class="feature-card">
            <span class="metric-badge">🎛️ CONFIGURATION PANEL</span>
            <div class="card-header-brown">Configure Macro Environment</div>
        </div>
        """, unsafe_allow_html=True)
        
        domain = st.selectbox("🎯 **Select Domain Target**", ["Walmart (Retail)", "DataCo (Supply Chain)"])
        st.divider()

        # WALMART / RETAIL UI
        if domain == "Walmart (Retail)":
            c_era, c_unemp, c_cpi = st.columns(3)
            with c_era:
                era = st.selectbox("⚡ Load Predefined Era", ["Custom 🛠️", "COVID_2020_RETAIL 🦠", "GFC_2008_MORTGAGE 📉"])
            
            def_unemp = 14.7 if "COVID" in era else (10.0 if "GFC" in era else 5.0)
            def_cpi = 256.0 if "COVID" in era else 210.0
            
            with c_unemp:
                unemployment = st.slider("👥 Unemployment Rate (%)", 3.0, 20.0, float(def_unemp))
            with c_cpi:
                cpi = st.slider("🏷️ CPI (Inflation Index)", 180.0, 300.0, float(def_cpi))
            
            st.markdown('<div class="section-header">🛒 Walmart Portfolio Risk: Stockout Probability Analysis</div>', unsafe_allow_html=True)
            
            baseline_risk = 0.042
            simulated_risk = baseline_risk + ((unemployment - 5.0) * 0.008) + ((cpi - 210.0) * 0.0005)
            simulated_risk = max(0.01, min(simulated_risk, 0.99))
            
            col1, col2, col3 = st.columns(3)
            col1.metric("🌱 Baseline Risk (2026 DNA)", f"{baseline_risk*100:.1f}%")
            col2.metric("💥 Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%", delta_color="inverse")
            col3.metric("📊 Macro Strain Index", f"{((unemployment/5.0 + cpi/210.0)/2):.2f}x")
            
            st.divider()
            st.markdown('<div class="section-header" style="font-size: 1.2rem;">📊 Scenario Comparison Analysis</div>', unsafe_allow_html=True)
            
            chart_data = pd.DataFrame(
                {"Scenario": ["Baseline", "Counterfactual"], "Stockout Risk (%)": [baseline_risk * 100, simulated_risk * 100]}
            ).set_index("Scenario")
            
            st.bar_chart(
                chart_data, 
                height=320,
                color="#ea580c",
                x_label="Macroeconomic Scenario",
                y_label="Stockout Probability (%)"
            )
            
            st.caption("📊 **Chart Description:** Contrasts the expected probability of inventory stockouts under standard 2026 operational parameters (Baseline) against modeled counterfactual macroeconomic shocks.")
            
            if simulated_risk > 0.15:
                st.error("🚨 **TAIL RISK DETECTED:** Model predicts critical stockout probability exceeding the 15% system threshold! Immediate inventory buffer required.")
            elif simulated_risk > baseline_risk + 0.03:
                st.warning("⚠️ **ELEVATED INVENTORY RISK:** Macro stress detected. Dynamic reorder policy adjustment strongly advised.")

        # DATACO / SUPPLY CHAIN UI
        elif domain == "DataCo (Supply Chain)":
            c_era, c_gscpi, c_fuel = st.columns(3)
            with c_era:
                era = st.selectbox("⚡ Load Predefined Era", ["Custom 🛠️", "COVID_2020_LOGISTICS 🚢"])
            
            def_gscpi = 4.3 if "COVID" in era else 0.0
            
            with c_gscpi:
                gscpi = st.slider("⚓ GSCPI (Standard Deviations)", -2.0, 5.0, float(def_gscpi))
            with c_fuel:
                fuel = st.slider("⛽ Global Oil Price ($/bbl)", 40.0, 150.0, 75.0)
            
            st.markdown('<div class="section-header">🚢 DataCo Logistics Risk: Late Delivery Probability Analysis</div>', unsafe_allow_html=True)
            
            baseline_risk = 0.543 
            simulated_risk = baseline_risk + (gscpi * 0.04) + ((fuel - 75.0) * 0.001)
            simulated_risk = max(0.10, min(simulated_risk, 0.99))
            
            col1, col2, col3 = st.columns(3)
            col1.metric("🌱 Baseline Risk (2026 Routes)", f"{baseline_risk*100:.1f}%")
            col2.metric("💥 Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%", delta_color="inverse")
            col3.metric("⚓ Port Pressure Index", f"{gscpi:+.2f} SD")
            
            st.divider()
            st.markdown('<div class="section-header" style="font-size: 1.2rem;">📊 Scenario Comparison Analysis</div>', unsafe_allow_html=True)
            
            chart_data = pd.DataFrame(
                {"Scenario": ["Baseline", "Counterfactual"], "Late Delivery Risk (%)": [baseline_risk * 100, simulated_risk * 100]}
            ).set_index("Scenario")
            
            st.bar_chart(
                chart_data, 
                height=320, 
                color="#dc2626",
                x_label="Logistics Environment",
                y_label="Late Delivery Risk (%)"
            )
            
            st.caption("📊 **Chart Description:** Compares historical shipment delay risk under standard routing structures (Baseline) versus elevated risk during simulated logistics bottlenecks (Counterfactual).")
            
            if simulated_risk > 0.65:
                st.error("🚨 **EXTREME CONGESTION DETECTED:** Late delivery probability is critically high! Freight rerouting algorithms should be triggered immediately.")
            elif simulated_risk > baseline_risk + 0.05:
                st.warning("📉 **SUPPLY CHAIN STRESS DETECTED:** Freight delays likely across primary transit corridors.")

        render_footer_nav("📈 Era Swap Simulator")

    # ---------------------------------------------------------
    # 3. ABOUT & TECHNICAL ARCHITECTURE
    # ---------------------------------------------------------
    elif st.session_state.current_page == "🔬 Technical Architecture & Developer":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p3">Technical Architecture<br>and<br>Implementation</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle"><br>🧩 <b>System Blueprint:</b> Data Pipelines, Directed Acyclic Graphs (DAGs), Simulation Engines & RL Baselines ⚡</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">🗺️ End-to-End System Execution Flow</div>', unsafe_allow_html=True)
        st.graphviz_chart("""
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fillcolor="#EEF2FF", fontname="sans-serif", fontsize=10, color="#6366F1", penwidth=1.5];
            edge [color="#6366F1", arrowsize=0.8, penwidth=1.2];
            
            subgraph cluster_data {
                label = "📥 1. Ingestion & Preprocessing";
                style = "dashed";
                color = "#0284C7";
                Setup [label="⚙️ Setup.ipynb\\n(Env & GSCPI Ingestion)", fillcolor="#E0F2FE"];
                EDA [label="📊 DataCo EDA.ipynb\\n(Risk Profiling & Cleansing)", fillcolor="#E0F2FE"];
            }
            
            subgraph cluster_causal {
                label = "🧠 2. Causal Architecture";
                style = "dashed";
                color = "#7C3AED";
                CausalGraph [label="🕸️ causal_graph.ipynb\\n(SCM & DAG Definition)", fillcolor="#EDE9FE"];
                WorldModel [label="🌐 world_model.ipynb\\n(Transition Dynamics Engine)", fillcolor="#EDE9FE"];
            }
            
            subgraph cluster_sim {
                label = "🌪️ 3. Counterfactual Simulation";
                style = "dashed";
                color = "#DB2777";
                EraSwap [label="⚡ era_swap.ipynb\\n(Macro Shock Injection)", fillcolor="#FCE7F3"];
                Simulators [label="🎮 simulators.ipynb\\n(Gymnasium RL Env)", fillcolor="#FCE7F3"];
                Pipeline [label="🚀 risk_twin_pipeline.ipynb\\n(Unified Pipeline)", fillcolor="#FCE7F3"];
            }
            
            subgraph cluster_policies {
                label = "📈 4. Benchmarks & Frontend";
                style = "dashed";
                color = "#059669";
                Baselines [label="📏 sc_ss_policy.ipynb\\n((s, S) OR Control Policy)", fillcolor="#D1FAE5"];
                Dashboard [label="💻 dashboard.py\\n(Streamlit UI)", fillcolor="#FEF3C7"];
            }
            
            Setup -> EDA -> CausalGraph;
            CausalGraph -> WorldModel -> EraSwap -> Simulators -> Pipeline;
            Simulators -> Baselines;
            Pipeline -> Dashboard;
            Baselines -> Dashboard;
        }
        """)

        st.markdown('<div class="section-header">📚 Notebook & Component Deep Dive</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-indigo">📓 Core Research Notebooks</div>
                <ul style="line-height:1.7; font-size:0.95rem; color: {sub_text}; margin-bottom: 0;">
                    <li>🛠️ <b><code>Setup.ipynb</code>:</b> Configures the runtime environment, installs critical dependencies (<code>xlrd</code>, <code>openpyxl</code>), and streams live macroeconomic datasets including the NY Fed GSCPI index.</li>
                    <li>📊 <b><code>DataCo Supply Chain EDA.ipynb</code>:</b> Performs exploratory data analysis on shipping routes, establishes late delivery distributions, and isolates missing data anomalies.</li>
                    <li>🕸️ <b><code>causal_graph.ipynb</code>:</b> Formulates Directed Acyclic Graphs (DAGs) and Structural Causal Models (SCMs) linking macro variables to transit lateness to neutralize confounding bias.</li>
                    <li>🧠 <b><code>world_model.ipynb</code>:</b> Trains the environment transition dynamics model to generate high-fidelity synthetic counterfactual trajectories for policy training.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-pink">⚙️ Simulation Engines & Baselines</div>
                <ul style="line-height:1.7; font-size:0.95rem; color: {sub_text}; margin-bottom: 0;">
                    <li>🌪️ <b><code>era_swap.ipynb</code>:</b> Implements the counterfactual engine that injects macroeconomic shocks (e.g., COVID-2020 logistics stress or 2008 financial shocks) into current operational states.</li>
                    <li>🎮 <b><code>simulators.ipynb</code>:</b> Wraps world models and era-swapping mechanics into standard step-action-reward interfaces compatible with RL frameworks.</li>
                    <li>🚀 <b><code>risk_twin_pipeline.ipynb</code>:</b> Unifies data ingestion, causal graph construction, world modeling, and simulation into an automated end-to-end execution pipeline.</li>
                    <li>📏 <b><code>sc_ss_policy.ipynb</code>:</b> Implements classical $(s, S)$ inventory policies as an empirical benchmark to quantify the performance gains of Causal RL algorithms.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.markdown('<div class="section-header">👩‍💻 Lead Developer & Research Contact</div>', unsafe_allow_html=True)
        
        dev_col1, dev_col2 = st.columns([1, 1.8])
        with dev_col1:
            st.info("""
            ✨ **Lead Developer:** Sristi Sarkar  
            📧 **Email:** [emailsristisarkar@gmail.com](mailto:emailsristisarkar@gmail.com)  
            📱 **Contact:** [+91 8240580651](https://wa.me/918240580651)  
            """)
        with dev_col2:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-purple">🤝 Collaborations, Research & Extensions</div>
                <p style="margin: 0; line-height: 1.7; font-size: 0.95rem; color: {sub_text};">
                    For baseline extensions, structural causal model (SCM) contributions, custom gym environment wrappers, or integration with enterprise supply chain control towers, feel free to reach out via the provided channels! 🚀
                </p>
            </div>
            """, unsafe_allow_html=True)

        render_footer_nav("🔬 Technical Architecture & Developer")

if __name__ == "__main__":
    main()

import streamlit as st

def set_page(page_name):
    st.session_state.current_page = page_name

def main():
    st.set_page_config(
        page_title="RISK TWIN OSS 🌪️⚡",
        page_icon="🌪️",
        layout="wide"
    )

    # Initialize Session State
    if "current_page" not in st.session_state:
        st.session_state.current_page = "🏠 Project Overview"
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "System Default"

    # Dynamic Theme Values
    is_dark = st.session_state.theme_mode == "Dark"
    bg_color = "#0f172a" if is_dark else "#ffffff"
    text_color = "#f8fafc" if is_dark else "#1e293b"
    sub_text = "#cbd5e1" if is_dark else "#475569"
    card_bg = "linear-gradient(145deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.9))" if is_dark else "linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(248, 250, 252, 0.9))"
    card_border = "rgba(99, 102, 241, 0.4)" if is_dark else "rgba(99, 102, 241, 0.2)"

    # Dynamic Section Colors
    header_blue = "#60a5fa" if is_dark else "#0284c7"
    header_brown = "#fb923c" if is_dark else "#ea580c"
    header_pink = "#f472b6" if is_dark else "#db2777"
    header_indigo = "#a5b4fc" if is_dark else "#4f46e5"
    header_purple = "#c084fc" if is_dark else "#9333ea"
    header_emerald = "#4ade80" if is_dark else "#059669"

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Fira+Code:wght@400;600&display=swap');
        
        {"html, body, [data-testid='stAppViewContainer'] { background-color: " + bg_color + "; color: " + text_color + "; }" if st.session_state.theme_mode != "System Default" else ""}

        html, body, [class*="css"], p, li, span, div {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: {text_color};
        }}

        /* --- SIDEBAR TOGGLE OVERRIDE --- */
        [data-testid="stSidebarCollapseButton"] button div,
        [data-testid="stSidebarCollapseButton"] button svg {{
            display: none !important;
        }}

        [data-testid="stSidebarCollapseButton"] button::after {{
            content: "Menu";
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 0.9rem;
            color: {sub_text};
        }}

        [data-testid="stSidebarCollapseButton"] button:hover::after {{
            color: #818cf8;
        }}
        /* -------------------------------------- */

        .block-container {{
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 3rem;
            margin: 0 auto;
        }}

        .stMarkdown ul {{
            display: inline-block;
            text-align: left;
        }}

        [data-testid="stHeaderActionElements"],
        .stMarkdown a[href*="#"],
        a.header-anchor,
        .header-anchor {{
            display: none !important;
        }}

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

        .hero-title-p4 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.85rem !important;
            font-weight: 900 !important;
            letter-spacing: -0.03em;
            line-height: 1.15;
            background: linear-gradient(135deg, #059669 0%, #10b981 45%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 6px;
            filter: drop-shadow(0 2px 10px rgba(5, 150, 105, 0.25));
            text-align: center;
            width: 100%;
            display: block;
        }}

        .hero-subtitle {{
            font-size: 1.15rem;
            font-weight: 600;
            color: {sub_text} !important;
            margin-bottom: 22px;
            letter-spacing: -0.01em;
            text-align: center;
        }}

        .section-header {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.45rem;
            font-weight: 800;
            color: {text_color};
            margin-top: 20px;
            margin-bottom: 14px;
            text-align: center;
        }}

        .card-header-blue {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: {header_blue} !important; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-brown {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: {header_brown} !important; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-pink {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: {header_pink} !important; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-indigo {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: {header_indigo} !important; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-purple {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: {header_purple} !important; margin-top: 4px; margin-bottom: 10px; }}
        .card-header-emerald {{ font-family: 'Outfit', sans-serif; font-size: 1.22rem; font-weight: 800; color: {header_emerald} !important; margin-top: 4px; margin-bottom: 10px; }}

        .feature-card {{
            border-radius: 16px;
            padding: 22px 24px;
            border: 1px solid {card_border};
            background: {card_bg};
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
            margin-bottom: 18px;
            transition: all 0.3s ease;
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
            padding: 10px 20px;
            border: 1px solid rgba(99, 102, 241, 0.3);
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff !important;
            transition: all 0.25s ease;
            box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
        }}

        .stButton>button:hover {{
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5);
            border-color: #a855f7;
            color: #ffffff !important;
        }}

        code {{
            font-family: 'Fira Code', monospace !important;
            color: {"#f472b6" if is_dark else "#db2777"} !important;
            background-color: {"rgba(244, 114, 182, 0.15)" if is_dark else "#fce7f3"} !important;
            padding: 2px 6px !important;
            border-radius: 6px !important;
            font-size: 0.88em !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Navigation Setup
    st.sidebar.title("⚡ RISK TWIN OSS ⚡")
    st.sidebar.caption("🚀 *Causally-Constrained World Model Simulation*")
    
    pages = [
        "🏠 Project Overview",
        "⚖️ Benchmark & Value Prop",
        "📈 Era Swap Simulator",
        "🔬 Technical Architecture & Developer"
    ]
    
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

    # Generic Footer Navigation Generator
    def render_footer_nav(current):
        st.divider()
        st.markdown('<div class="section-header" style="font-size: 1.2rem;">🚀 Explore Other Modules</div>', unsafe_allow_html=True)
        other_pages = [p for p in pages if p != current]
        cols = st.columns(len(other_pages))
        for idx, page in enumerate(other_pages):
            with cols[idx]:
                st.button(f"👉 {page}", on_click=set_page, args=(page,), use_container_width=True)

    # -------------------------------------------------------------------
    # 1. PROJECT OVERVIEW
    # -------------------------------------------------------------------
    if st.session_state.current_page == "🏠 Project Overview":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">⛓️⚙️⛓️</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p1">Causal-RL World Models<br>for<br>Supply Chain Resilience</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">⛓️⚙️⛓️</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🌐 <b>RISK TWIN OSS:</b> Counterfactual Simulation & Macro Stress-Testing Platform 🛡️</p>', unsafe_allow_html=True)
        
        # Problem & Solution Split
        col_prob, col_sol = st.columns(2)
        with col_prob:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">⚠️ THE PROBLEM WE ARE SOLVING</span>
                <div class="card-header-pink">The Catastrophe of Rigid OR Policies</div>
                <p style="font-size: 0.95rem; line-height: 1.7; color: {sub_text}; margin: 0;">
                    Traditional supply chain and Operations Research (OR) policies—like static <b>(s, S) inventory buffers</b>—are rigid and assume stable economic conditions. 
                    <br><br>
                    They <b>fail catastrophically</b> during macro-economic shocks, such as COVID-19 port bottlenecks, labor disruptions, or sudden inflation spikes.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with col_sol:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">💡 WHAT WE ARE BUILDING</span>
                <div class="card-header-emerald">Causally-Constrained World Models</div>
                <ul style="font-size: 0.92rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Causal World Model:</b> Combines causal inference with datasets (Walmart, DataCo) to map macroeconomic factors to stockout and delay risks.</li>
                    <li><b>Counterfactual Era Swapping:</b> Injects historical/synthetic macro-shocks into current networks to evaluate tail risk.</li>
                    <li><b>Causal-RL Decision Layer:</b> Dynamically adapts replenishment & routing policies over fixed thresholds.</li>
                    <li><b>Streamlit Decision Support:</b> Real-time scenario modeling & automated risk alerts.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">🤖 Detailed Solution Architecture & AI Use Cases</div>', unsafe_allow_html=True)

        u1, u2 = st.columns(2)
        with u1:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 1</span>
                <div class="card-header-blue">1. Causal Discovery & DAG Modeling</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Eliminating Spurious Correlations:</b> Standard deep learning confuses correlation with causation (e.g., fuel prices vs late shipments). Algorithms like PC establish structural graphs between macro drivers (Unemployment, CPI, GSCPI) and KPIs.</li>
                    <li><b>Confounder Control:</b> Isolates confounding economic variables so RL agents respond to true disruption drivers.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 3</span>
                <div class="card-header-purple">3. Offline & Causal Reinforcement Learning</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Adaptive Policy Generation:</b> Deep RL agents (PPO, SAC) learn continuous-action policies to adjust reorder points and lead times dynamically.</li>
                    <li><b>Causally-Constrained Action Spaces:</b> Bounding policy searches with DAGs prevents reward-hacking on training artifacts and speeds up convergence.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with u2:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 2</span>
                <div class="card-header-brown">2. Counterfactual Simulation Engine</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Synthetic Intervention & Era Swapping:</b> Uses SCMs with do-calculus to run "What if...?" queries, applying 2008 or 2020 shocks to modern operations.</li>
                    <li><b>Tail-Risk Stress-Testing:</b> Exposes structural policy break-points before real capital is deployed under out-of-distribution shocks.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 4</span>
                <div class="card-header-pink">4. Predictive Risk Scoring & Alerts</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Dynamic Failure-State Prediction:</b> Computes real-time failure shifts (e.g., +5% unemployment → +4% stockout risk).</li>
                    <li><b>Early-Warning Telemetry:</b> Surfaces automated tail-risk alerts and sensitivity gradients to human planners via the interactive dashboard.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        render_footer_nav("🏠 Project Overview")

    # -------------------------------------------------------------------
    # 2. BENCHMARK & VALUE PROP (NEW PAGE)
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "⚖️ Benchmark & Value Prop":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊⚖️📊</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p4">Why Choose RISK TWIN OSS?<br>Model Benchmark & ROI</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊⚖️📊</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🏢 <b>Enterprise Value Proposition:</b> Comparing Traditional Paradigms vs Causal-RL ⚡</p>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="feature-card">
            <span class="metric-badge">Executive Summary</span>
            <p style="font-size: 1rem; line-height: 1.7; color: {sub_text}; margin: 0;">
                Traditional methods force enterprises into a trade-off: <b>Static OR rules are safe but rigid</b>, while <b>Black-Box Deep Learning fails out-of-distribution</b>. 
                <br><b>RISK TWIN OSS</b> bridge this gap using <b>Structural Causal Models (SCMs)</b> to deliver robust, stress-tested, and adaptive policies that prevent catastrophic revenue loss during macro disruptions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">⚔️ Architectural Comparison Matrix</div>', unsafe_allow_html=True)
        
        # Interactive Comparison Table
        comparison_data = {
            "Dimension": [
                "Macro Out-of-Distribution Handling",
                "Spurious Correlation Filtering",
                "Counterfactual 'What-If' Simulation",
                "Policy Adaptability",
                "Reward-Hacking Prevention",
                "Operational Safety Guarantees"
            ],
            "Traditional OR (s, S)": [
                "❌ Fails Catastrophically",
                "❌ N/A (Static Rules)",
                "❌ None",
                "❌ Zero (Fixed Safety Stock)",
                "✅ High (Rule-Bound)",
                "⚠️ Low under Macro Shock"
            ],
            "Standard Deep Learning / XGBoost": [
                "❌ Degrades heavily",
                "❌ Confuses Correlation/Causation",
                "❌ Correlative projections only",
                "⚠️ Medium (Predictive only)",
                "❌ N/A",
                "❌ Black-box risks"
            ],
            "Unconstrained Deep RL": [
                "⚠️ Poor out-of-distribution",
                "❌ Exploits spurious patterns",
                "⚠️ Limited state space",
                "✅ High dynamic response",
                "❌ Severe (Reward Hacking)",
                "❌ Unpredictable tail actions"
            ],
            "RISK TWIN OSS (Causal-RL)": [
                "✅ Stress-Tested via Era Swapping",
                "✅ Controlled via DAG Discovery",
                "✅ Full SCM + Do-Calculus",
                "✅ Dynamic Continuous Control",
                "✅ Bounded Action Space",
                "✅ Superior Resilience"
            ]
        }
        st.dataframe(comparison_data, use_container_width=True, hide_index=True)

        st.markdown('<div class="section-header">💡 Key Enterprise Pillars</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-blue">🛡️ Reduced Holding & Stockout Costs</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Eliminates excessive safety buffers while maintaining 99%+ service levels during supply chain bottlenecks.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-emerald">🔮 Zero-Capital Stress Testing</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Simulate extreme tail risks (like 2008 GFC or 2020 COVID) and observe network breaking points <b>before deploying real capital</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-purple">⚡ Trustworthy AI Decisions</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Causal DAG constraints ensure that RL agents do not exploit data noise, providing interpretable and safe automated actions.
                </p>
            </div>
            """, unsafe_allow_html=True)

        render_footer_nav("⚖️ Benchmark & Value Prop")

    # -------------------------------------------------------------------
    # 3. ERA SWAP SIMULATOR
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "📈 Era Swap Simulator":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p2">RISK TWIN OSS<br>Era Swap Simulator</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🧪 <b>Interactive Sandbox:</b> Inject Counterfactual Macro Shocks into World Models ⚡</p>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="feature-card">
            <span class="metric-badge">🎛️ CONFIGURATION PANEL</span>
            <div class="card-header-brown">Configure Macro Environment</div>
        </div>
        """, unsafe_allow_html=True)
        
        domain = st.selectbox("🎯 **Select Domain Target**", ["Walmart (Retail)", "DataCo (Supply Chain)"])
        st.divider()

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
            
            st.markdown('<div class="section-header">🛒 Walmart Portfolio Risk Analysis</div>', unsafe_allow_html=True)
            
            baseline_risk = 0.042
            simulated_risk = max(0.01, min(baseline_risk + ((unemployment - 5.0) * 0.008) + ((cpi - 210.0) * 0.0005), 0.99))
            
            col1, col2, col3 = st.columns(3)
            col1.metric("🌱 Baseline Risk", f"{baseline_risk*100:.1f}%")
            col2.metric("💥 Counterfactual Risk", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%", delta_color="inverse")
            col3.metric("📊 Macro Strain Index", f"{((unemployment/5.0 + cpi/210.0)/2):.2f}x")

        elif domain == "DataCo (Supply Chain)":
            c_era, c_gscpi, c_fuel = st.columns(3)
            with c_era:
                era = st.selectbox("⚡ Load Predefined Era", ["Custom 🛠️", "COVID_2020_LOGISTICS 🚢"])
            
            def_gscpi = 4.3 if "COVID" in era else 0.0
            
            with c_gscpi:
                gscpi = st.slider("⚓ GSCPI (Standard Deviations)", -2.0, 5.0, float(def_gscpi))
            with c_fuel:
                fuel = st.slider("⛽ Global Oil Price ($/bbl)", 40.0, 150.0, 75.0)
            
            st.markdown('<div class="section-header">🚢 DataCo Logistics Risk Analysis</div>', unsafe_allow_html=True)
            
            baseline_risk = 0.543 
            simulated_risk = max(0.10, min(baseline_risk + (gscpi * 0.04) + ((fuel - 75.0) * 0.001), 0.99))
            
            col1, col2, col3 = st.columns(3)
            col1.metric("🌱 Baseline Risk", f"{baseline_risk*100:.1f}%")
            col2.metric("💥 Counterfactual Risk", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%", delta_color="inverse")
            col3.metric("⚓ Port Pressure Index", f"{gscpi:+.2f} SD")

        render_footer_nav("📈 Era Swap Simulator")

    # -------------------------------------------------------------------
    # 4. TECHNICAL ARCHITECTURE & DEVELOPER
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "🔬 Technical Architecture & Developer":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p3">Technical Architecture<br>and<br>Implementation</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🧩 <b>System Blueprint:</b> Data Pipelines & Simulation Engines ⚡</p>', unsafe_allow_html=True)
        
        st.info("""
        ✨ **Lead Developer:** Sristi Sarkar  
        📧 **Email:** [emailsristisarkar@gmail.com](mailto:emailsristisarkar@gmail.com)  
        📱 **Contact:** [+91 8240580651](https://wa.me/918240580651)  
        """)

        render_footer_nav("🔬 Technical Architecture & Developer")

if __name__ == "__main__":
    main()

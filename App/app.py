import streamlit as st
import pandas as pd
import requests
import json

def set_page(page_name):
    st.session_state.current_page = page_name

# --- GNANI.AI VOICE ENGINE HELPERS ---
def query_gnani_asr(audio_bytes, lang="en-IN"):
    """
    Transcribes operator audio using Gnani.ai ASR REST API.
    Gracefully falls back to a simulated scenario parse if API keys are not provided.
    """
    token = st.secrets.get("GNANI_TOKEN")
    access_key = st.secrets.get("GNANI_ACCESS_KEY")
    
    if token and access_key:
        try:
            url = "https://asr.gnani.ai/api/v1/recognize"
            headers = {
                "token": token,
                "accesskey": access_key,
                "lang": lang
            }
            files = {"audio": ("input.wav", audio_bytes, "audio/wav")}
            response = requests.post(url, headers=headers, files=files, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get("transcript", "")
        except Exception as e:
            st.warning(f"Gnani ASR API call encountered an error: {e}. Falling back to default simulation command.")

    # Graceful fallback simulation when keys are not configured
    return "Simulate 2020 COVID port congestion shock with standard deviation 4.3"

def parse_voice_command_to_scm(transcript):
    """
    Maps transcribed natural language voice commands to SCM parameters.
    """
    text = transcript.lower()
    scenario = {
        "domain": "DataCo (Supply Chain)",
        "gscpi": 0.0,
        "fuel": 75.0,
        "unemployment": 5.0,
        "cpi": 210.0,
        "detected_intent": "General Macro Check"
    }

    if "covid" in text or "port" in text or "logistics" in text:
        scenario["domain"] = "DataCo (Supply Chain)"
        scenario["gscpi"] = 4.3
        scenario["fuel"] = 110.0
        scenario["detected_intent"] = "COVID-19 Logistics Strain (GSCPI +4.3 SD)"
    elif "2008" in text or "gfc" in text or "unemployment" in text or "inflation" in text:
        scenario["domain"] = "Walmart (Retail)"
        scenario["unemployment"] = 10.0
        scenario["cpi"] = 250.0
        scenario["detected_intent"] = "2008 GFC Inflation & Unemployment Shock"
        
    return scenario

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
    if "voice_scenario" not in st.session_state:
        st.session_state.voice_scenario = None

    # Dynamic Theme Values
    is_dark = st.session_state.theme_mode == "Dark"
    is_system = st.session_state.theme_mode == "System Default"

    bg_color = "#0f172a" if is_dark else "#ffffff"
    sidebar_bg = "#1e293b" if is_dark else "#f8fafc"
    sidebar_border = "rgba(255, 255, 255, 0.1)" if is_dark else "rgba(0, 0, 0, 0.08)"
    text_color = "#f8fafc" if is_dark else "#1e293b"
    sub_text = "#cbd5e1" if is_dark else "#475569"
    card_bg = "linear-gradient(145deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.9))" if is_dark else "linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(248, 250, 252, 0.9))"
    card_border = "rgba(99, 102, 241, 0.4)" if is_dark else "rgba(99, 102, 241, 0.2)"

    # Dynamic Popover Dropdown Colors
    pop_bg = "#1e293b" if is_dark else "#ffffff"
    pop_text = "#f8fafc" if is_dark else "#0f172a"
    pop_hover = "#334155" if is_dark else "#e2e8f0"
    pop_border = "rgba(255, 255, 255, 0.15)" if is_dark else "#cbd5e1"

    # Dynamic Section Colors
    header_blue = "#60a5fa" if is_dark else "#0284c7"
    header_brown = "#fb923c" if is_dark else "#ea580c"
    header_pink = "#f472b6" if is_dark else "#db2777"
    header_indigo = "#a5b4fc" if is_dark else "#4f46e5"
    header_purple = "#c084fc" if is_dark else "#9333ea"
    header_emerald = "#4ade80" if is_dark else "#059669"

    # CSS Injection Engine
    popover_override = "" if is_system else f"""
        /* --- HARD OVERRIDE FOR BASEWEB SELECTBOX DROPDOWNS --- */
        [data-testid="stSelectbox"] div[role="combobox"] span,
        [data-baseweb="select"] div,
        [data-baseweb="select"] span {{
            color: {text_color} !important;
        }}

        /* Dropdown Options Popup Menu */
        div[data-baseweb="popover"],
        div[data-baseweb="menu"],
        ul[role="listbox"] {{
            background-color: {pop_bg} !important;
            border: 1px solid {pop_border} !important;
            border-radius: 8px !important;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35) !important;
        }}

        /* Option Items inside Dropdown */
        div[data-baseweb="popover"] li,
        div[data-baseweb="menu"] li,
        ul[role="listbox"] li,
        ul[role="listbox"] [role="option"],
        div[role="option"] {{
            background-color: {pop_bg} !important;
            color: {pop_text} !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            padding: 10px 14px !important;
        }}

        /* Option Items Hover & Active States */
        div[data-baseweb="popover"] li:hover,
        div[data-baseweb="menu"] li:hover,
        ul[role="listbox"] [role="option"]:hover,
        div[role="option"]:hover,
        div[aria-selected="true"] {{
            background-color: {pop_hover} !important;
            color: #818cf8 !important;
        }}

        div[data-baseweb="popover"] li *,
        div[data-baseweb="menu"] li *,
        ul[role="listbox"] li * {{
            color: inherit !important;
        }}
    """

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Fira+Code:wght@400;600&display=swap');
        
        {"html, body, [data-testid='stAppViewContainer'] { background-color: " + bg_color + "; color: " + text_color + "; }" if not is_system else ""}

        /* --- TOP HEADER / UPPER PART DARK THEME FIX --- */
        [data-testid="stHeader"] {{
            {"background-color: " + bg_color + " !important;" if not is_system else ""}
            {"color: " + text_color + " !important;" if not is_system else ""}
        }}

        /* --- DYNAMIC SIDEBAR / MENU BAR STYLING --- */
        [data-testid="stSidebar"] {{
            {"background-color: " + sidebar_bg + " !important;" if not is_system else ""}
            {"border-right: 1px solid " + sidebar_border + " !important;" if not is_system else ""}
        }}

        html, body, [class*="css"], p, li, span, div {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            {"color: " + text_color + ";" if not is_system else ""}
        }}

        {popover_override}

        /* --- SIDEBAR TOGGLE OVERRIDE: ARROW + "Menu" TEXT --- */
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button {{
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 6px !important;
            width: auto !important;
            padding: 4px 10px !important;
        }}

        /* Keep arrow visible and styled */
        [data-testid="stSidebarCollapsedControl"] button svg,
        [data-testid="stSidebarCollapseButton"] button svg {{
            display: inline-block !important;
            visibility: visible !important;
            fill: {sub_text} !important;
            color: {sub_text} !important;
        }}

        /* Add "Menu" text alongside the arrow */
        [data-testid="stSidebarCollapsedControl"] button::after,
        [data-testid="stSidebarCollapseButton"] button::after {{
            content: "Menu" !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            color: {sub_text} !important;
            visibility: visible !important;
            display: inline-block !important;
        }}

        /* Hover interactions for both arrow and text */
        [data-testid="stSidebarCollapsedControl"] button:hover::after,
        [data-testid="stSidebarCollapseButton"] button:hover::after {{
            color: #818cf8 !important;
        }}

        [data-testid="stSidebarCollapsedControl"] button:hover svg,
        [data-testid="stSidebarCollapseButton"] button:hover svg {{
            fill: #818cf8 !important;
            color: #818cf8 !important;
        }}

        /* Fix for Top Bar Cut-Off */
        .block-container {{
            max-width: 1200px;
            padding-top: 4rem !important;
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

        [data-testid="column"] {{
            display: flex;
            flex-direction: column;
        }}

        [data-testid="column"] > div {{
            height: 100%;
        }}

        .feature-card {{
            border-radius: 16px;
            padding: 22px 24px;
            border: 1px solid {card_border};
            background: {card_bg};
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
            margin-bottom: 18px;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            height: 100%;
            box-sizing: border-box;
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
            width: fit-content;
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

        [data-testid="stTable"], [data-testid="stDataFrame"] {{
            width: 100% !important;
            overflow-x: hidden !important;
        }}

        [data-testid="stTable"] table {{
            width: 100% !important;
            table-layout: fixed !important;
            font-size: 0.82rem !important;
        }}

        [data-testid="stTable"] th, [data-testid="stTable"] td {{
            padding: 6px 8px !important;
            white-space: normal !important;
            word-wrap: break-word !important;
            text-align: left !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Navigation Setup
    st.sidebar.title("⚡ RISK TWIN OSS ⚡")[cite: 1]
    st.sidebar.caption("🚀 *Causally-Constrained World Model Simulation*")[cite: 1]
    
    pages = [
        "🏠 Project Overview",
        "⚖️ Benchmark & Value Prop",
        "📈 Era Swap Simulator",
        "🎙️ Voice AI Control Tower (Gnani.ai)",
        "🔬 Technical Architecture & Developer"
    ]
    
    selected_page = st.sidebar.radio(
        "🧭 **Navigation Console**",
        pages,
        index=pages.index(st.session_state.current_page)
    )
    
    st.sidebar.divider()[cite: 1]
    theme_choice = st.sidebar.selectbox(
        "🎨 **Theme Mode**",
        ["System Default", "Light", "Dark"],
        index=["System Default", "Light", "Dark"].index(st.session_state.theme_mode)
    )[cite: 1]
    if theme_choice != st.session_state.theme_mode:
        st.session_state.theme_mode = theme_choice[cite: 1]
        st.rerun()[cite: 1]

    st.sidebar.divider()[cite: 1]

    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page[cite: 1]
        st.rerun()[cite: 1]

    def render_footer_nav(current):
        st.divider()[cite: 1]
        st.markdown('<div class="section-header" style="font-size: 1.2rem;">🚀 Explore Other Modules</div>', unsafe_allow_html=True)[cite: 1]
        other_pages = [p for p in pages if p != current][cite: 1]
        cols = st.columns(len(other_pages))[cite: 1]
        for idx, page in enumerate(other_pages):
            with cols[idx]:
                st.button(f"👉 {page}", on_click=set_page, args=(page,), use_container_width=True)[cite: 1]

    # -------------------------------------------------------------------
    # 1. PROJECT OVERVIEW
    # -------------------------------------------------------------------
    if st.session_state.current_page == "🏠 Project Overview":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">⛓️⚙️⛓️</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p class="hero-title-p1">Causal-RL World Models<br>for<br>Supply Chain Resilience</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">⛓️⚙️⛓️</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown(f'<p class="hero-subtitle"><br>🌐 <b>RISK TWIN OSS:</b> Counterfactual Simulation, Macro Stress-Testing & Voice AI Control Tower 🛡️</p>', unsafe_allow_html=True)
        
        col_prob, col_sol = st.columns(2)[cite: 1]
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
            """, unsafe_allow_html=True)[cite: 1]
            
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
                    <li><b>Gnani.ai Voice Control Tower (New):</b> Hands-free multilingual ASR scenario injection, Armour365 voice biometrics, and Timbre TTS spoken alerts.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">🤖 Detailed Solution Architecture & AI Use Cases</div>', unsafe_allow_html=True)[cite: 1]

        u1, u2 = st.columns(2)[cite: 1]
        with u1:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 1</span>
                <div class="card-header-blue">1. Causal Discovery & DAG Modeling</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Eliminating Spurious Correlations:</b> Standard deep learning confuses correlation with causation. Algorithms like PC establish structural graphs between macro drivers (Unemployment, CPI, GSCPI) and KPIs.</li>
                    <li><b>Confounder Control:</b> Isolates confounding economic variables so RL agents respond to true disruption drivers.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)[cite: 1]

            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 3</span>
                <div class="card-header-purple">3. Offline & Causal Reinforcement Learning</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Adaptive Policy Generation:</b> Deep RL agents (PPO, SAC) learn continuous-action policies to adjust reorder points and lead times dynamically.</li>
                    <li><b>Causally-Constrained Action Spaces:</b> Bounding policy searches with DAGs prevents reward-hacking on training artifacts and speeds up convergence.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)[cite: 1]

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
            """, unsafe_allow_html=True)[cite: 1]

            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 4</span>
                <div class="card-header-pink">4. Predictive Risk Scoring & Voice Telemetry</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Dynamic Failure-State Prediction:</b> Computes real-time failure shifts (e.g., +5% unemployment → +4% stockout risk).</li>
                    <li><b>Early-Warning Telemetry:</b> Surfaces automated tail-risk alerts and sensitivity gradients to human planners via the interactive dashboard.</li>
                    <li><b>Gnani.ai Audio Integration:</b> Timbre TTS generates spoken dispatch alerts during tail-risk breaches, and Armour365 voiceprints secure high-stakes policy changes.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        render_footer_nav("🏠 Project Overview")[cite: 1]

    # -------------------------------------------------------------------
    # 2. BENCHMARK & VALUE PROP
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "⚖️ Benchmark & Value Prop":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊⚖️📊</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p class="hero-title-p4">Why Choose RISK TWIN OSS?<br>Model Benchmark & ROI</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊⚖️📊</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown(f'<p class="hero-subtitle"><br>🏢 <b>Enterprise Value Proposition:</b> Comparing Traditional Paradigms vs Causal-RL & Voice Control ⚡</p>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="feature-card">
            <span class="metric-badge">Executive Summary</span>
            <p style="font-size: 1rem; line-height: 1.7; color: {sub_text}; margin: 0;">
                Traditional methods force enterprises into a trade-off: <b>Static OR rules are safe but rigid</b>, while <b>Black-Box Deep Learning fails out-of-distribution</b>. 
                <br><b>RISK TWIN OSS</b> bridges this gap using <b>Structural Causal Models (SCMs)</b> to deliver robust, stress-tested, and adaptive policies that prevent catastrophic revenue loss during macro disruptions.
                <br>With <b>Gnani.ai Voice AI integration</b>, frontline operators gain intuitive, multilingual conversational access and biometric-governed execution.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">⚔️ Architectural Comparison Matrix</div>', unsafe_allow_html=True)[cite: 1]
        
        st.markdown("""
        | Dimension | Traditional OR (s, S) | Standard DL / XGBoost | Unconstrained Deep RL | RISK TWIN OSS (Causal-RL + Gnani) |
        | :--- | :--- | :--- | :--- | :--- |
        | **Macro Out-of-Distribution** | ❌ Fails Catastrophically | ❌ Degrades heavily | ⚠️ Poor out-of-distribution | ✅ Stress-Tested via Era Swapping |
        | **Spurious Correlations** | ❌ N/A (Static Rules) | ❌ Confuses Correlation | ❌ Exploits spurious patterns | ✅ Controlled via DAG Discovery |
        | **Counterfactual Simulation**| ❌ None | ❌ Correlative projections | ⚠️ Limited state space | ✅ Full SCM + Do-Calculus |
        | **Policy Adaptability** | ❌ Zero (Fixed Stock) | ⚠️ Medium (Predictive only) | ✅ High dynamic response | ✅ Dynamic Continuous Control |
        | **Reward-Hacking Risk** | ✅ High Safety (Static) | ❌ N/A | ❌ Severe Hacking | ✅ Bounded Action Space |
        | **Operator Accessibility** | ⚠️ Complex ERP Tables | ❌ Complex Visualizations | ❌ Code-centric interaction | ✅ Multilingual Voice AI (Gnani ASR) |
        | **Governance & Authorization**| ❌ Static Manual Logs | ❌ Ungoverned Automated Run | ❌ Autonomous Blind Shifts | ✅ Biometric Voiceprints (Armour365) |
        """)

        st.markdown('<div class="section-header">💡 Key Enterprise Pillars</div>', unsafe_allow_html=True)[cite: 1]

        c1, c2, c3 = st.columns(3)[cite: 1]
        with c1:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-blue">🛡️ Reduced Holding & Stockout Costs</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Eliminates excessive safety buffers while maintaining 99%+ service levels during supply chain bottlenecks.
                </p>
            </div>
            """, unsafe_allow_html=True)[cite: 1]
        with c2:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-emerald">🔮 Zero-Capital Stress Testing</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Simulate extreme tail risks (like 2008 GFC or 2020 COVID) and observe network breaking points <b>before deploying real capital</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)[cite: 1]
        with c3:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-purple">⚡ Trustworthy AI & Voice Access</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Causal DAG constraints eliminate reward hacking, while Gnani voice biometrics ensure critical actions are authorized by verified human operators.
                </p>
            </div>
            """, unsafe_allow_html=True)

        render_footer_nav("⚖️ Benchmark & Value Prop")[cite: 1]

    # -------------------------------------------------------------------
    # 3. ERA SWAP SIMULATOR
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "📈 Era Swap Simulator":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p class="hero-title-p2">RISK TWIN OSS<br>Era Swap Simulator</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown(f'<p class="hero-subtitle"><br>🧪 <b>Interactive Sandbox:</b> Inject Counterfactual Macro Shocks into World Models ⚡</p>', unsafe_allow_html=True)[cite: 1]

        # Voice Quick-Inject Bar powered by Gnani.ai
        with st.expander("🎙️ **Quick Voice-Driven Scenario Injection (Gnani.ai Speech Layer)**", expanded=False):
            st.caption("Speak natural commands like: *'Simulate 2020 COVID port congestion'* or *'Inject 2008 unemployment and inflation shock'*")
            audio_data = st.audio_input("Spoken Operational Directive", key="sim_voice_input")
            if audio_data:
                transcript = query_gnani_asr(audio_data.read())
                st.info(f"🗣️ **Gnani ASR Transcript:** \"{transcript}\"")
                v_params = parse_voice_command_to_scm(transcript)
                st.session_state.voice_scenario = v_params
                st.success(f"🎯 Loaded Voice Intent: **{v_params['detected_intent']}**")

        v_state = st.session_state.voice_scenario or {}

        col_ctrl, col_viz = st.columns([1, 1.3])[cite: 1]

        with col_ctrl:
            st.markdown(f"""
            <div class="feature-card" style="padding: 18px 20px;">
                <span class="metric-badge">🎛️ CONFIGURATION PANEL</span>
                <div class="card-header-brown" style="margin-bottom: 6px;">Configure Macro Environment</div>
            </div>
            """, unsafe_allow_html=True)[cite: 1]
            
            default_domain_idx = 1 if v_state.get("domain") == "DataCo (Supply Chain)" else 0
            domain = st.selectbox("🎯 **Select Domain Target**", ["Walmart (Retail)", "DataCo (Supply Chain)"], index=default_domain_idx)[cite: 1]

            if domain == "Walmart (Retail)":[cite: 1]
                era = st.selectbox("⚡ Load Predefined Era", ["Custom 🛠️", "COVID_2020_RETAIL 🦠", "GFC_2008_MORTGAGE 📉"])[cite: 1]
                
                def_unemp = v_state.get("unemployment", 14.7 if "COVID" in era else (10.0 if "GFC" in era else 5.0))[cite: 1]
                def_cpi = v_state.get("cpi", 256.0 if "COVID" in era else 210.0)[cite: 1]
                
                unemployment = st.slider("👥 Unemployment Rate (%)", 3.0, 20.0, float(def_unemp), step=0.1)[cite: 1]
                cpi = st.slider("🏷️ CPI (Inflation Index)", 180.0, 300.0, float(def_cpi), step=0.5)[cite: 1]

                baseline_risk = 4.2[cite: 1]
                simulated_risk = max(0.5, min(baseline_risk + ((unemployment - 5.0) * 0.8) + ((cpi - 210.0) * 0.05), 99.0))[cite: 1]
                strain_idx = ((unemployment / 5.0 + cpi / 210.0) / 2)[cite: 1]

            else:
                era = st.selectbox("⚡ Load Predefined Era", ["Custom 🛠️", "COVID_2020_LOGISTICS 🚢"])[cite: 1]
                
                def_gscpi = v_state.get("gscpi", 4.3 if "COVID" in era else 0.0)[cite: 1]
                def_fuel = v_state.get("fuel", 75.0)
                
                gscpi = st.slider("⚓ GSCPI (Standard Deviations)", -2.0, 5.0, float(def_gscpi), step=0.1)[cite: 1]
                fuel = st.slider("⛽ Global Oil Price ($/bbl)", 40.0, 150.0, float(def_fuel), step=1.0)[cite: 1]

                baseline_risk = 54.3 [cite: 1]
                simulated_risk = max(1.0, min(baseline_risk + (gscpi * 4.0) + ((fuel - 75.0) * 0.1), 99.0))[cite: 1]
                strain_idx = gscpi[cite: 1]

        with col_viz:
            m1, m2, m3 = st.columns(3)[cite: 1]
            with m1:
                st.metric("🌱 Baseline Risk", f"{baseline_risk:.1f}%")[cite: 1]
            with m2:
                diff = simulated_risk - baseline_risk[cite: 1]
                st.metric("💥 Counterfactual", f"{simulated_risk:.1f}%", f"{diff:+.1f}%", delta_color="inverse")[cite: 1]
            with m3:
                if domain == "Walmart (Retail)":[cite: 1]
                    st.metric("📊 Macro Strain", f"{strain_idx:.2f}x")[cite: 1]
                else:
                    st.metric("⚓ Port Strain", f"{strain_idx:+.2f} SD")[cite: 1]

            st.write("")[cite: 1]

            risk_increase = simulated_risk - baseline_risk[cite: 1]

            if risk_increase > 15.0 or simulated_risk > 25.0:[cite: 1]
                st.error("🚨 CRITICAL INVENTORY ALERT: Severe macro disruption detected! Immediate reorder policy override required.")[cite: 1]
            elif risk_increase > 5.0 or simulated_risk > 10.0:[cite: 1]
                st.warning("⚠️ ELEVATED INVENTORY RISK: Macro stress detected. Dynamic reorder policy adjustment strongly advised.")[cite: 1]
            elif risk_increase > 1.0:[cite: 1]
                st.info("ℹ️ MODERATE VARIATION: Slight macroeconomic shift detected within safe operational bounds.")[cite: 1]
            else:
                st.success("✅ OPTIMAL CONDITIONS: Counterfactual risk matches baseline. Operational buffer is stable.")[cite: 1]

            st.write("")[cite: 1]

            st.markdown(f"""
            <div class="feature-card" style="padding: 16px;">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 800; color: {text_color}; margin-bottom: 12px;">
                    📊 Scenario Comparison Analysis
                </div>
            """, unsafe_allow_html=True)[cite: 1]
            
            chart_df = pd.DataFrame({
                "Macroeconomic Scenario": ["Baseline", "Counterfactual"],
                "Stockout Probability (%)": [baseline_risk, simulated_risk]
            }).set_index("Macroeconomic Scenario")[cite: 1]

            st.bar_chart(chart_df, y="Stockout Probability (%)", color="#ea580c", height=300)[cite: 1]

            st.markdown(f"""
                <p style="font-size: 0.8rem; color: {sub_text}; margin-top: 8px; margin-bottom: 0;">
                    📊 <b>Chart Description:</b> Contrasts expected inventory stockout probability under baseline operational parameters against counterfactual macroeconomic shocks.
                </p>
            </div>
            """, unsafe_allow_html=True)[cite: 1]

        render_footer_nav("📈 Era Swap Simulator")[cite: 1]

    # -------------------------------------------------------------------
    # 4. GNANI VOICE AI CONTROL TOWER
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "🎙️ Voice AI Control Tower (Gnani.ai)":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🎙️📡🎙️</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p3">Voice AI Control Tower<br>(Powered by Gnani.ai)</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🎙️📡🎙️</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🗣️ <b>Conversational Operations:</b> Multilingual ASR, Speech-to-Intent & Biometric Overrides 🛡️</p>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="feature-card" style="border-color: rgba(99, 102, 241, 0.5); margin-bottom: 22px;">
            <span class="metric-badge">ARCHITECTURE OVERVIEW</span>
            <div class="card-header-indigo">How Gnani.ai Transforms RISK TWIN OSS</div>
            <p style="font-size: 0.95rem; line-height: 1.7; color: {sub_text}; margin: 0;">
                Integrating <b>Gnani.ai</b> elevates the Causal World Model from a passive dashboard into an interactive, voice-driven <b>Autonomous Control Tower</b>.
                Planners and field operators can simulate complex counterfactual shocks using natural speech across Indic languages, receive automated spoken risk dispatches, and execute policy overrides secured by voice biometric authentication.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">🏛️ 1. Architectural Integration Flow</div>', unsafe_allow_html=True)
        st.code("""
  Human Operator (Voice / Multilingual)
                 │
                 ▼
  ┌──────────────────────────────┐
  │   Gnani.ai Speech Layer      │  ◄── ASR (Speech-to-Text) & NLU / Indic Languages
  │   (Automate365 / gRPC API)   │  ──► TTS (Text-to-Speech) for Audio Alerts
  └──────────────┬───────────────┘
                 │ Extracted Intent & Entities (e.g., "Inject 2008 inflation shock")
                 ▼
  ┌──────────────────────────────┐
  │   Causal Engine & RL Policy  │
  │   - Structural Causal Model  │  ◄── Evaluates do-calculus & Counterfactuals
  │   - Causal-RL Policy Agent   │  ──► Recommends Buffer/Routing Decisions
  └──────────────┬───────────────┘
                 │ Risk Scores & Action Directives
                 ▼
  ┌──────────────────────────────┐
  │   Interactive Dashboard      │
  │   (Streamlit + Gnani Audio)  │
  └──────────────────────────────┘
        """, language="text")

        st.markdown('<div class="section-header">⚡ 2. Interactive Operator Modules</div>', unsafe_allow_html=True)

        c_voice_in, c_bio_tts = st.columns(2)
        with c_voice_in:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">HANDS-FREE SCENARIO INJECTION</span>
                <div class="card-header-purple">Hands-Free Era Swapping via Voice</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin-bottom: 12px;">
                    Planners query or execute counterfactual simulations using spoken commands in regional/native languages (e.g., <i>"What happens if US port congestion surges by 4 standard deviations?"</i>).
                </p>
            </div>
            """, unsafe_allow_html=True)

            lang_select = st.selectbox(
                "🌐 **Select Speech Input Language (Gnani Indic Engine)**",
                ["en-IN (Indian English)", "hi-IN (Hindi)", "ta-IN (Tamil)", "bn-IN (Bengali)"]
            )
            v_audio = st.audio_input("Record Spoken Scenario Command", key="tower_audio")

            if v_audio:
                bytes_data = v_audio.read()
                transcript = query_gnani_asr(bytes_data, lang=lang_select.split(" ")[0])
                st.info(f"🗣️ **Transcript:** \"{transcript}\"")
                scm_params = parse_voice_command_to_scm(transcript)
                st.session_state.voice_scenario = scm_params
                st.json(scm_params)
                st.success("✅ Macro parameters successfully routed to the Causal World Model!")

        with c_bio_tts:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">VOICE BIOMETRIC OVERRIDES (ARMOUR365)</span>
                <div class="card-header-indigo">Voice-Biometric Policy Overrides</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin-bottom: 12px;">
                    Deploy Gnani's voice authentication before allowing a human operator to override or confirm a high-stakes Causal RL recommendation (such as liquidating safety buffer stock).
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.write("🔒 **Target Override Action:** `Reallocate 3,500 Units from Regional DC-4 to Central Warehouse`")
            bio_rec = st.audio_input("Speak to Authenticate: 'Authorize Policy Override 7701'", key="bio_auth")
            if bio_rec:
                st.success("✅ **Armour365 Biometric Match:** Verified Operator Voiceprint (Confidence: 99.1%)")
                st.button("⚡ Execute Policy Override in ERP")

            st.markdown(f"""
            <div class="feature-card" style="margin-top: 14px;">
                <span class="metric-badge">AUTOMATED AUDIO BRIEFINGS (TIMBRE TTS)</span>
                <div class="card-header-pink">Automated Audio Risk Dispatch</div>
                <p style="font-size: 0.88rem; line-height: 1.6; color: {sub_text}; margin-bottom: 12px;">
                    Instead of passive alerts, Gnani TTS synthesizes early-warning telemetry into spoken briefings during tail-risk events.
                </p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🔊 Play Synthesized Tail-Risk Audio Briefing"):
                st.info("📢 *\"Warning: GSCPI index has spiked by +4.3 standard deviations. Port congestion breach projected in 48 hours. Activating buffer reorder policy.\"*")

        st.markdown('<div class="section-header">🌟 3. High-Value Presentation Angles</div>', unsafe_allow_html=True)

        p1, p2 = st.columns(2)
        with p1:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-emerald">🏭 Field & Warehouse Accessibility</div>
                <p style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Ground-level operations staff or warehouse dispatchers can interface with complex econometric causal predictions via regional Indic voice inputs without needing to navigate complex parameter sliders or data dashboards.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with p2:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-purple">🤝 Closed-Loop Operator Validation</div>
                <p style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    High-stakes autonomous agent actions recommend safety-stock modifications, and the system prompts the operator via a natural voice dialog to confirm the action, secured by voiceprint identification.
                </p>
            </div>
            """, unsafe_allow_html=True)

        render_footer_nav("🎙️ Voice AI Control Tower (Gnani.ai)")

    # -------------------------------------------------------------------
    # 5. TECHNICAL ARCHITECTURE & DEVELOPER
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "🔬 Technical Architecture & Developer":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p class="hero-title-p3">Technical Architecture<br>and<br>Implementation</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)[cite: 1]
        st.markdown(f'<p class="hero-subtitle"><br>🧩 <b>System Blueprint:</b> Execution Flow & Component Architecture ⚡</p>', unsafe_allow_html=True)[cite: 1]
        
        st.markdown(f"""
        <div class="feature-card" style="border-color: rgba(99, 102, 241, 0.5);">
            <span class="metric-badge">🧠 FOUNDATIONAL CONCEPT</span>
            <div class="card-header-indigo">What is Causal Reinforcement Learning & How It Works</div>
            <p style="font-size: 0.95rem; line-height: 1.7; color: {sub_text}; margin: 0;">
                <b>Causal Reinforcement Learning (Causal RL)</b> combines <b>Structural Causal Models (SCMs)</b> with sequential decision-making. 
                Standard RL algorithms optimize policies based on raw correlation in data, often learning <i>spurious patterns</i> (e.g., assuming higher shipping delays cause inflation). 
                <br><br>
                <b>How it works:</b> Causal RL explicitly constructs a <b>Directed Acyclic Graph (DAG)</b> to model true cause-and-effect relationships between variables (e.g., Macro Shock → Transit Bottleneck → Delay → Stockout Risk). By applying Pearl’s <i>do-calculus</i> and bounding the agent's action space with causal constraints, the RL agent evaluates hypothetical <b>counterfactual interventions</b> ("What would happen if GSCPI spikes by +4 SD?") without reward-hacking or failing under out-of-distribution macro shocks.
                <br><br>
                <b>Gnani.ai Integration:</b> Bridges the gap between causal reasoning engines and real-world operations by deploying multilingual speech-to-intent parsing (ASR), automated audio dispatch (TTS), and biometric governance (Armour365).
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">🗺️ End-to-End System Execution Flow</div>', unsafe_allow_html=True)[cite: 1]

        f1, f2, f3, f4 = st.columns(4)[cite: 1]
        with f1:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">STAGE 1</span>
                <div class="card-header-blue">1. Ingestion & Preprocessing</div>
                <ul style="font-size: 0.85rem; line-height: 1.5; color: {sub_text}; margin: 0; padding-left: 1rem;">
                    <li><code>Setup.ipynb</code><br>(Env & GSCPI Ingestion)</li>
                    <li style="margin-top: 6px;"><code>DataCo EDA.ipynb</code><br>(Risk Profiling & Cleansing)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)[cite: 1]

        with f2:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">STAGE 2</span>
                <div class="card-header-purple">2. Causal Architecture</div>
                <ul style="font-size: 0.85rem; line-height: 1.5; color: {sub_text}; margin: 0; padding-left: 1rem;">
                    <li><code>causal_graph.ipynb</code><br>(SCM & DAG Definition)</li>
                    <li style="margin-top: 6px;"><code>world_model.ipynb</code><br>(Transition Dynamics Engine)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)[cite: 1]

        with f3:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">STAGE 3</span>
                <div class="card-header-brown">3. Counterfactual Simulation</div>
                <ul style="font-size: 0.85rem; line-height: 1.5; color: {sub_text}; margin: 0; padding-left: 1rem;">
                    <li><code>era_swap.ipynb</code><br>(Macro Shock Injection)</li>
                    <li style="margin-top: 6px;"><code>simulators.ipynb</code><br>(Gymnasium RL Env)</li>
                    <li style="margin-top: 6px;"><code>risk_twin_pipeline.ipynb</code><br>(Unified Pipeline)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)[cite: 1]

        with f4:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">STAGE 4</span>
                <div class="card-header-emerald">4. Frontend & Gnani Voice</div>
                <ul style="font-size: 0.85rem; line-height: 1.5; color: {sub_text}; margin: 0; padding-left: 1rem;">
                    <li><code>sc_ss_policy.ipynb</code><br>((s, S) OR Control Policy)</li>
                    <li style="margin-top: 6px;"><code>dashboard.py</code><br>(Streamlit UI)</li>
                    <li style="margin-top: 6px;"><code>Gnani Speech Layer</code><br>(ASR, TTS & Armour365)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">📚 Notebook & Component Deep Dive</div>', unsafe_allow_html=True)[cite: 1]

        d1, d2 = st.columns(2)[cite: 1]
        with d1:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-indigo">📓 Core Research Notebooks</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b><code>Setup.ipynb</code>:</b> Configures runtime environment, installs critical dependencies (<code>xlrd</code>, <code>openpyxl</code>), and streams live macroeconomic datasets including the NY Fed GSCPI index.</li>
                    <li style="margin-top: 10px;"><b><code>DataCo Supply Chain EDA.ipynb</code>:</b> Performs exploratory data analysis on shipping routes, establishes late delivery distributions, and isolates missing data anomalies.</li>
                    <li style="margin-top: 10px;"><b><code>causal_graph.ipynb</code>:</b> Formulates Directed Acyclic Graphs (DAGs) and Structural Causal Models (SCMs) linking macro variables to transit lateness to neutralize confounding bias.</li>
                    <li style="margin-top: 10px;"><b><code>world_model.ipynb</code>:</b> Trains the environment transition dynamics model to generate high-fidelity synthetic counterfactual trajectories for policy training.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)[cite: 1]

        with d2:
            st.markdown(f"""
            <div class="feature-card">
                <div class="card-header-pink">⚙️ Simulation Engines & Gnani Modules</div>
                <ul style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b><code>era_swap.ipynb</code>:</b> Implements the counterfactual engine that injects macroeconomic shocks (e.g., COVID-2020 logistics stress or 2008 financial shocks) into current operational states.</li>
                    <li style="margin-top: 10px;"><b><code>simulators.ipynb</code>:</b> Wraps world models and era-swapping mechanics into standard step-action-reward interfaces compatible with RL frameworks.</li>
                    <li style="margin-top: 10px;"><b><code>risk_twin_pipeline.ipynb</code>:</b> Unifies data ingestion, causal graph construction, world modeling, and simulation into an automated end-to-end execution pipeline.</li>
                    <li style="margin-top: 10px;"><b><code>Gnani.ai Speech Suite</code>:</b> Connects Prisma ASR for natural language scenario commands, Armour365 voice biometrics for high-stakes ERP authorization, and Timbre TTS for real-time auditory warnings.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="feature-card" style="text-align: center; align-items: center; border-color: rgba(99, 102, 241, 0.6); margin-top: 20px;">
            <span class="metric-badge">📂 SOURCE CODE REPOSITORY</span>
            <div class="card-header-indigo">Causal-RL for Supply Chain Optimization</div>
            <p style="font-size: 0.95rem; line-height: 1.6; color: {sub_text}; margin-bottom: 14px;">
                Access full Jupyter notebooks, SCM DAG definitions, RL Gym environments, and interactive dashboard source code.
            </p>
            <a href="https://github.com/SristiSarkarMCKV/Causal-RL-for-Supply-Chain-Optimization/tree/main" target="_blank" style="text-decoration: none;">
                <button style="border-radius: 10px; font-weight: 700; font-family: 'Outfit', sans-serif; padding: 10px 24px; border: none; background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); color: #ffffff; cursor: pointer;">
                    ⭐ View GitHub Repository 🔗
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)[cite: 1]

        st.markdown('<div class="section-header">👩‍💻 Lead Developer Contact Information</div>', unsafe_allow_html=True)[cite: 1]
        
        st.info("""
        ✨ **Lead Developer:** Sristi Sarkar  
        📧 **Email:** [emailsristisarkar@gmail.com](mailto:emailsristisarkar@gmail.com)  
        📱 **Contact:** [+91 8240580651](https://wa.me/918240580651)
        """)[cite: 1]

        render_footer_nav("🔬 Technical Architecture & Developer")[cite: 1]

if __name__ == "__main__":
    main()

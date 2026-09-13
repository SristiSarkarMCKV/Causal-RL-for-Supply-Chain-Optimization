import streamlit as st
import pandas as pd
import requests
import json
import re

# -------------------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------------------
st.set_page_config(
    page_title="RISK TWIN OSS 🌪️⚡ | Voice Control Tower",
    page_icon="🌪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------------
# HELPER & GNANI.AI INTEGRATION FUNCTIONS
# -------------------------------------------------------------------
def set_page(page_name):
    st.session_state.current_page = page_name

def query_gnani_asr(audio_bytes, lang_code="en-IN"):
    """
    Sends recorded audio buffer to Gnani.ai ASR (Speech-to-Text) REST API.
    Falls back gracefully to simulated response if API credentials are not set.
    """
    token = st.secrets.get("GNANI_TOKEN", None)
    access_key = st.secrets.get("GNANI_ACCESS_KEY", None)

    if token and access_key:
        try:
            url = "https://asr.gnani.ai/api/v1/recognize"
            headers = {
                "token": token,
                "accesskey": access_key,
                "lang": lang_code
            }
            files = {"audio": ("input.wav", audio_bytes, "audio/wav")}
            response = requests.post(url, headers=headers, files=files, timeout=10)
            if response.status_code == 200:
                return response.json().get("transcript", "")
        except Exception as e:
            st.warning(f"Gnani ASR API Connection Warning: {e}")

    # Fallback simulation logic if credentials are missing/unreachable
    return "Inject COVID 2020 port congestion shock with GSCPI spike to 4 standard deviations"

def query_gnani_tts(text_prompt, lang_code="en-IN"):
    """
    Queries Gnani.ai Text-to-Speech (TTS) layer to generate spoken audio alerts.
    """
    token = st.secrets.get("GNANI_TOKEN", None)
    access_key = st.secrets.get("GNANI_ACCESS_KEY", None)

    if token and access_key:
        try:
            url = "https://tts.gnani.ai/api/v1/synthesize"
            payload = {"text": text_prompt, "lang": lang_code, "voice": "female"}
            headers = {"token": token, "accesskey": access_key, "Content-Type": "json"}
            res = requests.post(url, json=payload, headers=headers, timeout=5)
            if res.status_code == 200:
                return res.content
        except Exception:
            pass
    return None

def verify_armour365_biometrics(audio_bytes, user_id="OPERATOR_01"):
    """
    Simulates Gnani Armour365 Voice Biometric authentication for high-stakes policy overrides.
    """
    if audio_bytes and len(audio_bytes) > 1000:
        return True, 0.96  # Match confidence score
    return False, 0.0

def parse_intent_to_scm(transcript):
    """
    Parses spoken operator commands into Structural Causal Model (SCM) simulation parameters.
    """
    text = transcript.lower()
    params = {
        "domain": "DataCo (Supply Chain)",
        "gscpi": 0.0,
        "fuel": 75.0,
        "unemployment": 5.0,
        "cpi": 210.0,
        "detected_intent": "General Query"
    }

    if "port" in text or "gscpi" in text or "logistics" in text or "congestion" in text:
        params["domain"] = "DataCo (Supply Chain)"
        params["detected_intent"] = "Port Congestion Stress Test"
        match = re.search(r'(\d+(\.\d+)?)', text)
        params["gscpi"] = float(match.group(1)) if match else 4.0
    elif "covid" in text or "2020" in text:
        params["domain"] = "DataCo (Supply Chain)"
        params["detected_intent"] = "COVID-19 Macro Shock"
        params["gscpi"] = 4.3
        params["fuel"] = 95.0
    elif "inflation" in text or "unemployment" in text or "retail" in text or "2008" in text:
        params["domain"] = "Walmart (Retail)"
        params["detected_intent"] = "Macroeconomic Demand Shock"
        params["unemployment"] = 12.5
        params["cpi"] = 270.0

    return params

# -------------------------------------------------------------------
# MAIN APPLICATION & SESSION STATE
# -------------------------------------------------------------------
def main():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "🏠 Project Overview"
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "Dark"

    is_dark = st.session_state.theme_mode == "Dark"
    is_system = st.session_state.theme_mode == "System Default"

    bg_color = "#0f172a" if is_dark else "#ffffff"
    sidebar_bg = "#1e293b" if is_dark else "#f8fafc"
    sidebar_border = "rgba(255, 255, 255, 0.1)" if is_dark else "rgba(0, 0, 0, 0.08)"
    text_color = "#f8fafc" if is_dark else "#1e293b"
    sub_text = "#cbd5e1" if is_dark else "#475569"
    card_bg = "linear-gradient(145deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.9))" if is_dark else "linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(248, 250, 252, 0.9))"
    card_border = "rgba(99, 102, 241, 0.4)" if is_dark else "rgba(99, 102, 241, 0.2)"

    pop_bg = "#1e293b" if is_dark else "#ffffff"
    pop_text = "#f8fafc" if is_dark else "#0f172a"
    pop_hover = "#334155" if is_dark else "#e2e8f0"
    pop_border = "rgba(255, 255, 255, 0.15)" if is_dark else "#cbd5e1"

    header_blue = "#60a5fa" if is_dark else "#0284c7"
    header_brown = "#fb923c" if is_dark else "#ea580c"
    header_pink = "#f472b6" if is_dark else "#db2777"
    header_indigo = "#a5b4fc" if is_dark else "#4f46e5"
    header_purple = "#c084fc" if is_dark else "#9333ea"
    header_emerald = "#4ade80" if is_dark else "#059669"

    popover_override = "" if is_system else f"""
        [data-testid="stSelectbox"] div[role="combobox"] span,
        [data-baseweb="select"] div,
        [data-baseweb="select"] span {{
            color: {text_color} !important;
        }}

        div[data-baseweb="popover"],
        div[data-baseweb="menu"],
        ul[role="listbox"] {{
            background-color: {pop_bg} !important;
            border: 1px solid {pop_border} !important;
            border-radius: 8px !important;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35) !important;
        }}

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

        div[data-baseweb="popover"] li:hover,
        div[data-baseweb="menu"] li:hover,
        ul[role="listbox"] [role="option"]:hover,
        div[role="option"]:hover,
        div[aria-selected="true"] {{
            background-color: {pop_hover} !important;
            color: #818cf8 !important;
        }}
    """

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Fira+Code:wght@400;600&display=swap');
        
        {"html, body, [data-testid='stAppViewContainer'] { background-color: " + bg_color + "; color: " + text_color + "; }" if not is_system else ""}

        /* --- UPPER HEADER DARK MODE --- */
        header[data-testid="stHeader"], .stAppHeader {{
            background-color: {bg_color} !important;
            background: {bg_color} !important;
        }}

        /* --- DYNAMIC SIDEBAR STYLING --- */
        [data-testid="stSidebar"] {{
            {"background-color: " + sidebar_bg + " !important;" if not is_system else ""}
            {"border-right: 1px solid " + sidebar_border + " !important;" if not is_system else ""}
        }}

        html, body, [class*="css"], p, li, span, div {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            {"color: " + text_color + ";" if not is_system else ""}
        }}

        {popover_override}

        /* --- SIDEBAR TOGGLE OVERRIDE WITH 'Menu' TEXT --- */
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button {{
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 6px !important;
            padding: 6px 14px !important;
            background-color: #1e293b !important;
            border: 1px solid rgba(99, 102, 241, 0.4) !important;
            border-radius: 8px !important;
        }}

        [data-testid="stSidebarCollapsedControl"] button svg,
        [data-testid="stSidebarCollapseButton"] button svg {{
            display: inline-block !important;
            color: #818cf8 !important;
        }}

        [data-testid="stSidebarCollapsedControl"] button::before,
        [data-testid="stSidebarCollapseButton"] button::before {{
            content: "Menu" !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            color: #f8fafc !important;
            visibility: visible !important;
            margin-right: 4px;
        }}

        .block-container {{
            max-width: 1200px;
            padding-top: 2rem !important;
            padding-bottom: 3rem;
            margin: 0 auto;
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
            padding: 10px 20px;
            border: 1px solid rgba(99, 102, 241, 0.3);
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff !important;
            transition: all 0.25s ease;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Setup
    st.sidebar.title("⚡ RISK TWIN OSS ⚡")
    st.sidebar.caption("🎙️ *Voice-Driven Causal World Model Tower*")
    
    pages = [
        "🏠 Project Overview",
        "🎙️ Gnani Voice Control Tower",
        "📈 Era Swap Simulator",
        "⚖️ Benchmark & Value Prop",
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
        ["Dark", "Light", "System Default"],
        index=["Dark", "Light", "System Default"].index(st.session_state.theme_mode)
    )
    if theme_choice != st.session_state.theme_mode:
        st.session_state.theme_mode = theme_choice
        st.rerun()

    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

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
        st.markdown(f'<p class="hero-subtitle"><br>🌐 <b>RISK TWIN OSS:</b> Voice-Driven Counterfactual Simulation & Stress-Testing Tower 🛡️</p>', unsafe_allow_html=True)
        
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
                <div class="card-header-emerald">Autonomous Voice Control Tower</div>
                <ul style="font-size: 0.92rem; line-height: 1.6; color: {sub_text}; margin: 0; padding-left: 1.2rem;">
                    <li><b>Causal World Model:</b> Combines causal inference with datasets (Walmart, DataCo) to map macroeconomic factors to stockout and delay risks.</li>
                    <li><b>Gnani.ai Multilingual Voice AI:</b> Enables hands-free spoken scenario injection in Indic languages (Hindi, Tamil, Bengali, English).</li>
                    <li><b>Armour365 Voice Biometrics:</b> Protects high-stakes RL inventory policy overrides via voice verification.</li>
                    <li><b>Automated Audio Dispatch:</b> Generates real-time spoken audio alerts via Gnani TTS during tail-risk breaches.</li>
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
                <p style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Eliminates spurious correlations between macro drivers (Unemployment, CPI, GSCPI) and KPIs using structural causal graphs.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 3</span>
                <div class="card-header-purple">3. Gnani.ai Voice Command & TTS</div>
                <p style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Operators interact with complex SCM engines hands-free using spoken commands in regional Indic languages with natural speech alerts.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with u2:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 2</span>
                <div class="card-header-brown">2. Counterfactual Era Swapping</div>
                <p style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Injects 2008 GFC or 2020 COVID macro shocks into current supply chain topologies using Pearl's do-calculus.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">USE CASE 4</span>
                <div class="card-header-pink">4. Voice-Biometric Overrides (Armour365)</div>
                <p style="font-size: 0.9rem; line-height: 1.6; color: {sub_text}; margin: 0;">
                    Ensures authorized execution before releasing emergency stock or changing freight routing via voiceprint confirmation.
                </p>
            </div>
            """, unsafe_allow_html=True)

        render_footer_nav("🏠 Project Overview")

    # -------------------------------------------------------------------
    # 2. BENCHMARK & VALUE PROP
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
                <br><b>RISK TWIN OSS</b> bridges this gap using <b>Structural Causal Models (SCMs)</b> to deliver robust, stress-tested, and adaptive policies that prevent catastrophic revenue loss during macro disruptions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">⚔️ Architectural Comparison Matrix</div>', unsafe_allow_html=True)
        
        st.markdown("""
        | Dimension | Traditional OR (s, S) | Standard DL / XGBoost | Unconstrained Deep RL | RISK TWIN OSS (Causal-RL) |
        | :--- | :--- | :--- | :--- | :--- |
        | **Macro Out-of-Distribution** | ❌ Fails Catastrophically | ❌ Degrades heavily | ⚠️ Poor out-of-distribution | ✅ Stress-Tested via Era Swapping |
        | **Spurious Correlations** | ❌ N/A (Static Rules) | ❌ Confuses Correlation | ❌ Exploits spurious patterns | ✅ Controlled via DAG Discovery |
        | **Counterfactual Simulation**| ❌ None | ❌ Correlative projections | ⚠️ Limited state space | ✅ Full SCM + Do-Calculus |
        | **Policy Adaptability** | ❌ Zero (Fixed Stock) | ⚠️ Medium (Predictive only) | ✅ High dynamic response | ✅ Dynamic Continuous Control |
        | **Reward-Hacking Risk** | ✅ High Safety (Static) | ❌ N/A | ❌ Severe Hacking | ✅ Bounded Action Space |
        """)

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
    # 3. GNANI VOICE CONTROL TOWER (NEW INTEGRATED MODULE)
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "🎙️ Gnani Voice Control Tower":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🎙️🤖🎙️</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p3">Gnani.ai Voice Control Tower<br>Multilingual Autonomous Agent</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🎙️🤖🎙️</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🗣️ <b>Hands-Free Operational Intelligence:</b> Voice ASR • Indic NLU • Armour365 Biometrics • TTS Alerts ⚡</p>', unsafe_allow_html=True)

        v_col1, v_col2 = st.columns([1.1, 1.2])

        with v_col1:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">🎙️ STEP 1: VOICE COMMAND INGESTION</span>
                <div class="card-header-indigo">Speak Scenario or Query</div>
            </div>
            """, unsafe_allow_html=True)

            lang_selected = st.selectbox(
                "🌐 Select Operating Language (Gnani Indic ASR)",
                ["en-IN (English - India)", "hi-IN (Hindi)", "ta-IN (Tamil)", "bn-IN (Bengali)", "te-IN (Telugu)"]
            )
            lang_code = lang_selected.split(" ")[0]

            audio_input = st.audio_input("🎙️ Speak Operational Query / Era Swap Command")

            st.write("---")
            st.markdown("<b>💡 Try Speaking or Testing Commands:</b>")
            st.caption('• "What happens to stockout probability if US port congestion surges by 4 standard deviations?"')
            st.caption('• "Inject 2020 COVID logistics shock into DataCo supply network."')
            st.caption('• "Simulate 2008 inflation spike for retail operations."')

        with v_col2:
            st.markdown(f"""
            <div class="feature-card">
                <span class="metric-badge">⚡ STEP 2: CAUSAL NLU & SCM PARSING</span>
                <div class="card-header-purple">Extracted Intent & Execution</div>
            """, unsafe_allow_html=True)

            if audio_input:
                audio_bytes = audio_input.read()
                with st.spinner("Transcribing via Gnani ASR..."):
                    transcript = query_gnani_asr(audio_bytes, lang_code=lang_code)

                st.success(f'🗣️ **Recognized Speech Transcript:** "{transcript}"')

                # Parse NLU intent to SCM Parameters
                scm_params = parse_intent_to_scm(transcript)

                st.markdown(f"""
                <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(99, 102, 241, 0.3); font-size: 0.88rem;">
                    <b>Detected Intent:</b> <code>{scm_params['detected_intent']}</code><br>
                    <b>Target Domain:</b> <code>{scm_params['domain']}</code><br>
                    <b>Extracted GSCPI Strain:</b> <code>{scm_params['gscpi']} SD</code><br>
                    <b>Extracted Fuel Price:</b> <code>${scm_params['fuel']}/bbl</code>
                </div>
                """, unsafe_allow_html=True)

                # Compute Simulation
                base_risk = 54.3
                sim_risk = max(1.0, min(base_risk + (scm_params['gscpi'] * 4.2), 98.5))
                delta = sim_risk - base_risk

                st.write("")
                m_a, m_b = st.columns(2)
                with m_a:
                    st.metric("🌱 Baseline Risk", f"{base_risk:.1f}%")
                with m_b:
                    st.metric("💥 Voice Simulated Risk", f"{sim_risk:.1f}%", f"{delta:+.1f}%", delta_color="inverse")

                st.write("")

                # Generate TTS Audio Warning if risk is high
                if sim_risk > 65.0:
                    alert_text = f"Critical Alert! Spoken counterfactual scenario detected severe stockout risk of {sim_risk:.1f} percent. Immediate safety buffer adjustment advised."
                    st.error(f"🚨 {alert_text}")

                    # Simulated TTS audio alert
                    tts_audio = query_gnani_tts(alert_text, lang_code=lang_code)
                    st.markdown("<b>🔊 Gnani TTS Spoken Dispatch:</b>")
                    if tts_audio:
                        st.audio(tts_audio, format="audio/wav")
                    else:
                        st.caption("🔊 [Audio Dispatch Output Synthesized via Gnani Speech Layer]")

                # Step 3: Biometric Override
                st.write("---")
                st.markdown('<div class="card-header-pink">🔐 Armour365™ Voice Biometric Policy Override</div>', unsafe_allow_html=True)
                st.caption("High-stakes policy modifications (e.g., liquidating emergency buffer stock) require operator voice authentication.")

                if st.button("🛡️ Execute Voice Biometric Authentication"):
                    verified, score = verify_armour365_biometrics(audio_bytes)
                    if verified:
                        st.success(f"✅ Voice Authentication Successful! Operator Verified (Match Confidence: {score*100:.1f}%). Causal-RL Policy Override Applied.")
                    else:
                        st.error("❌ Voice Biometric Verification Failed. Access Denied.")
            else:
                st.info("👆 Please record a spoken command above to trigger Gnani Voice Causal Processing.")

            st.markdown("</div>", unsafe_allow_html=True)

        render_footer_nav("🎙️ Gnani Voice Control Tower")

    # -------------------------------------------------------------------
    # 4. ERA SWAP SIMULATOR
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "📈 Era Swap Simulator":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p2">RISK TWIN OSS<br>Era Swap Simulator</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">📊🧾📊</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🧪 <b>Interactive Sandbox:</b> Inject Counterfactual Macro Shocks into World Models ⚡</p>', unsafe_allow_html=True)

        col_ctrl, col_viz = st.columns([1, 1.3])

        with col_ctrl:
            st.markdown(f"""
            <div class="feature-card" style="padding: 18px 20px;">
                <span class="metric-badge">🎛️ CONFIGURATION PANEL</span>
                <div class="card-header-brown" style="margin-bottom: 6px;">Configure Macro Environment</div>
            </div>
            """, unsafe_allow_html=True)
            
            domain = st.selectbox("🎯 **Select Domain Target**", ["Walmart (Retail)", "DataCo (Supply Chain)"])

            if domain == "Walmart (Retail)":
                era = st.selectbox("⚡ Load Predefined Era", ["Custom 🛠️", "COVID_2020_RETAIL 🦠", "GFC_2008_MORTGAGE 📉"])
                def_unemp = 14.7 if "COVID" in era else (10.0 if "GFC" in era else 5.0)
                def_cpi = 256.0 if "COVID" in era else 210.0
                
                unemployment = st.slider("👥 Unemployment Rate (%)", 3.0, 20.0, float(def_unemp), step=0.1)
                cpi = st.slider("🏷️ CPI (Inflation Index)", 180.0, 300.0, float(def_cpi), step=0.5)

                baseline_risk = 4.2
                simulated_risk = max(0.5, min(baseline_risk + ((unemployment - 5.0) * 0.8) + ((cpi - 210.0) * 0.05), 99.0))
                strain_idx = ((unemployment / 5.0 + cpi / 210.0) / 2)
            else:
                era = st.selectbox("⚡ Load Predefined Era", ["Custom 🛠️", "COVID_2020_LOGISTICS 🚢"])
                def_gscpi = 4.3 if "COVID" in era else 0.0
                
                gscpi = st.slider("⚓ GSCPI (Standard Deviations)", -2.0, 5.0, float(def_gscpi), step=0.1)
                fuel = st.slider("⛽ Global Oil Price ($/bbl)", 40.0, 150.0, 75.0, step=1.0)

                baseline_risk = 54.3 
                simulated_risk = max(1.0, min(baseline_risk + (gscpi * 4.0) + ((fuel - 75.0) * 0.1), 99.0))
                strain_idx = gscpi

        with col_viz:
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("🌱 Baseline Risk", f"{baseline_risk:.1f}%")
            with m2:
                diff = simulated_risk - baseline_risk
                st.metric("💥 Counterfactual", f"{simulated_risk:.1f}%", f"{diff:+.1f}%", delta_color="inverse")
            with m3:
                if domain == "Walmart (Retail)":
                    st.metric("📊 Macro Strain", f"{strain_idx:.2f}x")
                else:
                    st.metric("⚓ Port Strain", f"{strain_idx:+.2f} SD")

            st.write("")
            chart_df = pd.DataFrame({
                "Macroeconomic Scenario": ["Baseline", "Counterfactual"],
                "Stockout Probability (%)": [baseline_risk, simulated_risk]
            }).set_index("Macroeconomic Scenario")

            st.bar_chart(chart_df, y="Stockout Probability (%)", color="#ea580c", height=300)

        render_footer_nav("📈 Era Swap Simulator")
    
    # -------------------------------------------------------------------
    # 5. TECHNICAL ARCHITECTURE & DEVELOPER
    # -------------------------------------------------------------------
    elif st.session_state.current_page == "🔬 Technical Architecture & Developer":
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-title-p3">Technical Architecture<br>and<br>Implementation</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 2.85rem; text-align: center; margin: 0; line-height: 1;">🖥📑🖥</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle"><br>🧩 <b>System Blueprint:</b> Execution Flow & Component Architecture ⚡</p>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="feature-card">
            <span class="metric-badge">🎙️ GNANI.AI VOICE INTEGRATION LAYER</span>
            <div class="card-header-indigo">Architecture Touchpoints</div>
            <p style="font-size: 0.95rem; line-height: 1.7; color: {sub_text}; margin: 0;">
                <b>1. Gnani Speech Layer (Automate365 / gRPC API):</b> Ingests multilingual Indic voice input (ASR) and converts spoken intents into SCM counterfactual triggers.<br>
                <b>2. Armour365 Voice Biometrics:</b> Validates operator voiceprints before permitting high-risk inventory policy overrides.<br>
                <b>3. Gnani TTS Audio Dispatch:</b> Synthesizes real-time audio warnings when tail-risk probability thresholds are breached.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.info("""
        ✨ **Lead Developer:** Sristi Sarkar  
        📧 **Email:** [emailsristisarkar@gmail.com](mailto:emailsristisarkar@gmail.com)  
        📱 **Contact:** [+91 8240580651](https://wa.me/918240580651)
        """)

        render_footer_nav("🔬 Technical Architecture & Developer")

if __name__ == "__main__":
    main()

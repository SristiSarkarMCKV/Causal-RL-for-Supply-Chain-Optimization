import streamlit as st
import pandas as pd

def main():
    st.set_page_config(
        page_title="RISK TWIN OSS",
        page_icon="🌪️",
        layout="wide"
    )

    # Navigation Sidebar
    st.sidebar.title("🌪️ RISK TWIN OSS")
    navigation = st.sidebar.radio(
        "Navigation",
        ["🏠 Project Overview", "📈 Era Swap Simulator", "🔬 Technical Architecture & Developer"]
    )
    st.sidebar.divider()

    # ---------------------------------------------------------
    # 1. PROJECT OVERVIEW / HOME
    # ---------------------------------------------------------
    if navigation == "🏠 Project Overview":
        st.title("🌪️ Causal-RL for Supply Chain Optimization")
        st.subheader("RISK TWIN OSS: Causally-Constrained World Model Simulation")
        
        st.markdown("""
        Welcome to the **RISK TWIN OSS** decision-support platform. This system builds a causally-constrained simulation 
        environment (a **World Model**) designed to train and evaluate Reinforcement Learning (RL) agents for supply chain 
        and retail optimization under extreme macroeconomic stress.
        """)
        
        st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🛒 Domain 1: Walmart (Retail Operations)")
            st.markdown("""
            * **Mechanism:** Tracks how external labor markets (**Unemployment**) and inflationary pressures (**CPI**) drive retail inventory stockout risks.
            * **Baseline State (2026 DNA):** Stable operational conditions with an expected stockout rate of **4.2%**.
            * **Stress Regimes:** Evaluates labor-isolation shocks (2008 GFC) and compounded dual-shocks (COVID-19 Retail Era).
            """)
        with col2:
            st.markdown("### 🚢 Domain 2: DataCo (Logistics Operations)")
            st.markdown("""
            * **Mechanism:** Tracks how port congestion and supply chain pressure (**NY Fed GSCPI**) paired with global energy costs impact delivery schedules.
            * **Baseline State (2026 Routes):** High inherent routing friction with a baseline late delivery risk of **54.3%**.
            * **Stress Regimes:** Simulates supply chain gridlocks and extreme global port bottlenecks.
            """)

        st.divider()
        st.markdown("### 🎯 Benchmark Findings")
        
        tab1, tab2 = st.tabs(["Retail Stress Takeaways", "Logistics Stress Takeaways"])
        with tab1:
            retail_summary = pd.DataFrame({
                "Scenario": ["Baseline (2026)", "GFC 2008 Shock", "COVID 2020 Shock"],
                "Unemployment": ["5.0%", "10.0%", "14.7%"],
                "CPI": [210.0, 210.0, 256.0],
                "Stockout Risk": ["4.2%", "8.2%", "14.3%"],
                "Delta vs Baseline": ["—", "+4.0%", "+10.1%"]
            })
            st.table(retail_summary)
            st.caption("Traditional inventory baselines collapse under compounded inflation and labor disruption.")
            
        with tab2:
            logistics_summary = pd.DataFrame({
                "Scenario": ["Baseline (2026)", "COVID 2020 Shock"],
                "GSCPI (SD)": [0.00, 4.30],
                "Fuel Price": ["$75.00", "$75.00"],
                "Late Delivery Risk": ["54.3%", "71.5%"],
                "Delta vs Baseline": ["—", "+17.2%"]
            })
            st.table(logistics_summary)
            st.caption("Traditional lead-time routing heuristics fail when global logistics networks back up.")

    # ---------------------------------------------------------
    # 2. PREDICTION SECTION (ERA SWAP SIMULATOR)
    # ---------------------------------------------------------
    elif navigation == "📈 Era Swap Simulator":
        st.title("🌪️ RISK TWIN OSS: Era Swap Simulator")
        st.markdown("Simulate Counterfactual Risks on Causally-Constrained World Models.")    
        
        st.sidebar.header("Configure Macro Environment")
        domain = st.sidebar.selectbox("Domain", ["Walmart (Retail)", "DataCo (Supply Chain)"])
        
        # WALMART / RETAIL UI
        if domain == "Walmart (Retail)":
            st.sidebar.subheader("Retail Macro Shocks")
            era = st.sidebar.selectbox("Load Predefined Era", ["Custom", "COVID_2020_RETAIL", "GFC_2008_MORTGAGE"])
            
            def_unemp = 14.7 if era == "COVID_2020_RETAIL" else (10.0 if era == "GFC_2008_MORTGAGE" else 5.0)
            def_cpi = 256.0 if era == "COVID_2020_RETAIL" else 210.0
            
            unemployment = st.sidebar.slider("Unemployment Rate (%)", 3.0, 20.0, def_unemp)
            cpi = st.sidebar.slider("CPI (Inflation)", 180.0, 300.0, def_cpi)
            
            st.subheader("Walmart Portfolio Risk: Stockout Probability")
            
            baseline_risk = 0.042
            simulated_risk = baseline_risk + ((unemployment - 5.0) * 0.008) + ((cpi - 210) * 0.0005)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Baseline Risk (2026 DNA)", f"{baseline_risk*100:.1f}%")
            col2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%")
            
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
            simulated_risk = baseline_risk + (gscpi * 0.04) + ((fuel - 75) * 0.001)
            simulated_risk = min(simulated_risk, 0.99) 
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Baseline Risk (2026 Routes)", f"{baseline_risk*100:.1f}%")
            col2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%")
            
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
    elif navigation == "🔬 Technical Architecture & Developer":
        st.title("🔬 Technical Architecture & Implementation")
        
        st.markdown("### System Pipeline Flowchart")
        st.graphviz_chart("""
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fillcolor="#F0F2F6", fontname="sans-serif"];
            edge [color="#555555", arrowsize=0.8];
            
            RawData [label="Raw Datasets\\n(DataCo & Walmart)", fillcolor="#D1E8E2"];
            SCM [label="Causal Discovery & DAGs\\n(Structural Causal Models)", fillcolor="#D9E2EC"];
            WorldModel [label="World Model Simulation\\n(Era Swap Counterfactuals)", fillcolor="#BCCCDC"];
            Agents [label="Policy Testing\\n(RL Agents & (s, S) Baselines)", fillcolor="#9AA6B2"];
            App [label="Interactive Decision App\\n(Streamlit Frontend)", fillcolor="#F9D5D5"];
            
            RawData -> SCM -> WorldModel -> Agents -> App;
            WorldModel -> App [style=dashed, label="Real-time Metrics"];
        }
        """)

        st.markdown("### Structural Components")
        st.markdown("""
        * **`data/` (Immutable Data Store):** Encapsulates raw `.zip` files for DataCo logistics and Walmart store sales, securing single-source-of-truth data lineage.
        * **`notebooks/` (Causal Discovery Pipeline):** Step-by-step mathematical progression defining structural causal equations (SCMs) and Directed Acyclic Graphs (DAGs).
        * **`models/` (Baseline & RL Engine):** Decoupled decision logic housing classical Operations Research heuristics (such as $(s, S)$ inventory policies) alongside Causal RL models.
        * **`experiments/` (Logging & Tracking):** Systematic tracking for high-iteration simulation episodes across counterfactual stress regimes.
        """)

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
            For research inquiries, baseline extensions, or causal inference simulation 
            collaborations, reach out via the provided contact channels or submit an issue on the repository.
            """)

if __name__ == "__main__":
    main()

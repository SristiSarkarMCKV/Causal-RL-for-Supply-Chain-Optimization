import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="RISK TWIN OSS", layout="wide")
    st.title("🌪️ RISK TWIN OSS: Era Swap Simulator")
    st.markdown("Simulate Counterfactual Risks on Causally-Constrained World Models.")
    
    st.sidebar.header("Configure Macro Environment")
    domain = st.sidebar.selectbox("Domain", ["Walmart (Retail)", "DataCo (Supply Chain)"])
    
    # ---------------------------------------------------------
    # WALMART / RETAIL UI
    # ---------------------------------------------------------
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
        
        # Display Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Baseline Risk (2024 DNA)", f"{baseline_risk*100:.1f}%")
        col2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%")
        
        # Display Visual Comparison
        chart_data = pd.DataFrame(
            {"Risk Type": ["Baseline", "Counterfactual"], "Probability (%)": [baseline_risk * 100, simulated_risk * 100]}
        ).set_index("Risk Type")
        st.bar_chart(chart_data, height=250)
        
        if simulated_risk > 0.15:
            st.error("⚠️ TAIL RISK DETECTED: Model predicts stockout probability exceeds 15% threshold.")
            
    # ---------------------------------------------------------
    # DATACO / SUPPLY CHAIN UI
    # ---------------------------------------------------------
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
        
        # Display Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Baseline Risk (2024 Routes)", f"{baseline_risk*100:.1f}%")
        col2.metric("Counterfactual Risk (Era Swap)", f"{simulated_risk*100:.1f}%", f"+{(simulated_risk - baseline_risk)*100:.1f}%")
        
        # Display Visual Comparison
        chart_data = pd.DataFrame(
            {"Risk Type": ["Baseline", "Counterfactual"], "Probability (%)": [baseline_risk * 100, simulated_risk * 100]}
        ).set_index("Risk Type")
        st.bar_chart(chart_data, height=250, color="#ff4b4b")
        
        if simulated_risk > 0.65:
            st.error("⚠️ EXTREME CONGESTION DETECTED: Late delivery probability critically high.")
        elif simulated_risk > baseline_risk + 0.05:
            st.warning("📉 Supply Chain Stress detected. Delays likely.")

if __name__ == "__main__":
    main()
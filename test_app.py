import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os

# --- 1. ELEGANT PAGE CONFIG ---
st.set_page_config(
    page_title="SNOW Intelligence | Q3 War Room", 
    page_icon="❄️",
    layout="wide"
)

# --- 2. HIGH-CONTRAST BRANDED STYLING ---
# Using official Snowflake colors: Deep Navy (#051839) and Winter Blue (#005793)
st.markdown("""
    <style>
    /* Base Typography and Background */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .main { background-color: #ffffff !important; }
    
    /* High-Contrast Text */
    h1, h2, h3, p, span, label { 
        color: #051839 !important; 
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Executive Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #f0f4f9;
        border: 2px solid #051839;
        padding: 25px !important;
        border-radius: 12px;
    }
    
    /* Bold Metric Values */
    div[data-testid="stMetricValue"] > div {
        color: #005793 !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
    }

    /* Professional Q&A Cards (Dark Theme for the Finale) */
    .qa-card {
        background-color: #051839;
        color: #ffffff !important;
        padding: 35px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .qa-card p, .qa-card b, .qa-card span { color: #ffffff !important; }
    
    /* Strategic Sidebar */
    [data-testid="stSidebar"] { 
        background-color: #f8f9fb; 
        border-right: 1px solid #dee2e6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATA PERSISTENCE ---
@st.cache_data
def get_dashboard_data():
    # Attempt to load results from your notebook's JSON output
    if os.path.exists("qa_results.json"):
        with open("qa_results.json", "r") as f:
            return json.load(f)
    return None

results = get_dashboard_data()

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://www.snowflake.com/wp-content/uploads/2023/11/snowflake-logo-blue.png", width=180)
    st.markdown("### **Executive Briefing**")
    nav = st.radio("Strategic Focus", ["Briefing Overview", "Competitive Benchmarking", "Retention Risk (NRR)", "Q&A Readiness"])
    st.divider()
    st.caption("Intelligence Source: FY2026 Q3 10-Q & Peer Transcripts")

# --- 5. PERSISTENT EXECUTIVE TICKER ---
st.markdown("<h1 style='font-weight:800; margin-bottom:0;'>Quarterly Strategic Overview</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.1em; color:#54717d;'>FY2026 Q3 Performance and Risk Assessment</p>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Product Revenue", "$1,160M", "+28.8% YoY")
m2.metric("NRR", "125%", "-200 bps", delta_color="inverse")
m3.metric("RPO", "$6,900M", "+21.1% YoY")
m4.metric("Customers >$1M", "688", "+26.9% YoY")
st.divider()

# --- 6. INTELLIGENCE PILLARS ---

if nav == "Briefing Overview":
    st.markdown("### **Quarterly Situation Report**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        **Current Sentiment:** The market is increasingly focused on **consumption normalization**. While our 29% growth 
        outpaces many legacy peers, analysts are seeking proof that **Cortex AI** adoption will offset structural NRR 
        declines. 
        
        **Strategic Moat:** Our $6.9B RPO remains the strongest indicator of long-term enterprise commitment.
        """)
    with c2:
        st.info("**Key News:** The Anthropic partnership is a critical narrative lever to defend against 'Model Lock-in' fears.")

elif nav == "Competitive Benchmarking":
    st.markdown("### **Competitive Positioning: Growth vs. Margins**")
    
    # Robust Visual: Comparative Bar Chart
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Snowflake', x=['Rev Growth %', 'Gross Margin %'], y=[29, 76], marker_color='#005793'))
    fig.add_trace(go.Bar(name='Datadog', x=['Rev Growth %', 'Gross Margin %'], y=[26, 81], marker_color='#051839'))
    fig.add_trace(go.Bar(name='MongoDB', x=['Rev Growth %', 'Gross Margin %'], y=[22, 77], marker_color='#c5c9d1'))
    
    fig.update_layout(
        template="simple_white",
        barmode='group',
        height=500,
        legend=dict(orientation="h", y=1.1)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **CFO Insight:** We lead the group in top-line growth (29%), but **Datadog's 81% margin profile** remains the 
    benchmark for efficiency. Analysts will probe our path to matching this operating leverage as AI workloads scale.
    """)

elif nav == "Retention Risk (NRR)":
    st.markdown("### **Deep Dive: The NRR Glide Path**")
    
    # Robust Visual: High-Contrast Trend Line
    nrr_hist = pd.DataFrame({
        "Quarter": ["Q4'24", "Q1'25", "Q2'25", "Q3'25", "Q3'26"],
        "NRR": [131, 128, 127, 127, 125]
    })
    
    fig_nrr = px.line(nrr_hist, x="Quarter", y="NRR", markers=True, 
                      color_discrete_sequence=['#005793'])
    fig_nrr.update_layout(template="simple_white", yaxis_range=[120, 135])
    st.plotly_chart(fig_nrr, use_container_width=True)
    
    st.markdown("""
    **Risk Analysis:** 125% represents a historical low. The narrative shift must move from 'Normalization' 
    to 'Stabilization'—highlighting that our **$1M+ cohort** is seeing spend stabilization in the Financial Services vertical.
    """)

elif nav == "Q&A Readiness":
    st.markdown("### **🎯 Analyst Q&A Preparation: The Hot Seat**")
    st.markdown("#### *Predicted 'Hard' Questions & Data-Backed Defenses*")

    # Use a loop to render your generated pairs if they exist
    if results:
        for i, pair in enumerate(results['qa_pairs']):
            st.markdown(f"""
            <div class="qa-card">
                <b style="color: #4da3ff; font-size: 0.85em; text-transform: uppercase;">ANALYST THEME: {pair['question']['theme']}</b>
                <p style="font-size: 1.25em; margin-top: 10px; font-weight:600;">"{pair['question']['question']}"</p>
                <hr style="border: 0.5px solid #ffffff33; margin: 20px 0;">
                <p><b>Executive Defense:</b> {pair['response']}</p>
                <span style="font-size: 0.8em; color: #a5b1c2;">Data Basis: {pair['question']['data_basis']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please run the 'Earnings War Room' notebook to generate the latest Q&A results.")
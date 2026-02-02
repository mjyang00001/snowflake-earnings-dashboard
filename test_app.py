import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os

st.set_page_config(
    page_title="SNOW Intelligence | Q3 War Room", 
    page_icon="❄️",
    layout="wide"
)

st.markdown("""
    <style>
    /* Base Typography and Background */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    .main { background-color: #0a1929 !important; }

    /* Main Content - Light text on dark background */
    .main h1, .main h2, .main h3, .main p, .main span, .main label,
    .main div, .main li, .main em, .main strong {
        color: #e3f2fd !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Sidebar - keep readable on light background */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #051839 !important;
    }

    /* Expander Headers - Fix Text Overlap */
    .streamlit-expanderHeader {
        font-size: 1.1em !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }

    /* Hide the arrow icon completely */
    details summary::before,
    details summary::marker,
    summary::-webkit-details-marker {
        display: none !important;
    }

    /* Remove padding since no arrow */
    details summary {
        padding-left: 0 !important;
        list-style: none !important;
    }

    /* Hide any ::before pseudo-elements that might contain arrow text */
    .streamlit-expanderHeader::before {
        content: none !important;
        display: none !important;
    }
    
    /* Executive Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #f0f4f9;
        border: 2px solid #051839;
        padding: 25px !important;
        border-radius: 12px;
    }

    /* NRR Delta Badge - Red Background (2nd column) */
    div[data-testid="stHorizontalBlock"] > div:nth-of-type(2) [data-testid="stMetricDelta"] {
        background-color: #8B0000 !important;
        border-radius: 6px !important;
        padding: 4px 8px !important;
    }

    /* ALL Metric Text - Force Dark Navy (except deltas) */
    div[data-testid="stMetric"] *:not([data-testid="stMetricDelta"]):not([data-testid="stMetricDelta"] *) {
        color: #051839 !important;
    }

    /* Bold Metric Values - Bright Blue */
    div[data-testid="stMetricValue"] > div {
        color: #005793 !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
    }

    /* Metric Delta - Default Green */
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        color: #ffffff !important;
        background-color: #1e4620 !important;
        border-radius: 6px !important;
        padding: 4px 8px !important;
    }

    div[data-testid="stMetric"] [data-testid="stMetricDelta"] svg {
        fill: #ffffff !important;
    }

    /* Metric Delta - Red for negative (down arrow) - Using nth-of-type for NRR column */
    div[data-testid="stHorizontalBlock"] > div:nth-of-type(2) [data-testid="stMetricDelta"] {
        color: #dc3545 !important;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-of-type(2) [data-testid="stMetricDelta"] svg {
        fill: #dc3545 !important;
    }

    /* Professional Q&A Cards (High Contrast for Dark Mode) */
    .qa-card {
        background-color: #1a1a1a;
        color: #ffffff !important;
        padding: 35px;
        border-radius: 15px;
        margin-bottom: 25px;
        border: 2px solid #29B5E8;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .qa-card p, .qa-card b, .qa-card span { color: #ffffff !important; }
    .qa-card .theme-tag {
        color: #000000 !important;
        background-color: #29B5E8;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.75em;
        text-transform: uppercase;
        font-weight: 700;
    }
    .qa-card hr { border: 1px solid #444444 !important; }
    
    /* Strategic Sidebar */
    [data-testid="stSidebar"] { 
        background-color: #f8f9fb; 
        border-right: 1px solid #dee2e6;
    }
    </style>
    """, unsafe_allow_html=True)


@st.cache_data
def get_dashboard_data():
    if os.path.exists("qa_results.json"):
        with open("qa_results.json", "r") as f:
            return json.load(f)
    return None

results = get_dashboard_data()

with st.sidebar:
    st.image("https://www.snowflake.com/wp-content/uploads/2023/11/snowflake-logo-blue.png", width=180)
    st.markdown("### **Executive Briefing**")
    nav = st.radio("Strategic Focus", ["Executive Brief", "Briefing Overview", "Competitive Intelligence", "Retention Risk (NRR)", "Q&A Readiness"])
    st.divider()
    st.caption("Intelligence Source: FY2026 Q3 10-Q & Peer Transcripts")


# --- 6. INTELLIGENCE PILLARS ---

if nav == "Executive Brief":
    st.markdown("<h1 style='font-weight:800; margin-bottom:0; color:#29B5E8 !important;'>Quarterly Strategic Overview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.1em; color:#A0C4D9 !important;'>FY2026 Q3 Performance and Risk Assessment</p>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Product Revenue", "$1,160M", "+28.8% YoY")
    m2.metric("Net Revenue Retention", "125%", "-200 bps", delta_color="inverse")
    m3.metric("Remaining Perf. Obligations", "$6,900M", "+21.1% YoY")
    m4.metric("Customers >$1M", "688", "+26.9% YoY")
    st.divider()

    st.markdown("### **AI Powered Earnings Call Preparation**")
    st.markdown("**What This Dashboard Does:** Uses AI to predict the toughest analyst questions based on 317 historical earnings call questions, SEC filings, and equity research from 10+ sell side firms.")

    st.divider()

    
    if results and len(results['qa_pairs']) > 0:
        st.markdown("### **Top 3 Predicted Analyst Questions**")
        st.markdown("*High level overview of the toughest questions analysts are likely to ask:*")
        st.markdown("")

        for i, pair in enumerate(results['qa_pairs'], 1):
            # Extract first sentence or first 100 chars of question as preview
            question_text = pair['question']['question']
            preview = question_text.split('?')[0] + '?' if '?' in question_text else question_text[:100] + '...'
            st.markdown(f"**{i}. {pair['question']['theme']}**")
            st.markdown(f"   *{preview}*")
            st.markdown("")

        st.info("→ **Full Q&A preparation with detailed responses available in 'Q&A Readiness' tab**")

        st.divider()

        st.markdown("### **Key Talking Points for CFO**")
        col1, col2 = st.columns(2)
        with col1:
            st.success("**Strength: Revenue Growth**\n\n29% YoY product revenue growth outpaces peers (Datadog 26%, MongoDB 22%). Emphasize enterprise adoption with 688 customers spending >$1M.")
        with col2:
            st.warning("**Risk: NRR Decline**\n\nNRR at 125% (historical low). Narrative must shift from 'normalization' to 'stabilization' - highlight that large customer cohort spending is stabilizing.")
    else:
        st.warning("No Q&A predictions available. Please run the earnings_war_room.ipynb notebook to generate predictions.")

elif nav == "Briefing Overview":
    st.markdown("### **Quarterly Situation Report**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        **Current Sentiment:** The market is increasingly focused on **consumption normalization**. While our 29% growth 
        outpaces many legacy peers, analysts are seeking proof that **Cortex AI** adoption will offset structural NRR 
        declines. 
        
        **Strategic Moat:** Our $6.9B RPO remains the strongest indicator of long term enterprise commitment.
        """)
    with c2:
        st.info("**Key News:** The Anthropic partnership is a critical narrative lever to defend against 'Model Lock in' fears.")

elif nav == "Competitive Intelligence":
    st.markdown("### **We Lead on Growth (29%), Trail on Margins vs. Datadog**")

    
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

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Our Position:**
        - **Growth Leader:** 29% YoY revenue growth outpaces Datadog (26%) and MongoDB (22%)
        - **Strong RPO:** $6.9B in remaining performance obligations signals enterprise commitment
        - **Customer Expansion:** 688 customers spending >$1M annually (+27% YoY)
        """)
    with col2:
        st.markdown("""
        **Key Competitive Threats:**
        - **Databricks:** Competing on lakehouse architecture and Iceberg support
        - **Microsoft Fabric:** Bundling advantage with Azure ecosystem
        - **Margin Gap:** Datadog's 81% gross margin vs our 76% - analysts will probe efficiency
        """)

    st.info("**CFO Talking Point:** We're winning on growth while investing in AI capabilities. As Cortex workloads scale, margins will naturally expand toward peer benchmarks.")

elif nav == "Retention Risk (NRR)":
    st.markdown("### **NRR at Historic Low: 13 Consecutive Quarters of Decline**")
    
    
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
    st.markdown("### **Analyst Q&A Preparation: The Hot Seat**")
    st.markdown("#### *Predicted 'Hard' Questions & Data Backed Defenses*")
    st.markdown("")

    if results:
        for i, pair in enumerate(results['qa_pairs'], 1):
            with st.expander(f"**Question {i}: {pair['question']['theme']}**", expanded=False):
                st.markdown("**Analyst Question:**")
                st.markdown(f"*\"{pair['question']['question']}\"*")
                st.markdown("")
                st.markdown("**Executive Response:**")
                st.markdown(pair['response'])
                st.markdown("")
                st.caption(f"Data basis: {pair['question']['data_basis']}")
    else:
        st.warning("Please run the 'Earnings War Room' notebook to generate the latest Q&A results.")
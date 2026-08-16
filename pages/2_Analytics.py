import streamlit as st
import pandas as pd

from components.load_css import load_css
from components.navbar import navbar
from components.empty_state import empty_analytics, empty_filter
from components.analytics_filter import analytics_filter
from components.analytics_kpi import analytics_kpi
from components.analytics_charts import prediction_section
from components.analytics_distribution import age_distribution, biomarker_comparison 
from components.high_risk_patient import high_risk_patient 
from components.ai_clinical_insight import clinical_recommendation
from components.empty_state import empty_analytics
from components.footer import footer

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

load_css()
navbar()

# Load History
history = st.session_state.get("history", [])

if not history:
    empty_analytics()
    st.stop()

df = pd.DataFrame(history)

if df.empty:
    empty_analytics()
    st.stop()

if "Prediction" not in df.columns:
    empty_analytics()
    st.stop()

# FILTER
df = analytics_filter(df)

# FILTER RESULT

if df.empty:
    empty_filter()
    st.stop()


# DASHBOARD    
st.write("")

analytics_kpi(df)

st.divider()

prediction_section(df)

st.divider()

col1, col2 = st.columns(2)

with col1:
    age_distribution(df)

with col2:
    biomarker_comparison(df)

st.divider()

high_risk_patient(df)

st.divider()

clinical_recommendation(df)

st.divider()

footer()
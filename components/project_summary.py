import streamlit as st

def project_summary():

    st.write("")
    st.markdown("""
<div class="chart-section">

<div class="chart-header">

<div>

<div class="section-title">
📊 Project Summary
</div>

<div class="section-subtitle">
Overview of the AI Clinical Decision Support System
</div>

</div>

</div>
""", unsafe_allow_html=True)

    st.write("")

    cards = [

         {
            "icon":"👥",
            "value":"264",
            "title":"Clinical Patients",
            "desc":"Patient records used for model development.",
            "css":"primary"
        },

        {
            "icon":"🎯",
            "value":"98.11%",
            "title":"Model Accuracy",
            "desc":"Performance after hyperparameter tuning.",
            "css":"success"
        },

        {
            "icon":"🧪",
            "value":"11",
            "title":"Biomarkers",
            "desc":"Clinical laboratory biomarkers analysed.",
            "css":"warning"
        },

        {
            "icon":"📑",
            "value":"3",
            "title":"Prediction Classes",
            "desc":"Non-Diabetic, Prediabetes and Diabetes.",
            "css":"danger"
        }

    ]

    cols = st.columns(4,gap="large")

    for col,card in zip(cols,cards):

        with col:

            st.markdown(f"""

<div class="summary-card {card['css']}">

<div class="summary-top-line">
</div>

<div class="summary-icon">
{card['icon']}
</div>

<div class="summary-value">
{card['value']}
</div>

<div class="summary-title">
{card['title']}
</div>

<div class="summary-description">
{card['desc']}
</div>

</div>

""",unsafe_allow_html=True)

    st.divider()

import streamlit as st


def system_features():

    st.markdown("""

<div class="chart-section">

<div class="chart-header">

<div>

<div class="section-title">
🚀 System Features
</div>

<div class="section-subtitle">
Core capabilities of the AI Clinical Decision Support System

</div>

</div>

</div>

""", unsafe_allow_html=True)

    st.write("")
    features = [

        {
            "icon":"🧪",
            "title":"Clinical Laboratory Data",
            "description":"Input patient laboratory biomarkers including HbA1c, BMI, cholesterol profile, creatinine, urea, and other clinical indicators used for diabetes prediction."
        },

        {
            "icon":"🤖",
            "title":"AI Prediction Engine",
            "description":"Generate multiclass diabetes predictions using a Tuned XGBoost model trained on clinical laboratory biomarkers with high predictive performance."
        },

        {
            "icon":"📊",
            "title":"Interactive Analytics",
            "description":"Explore prediction trends, patient demographics, biomarker analysis, and clinical distributions through interactive visual dashboards."
        },

        {
            "icon":"💡",
            "title":"Clinical Recommendations",
            "description":"Receive AI-assisted clinical recommendations based on prediction outcomes to support healthcare professionals during patient assessment."
        }

    ]

    col1, col2 = st.columns(2, gap="large")

    columns = [col1, col2, col1, col2]

    for col, feature in zip(columns, features):

        with col:
            st.markdown(f"""

<div class="feature-card">

<div class="feature-icon">
{feature["icon"]}
</div>

<div class="feature-title">
{feature["title"]}
</div>

<div class="feature-description">
{feature["description"]}
</div>

</div>

""", unsafe_allow_html=True)
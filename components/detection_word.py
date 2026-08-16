import streamlit as st

# AI Insight
def detection_word():

    st.markdown(f"""

<div class="insight-card">

<div class="insight-header">

<div class="insight-title">
🔬 Why Early Detection Matters
</div>

<div class="insight-badge">
💚 Preventive Healthcare
</div>

</div>

<div class="insight-body">

<p>

Diabetes is one of the leading chronic diseases worldwide, and many individuals remain undiagnosed until serious complications develop.
Early screening and regular health monitoring can help identify potential risks before symptoms become severe.
<b>This AI-powered system supports healthcare </b> awareness by providing predictive insights based on clinical data,
enabling users to take proactive steps toward a healthier lifestyle.

</p>

<div class="recommendation-item">
✔️ <b>Early Risk Identification</b> – Detect potential diabetes risk at an early stage.
</div>

<div class="recommendation-item">
✔️ <b>Support Preventive Healthcare</b> – Encourage timely screening and routine health monitoring.
</div>

<div class="recommendation-item">
✔️ <b>Encourage Healthy Lifestyle</b> – Promote healthier habits through increased awareness.
</div>

<div class="recommendation-item">
✔️ <b>AI-Assisted Decision Support</b> – Provide data-driven insights to complement medical evaluation.
</div>

<div class="insight-footer">

<b>Disclaimer</b><br>

This application is designed to support diabetes awareness and early risk assessment.
Prediction results are generated using a machine learning model based on clinical health data and
should not be considered a substitute for professional medical diagnosis, treatment, or healthcare advice.

</div>

</div>

</div>

""", unsafe_allow_html=True)

    
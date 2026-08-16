import streamlit as st


def about_page():

    st.markdown("""

<div class="system-card">

<div class="system-header">

<div class="system-title">
ℹ️ System Information
</div>

<div class="system-version">
Version 1.0
</div>

</div>

<div class="system-divider"></div>

<div class="system-grid">

<div class="system-item">

<div class="system-item-title">
🧠 AI Model
</div>

<div class="system-item-value">
Tuned XGBoost
</div>

<div class="system-item-desc">
Multiclass classification model optimized using
Randomized Search Cross Validation for diabetes
risk prediction.
</div>

</div>

<div class="system-item">

<div class="system-item-title">
🏥  Purpose
</div>

<div class="system-item-value">
Clinical Decision Support
</div>

<div class="system-item-desc">
Designed to assist healthcare professionals during
early diabetes screening and patient risk assessment.
</div>

</div>

<div class="system-item">

<div class="system-item-title">
📊 Prediction Classes
</div>

<div class="system-item-value">
3 Risk Categories
</div>

<div class="system-item-desc">
• Non-Diabetic<br>
• Prediabetes<br>
• Diabetes
</div>

</div>

<div class="system-item">

<div class="system-item-title">
📅 Release
</div>

<div class="system-item-value">
July 2026
</div>

<div class="system-item-desc">
Current production version developed for interactive
clinical analytics and AI-assisted patient monitoring.
</div>

</div>
</div>

<div class="system-divider"></div>

<div class="system-notice">

<div class="system-notice-title">
⚕️ Clinical Notice
</div>

<div class="system-notice-text">
This dashboard integrates machine learning predictions,
clinical laboratory biomarkers, and descriptive analytics
to support healthcare professionals during diabetes
screening and patient risk assessment.

The prediction results are generated using a Tuned
XGBoost Multiclass Classifier trained on historical
clinical data. All charts and statistics presented
throughout the dashboard summarize aggregated patient
predictions and are intended to facilitate clinical
monitoring and decision support.

Although the model demonstrates strong predictive
performance, all recommendations and risk classifications
should be interpreted as supportive information rather
than definitive medical diagnoses.

Clinical decisions should always be confirmed through
appropriate laboratory examinations, patient history,
physical assessment, and professional medical judgment.

This system is designed to improve clinical efficiency,
support early risk identification, and enable
data-driven healthcare decisions without replacing
licensed healthcare professionals.

</div>
</div>

""", unsafe_allow_html=True)
    
    st.markdown("""
<div class="insight-card">

<div class="insight-header">

<div class="insight-title">
⚙️ AI Prediction Workflow
</div>

<div class="insight-badge">
System Methodology
</div>

</div>

<div class="insight-body">

<p>
This application integrates clinical data, statistical analysis, 
and machine learning techniques to support early diabetes risk assessment. 
The prediction results are designed to provide reliable, 
data-driven insights that complement healthcare decision-making.
</p>

<div class="recommendation-section">

<div class="about-grid">

<div class="about-item">
<div class="about-icon">📂</div>
<div class="about-title">Dataset</div>
<div class="about-text">
Clinical patient records containing demographic information,
laboratory test results, and health indicators.
</div>
</div>

<div class="about-item">
<div class="about-icon">🧹</div>
<div class="about-title">Preprocessing</div>
<div class="about-text">
Data cleaning, feature preparation, and transformation
to ensure high-quality input for analysis.
</div>
</div>

<div class="about-item">
<div class="about-icon">📊</div>
<div class="about-title">Statistical Analysis</div>
<div class="about-text">
Statistical validation of clinical variables to understand
data characteristics before model development.
</div>
</div>

<div class="about-item">
<div class="about-icon">🧠</div>
<div class="about-title">Machine Learning</div>
<div class="about-text">
XGBoost multiclass classification model trained to identify
diabetic, pre-diabetic, and non-diabetic conditions.
</div>
</div>

<div class="about-item">
<div class="about-icon">🎯</div>
<div class="about-title">Prediction</div>
<div class="about-text">
AI-generated predictions provide decision-support insights
for early diabetes risk assessment.
</div>
</div>

</div>

</div>

<div class="insight-footer">

<b>System Overview</b><br>

The prediction workflow combines clinical data, statistical validation,
and machine learning to generate accurate and explainable diabetes
risk predictions for educational and decision-support purposes.

</div>

</div>

</div>
""", unsafe_allow_html=True)
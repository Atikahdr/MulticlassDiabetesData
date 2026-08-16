import streamlit as st

def recommendations(pred_class):

    if pred_class == 0:

        recommendations = [

            "Maintain a balanced and nutritious diet.",
            "Exercise at least 150 minutes every week.",
            "Stay hydrated and maintain healthy body weight.",
            "Perform HbA1c screening annually.",
            "Get adequate sleep and manage stress."

        ]

    elif pred_class == 1:

        recommendations = [

            "Reduce sugar and refined carbohydrate intake.",
            "Increase physical activity every day.",
            "Maintain an ideal body weight.",
            "Monitor fasting blood glucose every 3–6 months.",
            "Consult a healthcare professional for lifestyle intervention."

        ]

    else:

        recommendations = [

            "Consult an endocrinologist immediately.",
            "Follow prescribed medication consistently.",
            "Monitor blood glucose regularly.",
            "Follow a diabetic-friendly meal plan.",
            "Schedule regular follow-up appointments."

        ]

    recommendation_html = ""

    for rec in recommendations:
        recommendation_html += f"""
<div class="recommendation-item">
✔️ {rec}
</div>
"""

    st.markdown(
    f"""
<div class="insight-card">

<div class="insight-header">

<div class="insight-title">
💡 Clinical Recommendation
</div>

</div>

<div class="insight-divider"></div>

<div class="insight-body">

<div class="recommendation-section">
{recommendation_html}
</div>

<div class="insight-footer">

<b>System Overview</b><br>

This prediction is generated using the Tuned XGBoost model and is intended only as a Clinical Decision Support System (CDSS).
Final diagnosis should always be confirmed by qualified healthcare professionals.

</div>
</div>

</div>
""",
    unsafe_allow_html=True)
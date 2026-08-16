import streamlit as st

# AI Insight
def clinical_recommendation(df):

    diabetes = df[df["Prediction"] =="Diabetes"]

    if diabetes.empty:
        st.success("No patients requiring clinical recommendation.")
        return
    
    # Statistics
    total = len(df)
    diabetes_count = len(diabetes)

    diabetes_pct = diabetes_count / total * 100
    avg_age = diabetes["AGE"].mean()
    avg_bmi =  diabetes["BMI"].mean()
    avg_hba1c = diabetes["HbA1c"].mean()
    avg_confidence = diabetes["Confidence"].max()

    recommendations = []

    # Recommendation 1
    if avg_hba1c >= 6.5:
        recommendations.append(
            "Review patients with <b>HbA1c ≥ 6.5%</b> and "
            "confirm the diagnosis using appropriate laboratory testing."
        )

    # Recommendation 2
    if avg_bmi >= 25:
        recommendations.append(
            "Encourage <b>weight management</b>, regular physical activity,"
            "and nutritional counseling for overweight patients."
        )

    # Recommendation 3
    if diabetes_pct >= 30:
        recommendations.append(
            "Encourage <b>weight management</b>, regular physical activity,"
            "and nutritional counseling for overweight patients."                                                                                                                                                                                                                                                                                                           
        )

    # Recommendation 4
    if avg_confidence >= 90:
        recommendations.append(
            "Predictions show <b>high model confidence</b>; however," 
            "clinical decisions should always be confirmed by healthcare professionals."
        )

    recommendation_html = ""

    for rec in recommendations:
        recommendation_html += f"""

<div class="recommendation-item">
✔️ {rec}
</div>
"""

    st.markdown(f"""

<div class="insight-card">

<div class="insight-header">

<div class="insight-title">
🧠 Clinical Recommendations
</div>

<div class="insight-badge">
{len(recommendations)} Recommendations
</div>

</div>

<div class="insight-body">

<p>

Based on analysis of <b>{total}</b> patient records, the model identified
<b>{diabetes_count}</b> patients
(<b>{diabetes_pct:.1f}%</b>) as Diabetes.
The average patient profile includes an age of
<b>{avg_age:.1f}</b> years,
BMI of <b>{avg_bmi:.1f}</b> kg/m²,
HbA1c of <b>{avg_hba1c:.2f}%</b>,
and an average prediction confidence of
<b>{avg_confidence:.1f}%</b>.

</p>

<div class="recommendation-section">

{recommendation_html}

</div>

<div class="insight-footer">

<b>Disclaimer</b><br>

These recommendations are generated from aggregated prediction results and
are intended to support clinical decision-making. They should not replace professional medical evaluation, diagnosis, or treatment.

</div>

</div>

</div>

""", unsafe_allow_html=True)
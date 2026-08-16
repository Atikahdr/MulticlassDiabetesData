import streamlit as st
import plotly.graph_objects as go

from components.recommendation import recommendations

@st.dialog(" ", width="large")
def prediction_result(pred_class, probabilities, patient_info):

    confidence = max(probabilities) * 100

    patient_name = patient_info["Patient Name"]
    medical_record = patient_info["Medical Record"]

    gender = patient_info.get("Gender", 0)

    gender_text = {
        0: "👨 Male",
        1: "👩 Female"
    }.get(gender, "Unknown")

    age = patient_info["AGE"]
    assessment_time = patient_info["Assessment Time"]

    # RESULT

    if pred_class == 0:

        card_class = "green"
        badge = "✅ Low Risk"
        title = "Non-Diabetic"

    elif pred_class == 1:

        card_class = "yellow"
        badge = "⚠️ Moderate Risk"
        title = "Prediabetes"

    else:

        card_class = "red"
        badge = "🔴 High Risk"
        title = "Diabetes"

    # PATIENT INFORMATION
    st.markdown(
        f"""
<div class="patient-result-card">

<div class="patient-result-title">
👤 Patient Name
</div>

<div class="patient-result">

<div class="patient-label">
Medical Record :
</div>

<div class="patient-value">
{medical_record}
</div>

<div class="patient-label">
Patient Name    :
</div>

<div class="patient-value">
{patient_name}
</div>

<div class="patient-label">
Gender :
</div>

<div class="patient-value">
{gender_text}
</div>

<div class="patient-label">
Age :
</div>

<div class="patient-value">
{age} years
</div>

<div class="patient-label">
Assessment Time :
</div>

<div class="patient-value">
{assessment_time}
</div>

</div>
""",
unsafe_allow_html=True
)

    st.write("")

    # RESULT CARD
    left, right = st.columns([1.1, 1], gap="large")

    with left:

        st.markdown(
            f"""
            
<div class="result-card {card_class}">

<div class="result-title">
🎯 AI Prediction Result
</div>


<div class="result-badge">
{badge}
</div>

<div class="result-class">
{title}
</div>

<div class="result-confidence">
Prediction Confidence
<b>{confidence:.2f}%</b>
</div>

<div class="confidence-bar">

<div
class="confidence-fill"
style="width:{confidence:.2f}%;">
</div>
</div>

</div>
""",
unsafe_allow_html=True
)

    # CHART
    with right:

        fig = go.Figure()

        fig.add_trace(

            go.Bar(

                y=[
                    "Non-Diabetic",
                    "Prediabetes",
                    "Diabetes"
                ],

                x=[p * 100 for p in probabilities],

                orientation="h",

                marker=dict(
                
                    color=[
                        "#10B981",
                        "#F59E0B",
                        "#EF4444"
                    ],

                    cornerradius=12

                ),

                text=[
                    f"{p*100:.2f}%"
                    for p in probabilities
                ],

                textposition="outside"

            )

        )

        fig.update_layout(
            
            title=dict(
                text="📊 Probability Distribution",
                x=0.03,
                xanchor="left",
                font=dict(
                    size=20,
                    family="Arial"
                )
            ),

            height=320,

            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            ),

            yaxis=dict(

                showgrid=False

            ),

            xaxis_title="Probability (%)",
            showlegend=False,
            template="plotly_white"

        )

        st.plotly_chart(
            fig,
            width="stretch",
            config={"displayModeBar": False}
        )

    recommendations(pred_class)
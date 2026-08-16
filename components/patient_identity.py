import streamlit as st

def patient_identity():

    st.markdown("""
<div class="patient-card">

<div class="patient-header">

<div>

<div class="patient-title">
👤 Patient Identity
</div>

<div class="patient-subtitle">
Enter the patient's basic information before generating the prediction.
</div>

</div>

<div class="patient-badge">
Required
</div>

</div>

</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:

        patient_name = st.text_input(
            "Patient Name",
            placeholder="Enter patient name",
            key="patient_name"
        )

    with col2:

        patient_id = st.text_input(
            "Medical Record Number",
            placeholder="MR-000001",
            key="patient_id"
        )

    return {

        "patient_name": patient_name,
        "patient_id": patient_id

    }
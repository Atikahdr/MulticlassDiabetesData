import streamlit as st

def patient_profile():

    st.markdown("""
<div class="profile-card">

<div class="profile-header">

<div>

<div class="profile-title">
📋 Patient Profile
</div>

<div class="profile-subtitle">
Demographic information and clinical indicators used to support diabetes risk prediction.
</div>

</div>

<div class="profile-badge">
Clinical Data
</div>

</div>

</div>
    """, unsafe_allow_html=True)


    col1, col2 = st.columns(2, gap="large")

    with col1:

        gender = st.radio(
            "Gender",
            [0, 1],
            horizontal=True,
            format_func=lambda x: "👨 Male" if x == 0 else "👩 Female",
        )
        

        bmi = st.slider(
            "BMI (kg/m²)",
            10.0,
            50.0,
            24.5,
            0.1,
            key="bmi"
        )

    with col2:

        age = st.slider(
            "Age (Years)",
            1,
            100,
            35,
            key="age"
        )

        hba1c = st.slider(
            "HbA1c (%)",
            3.0,
            15.0,
            8.1,
            0.1,
            key="hba1c"
        )

    return {
        "gender": gender,
        "age": age,
        "bmi": bmi,
        "hba1c": hba1c
    }
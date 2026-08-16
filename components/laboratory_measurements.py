import streamlit as st

def laboratory_measurements():

    st.markdown("""
<div class="lab-card">

<div class="lab-header">

<div>

<div class="lab-title">
🧪 Clinical Laboratory Measurements
</div>

<div class="lab-subtitle">
Clinical laboratory biomarkers analyzed by the AI model to estimate diabetes risk.
</div>

</div>

<div class="lab-badge">
Biomarkers
</div>

</div>

</div>
    """, unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")

    with left:

        cr = st.number_input(
            "Creatinine (mg/dL)",
            min_value=0.10,
            max_value=15.00,
            value=1.00,
            step=0.10,
            format="%.2f",
            key="cr"
        )

        chol = st.number_input(
            "Cholesterol (mg/dL)",
            min_value=100.0,
            max_value=400.0,
            value=180.0,
            step=1.0,
            key="chol"
        )

        ldl = st.number_input(
            "LDL (mg/dL)",
            min_value=50.0,
            max_value=300.0,
            value=100.0,
            step=1.0,
            key="ldl"
        )

        vldl = st.number_input(
            "VLDL (mg/dL)",
            min_value=5.0,
            max_value=80.0,
            value=30.0,
            step=1.0,
            key="vldl"
        )

    with right:

        urea = st.number_input(
            "Urea (mg/dL)",
            min_value=1.0,
            max_value=300.0,
            value=30.0,
            step=1.0,
            key="urea"
        )

        hdl = st.number_input(
            "HDL (mg/dL)",
            min_value=20.0,
            max_value=100.0,
            value=50.0,
            step=1.0,
            key="hdl"
        )

        tg = st.number_input(
            "Triglycerides (mg/dL)",
            min_value=30.0,
            max_value=600.0,
            value=150.0,
            step=1.0,
            key="tg"
        )

    return {
        "Cr_mgdl": cr,
        "Urea_mgdl": urea,
        "Chol_mgdl": chol,
        "HDL_mgdl": hdl,
        "LDL_mgdl": ldl,
        "TG_mgdl": tg,
        "VLDL_mgdl": vldl,
    }
import streamlit as st

def hero():

    left, right = st.columns([1.7, 1], gap="large")
    
    # LEFT
    with left:

        st.markdown(
                    """
<div class="hero-card">

<div class="hero-top">

<span class="hero-badge">
🧠 AI Powered Healthcare
</span>

<span class="hero-version">
Version 1.0
</span>

</div>

<div class="hero-title">
Diabetes Clinical
<br>
Decision Support System
</div>

<div class="hero-description">
AI-assisted platform for early diabetes screening using
clinical laboratory biomarkers and a <b>Tuned XGBoost Multiclass Classification Model</b>
<br>
Designed to support healthcare professionals through
interactive prediction, clinical analytics,
and patient monitoring.

</div>

</div>
""", unsafe_allow_html=True)
        
        st.write("")

        b1, b2 = st.columns(2)

        with b1:

            if st.button(
                "🚀 Start Prediction",
                type="primary",
                use_container_width=True,
            ):
                
                st.switch_page("pages/1_Prediction.py")

        with b2:

            if st.button(
                "📊 View Analytics",
                use_container_width=True,
                key="analytics",
            ):
                st.switch_page("pages/2_Analytics.py")

    # RIGHT
    with right:

        st.image(
            "assets/doctor.png",
            width=430
        )

        st.markdown(
            """
<div style="text-align:center;color:#6B7280;font-size:14px;">
AI-assisted clinical decision support
</div>
""",
            unsafe_allow_html=True
        )

    st.divider()
import streamlit as st


def navbar():

    if "app_theme" not in st.session_state:
            st.session_state.app_theme = "light"

    st.markdown("""
<div class="app-header">

<div class="app-title">
🧬 Diabetes Clinical AI
</div>

<div class="app-subtitle">
Clinical Decision Support System for Early Diabetes Risk Assessment
</div>


</div>
""", unsafe_allow_html=True)
    
    # NAVIGATION
    left, nav1, nav2, nav3, nav4, nav5= st.columns([5, 1, 1, 1, 1, 1])

    with nav1:
        st.page_link("app.py", label="Dashboard")

    with nav2:
        st.page_link("pages/1_Prediction.py", label="Prediction")

    with nav3:
        st.page_link("pages/2_Analytics.py", label="Analytics")

    with nav4:
        st.page_link("pages/3_History.py", label="History")

    with nav5:
        st.page_link("pages/4_About.py", label="About")

    st.divider()
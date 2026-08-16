import streamlit as st

def prediction_button():

    st.markdown("<br>", unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "🚀 Generate Diabetes Prediction",
        type="primary",
        width="stretch"
    )

    return submitted
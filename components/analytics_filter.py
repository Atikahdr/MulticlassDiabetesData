import streamlit as st
import pandas as pd
from datetime import datetime


def analytics_filter(df):

    # DEFAULT SESSION STATE
    if "filter_date" not in st.session_state:
        st.session_state.filter_date = ()

    if "filter_gender" not in st.session_state:
        st.session_state.filter_gender = "All"

    if "filter_prediction" not in st.session_state:
        st.session_state.filter_prediction = "All"

    if "filter_keyword" not in st.session_state:
        st.session_state.filter_keyword = ""


    # RESET CALLBACK
    def reset_filters():

        st.session_state.filter_date = ()
        st.session_state.filter_gender = "All"
        st.session_state.filter_prediction = "All"
        st.session_state.filter_keyword = ""

    # HEADER
    col1, col2 = st.columns([5, 1.5])

    with col1:

        st.markdown("""
<div class="analytics-header-card">

<div class="analytics-title">
📊 Clinical Analytics Dashboard
</div>

<div class="analytics-subtitle">
Interactive Diabetes Monitoring
</div>

<div class="analytics-description">
AI-powered clinical decision support dashboard for monitoring patient predictions,
disease trends, and laboratory biomarkers.
</div>

</div>
""", unsafe_allow_html=True)

    with col2:

        now = datetime.now()

        st.markdown(f"""
<div class="analytics-header-card analytics-update">

<div class="time-title">
Last Updated
</div>

<div class="time-value">
{now.strftime("%d %b %Y")}
</div>

<div class="time-caption">
{now.strftime("%I:%M %p")}
</div>

</div>
""", unsafe_allow_html=True)

    st.write("")


    # FILTER
    st.markdown(
        '<div class="analytics-filter-card">',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(
        [1.3, 1.1, 1.2, 2.2, 0.8],
        vertical_alignment="bottom"
    )

    #Date Range
    with c1:

        date_range = st.date_input(
            "📅 Date",
            key="filter_date",
            width="stretch"
        )

    # Gender
    with c2:

        gender = st.selectbox(
            "👤 Gender",
            ["All", "Male", "Female"],
            key="filter_gender",
            width="stretch"
        )

    # Prediction
    with c3:

        prediction = st.selectbox(
            "🎯 Prediction",
            ["All", "Non-Diabetic", "Prediabetes", "Diabetes"],
            key="filter_prediction",
            width="stretch"
        )

    # Search
    with c4:

        keyword = st.text_input(
            "🔍 Search Patient",
            placeholder="Medical Record / Patient Name...",
            key="filter_keyword",
            width="stretch"
        )

    # Reset
    with c5:

        st.button(
            "↻ Reset",
            key="reset_analytics",
            use_container_width=True,
            on_click=reset_filters
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # APPLY FILTER
    df_filtered = df.copy()

    # Date
    if len(date_range) == 2:

        start, end = date_range

        df_filtered = df_filtered[
            (pd.to_datetime(df_filtered["Date"]).dt.date >= start)
            &
            (pd.to_datetime(df_filtered["Date"]).dt.date <= end)
        ]

    # Gender
    if gender != "All":

        gender_value = 0 if gender == "Male" else 1

        df_filtered = df_filtered[
            df_filtered["Gender"] == gender_value
        ]

    # Prediction
    if prediction != "All":

        df_filtered = df_filtered[
            df_filtered["Prediction"] == prediction
        ]

    # Search
    if keyword.strip():

        df_filtered = df_filtered[
            df_filtered["Patient Name"].str.contains(
                keyword,
                case=False,
                na=False
            )
            |
            df_filtered["Medical Record"].astype(str).str.contains(
                keyword,
                case=False,
                na=False
            )
        ]

    return df_filtered
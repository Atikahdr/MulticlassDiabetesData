import streamlit as st


def empty_analytics():

    st.markdown(
        """
<div class="empty-state">

<div class="empty-icon">
📊
</div>

<div class="empty-title">
No Prediction History Available
</div>

<div class="empty-subtitle">
Analytics Dashboard
</div>

<div class="empty-description">

There are currently no prediction records available for analysis.

Generate your first diabetes prediction to unlock interactive
analytics, patient statistics, clinical insights, and AI-powered
visualizations.

</div>

<div class="empty-highlight">

✓ Clinical Dashboard<br>
✓ Patient Statistics<br>
✓ AI Clinical Insights<br>
✓ Prediction Distribution

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2, col3 = st.columns([2,2,2])

    with col2:

        if st.button(
            "🚀 Start First Prediction",
            type="primary",
            use_container_width=True,
        ):
            st.switch_page("pages/1_Prediction.py")


# Empty History
def empty_history():

    st.markdown(
        """
<div class="empty-state">

<div class="empty-icon">
📜
</div>

<div class="empty-title">
No Prediction History Available
</div>

<div class="empty-subtitle">
Patient Prediction Records
</div>

<div class="empty-description">

There are currently no prediction records stored in the system.

Generate your first diabetes prediction to begin building
a complete patient history for clinical review, monitoring,
and future analytics.

</div>

<div class="empty-highlight">

✓ Store Patient Records<br>
✓ Track Previous Predictions<br>
✓ Review Clinical Assessments<br>
✓ Support Long-Term Monitoring

</div>

</div>
""",
        unsafe_allow_html=True,)

    st.write("")

    col1, col2, col3 = st.columns([2,2,2])

    with col2:

        if st.button(
            "🚀 Start First Prediction",
            type="primary",
            use_container_width=True,
            key="history_empty_prediction"
        ):

            st.switch_page("pages/1_Prediction.py")

def empty_filter():
    st.markdown("""

<div class="empty-state">
<div class="empty-icon">
🔍
</div>

<div class="empty-title">
No Matching Data
</div>

<div class="empty-description">
No prediction records match your selected filters.<br><br>

Please try changing the Prediction category,
Search keyword, or Date Range.
</div>

</div>


""", unsafe_allow_html=True)
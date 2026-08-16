import streamlit as st
import pandas as pd

from components import footer
from components.empty_state import empty_history
from components.analytics_kpi import analytics_kpi


def history_page():

    # HISTORY DATA EXISTS CHECK
    history = st.session_state.get("history", [])
    
    if len(history) == 0:
    
        empty_history()
        st.stop()
        
    df = pd.DataFrame(history)
    
    if df.empty:
    
        empty_history()
        st.stop()
    
    if "Prediction" not in df.columns:
    
        empty_history()
        st.stop()
        
    st.markdown("""
<div class="analytics-header-card">

<div class="analytics-title">
📜 Prediction History
</div>

<div class="analytics-subtitle">
Prediction Records & Clinical Review
</div>

<div class="analytics-description">
Review previous diabetes prediction results, patient records, and clinical assessment history for monitoring and follow-up.
</div>

</div>
""", unsafe_allow_html=True)

    st.write("")

    # Card
    st.markdown(
        '<div class="analytics-filter-card">', 
        unsafe_allow_html=True)
    
    # KPI Dashboard
    analytics_kpi(df)

    st.divider()

    # TOOLBAR
    col1, col2, col3, col4 = st.columns(
        [4,1,2,1.2],
        vertical_alignment="bottom"
    )

    with col1:

        keyword = st.text_input(
            "",
            placeholder="🔍 Search Medical Record Patient",
            label_visibility="collapsed"
        )

    with col2:

        search = st.button(
            "🔎 Search",
            width="stretch"
        )

    with col3:

        if len(df) > 0:

            selected_patient = st.multiselect(
                "",
                options=df["Patient Name"].unique(),
                placeholder="Select patient...",
                label_visibility="collapsed"
            )

        else:

            selected_patient = []

            st.multiselect(
                "",
                options=[],
                placeholder="No Data",
                disabled=True,
                label_visibility="collapsed"
            )

    with col4:

        st.write("")
        clear_all = st.button(
            "🗑 Clear All",
            width="stretch"
        )

    # SEARCH
    if search and keyword != "":

        df = df[
            df["Medical Record"]
            .str.contains(keyword, case=False, na=False)
        ]

    # DELETE SELECTED
    if len(selected_patient) > 0:

        if st.button(
            "🗑 Delete Selected",
            width="stretch"
        ):

            st.session_state.history = [

                item
                for item in st.session_state.history
                if item["Patient Name"] not in selected_patient

            ]

            st.success("Selected patient deleted.")

            st.rerun()

    # CLEAR HISTORY
    if clear_all:

        st.session_state.history = []
        st.success("History cleared.")

        st.rerun()

    st.write("")
    # TABLE
    if len(df) == 0:

        st.info("No prediction history available.")

        return

    html = """
<table class="history-table">

<thead>

<tr>

<th>Date</th>
<th>Medical Record</th>
<th>Patient</th>
<th>Age</th>
<th>Gender</th>
<th>BMI</th>
<th>HbA1c</th>
<th>Creatinine</th>
<th>Urea</th>
<th>Cholesterol</th>
<th>HDL</th>
<th>LDL</th>
<th>Triglycerides</th>
<th>VLDL</th>
<th>Prediction</th>
<th>Confidence</th>

</tr>

</thead>

<tbody>
"""

    for _, row in df.iterrows():

        if row["Prediction"] == "Non-Diabetic":

            badge = """
<span class="history-badge badge-normal">
✅ Non Diabetic
</span>
"""

        elif row["Prediction"] == "Prediabetes":

            badge = """
<span class="history-badge badge-prediabetes">
⚠️ Prediabetes
</span>
"""

        else:

            badge = """
<span class="history-badge badge-diabetes">
🔴 Diabetes
</span>
"""

        gender = "Male" if row["Gender"] == 0 else "Female"

        html += f"""

<tr>

<td>{row['Date']}</td>
<td>{row['Medical Record']}</td>
<td>{row['Patient Name']}</td>
<td>{row['AGE']}</td>
<td>{"Male" if row["Gender"] == 0 else "Female"}</td>
<td>{row['BMI']:.1f}</td>
<td>{row['HbA1c']:.1f}</td>
<td>{row['Cr_mgdl']:.2f}</td>
<td>{row['Urea_mgdl']:.2f}</td>
<td>{row['Chol_mgdl']:.2f}</td>
<td>{row['HDL_mgdl']:.2f}</td>
<td>{row['LDL_mgdl']:.2f}</td>
<td>{row['TG_mgdl']:.2f}</td>
<td>{row['VLDL_mgdl']:.2f}</td>
<td>{badge}</td>
<td>{row['Confidence']:.2f}%</td>

</tr>

"""

    html += """

</tbody>

</table>

"""

    st.markdown(html, unsafe_allow_html=True)
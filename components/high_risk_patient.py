import streamlit as st

# High Risk Patient (Table)
def high_risk_patient(df):

    if df.empty:
        return

    highest = df.loc[df["Confidence"].idxmax()]
    
    st.markdown("""
<div class="chart-section">
                    
<div class="chart-header">
    
<div>
    
<div class="chart-title">
🚨 High Risk Patients
</div>
    
<div class="chart-subtitle">
Patients predicted as Diabetes with Prediction Confidence ≥ 80%
</div>
    
</div>
    
<div class="analytics-live">
<span class="live-dot"></span>
LIVE
</div>
    
</div>
    
""", unsafe_allow_html=True)

    high = (
        df[
            (df["Prediction"] == "Diabetes") &
            (df["Confidence"] >= 80)
        ]
        .sort_values(
            by="Confidence",
            ascending=False
        )
        .reset_index(drop=True)
    )

    if high.empty:

        st.success("✅ No high-risk patients detected.")

        return

    # SUMMARY KPI
    total_high = len(high)
    avg_age = high["AGE"].mean()
    avg_hba1c = high["HbA1c"].mean()
    avg_conf = high["Confidence"].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
    
        st.markdown(f"""
    
<div class="kpi-summary">

<div class="kpi-summary-title">
Hight Risk Patients
</div>

<div class="kpi-summary-value">
{total_high}
</div>

<div class="kpi-summary-unit">
Patients Requiring Review
</div>

</div>

""", unsafe_allow_html=True)

    with c2:
    
        st.markdown(f"""
    
<div class="kpi-summary">

<div class="kpi-summary-title">
Average HbA1c
</div>

<div class="kpi-summary-value">
{avg_hba1c:.1f}%
</div>

<div class="kpi-summary-unit">
Mean Glycemic Level
</div>

</div>

""", unsafe_allow_html=True)
    
    with c3:
    
        st.markdown(f"""
    
<div class="kpi-summary">

<div class="kpi-summary-title">
Average Age
</div>

<div class="kpi-summary-value">
{avg_age:.1f}
</div>

<div class="kpi-summary-unit">
Across High-Risk Patients
</div>

</div>

""", unsafe_allow_html=True)

    with c4:
        
        st.markdown(f"""
        
<div class="kpi-summary">

<div class="kpi-summary-title">
Avg Confidence
</div>

<div class="kpi-summary-value">
{avg_conf:.1f}
</div>

<div class="kpi-summary-unit">
Model Prediction Confidence
</div>

</div>

""", unsafe_allow_html=True)
        
    st.write("")

    # TABLE
    html = """
<table class="history-table">

<thead>

<tr>

<th>Clinical Priority</th>
<th>Medical Record</th>
<th>Patient</th>
<th>Age</th>
<th>Gender</th>
<th>HbA1c</th>
<th>BMI</th>
<th>Confidence</th>
<th>Clinical Action</th>

</tr>

</thead>

<tbody>
"""

    for _, row in high.iterrows():

        gender = "Male" if row["Gender"] == 0 else "Female"

        # PRIORITY
        if row["Confidence"] >= 95:

            priority = """
<span class="priority-critical">
P1 • Critical
</span>
"""

            action = """
<span class="history-badge badge-critical">
Urgent Review
</span>
"""

        elif row["Confidence"] >= 90:

            priority = """
<span class="priority-high">
P2 • High
</span>
"""

            action = """
<span class="history-badge badge-high">
Clinical Review
</span>
"""

        else:

            priority = """
<span class="priority-medium">
P3 • Moderate
</span>
"""

            action = """
<span class="history-badge badge-medium">
Follow-up
</span>
"""

        # CONFIDENCE BADGE
        confidence = f"""
<span class="confidence-badge">
{row['Confidence']:.1f}%
</span>
"""

        html += f"""

<tr>

<td>{priority}</td>
<td>{row['Medical Record']}</td>

<td>
<b>{row['Patient Name']}</b>
</td>

<td>{int(row['AGE'])}</td>
<td>{gender}</td>

<td>
<b>{row['HbA1c']:.1f}%</b>
</td>

<td>{row['BMI']:.1f}</td>
<td>{confidence}</td>
<td>{action}</td>

</tr>

"""
    html += """

</tbody>

</table>

"""
    st.markdown(
        html,
        unsafe_allow_html=True
    )

    # FOOTER INSIGHT
    highest = high.iloc[0]

    st.error(
        f"""
**Clinical Insight**

The highest-risk patient is **{highest['Patient Name']}**
with **HbA1c {highest['HbA1c']:.1f}%**
and a prediction confidence of
**{highest['Confidence']:.1f}%**.
Immediate clinical assessment is recommended.
"""
    )
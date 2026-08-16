import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# Age Distribution
def age_distribution(df):

    st.markdown("""
<div class="chart-section">
                
<div class="chart-header">

<div>

<div class="chart-title">
👥 Age Distribution
</div>

<div class="chart-subtitle">
Patient Age Analysis
</div>

</div>

<div class="analytics-live">
<span class="live-dot"></span>
LIVE
</div>

</div>

""", unsafe_allow_html=True)

    # KPI
    avg_age = df["AGE"].mean()
    median_age = df["AGE"].median()
    senior_percent = (
        (df["AGE"] >= 60).sum()
        / len(df)
        * 100
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(f"""

<div class="kpi-summary">

<div class="kpi-summary-title">
Average Age
</div>

<div class="kpi-summary-value">
{avg_age:.1f}
</div>

<div class="kpi-summary-unit">
Years
</div>

</div>

""", unsafe_allow_html=True)

    with c2:

        st.markdown(f"""

<div class="kpi-summary">

<div class="kpi-summary-title">
Median Age
</div>

<div class="kpi-summary-value">
{median_age:.0f}
</div>

<div class="kpi-summary-unit">
Years
</div>

</div>

""", unsafe_allow_html=True)

    with c3:

        st.markdown(f"""

<div class="kpi-summary">

<div class="kpi-summary-title">
Senior Patients
</div>

<div class="kpi-summary-value">
{senior_percent:.0f}%
</div>

<div class="kpi-summary-unit">
Age ≥ 60
</div>

</div>

""", unsafe_allow_html=True)

    st.write("")

    # Age Group
    bins = [0, 30, 40, 50, 60, 120]

    labels = [
        "18-30",
        "31-40",
        "41-50",
        "51-60",
        "60+"
    ]

    age_df = df.copy()

    age_df["Age Group"] = pd.cut(

        age_df["AGE"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    age_count = (

        age_df
        .groupby("Age Group", observed=False)
        .size()
        .reindex(labels)
        .reset_index(name="Patients")
    )

    # Colors
    colors = [
        "#BFDBFE",
        "#93C5FD",
        "#60A5FA",
        "#3B82F6",
        "#2563EB"
    ]

    # Chart
    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            y=age_count["Age Group"],
            x=age_count["Patients"],
            orientation="h",
            text=age_count["Patients"],
            textposition="outside",

            marker=dict(
                color=colors,
                line=dict(
                    width=0
                )
            ),

            hovertemplate=

            "<b>Age Group</b>: %{y}<br>" +
            "<b>Total Patients</b>: %{x}<extra></extra>"
        )
    )

    fig.update_layout(

        height=445,
        template="plotly_white",
        showlegend=False,
        bargap=0.35,
        margin=dict(
            l=20,
            r=20,
            t=10,
            b=10

        ),

        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_title="Number of Patients",
        yaxis_title=""

    )

    fig.update_xaxes(

        showgrid=True,
        gridcolor="#E5E7EB",
        zeroline=False,
        showline=False

    )

    fig.update_yaxes(

        showgrid=False,
        autorange="reversed"

    )

    config = {

        "displayModeBar": "hover",
        "displaylogo": False,
        "modeBarButtonsToRemove": [
            "lasso2d",
            "select2d",
            "toggleSpikelines"

        ],

        "toImageButtonOptions": {
            "format": "png",
            "filename": "Age_Distribution",
            "scale": 2
        }
    }

    st.plotly_chart(

        fig,
        width='stretch',
        config=config

    )

    # Insight
    highest_group = age_count.loc[
        age_count["Patients"].idxmax(),
        "Age Group"
    ]

    highest_total = age_count["Patients"].max()

    st.info(f"""
**Clinical Insight**

The largest proportion of patients belongs to the
**{highest_group}** age group with
**{highest_total}** recorded patients.
This suggests that diabetes screening and preventive interventions
should prioritize individuals within this age range.

""")

# Biomarker Comparison
def biomarker_comparison(df):

    st.markdown("""
<div class="chart-section">

<div class="chart-header">

<div>

<div class="chart-title">
🧪 Biomarker Analysis
</div>

<div class="chart-subtitle">
Clinical Biomarker Comparison
</div>

</div>

<div class="analytics-live">
<span class="live-dot"></span>
LIVE
</div>

</div>

""", unsafe_allow_html=True)

    # Biomarker Reference
    reference ={
        "BMI":24.9,
        "HbA1c":6.5,
        "Cr_mgdl":1.3,
        "Urea_mgdl":43,
        "Chol_mgdl":200,
        "HDL_mgdl":40,
        "LDL_mgdl":100,
        "TG_mgdl":150,
        "VLDL_mgdl":30

    }

    units = {
        "BMI":"kg/m²",
        "HbA1c":"%",
        "Cr_mgdl":"mg/dL",
        "Urea_mgdl":"mg/dL",
        "Chol_mgdl":"mg/dL",
        "HDL_mgdl":"mg/dL",
        "LDL_mgdl":"mg/dL",
        "TG_mgdl":"mg/dL",
        "VLDL_mgdl":"mg/dL"
    }

    biomarker = st.selectbox(

        "Select Biomarker",
        list(reference.keys())
    )

    # KPI 
    avg = df[biomarker].mean()
    normal = reference[biomarker]
    diff = avg-normal

    c1,c2,c3 = st.columns(3)

    with c1:

        st.markdown(f"""
        <div class="kpi-summary">

<div class="kpi-summary-title">
Average Value
</div>

<div class="kpi-summary-value">
{avg:.2f}
</div>

<div class="kpi-summary-unit">
{units[biomarker]}
</div>

</div>

""",unsafe_allow_html=True)

    with c2:

        st.markdown(f"""

<div class="kpi-summary">

<div class="kpi-summary-title">
Normal Upper Limit
</div>

<div class="kpi-summary-value">
{normal}
</div>

<div class="kpi-summary-unit">
{units[biomarker]}
</div>

</div>

""",unsafe_allow_html=True)

    with c3:

        color = "#EF4444" if diff>0 else "#F59E0B"
        arrow = "▲" if diff>0 else "▼"

        st.markdown(f"""

<div class="kpi-summary">

<div class="kpi-summary-title">
Difference
</div>

<div class="kpi-summary-value" style="color:{color};">
{diff:+.2f} {arrow}
</div>

<div class="kpi-summary-unit">
vs Normal
</div>

</div>

""",unsafe_allow_html=True)

    st.write("")

    # BAR CHART
    compare = (
        df
        .groupby("Prediction")[biomarker]
        .mean()
        .reset_index()
    )

    color_map = {

        "Non-Diabetic": "#10B981",
        "Prediabetes": "#F59E0B",
        "Diabetes": "#EF4444"
    }

    colors = [

        color_map[x]
        for x in compare["Prediction"]
    ]

    fig = go.Figure()

    fig.add_trace(

        go.Bar(
            x=compare["Prediction"],
            y=compare[biomarker],
            text=compare[biomarker].round(2),
            textposition="outside",
            marker=dict(
                color=colors,
                line=dict(
                    color="white",
                    width=2
                )
            ),

            hovertemplate=

            "<b>Prediction</b>: %{x}<br>" +
            "<b>Average</b>: %{y:.2f} " +

            units[biomarker] +

            "<extra></extra>"
        )
    )

    # Reference Line
    fig.add_hline(

        y=normal,
        line_dash="dash",
        line_color="#2563EB",
        annotation_text=f"Normal Limit ({normal})",
        annotation_position="top left"
    )

    fig.update_traces(
        textposition="outside",
        marker=dict(
            cornerradius=12
        )
    )

    fig.update_layout(

        height=360,
        bargap=0.45,
        template="plotly_white",
        margin=dict(

            l=20,
            r=20,
            t=20,
            b=10

        ),

        showlegend=False,
        plot_bgcolor="white",
        paper_bgcolor="white",
        yaxis_title=units[biomarker],
        xaxis_title="Prediction"

    )

    fig.update_yaxes(

        showgrid=True,
        gridcolor="#E5E7EB",
        zeroline=False

    )

    fig.update_xaxes(

        showgrid=False
    )

    fig.add_hrect(

        y0=0,
        y1=normal,
        fillcolor="#DCFCE7",
        opacity=0.25,
        line_width=0

    )

    st.plotly_chart(

        fig,
        width='stretch',
        config={
            "displayModeBar":"hover",
            "displaylogo":False
        }
    )

    # Insight
    if diff>0:

        msg=f"""
Average **{biomarker}** exceeds the recommended clinical threshold by
**{diff:.2f} {units[biomarker]}**.
This suggests an overall increase across the patient population and may indicate
the need for further clinical assessment and routine monitoring.
"""

    else:

        msg=f"""
Average **{biomarker}** remains within the recommended clinical range,
indicating overall biomarker levels are under the clinical threshold.
"""

    st.info(f"""

**Clinical Insight**

{msg}

""")
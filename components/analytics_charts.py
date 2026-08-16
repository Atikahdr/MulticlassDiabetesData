import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def prediction_section(df):

    left, right = st.columns(2, gap="large")

    # LEFT

    with left:

        st.markdown("""
<div class="chart-section">

<div class="chart-header">

<div>

<div class="chart-title">
📈 Prediction Trend
</div>

<div class="chart-subtitle">
Daily prediction activity
</div>

</div>

<div class="analytics-live">
<span class="live-dot"></span>
LIVE
</div>

</div>
""", unsafe_allow_html=True)

        # Prediction Trend
        trend = (
            df.
            groupby("Date")
            .size()
            .reset_index(name="Predictions")
        )

        trend["Date"] = pd.to_datetime(trend["Date"])

        trend = trend.sort_values("Date")

        # Summary
        total_prediction = trend["Predictions"].sum()

        peak_day = trend.loc[
            trend["Predictions"].idxmax(),
            "Date"
        ]


        peak_value = trend["Predictions"].max()

        avg_prediction = trend["Predictions"].mean()

        last_prediction = trend.iloc[-1]["Predictions"]
        first_prediction = trend.iloc[0]["Predictions"]

        if last_prediction > first_prediction:
            trend_status = "Increasing"

        elif last_prediction < first_prediction:
            trend_status = "Decreasing"

        else:
            trend_status = "Stable"

        fig = px.line(
            trend,
            x="Date",
            y="Predictions"
        )

        fig.update_traces(

            mode="lines+markers+text",
            text=trend["Predictions"],
            textposition="top center",

            line=dict(
                color="#2563EB",
                width=4,
                shape="spline"
            ),

            marker=dict(

                size=9,

                color="white",

                line=dict(
                    color="#2563EB",
                    width=3
                )

            ),

            fill="tozeroy",
            fillcolor="rgba(37,99,235,.12)",

            hovertemplate=
            "<b>Date</b>: %{x}<br>"
            "<b>Total</b>: %{y}<extra></extra>"
        )

        fig.update_layout(

            template="plotly_white",

            height=360,

            margin=dict(
                l=10,
                r=10,
                t=5,
                b=5
            ),

            paper_bgcolor="white",
            hovermode="x unified",
            showlegend=False
        )

        fig.update_xaxes(

            title="",
            showgrid=False

        )

        fig.update_yaxes(

            title="Predictions",
            showgrid=True,
            gridcolor="#E5E7EB",
            zeroline=False
        )

        st.plotly_chart(
            fig,
            width='stretch',
            config={
                "displayModeBar": "hover",
                "displaylogo": False,
                "modeBarButtonsToRemove": [
                    "lasso2d",
                    "select2d",
                    "toggleSpikelines",
                    "hoverClosestCartesian",
                    "hoverCompareCartesian"

                ],

                "toImageButtonOptions": {
                    "format": "png",
                    "filename": "Prediction_Trend",
                    "height": 600,
                    "width": 1200,
                    "scale": 2
                }

            }
        )

        st.info(f"""
    **Clinical Insight**

A total of **{total_prediction}** prediction records were generated during the selected period. 
The highest daily activity was recorded on **{peak_day.strftime("%d %b %Y")}**, with **{peak_value}** predictions.

The average daily prediction volume was **{avg_prediction:.1f}**, 
indicating an overall **{trend_status.lower()}** screening trend throughout the selected time period.

""" )

    # RIGHT
    with right:

        st.markdown("""

<div class="chart-section">

<div class="chart-header">

<div>

<div class="chart-title">
📉 Prediction Distribution
</div>

<div class="chart-subtitle">
Percentage of prediction classes
</div>

</div>

<div class="analytics-live">
<span class="live-dot"></span>
LIVE
</div>

</div>

""", unsafe_allow_html=True)

        pie = (
            df["Prediction"]
            .value_counts()
            .reset_index()
        )

        pie.columns = [
            "Prediction",
            "Total"
        ]

        diabetes = len(df[df["Prediction"]=="Diabetes"])
        pre = len(df[df["Prediction"]=="Prediabetes"])
        normal = len(df[df["Prediction"]=="Non-Diabetic"])

        total = len(df)

        # Count 
        diabetes_pct = diabetes/total*100
        pre_pct = pre/total*100
        normal_pct = normal/total*100

        fig = px.pie(

            pie,
            names="Prediction",
            values="Total",
            hole=.72,
            color="Prediction",
            color_discrete_map={

                "Non-Diabetic":"#10B981",
                "Prediabetes":"#F59E0B",
                "Diabetes":"#EF4444"
            }
        )

        fig.update_traces(

            textinfo="percent",
            textfont_size=16,
            marker=dict(

                line=dict(
                    color="white",
                    width=3
                )
            )
        )

        fig.update_layout(

            template="plotly_white",
            height=360,
            margin=dict(
                l=10,
                r=10,
                t=5,
                b=5
            ),

                    plot_bgcolor="white",

            annotations=[
                dict(
                    text=f"<b>{total}</b><br>Patients",
                    x=.5,
                    y=.5,
                    showarrow=False,

                    font=dict(
                        size=22
                    )
                )
            ],

            legend=dict(
                orientation="h",
                y=-0.12,
                x=.5,
                xanchor="center"
            )

        )

        config = {

            "displayModeBar":"hover",
            "displaylogo":False,
            "modeBarButtonsToRemove":[

                "zoom2d",
                "pan2d",
                "zoomIn2d",
                "zoomOut2d",
                "autoScale2d",
                "lasso2d",
                "select2d"

            ]

        }

        st.plotly_chart(

            fig,
            width='stretch',
            config=config
        )

        st.info(f"""

**Clinical Insight**

A total of **{diabetes_pct:.1f}%** of patients were classified as **Diabetes**,
with **{pre_pct:.1f}%** categorized as **Prediabetes**.
Only **{normal_pct:.1f}%** remained within the **Non-Diabetic** group,
highlighting the importance of continuous screening and early clinical intervention
for individuals at elevated metabolic risk.

""")

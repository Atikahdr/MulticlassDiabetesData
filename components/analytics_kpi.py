import streamlit as st
import pandas as pd


def sparkline(values, color):

    if len(values) < 2:
      values = [0, values[0] if values else 0]

    max_v = max(values)
    min_v = min(values)

    if max_v == min_v:
       max_v += 1

    width = 170
    height = 40

    step = width / (len(values) - 1)

    points = []

    for i, v in enumerate(values):

       x = i * step

       y = height - (
            (v - min_v) /
            (max_v - min_v)
       ) * height

       points.append(f"{x},{y}")

    return f"""
<svg width="{width}" height="{height}">
<polyline
fill="none"
stroke="{color}"
stroke-width="3"
stroke-linecap="round"
stroke-linejoin="round"
points="{''.join(points)}"
/>
</svg>
"""

# Trend Badge
def trend_badge(values):

    if len(values) < 2:
        return (
            "▬ No Change",
            "badge-primary",
            "No previous period is available for comparison."
        )

    previous = values[-2]
    current = values[-1]

    # Previous = 0
    if previous == 0:

        if current == 0:

            return (
                "▬ No Change",
                "badge-primary",
                "No change compared with the previous period."
            )

        return (
            f"▲ +{current} Cases",
            "badge-success",
            f"{current} new case(s) were recorded compared with the previous period."
        )

    change = ((current - previous) / previous) * 100
    diff = current - previous

    if diff > 0:

        return (
            f"▲ +{diff} Cases",
            "badge-success",
            f"Increased by {diff} case(s) ({change:.1f}%) compared with the previous period."
        )

    elif diff < 0:

        return (
            f"▼ {abs(diff)} Cases",
            "badge-danger",
            f"Decreased by {abs(diff)} case(s) ({abs(change):.1f}%) compared with the previous period."
        )

    else:

        return (
            "▬ No Change",
            "badge-primary",
            "No change compared with the previous period."
        )

# KPI

def analytics_kpi(df):

    total = len(df)

    normal = len(
        df[
            df["Prediction"] == "Non-Diabetic"
        ]
    )

    pre = len(
        df[
            df["Prediction"] == "Prediabetes"
        ]
    )

    diabetes = len(
        df[
            df["Prediction"] == "Diabetes"
        ]
    )

    if "Date" in df.columns:

        trend = (

            df
            .groupby("Date")
            .size()
            .sort_index()

        )

        total_trend = trend.tolist()

        normal_trend = (

            df[
                df["Prediction"] == "Non-Diabetic"
            ]
            .groupby("Date")
            .size()
            .reindex(
                trend.index,
                fill_value=0
            )
            .tolist()

        )

        pre_trend = (

            df[
                df["Prediction"] == "Prediabetes"
            ]
            .groupby("Date")
            .size()
            .reindex(
                trend.index,
                fill_value=0
            )
            .tolist()

        )

        diabetes_trend = (

            df[
                df["Prediction"] == "Diabetes"
            ]
            .groupby("Date")
            .size()
            .reindex(
                trend.index,
                fill_value=0
            )
            .tolist()

        )

    else:

        total_trend = [0]
        normal_trend = [0]
        pre_trend = [0]
        diabetes_trend = [0]

    cards = [

        (
            "👥",
            "Total Patients",
            total,
            "#2563EB",
            "primary",
            total_trend
        ),

        (
            "✅",
            "Non-Diabetic",
            normal,
            "#10B981",
            "success",
            normal_trend
        ),

        (
            "⚠️",
            "Prediabetes",
            pre,
            "#F59E0B",
            "warning",
            pre_trend
        ),

        (
            "🔴",
            "Diabetes",
            diabetes,
            "#EF4444",
            "danger",
            diabetes_trend
        )

    ]

    cols = st.columns(4)

    for col, card in zip(cols, cards):
        icon, title, value, color, css, trend = card
        badge, badge_class, tooltip = trend_badge(trend)

        with col:

            st.markdown(
                f"""
<div class="kpi-card">

<div class="kpi-top">

<div class="kpi-icon {css}">
{icon}
</div>

<div class="kpi-badge {badge_class}"
title="{tooltip}">
{badge}
</div>

</div>

<div class="kpi-value">
{value}
</div>

<div class="kpi-title">
{title}
</div>

<div class="kpi-sparkline">
{sparkline(trend, color)}
</div>

<div class="kpi-footer">
Based on current filters
</div>

</div>
""",
                unsafe_allow_html=True
            )
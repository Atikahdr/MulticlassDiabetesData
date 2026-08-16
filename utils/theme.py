import streamlit as st

THEMES = {
    "light": {
        "background": "#F5F8FD",
        "card": "#FFFFFF",
        "text": "#0F172A",
        "text-light": "#64748B",
        "border": "#E2E8F0",

        "input-bg": "#F3F8FF",
        "input-border": "#BFDBFE",

        "nav-bg": "#EFF6FF",
        "nav-hover": "#DBEAFE",
        "nav-text": "#2563EB",

        "status-bg": "#ECFDF5",
        "status-text": "#047857",

        "shadow-sm": "0 4px 10px rgba(15,23,42,.05)",
        "shadow": "0 12px 35px rgba(15,23,42,.08)",
        "shadow-lg": "0 20px 45px rgba(15,23,42,.12)",
    },
    "dark": {
        "background": "#0B1220",
        "card": "#1E293B",
        "text": "#F1F5F9",
        "text-light": "#94A3B8",
        "border": "#334155",

        "input-bg": "#16233B",
        "input-border": "#3B82F6",

        "nav-bg": "#1E293B",
        "nav-hover": "#27354D",
        "nav-text": "#93C5FD",

        "status-bg": "#052E1B",
        "status-text": "#86EFAC",

        "shadow-sm": "0 4px 10px rgba(0,0,0,.35)",
        "shadow": "0 12px 35px rgba(0,0,0,.45)",
        "shadow-lg": "0 20px 45px rgba(0,0,0,.55)",
        "box-shadow":"0 12px 30px var(--shadow-primary);"
    },
}


def inject_theme():

    if "app_theme" not in st.session_state:
        st.session_state.app_theme = "light"

    palette = THEMES[st.session_state.app_theme]
    vars_css = "\n".join(f"--{name}:{value};" for name, value in palette.items())

    st.markdown(
        f"""
<style>
:root{{
{vars_css}
}}
</style>
""",
        unsafe_allow_html=True,
    )


def theme_toggle_button(label_container=st):

    current = st.session_state.get("app_theme", "light")
    icon = "🌙" if current == "light" else "☀️"
    label = "Mode Gelap" if current == "light" else "Mode Terang"

    if label_container.button(f"{icon} {label}", key="theme_toggle_btn"):
        st.session_state.app_theme = "dark" if current == "light" else "light"
        st.rerun()
import streamlit as st

from components.load_css import load_css
from utils.theme import inject_theme
from components.navbar import navbar
from components.about import about_page
from components.footer import footer

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_theme()
load_css()
navbar()
about_page()
footer()
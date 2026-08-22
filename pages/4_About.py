import streamlit as st

from components.load_css import load_css
from components.navbar import navbar
from components.about import about_page
from components.footer import footer

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()
navbar()
about_page()
footer()
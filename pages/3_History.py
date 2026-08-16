import streamlit as st
import pandas as pd

from components.load_css import load_css
from utils.theme import inject_theme
from components.navbar import navbar
from components.history import history_page
from components.footer import footer

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_theme()
load_css()
navbar()

history_page()
footer()
import streamlit as st
import pandas as pd

from components.load_css import load_css
from components.navbar import navbar
from components.history import history_page
from components.footer import footer

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()
navbar()

history_page()
footer()
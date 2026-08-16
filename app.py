import streamlit as st

from components.load_css import load_css
from components.navbar import navbar
from components.hero import hero
from components.project_summary import project_summary
from components.system_features import system_features
from components.detection_word import detection_word

from components.footer import footer


# PAGE CONFIG

st.set_page_config(
    page_title="Diabetes Clinical AI",
    page_icon="🧬",
    layout="wide"
)

# LOAD CSS

load_css()

# HEADER

navbar()

hero()

project_summary()

system_features()

detection_word()

footer()
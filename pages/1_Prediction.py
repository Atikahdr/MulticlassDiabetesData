import streamlit as st
import pandas as pd
import joblib 

from datetime import datetime

from components.load_css import load_css
from components.navbar import navbar
from components.input_form import input_form
from components.prediction_result import prediction_result
from utils.predict import predict_patient

# PAGE CONFIG
st.set_page_config(
    page_title="Prediction",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# LOAD THEME & CSS

load_css()

# NAVBAR

navbar()

# LOAD MODEL

@st.cache_resource
def load_artifacts():
    
    model = joblib.load("model/tuned_xgboost.pkl")
    scaler = joblib.load("model/scaler.pkl")
    feature_columns = joblib.load("model/feature_columns.pkl")

    return model, scaler, feature_columns

model, scaler, feature_columns = load_artifacts()

# INPUT FORM

submitted, patient_info, patient_data = input_form()


# PREDICTION
if submitted:

    prediction, probabilities = predict_patient(
        model=model,
        scaler=scaler,
        feature_columns=feature_columns,
        patient_data=patient_data
    )

    st.write("")
    st.write("")

    prediction_result(
        pred_class=prediction,
        probabilities=probabilities,
        patient_info=patient_info
    )

    label = {
        0: "Non-Diabetic",
        1: "Prediabetes",
        2: "Diabetes"
    }

    history_item = {
        "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "Medical Record": patient_info["Medical Record"],
        "Patient Name": patient_info["Patient Name"],
        **patient_data, # Clinical Data
        "Prediction": label[prediction],
        "Confidence": max(probabilities) * 100
    }

        
    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(history_item)
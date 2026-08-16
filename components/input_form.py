import streamlit as st
from datetime import datetime

from components.validation import validate_form, validation_popup
from components.patient_identity import patient_identity
from components.patient_profile import patient_profile
from components.laboratory_measurements import laboratory_measurements
from components.prediction_button import prediction_button


def input_form():

    assessment_time = datetime.now().strftime(
        "%d %b %Y • %H:%M"
    )

    with st.form(
        "input_form",
        clear_on_submit=False
    ):

        patient = patient_identity()
        profile = patient_profile()
        laboratory = laboratory_measurements()
        submitted = prediction_button()

    if submitted:

        errors = validate_form(patient)

        if errors:

            validation_popup(errors)
            return False, None, None

    patient_info = {

        "Patient Name": patient["patient_name"],
        "Medical Record": patient["patient_id"],
        "Assessment Time": assessment_time,

        "Gender": profile["gender"],
        "AGE": profile["age"],
        "BMI": profile["bmi"],
        "HbA1c": profile["hba1c"],

    }

    patient_data = {

        "Gender": profile["gender"],
        "AGE": profile["age"],
        "BMI": profile["bmi"],
        "HbA1c": profile["hba1c"],

        **laboratory,

    }

    return submitted, patient_info, patient_data
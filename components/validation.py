import streamlit as st

@st.dialog(" ")
def validation_popup(errors):

    html = f"""
<div class="validation-modal">

<div class="validation-icon">
⚠️
</div>

<div class="validation-heading">
Validation Required
</div>

<div class="validation-subtitle">
Please complete the required information before generating
the diabetes prediction.
</div>

<div class="validation-list">

{''.join(
f'<div class="validation-item">✓ {item}</div>'
for item in errors
)}

</div>

</div>
    """

    st.markdown(html, unsafe_allow_html=True)

    if st.button(
        "Continue Editing",
        type="primary",
        use_container_width=True
    ):
        
        st.rerun()

def validate_form(patient):

    errors = []

    if patient["patient_name"].strip() == "":
        errors.append("Patient Name")

    if patient["patient_id"].strip() == "":
        errors.append("Medical Record Number")

    return errors
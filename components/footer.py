import streamlit as st


def footer():

     st.markdown("""
<div class="footer">

<div class="footer-grid">

<!-- LEFT -->

<div>

<div class="footer-title">
⚕️ Clinical Decision Support System
</div>

<div class="footer-text">
AI-powered platform for diabetes screening using
clinical laboratory biomarkers and machine learning.
</div>

<div class="footer-links">

<a href="https://github.com/atikahdr"
target="_blank">
💻 GitHub
</a>

<a href="https://share.streamlit.io/user/atikahdr"
target="_blank">
🌐 Portfolio
</a>
</div>

</div>


<!-- CENTER -->

<div>
<div class="footer-title">
🤖 AI Model
</div>

<div class="footer-text">
Tuned XGBoost <br>
Multiclass Classification <br>
Clinical Decision Support
</div>

</div>


<!-- RIGHT -->

<div>
<div class="footer-title">
ℹ️ System
</div>

<div class="footer-text">
Version 1.1 <br>
Built with Streamlit <br>
© 2026 Atikah Dwi Rizky
</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)
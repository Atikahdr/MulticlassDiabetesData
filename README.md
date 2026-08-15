Dataset by Kaggle : https://www.kaggle.com/datasets/yasserhessein/multiclass-diabetes-dataset

Machine Learning Prediction by Streamlit : https://multiclassdiabetesdata-machinelearning-prediction.streamlit.app/

 ---
 
🧪 Multiclass Diabetes Clinical Decision Support System
---
An AI-powered Clinical Decision Support System (CDSS) for multiclass diabetes prediction using clinical laboratory biomarkers and machine learning.

The project combines data analysis, statistical testing, feature engineering, machine learning, model evaluation, and Streamlit deployment into an interactive clinical prediction and analytics platform.

    Disclaimer: This system is designed to support clinical decision-making and early screening. 
                It is not intended to replace professional medical diagnosis or clinical judgment.
---

📌 Project Overview
---
The objective of this project is to develop a machine learning system capable of classifying patients into three diabetes-related categories:

    ✅ Non-Diabetic
    ⚠️ Prediabetes
    🔴 Diabetes

The system uses demographic information and clinical laboratory biomarkers to generate predictions and provide an interactive analytics environment for monitoring patient outcomes.

Key Components

    🧹 Data Cleaning & Preprocessing
    📊 Exploratory Data Analysis
    🧪 Statistical Analysis
    🔍 Feature Selection & Multicollinearity Analysis
    🤖 Machine Learning Model Comparison
    ⚙️ Hyperparameter Tuning
    📈 Model Evaluation & ROC-AUC Analysis
    🔎 Overfitting & Generalization Analysis
    🚀 Streamlit Deployment
    📊 Interactive Clinical Analytics
    💡 Clinical Recommendations

  ---

📂 Dataset
---
The dataset contains 264 patient records with demographic and clinical laboratory information.

**Clinical Features**

|Feature |Description|
---------|-------------
|Gender |	Patient gender|
|AGE |	Patient age|
|HbA1c | Glycated hemoglobin|
|BMI	| Body Mass Index|
|Urea |	Blood urea measurement|
|Creatinine |	Creatinine level|
|Cholesterol |	Total cholesterol|
|HDL |	High-density lipoprotein|
|LDL |	Low-density lipoprotein|
|TG |	Triglycerides|
|VLDL |	Very-low-density lipoprotein|

**Target**

The target variable contains three classes:

- Non-Diabeti
- Prediabetes
- Diabetes
---

🧹 1. Data Cleaning & Preprocessing
---
The dataset was prepared before modeling through several preprocessing steps:

 - Data quality inspection
 - Missing-value checkin
 - Data type validation
 - Duplicate checking
 - Numerical feature inspection
 - Categorical feature encoding
 - Unit consistency checking
 - Distribution analysis

The cleaned dataset was then prepared for exploratory analysis and machine learning.
  
  ---
  
  📊2. Exploratory Data Analysis
---
Exploratory Data Analysis was performed to understand patient characteristics and identify patterns within the clinical variables.

The analysis included:

- Distribution analysis
- Descriptive statistics
- Skewness analysis
- Patient demographic analysis
- Biomarker distribution
- Target class distribution
- Relationship between clinical variables and diabetes categories

 ---
 
🎯 3. Target Class Distribution
---

The dataset contains three prediction classes:

|Class |Patients |Percentage | 
|------|-----------|----------|
|Diabetes |	128 |	48.48% |
|Non-Diabetic |	96 |	36.36% |
|Prediabetes |	40 |	15.15% |

The class distribution was evaluated before model development to determine whether class imbalance could affect model performance.

 ---
 
 🧪 4. Statistical Analysis
---
Statistical testing was performed to determine which clinical variables showed meaningful differences across diabetes categories.

🔹 Chi-Square Test

The categorical relationship between gender and diabetes classification was evaluated using the Chi-Square test.

**Result:**

- Chi-Square: 14.0321
- p-value: 0.0009

This indicates a statistically significant association between gender and the target classification.

**Kruskal-Wallis Test**

Because several numerical variables did not follow a normal distribution, the Kruskal-Wallis test was used to compare distributions across the three diabetes categories.

Significant features included:

- HbA1c
- BMI
- AGE
- TG
- VLDL
- Cholesterol
- Urea
- Creatinine

These findings supported the relevance of several clinical biomarkers for the classification task.
 
 ---
 
🔍 5. Feature Selection & Multicollinearity
---

Feature relationships were further evaluated using Variance Inflation Factor (VIF).

The final feature set showed acceptable multicollinearity levels, with the predictor variables remaining within a safe VIF range.

This step helped ensure that highly redundant predictors did not unnecessarily affect the model.

**Final Features**

- Gender
- AGE
- HbA1c
- BMI
- Cr_mgdl
- Urea_mgdl
- Chol_mgdl
- HDL_mgdl
- LDL_mgdl
- TG_mgdl
- VLDL_mgdl
 ---
 
🤖 6. Machine Learning Model Comparison
---

Several classification algorithms were evaluated as baseline models:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- K-Nearest Neighbors
- Support Vector Machine
- XGBoost

Models were evaluated using Stratified 5-Fold Cross Validation.

**Baseline Performance**

|Model | Accuracy|
|-----|------|
|XGBoost |	97.63%|
|Random Forest |	96.69%|
|Decision Tree |	96.69%|
|Logistic Regression	| 85.30%|
|KNN	| 79.60%|

Among the evaluated models, XGBoost achieved the strongest baseline performance.
 
 ---
 
⚙️ 7. Hyperparameter Tuning
---
The XGBoost model was further optimized using RandomizedSearchCV with:

- 50 parameter combinations
- 5-fold cross-validation
- Weighted F1-score as the optimization metric

**Best Parameters**

    - n_estimators = 50
    - max_depth = 6
    - learning_rate = 0.05
    - subsample = 0.9
    - colsample_bytree = 0.8
    - min_child_weight = 3

**Best Cross-Validation Score**

Weighted F1 Score: 97.13%

 ---

📈 8. Final Model Evaluation
---

The tuned XGBoost model was evaluated on the test dataset.

**Final Performance**
|Metric |	Score |
|-------|-------|
|Accuracy	| 98.11%|
|F1 Score	| 98.12%|
|ROC-AUC |	99.91%|

The results demonstrate strong predictive performance across the three diabetes categories.

**ROC-AUC**

ROC-AUC was used as an additional evaluation metric to assess the model's ability to distinguish between the multiclass outcomes.

 ---

🔎 9. Overfitting & Generalization Check
---

Model performance was reviewed across training and testing datasets to evaluate generalization.

The analysis was used to identify potential overfitting and ensure that the final model's performance was not solely dependent on the training data.

Cross-validation results were also considered alongside the final test performance to provide a more reliable assessment of model behavior.

 ---

🖥️ 10. Streamlit Clinical Dashboard
---

The final model was integrated into an interactive Streamlit application.

The dashboard was designed as a Clinical Decision Support System rather than only a prediction interface.

**🏠 Dashboard**

The Home dashboard provides:

- AI-powered system introduction
- Project Summary
- Model performance overvie
- System Features
- AI Clinical Workflow
- Technology Stack

**🔮 Prediction**

Users can enter patient information and clinical laboratory biomarkers to generate a multiclass prediction.

The prediction workflow includes:

    Patient Information
            ↓
    Clinical Biomarkers
            ↓
    Tuned XGBoost Model
            ↓
        Prediction
            ↓
      Confidence Score
            ↓
    Clinical Recommendation
 ---

📊 11. Clinical Analytics Dashboard
---

The Analytics dashboard provides an interactive overview of prediction results.

**Analytics Features**

    📌 Total Patients
    ✅ Non-Diabetic Cases
    ⚠️Prediabetes Cases
    🔴 Diabetes Cases
    📈 Prediction Trend
    🍩 Prediction Distribution
    👥 Age Distribution
    🧪 Biomarker Analysis
    🚨 High-Risk Patient Monitoring
    💡 Clinical Recommendations

The dashboard also includes filtering functionality to allow users to explore prediction results dynamically.

 ---

📜 12. Prediction History
---

Each prediction can be recorded in the application history.

The history section provides patient-level information including:

 - Medical Record
 - Patient Name
 - Age
 - Gender
 - BMI
 - HbA1c
 - Prediction
 - Confidence
 - Assessment Time
  
This allows previous prediction results to be reviewed and monitored.

 ---

🚨 13. High-Risk Patient Monitoring
---

A dedicated High-Risk Patients table was implemented to highlight patients classified as Diabetes with high prediction confidence.

The monitoring interface includes:

- Patient identification
- Demographic information
- BMI
- HbA1c
- Prediction confidence
- Risk classification

This feature helps users quickly identify predictions that may require further clinical attention.

 ---

💡 14. Clinical Recommendations
---
The system provides AI-assisted recommendations based on prediction outcomes and observed clinical indicators.

Recommendations are intended to support healthcare professionals by highlighting potential areas for further assessment.

    These recommendations are supportive insights only and should not be interpreted as medical diagnosis or treatment instructions.
    
 ---
 
🎨 15. Professional UI & User Experience
---

The application was designed with a modern healthcare dashboard interface inspired by enterprise analytics platforms.

The UI includes:

- Responsive layouts
- Premium KPI cards
- Interactive Plotly charts
- Hover animations
- Light / Dark theme support
- Interactive navigation
- Prediction history
- Clinical insight cards
- Risk badges
- Responsive feature cards
- Professional dashboard sections

 ---

🛠️ Technology Stack
---

|Technology |	Purpose |
|-----------|---------|
|🐍 Python	| Core programming language|
|⚡ Streamlit	| Web application & deployment|
|🌳 XGBoost	| Final machine learning model|
|📊 Plotly	| Interactive visualization|
|🐼 Pandas	| Data processing|
|🔢 NumPy	| Numerical computation|
|🤖 Scikit-learn |	ML preprocessing & evaluation|
|🎨 HTML/CSS	| Dashboard UI customization|

 ---

 🎯 Conclusion
---
This project demonstrates an end-to-end Machine Learning and Data Science workflow, starting from raw clinical data preparation and exploratory analysis through statistical testing, feature analysis, model development, hyperparameter optimization, evaluation, and deployment.

The final **Tuned XGBoost Multiclass Classifier** achieved:

    98.11% Accuracy · 98.12% F1 Score · 99.91% ROC-AUC

Beyond the predictive model, the project extends machine learning into a complete **Clinical Decision Support System** with patient prediction, analytics, prediction history, high-risk monitoring, and clinical recommendation features.

The project demonstrates practical skills in:

**Data Science → Machine Learning → Model Evaluation → Visualization → Application Development → Deployment**

 ---
 
👩‍💻 Author
---
Atikah Dwi Rizky

Information Systems | Data Science & Machine Learning

---

⚠️ Medical Disclaimer
---
This project is developed for educational, research, and demonstration purposes.

The predictions and recommendations generated by this system should not be considered a definitive medical diagnosis, treatment recommendation, or substitute for professional medical judgment.


 
 

Machine Learning Prediction by Streamlit : https://multiclassdiabetesdata-machinelearning-prediction.streamlit.app/

🧪 Multiclass Diabetes Classification
---
📌 Project Overview
---
This project aims to build a multiclass classification model to predict diabetes categories based on clinical and laboratory features. The dataset contains demographic, metabolic, and kidney-related biomarkers.

The objective is not only to detect diabetes, but also to analyze feature interactions that may help differentiate metabolic severity.

  ---

🔎 1. Data Cleaning
---
In a medical context, Total Cholesterol cannot be 0 (normally >100 mg/dL or >2 mmol/L).

A value of 0 likely indicates:
 - Input error
 - Laboratory result not recorded
 - Missing value incorrectly stored as 0

Therefore, cholesterol values equal to 0 were treated as invalid entries and handled appropriately during preprocessing.
  
  ---
  
  📊 2. Target Class Distribution
---
The dataset contains three classes with the following proportions:

|Class	| Proportion|
|-------|-----------|
|2	| 47.89%|
|0	| 36.78%|
|1	| 15.33%|

The dataset is moderately imbalanced, particularly for Class 1, which motivates the use of SMOTE in the modeling stage.

 ---
 
⚙️ 3. Feature Engineering
---

To enhance biological interpretability and capture interactions, new features were created:

🧪 New Features

 - Urea_Cr_Ratio
   Clinically relevant ratio used to assess kidney function.

 - BMI_HbA1c
   Interaction between obesity (BMI) and blood sugar control (HbA1c). Helps capture metabolic risk patterns.

 - AGE_BMI
   Combines age and obesity, both important diabetes risk factors.

These engineered features significantly improved class separability.

 ---
 
 📈 4. Feature Selection
---

🔹 ANOVA Test

   Top significant features based on F-Score:

  | Feature	| F-Score	| p-value|
  | --------|---------|----------|  
  | BMI_HbA1c	| 263.26	| 4.95e-63 |
  | HbA1c	| 195.42	| 2.15e-52 |
  | BMI	| 184.78	| 1.58e-50 |
  | AGE_BMI	| 171.47	| 4.26e-48 |
  | AGE	| 58.39	| 1.20e-21 |

Features like HDL and LDL showed low significance.

🔹 Chi-Square Test

  | Feature	  | Score	    | p-value   |
  |-----------|-----------|-----------|
  | BMI_HbA1c	| 7.73e+06	| 4.25e-229 |
  | HbA1c	    | 1.88e+04	| 1.82e-115 |

Both tests confirm that HbA1c and BMI_HbA1c are extremely strong predictors.

⭐ Feature Importance Insight

 - HbA1c indicates whether someone has diabetes, but does not fully differentiate metabolic severity.

 - BMI_HbA1c (interaction feature) reveals:
    - High BMI + High HbA1c → likely Type 2 diabetes (insulin resistance)
    - Low BMI + High HbA1c → possible Type 1 diabetes

This interaction provides better clinical interpretability.
 
 ---
 
 🤖 5. Model Comparison
---

| Algorithm	 | ROC AUC | Accuracy	| STD |
|------------|---------|----------|-----|
| Random Forest	| 99.50	| 97.12	| 2.79 |
| Gradient Boosting	| 99.31	| 98.07	| 2.36 |
| Decision Tree	| 98.10	| 97.60	| 2.16 |
| SVM	| 96.06	| 87.03	| 4.66 | 
| Logistic Regression	| 92.43	| 87.02	| 5.36 |
| KNN	| 89.79	| 79.85	| 6.23 | 

🏆 Best Model: Random Forest

Random Forest achieved the highest ROC AUC with strong stability.

 ---
 
⚖️ 6. Handling Class Imbalance (SMOTE)
---

Oversampling was performed after train-test split and during cross-validation.

Important principle:
 - SMOTE applied only to training data
 - Validation/test data kept in original distribution

This prevents data leakage and ensures realistic model evaluation.
 
 ---
 
🔧 7. Hyperparameter Tuning
---

Best Parameters:

    Best Parameters: {'n_estimators': 200}
    Best CV Accuracy: 0.9766666666666666
    
Tuning improved model generalization and stability.

 ---

📉 8. Overfitting Check
---

🔹 Gap (Train – Test)

 - Accuracy Gap: 1.89%
 - ROC AUC Gap: 0.34%

The small gap indicates very low overfitting and strong generalization performance.

 ---

📊 9. Final Model & ROC Curve
---

The final selected model is Random Forest with 200 trees.

The ROC Curve demonstrates excellent class separability with near-perfect AUC values.

 ---


🎯 Conclusion
---

 - Engineered interaction features significantly improved performance.
 - HbA1c alone is powerful, but combining it with BMI enhances predictive power.
 - Random Forest provides robust performance with minimal overfitting.
 - Proper SMOTE implementation ensured fair validation.

This project highlights how combining clinical domain knowledge + feature engineering + proper validation strategy leads to highly accurate multiclass classification models.

 ---

🚀 Deployment Ready
---

The multiclass diabetes classification model has been fully trained, validated, and evaluated.

After performing:
 - Data cleaning
 - Feature engineering
 - Feature selection (ANOVA & Chi-Square)
 - Class balancing using SMOTE
 - Hyperparameter tuning
 - Overfitting validation

The final Random Forest model demonstrates strong generalization performance and stable metrics.

- ✅ The multiclass dataset pipeline is production-ready
- ✅ The trained model is ready for deployment
- ✅ Successfully deployed using Streamlit for interactive prediction

The Streamlit application allows users to:

- Input clinical parameters (Age, BMI, HbA1c, Cholesterol, etc.)
- Automatically generate engineered features
- Predict diabetes class in real-time
- Display prediction probabilities

This ensures the model is not only accurate in experimentation, but also practical for real-world usage.
 
 ---

📚 Concepts Covered
---

- 🧾 Multiclass Classification
- 🧪 Clinical Data Analysis
- 🧹 Data Cleaning & Missing Value Handling
- ⚙️ Feature Engineering (Biological Feature Interaction)
- 📊 Statistical Feature Selection (ANOVA & Chi-Square)
- ⚖️ Handling Imbalanced Data (SMOTE)
- 🤖 Ensemble Learning (Random Forest, Gradient Boosting)
- 🔧 Hyperparameter Tuning
- 📈 ROC AUC Evaluation & Model Comparison
- 🚀 Model Deployment with Streamlit


 
 

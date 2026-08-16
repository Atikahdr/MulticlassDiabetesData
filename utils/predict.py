import pandas as pd

def predict_patient(model, scaler, feature_columns, patient_data):

    df = pd.DataFrame([patient_data])

    df = df[feature_columns]

    # Scaling
    df_scaled = scaler.transform(df)

    #Predict
    prediction = model.predict(df_scaled)[0]

    #Probability
    probabilites = model.predict_proba(df_scaled)[0]

    return prediction, probabilites
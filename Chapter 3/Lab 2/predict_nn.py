import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

# Load the trained model
nn_model = load_model('trained_nn_model.h5')

# Load the preprocessor
preprocessor = joblib.load('preprocessor.pkl')

# Function to classify severity based on delta-V
def classify_severity(delta_v):
    if delta_v < 10:
        return 'low'
    elif 10 <= delta_v < 20:
        return 'medium'
    else:
        return 'high'

# Prediction function
def predict_injury_risk(vehicle_type, delta_v, peak_acceleration):
    severity = classify_severity(delta_v)
    input_data = pd.DataFrame([[vehicle_type, severity, peak_acceleration]], 
                              columns=['vehicle_type', 'severity', 'peak_acceleration'])
    input_transformed = preprocessor.transform(input_data)
    prediction = nn_model.predict(input_transformed)
    return prediction[0][0]

# Example usage: Predict injury risk for a sedan with delta-V of 12 mph, peak acceleration of 55g
predicted_risk = predict_injury_risk('sedan', 12, 55)
print(f'Predicted Injury Risk for Sedan with delta-V of 12 mph, 55g acceleration: {predicted_risk:.2f}')

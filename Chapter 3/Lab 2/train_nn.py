import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import joblib

# Load synthetic data
df = pd.read_csv('synthetic_crash_data.csv')

# Features and target
X = df[['vehicle_type', 'severity', 'peak_acceleration']]
y = df['injury_risk']

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['peak_acceleration']),
        ('cat', OneHotEncoder(), ['vehicle_type', 'severity'])
    ])

# Transform data
X_transformed = preprocessor.fit_transform(X)

# Save preprocessor
joblib.dump(preprocessor, 'preprocessor.pkl')

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Neural Network model
def create_nn_model():
    model = Sequential()
    model.add(Input(shape=(X_train.shape[1],)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

nn_model = create_nn_model()

# Train model
nn_model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Evaluate model
test_loss, test_accuracy = nn_model.evaluate(X_test, y_test)
print(f'Test loss: {test_loss}')
print(f'Test accuracy: {test_accuracy}')

# Save the trained model
nn_model.save('trained_nn_model.h5')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to classify severity based on delta-V
def classify_severity(delta_v):
    if delta_v < 10:
        return 'low'
    elif 10 <= delta_v < 20:
        return 'medium'
    else:
        return 'high'

# Generate realistic synthetic data with added noise
np.random.seed(42)
vehicle_types = ['car', 'truck', 'suv', 'sedan']
num_samples = 200

vehicle_type = np.random.choice(vehicle_types, num_samples)
delta_v = np.random.uniform(5, 30, num_samples)
peak_acceleration = delta_v * np.random.uniform(1.8, 2.8, num_samples)  # Add variability to peak acceleration
injury_risk = (np.random.uniform(0, 1, num_samples) < (delta_v / 30)).astype(int)  # Probability-based injury risk with noise

data = {
    'vehicle_type': vehicle_type,
    'delta_v': delta_v,
    'peak_acceleration': peak_acceleration,
    'injury_risk': injury_risk
}

df = pd.DataFrame(data)
df['severity'] = df['delta_v'].apply(classify_severity)

# Save to CSV
df.to_csv('synthetic_crash_data.csv', index=False)
print(df.head())

# Plotting the data
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='delta_v', y='peak_acceleration', hue='injury_risk', palette='coolwarm')
plt.title('Scatter Plot of Delta-V vs. Peak Acceleration')
plt.xlabel('Delta-V (mph)')
plt.ylabel('Peak Acceleration (g)')
plt.legend(title='Injury Risk')
plt.show()

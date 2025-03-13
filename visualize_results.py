import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Load data
data = pd.read_csv('jenkins_build_data.csv')

# Load the trained model
model = joblib.load('failure_prediction_model.pkl')

# Features
X = data[['build_time_seconds', 'tests_failed', 'total_tests']]

# Get predictions
data['predicted_result'] = model.predict(X)

# Visualize actual vs. predicted results
plt.figure(figsize=(8, 6))
sns.countplot(x='result', data=data, label='Actual', alpha=0.7)
sns.countplot(x='predicted_result', data=data, label='Predicted', alpha=0.5)
plt.legend()
plt.title('Actual vs Predicted Build Results')
plt.xlabel('Build Result (0=SUCCESS, 1=FAILURE)')
plt.ylabel('Count')

# Save the plot
plt.savefig('build_results_comparison.png')
print('Visualization saved as build_results_comparison.png')

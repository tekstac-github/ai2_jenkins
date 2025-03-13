import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load sample data
data = pd.read_csv('jenkins_build_data.csv')

# Preprocess data
# Convert 'result' to binary (SUCCESS=0, FAILURE=1)
data['result'] = data['result'].apply(lambda x: 1 if x == 'FAILURE' else 0)

# Features and target
X = data[['build_time_seconds', 'tests_failed', 'total_tests']]
y = data['result']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Model accuracy: {accuracy * 100:.2f}%')

# Save model
joblib.dump(model, 'failure_prediction_model.pkl')
print('Model saved as failure_prediction_model.pkl')


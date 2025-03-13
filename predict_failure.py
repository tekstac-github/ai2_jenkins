import pandas as pd
import joblib

# Load the trained model
model = joblib.load('failure_prediction_model.pkl')

# Simulate live build data (replace with actual data in production)
live_data = pd.DataFrame({
    'build_time_seconds': [150],
    'tests_failed': [1],
    'total_tests': [100]
})

# Make prediction
prediction = model.predict(live_data)

# Output prediction (0 = SUCCESS, 1 = FAILURE)
print('FAILURE' if prediction[0] == 1 else 'SUCCESS')


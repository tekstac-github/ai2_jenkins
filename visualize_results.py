import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the build data
data = pd.read_csv('jenkins_build_data.csv')

# Debugging: Print columns to check
print("CSV Columns:", data.columns)

# Ensure required columns exist
required_columns = {'build_num', 'build_time', 'tests_failed', 'total_tests', 'result'}
if not required_columns.issubset(set(data.columns)):
    print("Error: Required columns not found in data")
    exit(1)

# Visualize build time distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['build_time'], bins=30, kde=True)
plt.title('Build Time Distribution')
plt.xlabel('Build Time (seconds)')
plt.ylabel('Frequency')
plt.show()

# Visualize tests failed vs total tests
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_tests', y='tests_failed', hue='result', data=data)
plt.title('Tests Failed vs Total Tests')
plt.xlabel('Total Tests')
plt.ylabel('Tests Failed')
plt.show()

# Visualize build results
plt.figure(figsize=(6, 4))
sns.countplot(x='result', data=data)
plt.title('Build Results Count')
plt.xlabel('Result')
plt.ylabel('Count')
plt.show()

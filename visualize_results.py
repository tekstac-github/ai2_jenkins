import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('jenkins_build_data.csv')

# Debugging: Print actual columns in the data
print(f"CSV Columns: {data.columns}")

# Check if the expected columns are present
required_columns = {'build_number', 'build_time_seconds', 'tests_failed', 'total_tests', 'result'}
if not required_columns.issubset(data.columns):
    missing_columns = required_columns - set(data.columns)
    print(f"Error: Required columns not found in data: {missing_columns}")
    exit(1)

# Visualize build time distribution
sns.histplot(data['build_time_seconds'], bins=30, kde=True)
plt.title('Build Time Distribution')
plt.xlabel('Build Time (seconds)')
plt.ylabel('Frequency')
plt.show()

# Visualize tests failed vs total tests
plt.scatter(data['total_tests'], data['tests_failed'], alpha=0.5)
plt.title('Tests Failed vs Total Tests')
plt.xlabel('Total Tests')
plt.ylabel('Tests Failed')
plt.show()

# Visualize build results
sns.countplot(x='result', data=data)
plt.title('Build Results Count')
plt.show()

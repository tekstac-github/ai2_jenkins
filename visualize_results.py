import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('jenkins_build_data.csv')

# Print column names for debugging
print(f"CSV Columns: {data.columns}")

# Check for required columns
required_columns = {'build_num', 'build_time', 'tests_failed', 'total_tests', 'result'}
if not required_columns.issubset(data.columns):
    print('Error: Required columns not found in data')
    exit(1)

# Visualization: Build time distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['build_time'], bins=30, kde=True)
plt.title('Distribution of Build Time')
plt.xlabel('Build Time (seconds)')
plt.ylabel('Frequency')
plt.show()

# Visualization: Tests failed vs total tests
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_tests', y='tests_failed', hue='result', data=data)
plt.title('Tests Failed vs Total Tests')
plt.xlabel('Total Tests')
plt.ylabel('Tests Failed')
plt.legend(title='Build Result')
plt.show()

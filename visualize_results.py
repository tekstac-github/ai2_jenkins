import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
try:
    data = pd.read_csv('jenkins_build_data.csv')
except FileNotFoundError:
    print('Error: jenkins_build_data.csv not found.')
    exit(1)

# Visualize build duration
plt.figure(figsize=(10, 6))
sns.histplot(data['build_duration'], bins=30, kde=True)
plt.title('Build Duration Distribution')
plt.xlabel('Build Duration (seconds)')
plt.ylabel('Frequency')
plt.savefig('build_duration_distribution.png')

# Visualize build outcomes
plt.figure(figsize=(6, 6))
sns.countplot(x='build_status', data=data)
plt.title('Build Status Count')
plt.xlabel('Build Status')
plt.ylabel('Count')
plt.savefig('build_status_count.png')

print('Visualization completed successfully.')

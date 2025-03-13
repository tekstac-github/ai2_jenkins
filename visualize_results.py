import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
try:
    data = pd.read_csv('jenkins_build_data.csv')
    print("CSV Columns:", data.columns)
except FileNotFoundError:
    print("Error: jenkins_build_data.csv not found")
    exit(1)

# Ensure the expected columns exist
if 'build_duration' not in data.columns or 'build_status' not in data.columns:
    print("Error: Required columns not found in data")
    exit(1)

# Build duration histogram
plt.figure(figsize=(8, 6))
sns.histplot(data['build_duration'], bins=30, kde=True)
plt.title('Build Duration Distribution')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.savefig('build_duration_distribution.png')

# Build status count plot
plt.figure(figsize=(8, 6))
sns.countplot(x='build_status', data=data)
plt.title('Build Status Counts')
plt.xlabel('Status')
plt.ylabel('Count')
plt.savefig('build_status_counts.png')

print("Visualizations saved successfully!")

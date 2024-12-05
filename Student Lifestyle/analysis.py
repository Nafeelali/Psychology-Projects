import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'student_lifestyle_dataset.csv'
df = pd.read_csv(data_path)

# Correlation heatmap
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numeric Variables')
plt.savefig('correlation_matrix.png')
plt.close()

# Distribution of GPA
plt.figure(figsize=(8, 6))
sns.histplot(df['GPA'], kde=True, bins=20, color='blue')
plt.title('Distribution of GPA')
plt.xlabel('GPA')
plt.ylabel('Frequency')
plt.savefig('gpa_distribution.png')
plt.close()

# Study Hours vs GPA
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Study_Hours_Per_Day', y='GPA', hue='Stress_Level', data=df, palette='viridis')
plt.title('Study Hours vs GPA')
plt.xlabel('Study Hours Per Day')
plt.ylabel('GPA')
plt.legend(title='Stress Level')
plt.savefig('study_hours_vs_gpa.png')
plt.close()

# Sleep Hours vs GPA
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Sleep_Hours_Per_Day', y='GPA', hue='Stress_Level', data=df, palette='coolwarm')
plt.title('Sleep Hours vs GPA')
plt.xlabel('Sleep Hours Per Day')
plt.ylabel('GPA')
plt.legend(title='Stress Level')
plt.savefig('sleep_hours_vs_gpa.png')
plt.close()

# Physical Activity vs GPA
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Physical_Activity_Hours_Per_Day', y='GPA', hue='Stress_Level', data=df, palette='plasma')
plt.title('Physical Activity vs GPA')
plt.xlabel('Physical Activity Hours Per Day')
plt.ylabel('GPA')
plt.legend(title='Stress Level')
plt.savefig('physical_activity_vs_gpa.png')
plt.close()

# Social Hours vs Stress Level
plt.figure(figsize=(8, 6))
sns.boxplot(x='Stress_Level', y='Social_Hours_Per_Day', data=df, palette='Set2')
plt.title('Social Hours vs Stress Level')
plt.xlabel('Stress Level')
plt.ylabel('Social Hours Per Day')
plt.savefig('social_hours_vs_stress_level.png')
plt.close()
"""

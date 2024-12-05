import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = 'integration_problem_set.json'
data = pd.read_json(file_path)

# Overview of the data
print("Dataset Shape:", data.shape)
print("Sample Data:\n", data.head())
print("\nData Info:")
print(data.info())

# Distribution of Difficulty
difficulty_counts = data['difficulty'].value_counts()
print("\nDifficulty Distribution:\n", difficulty_counts)

# Distribution of Category
category_counts = data['category'].value_counts()
print("\nCategory Distribution:\n", category_counts)

# Add a column for question length
data['question_length'] = data['question'].apply(len)

# Basic statistics for question length
print("\nQuestion Length Stats:\n", data['question_length'].describe())

# Visualization: Difficulty Distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=difficulty_counts.index, y=difficulty_counts.values, palette="viridis")
plt.title('Difficulty Distribution')
plt.xlabel('Difficulty')
plt.ylabel('Count')
plt.show()

# Visualization: Category Distribution
plt.figure(figsize=(12, 6))
sns.barplot(y=category_counts.index, x=category_counts.values, palette="magma")
plt.title('Category Distribution')
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()

# Question Length Distribution
plt.figure(figsize=(10, 5))
sns.histplot(data['question_length'], bins=30, kde=True, color='blue')
plt.title('Question Length Distribution')
plt.xlabel('Question Length')
plt.ylabel('Frequency')
plt.show()

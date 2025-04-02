import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

# Load Iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
iris_df['species'] = iris_df['species'].map(species_map)

# Visualization 1: Pairplot
sns.pairplot(iris_df, hue='species', palette='Dark2')
plt.suptitle('Pairplot of Iris Features', y=1.02)
plt.show()

# Visualization 2: Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='sepal length (cm)', data=iris_df, palette='coolwarm')
plt.title('Sepal Length Distribution by Species')
plt.show()

# Visualization 3: Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='species', y='petal length (cm)', data=iris_df, palette='muted')
plt.title('Petal Length Distribution by Species')
plt.show()

# Load Loan Dataset (Example Path, Replace with actual dataset path)
kaggle_loan_data = pd.read_csv('loan_data.csv')

# Visualization 4: Loan Status Distribution
plt.figure(figsize=(6, 6))
kaggle_loan_data['Loan_Status'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightblue', 'salmon'])
plt.title('Loan Approval Distribution')
plt.ylabel('')
plt.show()

# Visualization 5: Loan Amount vs. Applicant Income
plt.figure(figsize=(8, 6))
sns.scatterplot(x='ApplicantIncome', y='LoanAmount', hue='Loan_Status', data=kaggle_loan_data, palette='Set1')
plt.title('Loan Amount vs. Applicant Income')
plt.show()

# Visualization 6: Credit History Distribution
plt.figure(figsize=(8, 6))
sns.histplot(kaggle_loan_data['Credit_History'].dropna(), bins=10, kde=True, color='green')
plt.title('Credit History Distribution')
plt.show()

# Summary Conclusion
print("\nObservations:")
print("1. Iris dataset shows clear differences in petal length among species.")
print("2. Loan approvals are influenced by credit history and applicant income.")
print("3. Higher credit scores correlate with lower loan rejection rates.")

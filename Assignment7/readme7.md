--Data Visualization with Matplotlib

--Project Overview

This project demonstrates data visualization techniques using Matplotlib and Seaborn on two datasets:

-Fisher's Iris Dataset – A foundational dataset in data science and biology used to distinguish iris species based on their physical traits.

-Kaggle Loan Dataset – A real-world dataset used to explore trends in loan approvals.

Objectives

-Import and manipulate real-world datasets into a workable form.

-Utilize Matplotlib and Seaborn to create compelling visualizations.

-Analyze visual patterns and extract insights from the data.

Datasets Used

1. Fisher’s Iris Dataset

-The dataset contains measurements of three iris species: Setosa, Versicolor, and Virginica.

-Features include sepal length, sepal width, petal length, and petal width.

2. Kaggle Loan Dataset

-Contains information on loan applicants, including credit history, applicant income, loan amount, and approval status.

-Used to analyze factors influencing loan approval decisions.

--Data Visualizations

Iris Dataset

-Pairplot – Displays relationships between features, categorized by species.

-Boxplot – Highlights variations in sepal length among species.

-Violin Plot – Shows the distribution of petal length for each species.

Kaggle Loan Dataset

-Loan Status Pie Chart – Illustrates loan approval distribution.

-Scatter Plot (Loan Amount vs. Applicant Income) – Shows income impact on loan amounts.

-Credit History Distribution – Highlights trends in applicants' credit history.

Key Insights

-Different iris species exhibit clear variations in petal and sepal dimensions.

-Loan approval rates are strongly influenced by credit history and applicant income.

-Higher credit scores tend to correlate with lower loan rejection rates.

How to Run the Code

Install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn

Download the Kaggle loan dataset and save it as loan_data.csv in the same directory.

Run the Python script:

python data_visualization.py

Limitations

-Some missing values in the Kaggle dataset require preprocessing.

-Additional visualizations may be required for a deeper analysis of loan trends.




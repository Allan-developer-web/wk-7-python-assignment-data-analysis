# wk-7-python-assignment-data-analysis

📊 Data Analysis and Visualization Project
📌 Overview

This project demonstrates how to:

Load and explore a dataset (the Iris dataset in CSV format).

Perform basic statistical analysis.

Create data visualizations using matplotlib and seaborn.

Summarize findings and insights.

The dataset used is the Iris dataset, a classic dataset in machine learning and data science. It contains 150 observations of iris flowers across three species (Setosa, Versicolor, Virginica) with measurements of:

Sepal length

Sepal width

Petal length

Petal width

📂 Project Structure
project-folder/
│── iris.csv                 # Dataset file
│── iris_analysis_csv.ipynb  # Jupyter Notebook (main report)
│── iris_analysis_csv.py     # Python script version
│── README.md                # Project documentation

🛠️ Requirements

Make sure you have the following installed:

Python 3.8+

Jupyter Notebook (for .ipynb file)

Required Python libraries:

pip install pandas numpy matplotlib seaborn

🚀 How to Run
Option 1: Run the Jupyter Notebook

Open a terminal and launch Jupyter Notebook:

jupyter notebook


Open iris_analysis_csv.ipynb.

Run each cell step by step.

Option 2: Run the Python Script

Place iris.csv in the same folder as iris_analysis_csv.py.

Run the script:

python iris_analysis_csv.py

📊 Analysis Steps
1. Data Loading & Cleaning

Load dataset from iris.csv.

Display first few rows.

Check data types, structure, and missing values.

Drop missing values if present.

2. Basic Data Analysis

Compute descriptive statistics (mean, std, min, max).

Group by species and calculate average values.

3. Data Visualization

Four different plots were created:

Line Chart → Sepal & Petal length trends across dataset indices.

Bar Chart → Average petal length per species.

Histogram → Distribution of sepal width.

Scatter Plot → Sepal length vs Petal length (colored by species).

Each plot includes titles, axis labels, and legends for clarity.

4. Findings

Setosa: Smallest petal dimensions.

Virginica: Largest sepal and petal dimensions.

Versicolor: Intermediate values.

Petal length is a strong distinguishing feature among species.

📌 Key Insights

The dataset is clean and well-structured.

Statistical and visual analysis clearly separates species.

This project demonstrates Exploratory Data Analysis (EDA) and can serve as a foundation for machine learning classification tasks.

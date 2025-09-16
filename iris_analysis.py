# Data Analysis and Visualization Project

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load dataset from CSV
    df = pd.read_csv("iris.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: iris.csv file not found.")
except Exception as e:
    print("An error occurred while loading the dataset:", e)

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Check dataset info (data types, nulls, etc.)
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Cleaning (if missing values exist, drop or fill)
df = df.dropna()

# Task 2: Basic Data Analysis

print("\nBasic Statistics:")
print(df.describe())

grouped = df.groupby("species").mean()
print("\nMean values by species:")
print(grouped)

print("\nObservations:")
print("- Setosa generally has smaller petal dimensions.")
print("- Virginica tends to have the largest sepal and petal dimensions.")
print("- Versicolor is in-between the other two species.")


# Task 3: Data Visualization

sns.set(style="whitegrid")

# (1) Line chart
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Trend of Sepal & Petal Lengths over Index")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# (2) Bar chart
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# (3) Histogram
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# (4) Scatter plot
plt.figure(figsize=(6,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set1")
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

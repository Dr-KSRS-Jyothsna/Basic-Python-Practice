"""
File: seaborn_visualization_basics.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates basic and commonly used Seaborn plots
for data visualization and analysis.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. Create a simple Pandas DataFrame
# --------------------------------------------------
data = {
    "Name": ["Asha", "Bala", "Chitra", "Deepak"],
    "Marks": [78, 85, 90, 88],
    "Hours_Studied": [4, 5, 6, 5],
    "Department": ["ECE", "ECE", "CSE", "CSE"]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

# --------------------------------------------------
# 2. Bar Plot (Comparison)
# --------------------------------------------------
plt.figure()
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Bar Plot - Marks of Students")
plt.show()

# --------------------------------------------------
# 3. Line Plot (Trend)
# --------------------------------------------------
plt.figure()
sns.lineplot(x="Hours_Studied", y="Marks", data=df, marker="o")
plt.title("Line Plot - Study Hours vs Marks")
plt.show()

# --------------------------------------------------
# 4. Scatter Plot (Relationship)
# --------------------------------------------------
plt.figure()
sns.scatterplot(x="Hours_Studied", y="Marks", hue="Department", data=df)
plt.title("Scatter Plot - Marks vs Study Hours")
plt.show()

# --------------------------------------------------
# 5. Histogram (Distribution)
# --------------------------------------------------
plt.figure()
sns.histplot(df["Marks"], bins=5, kde=True)
plt.title("Histogram - Distribution of Marks")
plt.show()

# --------------------------------------------------
# 6. Box Plot (Spread & Outliers)
# --------------------------------------------------
plt.figure()
sns.boxplot(x="Department", y="Marks", data=df)
plt.title("Box Plot - Marks by Department")
plt.show()

# --------------------------------------------------
# 7. Heatmap (Matrix Visualization)
# --------------------------------------------------
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

plt.figure()
sns.heatmap(matrix, annot=True, cmap="viridis")
plt.title("Heatmap Example")
plt.show()

# --------------------------------------------------
# 8. Correlation Heatmap (Very Important in ML)
# --------------------------------------------------
plt.figure()
sns.heatmap(df[["Marks", "Hours_Studied"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

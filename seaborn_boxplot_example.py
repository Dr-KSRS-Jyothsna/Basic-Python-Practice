"""
File: seaborn_boxplot_example.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates how to create a box plot using Seaborn
to compare birth rates across income groups.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------------
# Create sample dataset
# --------------------------------------------------
data = {
    "IncomeGroup": [
        "High income", "High income", "High income", "High income",
        "Low income", "Low income", "Low income", "Low income",
        "Upper middle income", "Upper middle income",
        "Upper middle income", "Upper middle income",
        "Lower middle income", "Lower middle income",
        "Lower middle income", "Lower middle income"
    ],
    "BirthRate": [
        8, 10, 12, 21,
        25, 35, 37, 50,
        9, 18, 21, 31,
        11, 24, 30, 40
    ]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# Create box plot
# --------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x="IncomeGroup", y="BirthRate", data=df)

plt.title("Birth Rate by Income Group")
plt.xlabel("Income Group")
plt.ylabel("Birth Rate")

plt.show()

"""
File: matplotlib_vs_seaborn_comparison.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program compares plotting using:
1. Matplotlib alone
2. Matplotlib + Seaborn

The same data is visualized to show differences in code simplicity,
styling, and statistical support.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --------------------------------------------------
# Sample Data (Pandas DataFrame)
# --------------------------------------------------
data = {
    "Hours_Studied": [2, 4, 6, 8, 10],
    "Marks": [40, 55, 70, 85, 95]
}

df = pd.DataFrame(data)

# ==================================================
# PART 1: Matplotlib ONLY
# ==================================================
plt.figure()
plt.scatter(df["Hours_Studied"], df["Marks"],
            color="blue", marker="o")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Matplotlib Only: Marks vs Hours Studied")
plt.grid(True)
plt.show()

# ==================================================
# PART 2: Matplotlib + Seaborn
# ==================================================
plt.figure()
sns.scatterplot(x="Hours_Studied",
                y="Marks",
                data=df,
                s=100)
plt.title("Matplotlib + Seaborn: Marks vs Hours Studied")
plt.show()

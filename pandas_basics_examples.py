"""
File: pandas_basics_examples.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates basic and intermediate usage of the Pandas
library, including Series, DataFrame creation, filtering, and simple analysis.
"""

import pandas as pd

# --------------------------------------------------
# 1. EASY: Creating a Series
# --------------------------------------------------
marks = pd.Series([78, 85, 90, 88])
print("Pandas Series:")
print(marks)

print("-" * 60)

# --------------------------------------------------
# 2. EASY: Creating a DataFrame
# --------------------------------------------------
data = {
    "Name": ["Asha", "Bala", "Chitra", "Deepak"],
    "Marks": [78, 85, 90, 88],
    "Passed": [True, True, True, True]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 3. EASY: Accessing Columns
# --------------------------------------------------
print("Marks column:")
print(df["Marks"])

print("-" * 60)

# --------------------------------------------------
# 4. EASY: Accessing Rows using loc
# --------------------------------------------------
print("First two rows:")
print(df.loc[0:1])

print("-" * 60)

# --------------------------------------------------
# 5. INTERMEDIATE: Filtering Data (Masking)
# --------------------------------------------------
print("Students with Marks > 85:")
print(df[df["Marks"] > 85])

print("-" * 60)

# --------------------------------------------------
# 6. INTERMEDIATE: Adding a New Column
# --------------------------------------------------
df["Grade"] = ["B", "B", "A", "A"]
print("DataFrame after adding Grade column:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 7. INTERMEDIATE: Basic Statistics
# --------------------------------------------------
print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

print("-" * 60)

# --------------------------------------------------
# 8. INTERMEDIATE: Sorting Data
# --------------------------------------------------
sorted_df = df.sort_values(by="Marks", ascending=False)
print("DataFrame sorted by Marks (Descending):")
print(sorted_df)

print("-" * 60)

# --------------------------------------------------
# 9. INTERMEDIATE: Handling Missing Values
# --------------------------------------------------
df_with_nan = df.copy()
df_with_nan.loc[2, "Marks"] = None

print("DataFrame with missing value:")
print(df_with_nan)

print("\nFilling missing value with average marks:")
df_with_nan["Marks"].fillna(df["Marks"].mean(), inplace=True)
print(df_with_nan)

print("-" * 60)

# --------------------------------------------------
# 10. INTERMEDIATE: Grouping Data
# --------------------------------------------------
group_data = {
    "Department": ["ECE", "ECE", "CSE", "CSE"],
    "Marks": [78, 85, 90, 88]
}

group_df = pd.DataFrame(group_data)

print("Group-wise Average Marks:")
print(group_df.groupby("Department")["Marks"].mean())

"""
File: pandas_data_manipulation_all.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates common Pandas data manipulation operations:
- Adding rows and columns
- Deleting rows and columns
- Updating values
- Renaming columns
- Handling missing values
- Sorting and filtering data
"""

import pandas as pd

# --------------------------------------------------
# 1. Create Initial DataFrame
# --------------------------------------------------
data = {
    "Name": ["Asha", "Bala", "Chitra"],
    "Marks": [78, 85, 90],
    "Passed": [True, True, True]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 2. ADDING A NEW COLUMN
# --------------------------------------------------
df["Grade"] = ["B", "B", "A"]
print("After adding a new column (Grade):")
print(df)

print("-" * 60)

# --------------------------------------------------
# 3. ADDING A NEW ROW
# --------------------------------------------------
df.loc[len(df)] = ["Deepak", 88, True, "A"]
print("After adding a new row:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 4. UPDATING DATA (Modify a value)
# --------------------------------------------------
df.loc[1, "Marks"] = 87
print("After updating Bala's marks:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 5. DELETING A COLUMN using drop()
# --------------------------------------------------
df.drop("Passed", axis=1, inplace=True)
print("After deleting 'Passed' column:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 6. DELETING A ROW using drop()
# --------------------------------------------------
df.drop(0, axis=0, inplace=True)
print("After deleting row with index 0:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 7. RESET INDEX (Good practice after deleting rows)
# --------------------------------------------------
df.reset_index(drop=True, inplace=True)
print("After resetting index:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 8. RENAMING COLUMNS
# --------------------------------------------------
df.rename(columns={"Marks": "Score"}, inplace=True)
print("After renaming 'Marks' to 'Score':")
print(df)

print("-" * 60)

# --------------------------------------------------
# 9. HANDLING MISSING VALUES
# --------------------------------------------------
df.loc[1, "Score"] = None
print("After introducing missing value:")
print(df)

df["Score"].fillna(df["Score"].mean(), inplace=True)
print("After filling missing value with average:")
print(df)

print("-" * 60)

# --------------------------------------------------
# 10. FILTERING DATA (Masking)
# --------------------------------------------------
print("Students with Score > 85:")
print(df[df["Score"] > 85])

print("-" * 60)

# --------------------------------------------------
# 11. SORTING DATA
# --------------------------------------------------
sorted_df = df.sort_values(by="Score", ascending=False)
print("Data sorted by Score (Descending):")
print(sorted_df)

print("-" * 60)

# --------------------------------------------------
# 12. BASIC STATISTICS
# --------------------------------------------------
print("Average Score:", df["Score"].mean())
print("Maximum Score:", df["Score"].max())
print("Minimum Score:", df["Score"].min())

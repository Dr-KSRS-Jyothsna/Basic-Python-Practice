"""
File: numpy_row_and_column_selection.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates how to select rows, columns,
specific elements, and slices from NumPy arrays.
"""

import numpy as np

print("=" * 70)
print("NUMPY ROW AND COLUMN SELECTION")
print("=" * 70)

# --------------------------------------------------
# CREATING A SAMPLE MATRIX
# --------------------------------------------------
b = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print("\nMatrix b:")
print(b)

# Matrix reference
print("\nMatrix indices:")
print("Rows -> 0, 1, 2")
print("Cols -> 0, 1, 2")

# --------------------------------------------------
# 1. ROW SELECTION
# --------------------------------------------------
print("\n1. ROW SELECTION")

print("Row at index 1:", b[1])
print("Rows from index 1 to 2:", b[1:3])

# --------------------------------------------------
# 2. COLUMN SELECTION (IMPORTANT)
# --------------------------------------------------
print("\n2. COLUMN SELECTION")

print("Column at index 0:", b[:, 0])
print("Column at index 1:", b[:, 1])
print("Columns from index 1 to 2:\n", b[:, 1:3])

# --------------------------------------------------
# 3. ROWS AND COLUMNS TOGETHER
# --------------------------------------------------
print("\n3. ROWS AND COLUMNS TOGETHER")

print("Rows 1–2 and Columns 0–1:\n", b[1:3, 0:2])

# --------------------------------------------------
# 4. SINGLE ELEMENT ACCESS
# --------------------------------------------------
print("\n4. SINGLE ELEMENT ACCESS")

print("Element at row 2, column 1:", b[2, 1])

# --------------------------------------------------
# 5. NON-CONTINUOUS COLUMN SELECTION
# --------------------------------------------------
print("\n5. NON-CONTINUOUS COLUMN SELECTION")

print("Columns 0 and 2:\n", b[:, [0, 2]])

# --------------------------------------------------
# 6. BOOLEAN INDEXING
# --------------------------------------------------
print("\n6. BOOLEAN INDEXING")

print("Elements greater than 50:", b[b > 50])

# --------------------------------------------------
# 7. PRACTICAL EXAMPLE
# --------------------------------------------------
print("\n7. PRACTICAL EXAMPLE")

marks = np.array([[78, 85, 90],
                  [66, 72, 88],
                  [91, 95, 89]])

print("Marks matrix:\n", marks)

print("All students, subject 2 marks:", marks[:, 1])
print("Top scores (>90):", marks[marks > 90])

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
print("\nSUMMARY:")
print("Use array[row_index] for rows")
print("Use array[:, col_index] for columns")
print("Use array[rows, columns] for combined selection")

print("\nNumPy row and column selection demo completed.")

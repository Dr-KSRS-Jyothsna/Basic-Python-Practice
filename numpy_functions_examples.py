"""
File: numpy_functions_examples.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates commonly used NumPy functions
with simple to moderately complex examples.
"""

import numpy as np

print("=" * 70)
print("NUMPY FUNCTIONS : BASIC TO ADVANCED")
print("=" * 70)

# --------------------------------------------------
# 1. ARRAY CREATION FUNCTIONS
# --------------------------------------------------
print("\n1. ARRAY CREATION FUNCTIONS")

a = np.array([1, 2, 3, 4, 5])
print("Array using array():", a)

zeros = np.zeros(5)
ones = np.ones(5)
full = np.full(5, 7)

print("Zeros:", zeros)
print("Ones:", ones)
print("Full (all 7s):", full)

# --------------------------------------------------
# 2. RANGE & SEQUENCE FUNCTIONS
# --------------------------------------------------
print("\n2. RANGE & SEQUENCE FUNCTIONS")

r1 = np.arange(1, 10, 2)
r2 = np.linspace(1, 10, 5)

print("arange(1,10,2):", r1)
print("linspace(1,10,5):", r2)

# --------------------------------------------------
# 3. BASIC MATHEMATICAL FUNCTIONS
# --------------------------------------------------
print("\n3. BASIC MATHEMATICAL FUNCTIONS")

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Standard Deviation:", np.std(a))
print("Square root:", np.sqrt(a))

# --------------------------------------------------
# 4. AGGREGATION FUNCTIONS
# --------------------------------------------------
print("\n4. AGGREGATION FUNCTIONS")

print("Cumulative sum:", np.cumsum(a))
print("Product of elements:", np.prod(a))

# --------------------------------------------------
# 5. SORTING & SEARCH FUNCTIONS
# --------------------------------------------------
print("\n5. SORTING & SEARCH FUNCTIONS")

b = np.array([30, 10, 50, 20])
print("Original array:", b)

print("Sorted array:", np.sort(b))
print("Index of max value:", np.argmax(b))
print("Index of min value:", np.argmin(b))

# --------------------------------------------------
# 6. SHAPE & RESHAPING FUNCTIONS
# --------------------------------------------------
print("\n6. SHAPE & RESHAPING FUNCTIONS")

c = np.array([1, 2, 3, 4, 5, 6])
reshaped = c.reshape(2, 3)

print("Original array:", c)
print("Reshaped (2x3):\n", reshaped)
print("Shape:", reshaped.shape)
print("Size:", reshaped.size)

# --------------------------------------------------
# 7. MATRIX FUNCTIONS
# --------------------------------------------------
print("\n7. MATRIX FUNCTIONS")

M = np.array([[1, 2], [3, 4]])

print("Matrix:\n", M)
print("Transpose:\n", np.transpose(M))
print("Matrix inverse:\n", np.linalg.inv(M))
print("Determinant:", np.linalg.det(M))

# --------------------------------------------------
# 8. LOGICAL & BOOLEAN FUNCTIONS
# --------------------------------------------------
print("\n8. LOGICAL & BOOLEAN FUNCTIONS")

nums = np.array([10, 25, 5, 30, 18])
print("Original:", nums)

print("Values > 15:", nums[nums > 15])
print("Any value > 25?:", np.any(nums > 25))
print("All values > 0?:", np.all(nums > 0))

# --------------------------------------------------
# 9. REAL-WORLD STYLE EXAMPLE
# --------------------------------------------------
print("\n9. REAL-WORLD EXAMPLE (MARKS ANALYSIS)")

marks = np.array([78, 85, 90, 66, 72])
print("Marks:", marks)
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Passed students:", marks[marks >= 50])

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
print("\nSUMMARY:")
print("NumPy provides built-in functions for fast numerical computation.")
print("These functions are heavily used in Data Science, ML, AI, and GNSS.")

print("\nNumPy functions program executed successfully.")

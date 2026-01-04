"""
File: numpy_basics_to_advanced.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates NumPy concepts starting from very basic
array creation to slightly advanced numerical and matrix operations.
"""

import numpy as np

print("=" * 70)
print("NUMPY : BASIC TO ADVANCED EXAMPLES")
print("=" * 70)

# --------------------------------------------------
# 1. VERY BASIC: CREATING NUMPY ARRAY
# --------------------------------------------------
print("\n1. BASIC ARRAY CREATION")

arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)
print("Type:", type(arr))

# --------------------------------------------------
# 2. NUMPY ARRAY VS PYTHON LIST
# --------------------------------------------------
print("\n2. ARRAY VS LIST")

lst = [1, 2, 3, 4, 5]
print("List * 2:", lst * 2)
print("Array * 2:", arr * 2)

# --------------------------------------------------
# 3. ARRAY PROPERTIES
# --------------------------------------------------
print("\n3. ARRAY PROPERTIES")

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# --------------------------------------------------
# 4. BASIC MATHEMATICAL OPERATIONS
# --------------------------------------------------
print("\n4. BASIC MATH OPERATIONS")

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Square root:", np.sqrt(arr))

# --------------------------------------------------
# 5. ARRAY INDEXING AND SLICING
# --------------------------------------------------
print("\n5. INDEXING AND SLICING")

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])
print("Reverse:", arr[::-1])

# --------------------------------------------------
# 6. CREATING ARRAYS USING BUILT-IN FUNCTIONS
# --------------------------------------------------
print("\n6. ARRAY CREATION FUNCTIONS")

zeros = np.zeros(5)
ones = np.ones(5)
range_arr = np.arange(1, 10, 2)

print("Zeros array:", zeros)
print("Ones array:", ones)
print("Range array:", range_arr)

# --------------------------------------------------
# 7. RESHAPING ARRAYS
# --------------------------------------------------
print("\n7. RESHAPING")

arr2 = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr2.reshape(2, 3)

print("Original:", arr2)
print("Reshaped (2x3):\n", reshaped)

# --------------------------------------------------
# 8. MATRIX OPERATIONS
# --------------------------------------------------
print("\n8. MATRIX OPERATIONS")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Addition:\n", A + B)
print("Multiplication:\n", A * B)
print("Matrix Dot Product:\n", np.dot(A, B))
print("Transpose of A:\n", A.T)

# --------------------------------------------------
# 9. BOOLEAN MASKING
# --------------------------------------------------
print("\n9. BOOLEAN MASKING")

numbers = np.array([10, 25, 30, 5, 18])
print("Original array:", numbers)
print("Values > 15:", numbers[numbers > 15])

# --------------------------------------------------
# 10. SIMPLE REAL-WORLD EXAMPLE
# --------------------------------------------------
print("\n10. REAL-WORLD EXAMPLE")

marks = np.array([78, 85, 90, 66, 72])
print("Marks:", marks)
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Passed students marks:", marks[marks >= 50])

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
print("\nSUMMARY:")
print("NumPy provides fast and efficient numerical operations.")
print("It is the foundation for Data Science, ML, AI, and Signal Processing.")

print("\nNumPy program execution completed successfully.")

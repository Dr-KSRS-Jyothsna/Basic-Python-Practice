"""
File: numpy_masking.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates masking in NumPy.
Masking is used to select or modify elements of an array
based on given conditions.
"""

import numpy as np

# --------------------------------------------------
# 1. Create a NumPy array
# --------------------------------------------------
a = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(a)

print("-" * 60)

# --------------------------------------------------
# 2. Boolean Mask Creation
# --------------------------------------------------
mask = a > 25
print("Mask (a > 25):")
print(mask)

print("-" * 60)

# --------------------------------------------------
# 3. Applying Mask (Filtering values)
# --------------------------------------------------
filtered_values = a[mask]
print("Filtered values (greater than 25):")
print(filtered_values)

print("-" * 60)

# --------------------------------------------------
# 4. Direct Masking (One-line method)
# --------------------------------------------------
print("Direct masking result:")
print(a[a > 25])

print("-" * 60)

# --------------------------------------------------
# 5. Masking with Multiple Conditions
# --------------------------------------------------
print("Values between 20 and 50:")
print(a[(a > 20) & (a < 50)])

print("-" * 60)

# --------------------------------------------------
# 6. Replace Values Using Masking
# --------------------------------------------------
b = a.copy()
b[b < 30] = 0
print("After replacing values < 30 with 0:")
print(b)

print("-" * 60)

# --------------------------------------------------
# 7. Masking in 2D Array
# --------------------------------------------------
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

print("2D Array:")
print(matrix)

print("Values greater than 30 in 2D array:")
print(matrix[matrix > 30])

print("-" * 60)

# --------------------------------------------------
# Summary
# --------------------------------------------------
print("Masking allows condition-based selection and modification of data.")

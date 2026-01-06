"""
File: numpy_reshape.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates the NumPy reshape() function
and explains the effect of memory order using 'C' and 'F'.
"""

import numpy as np

# --------------------------------------------------
# Original 1D array
# --------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(arr)
print("Shape:", arr.shape)

print("-" * 60)

# --------------------------------------------------
# Reshape using default order (order='C')
# --------------------------------------------------
reshaped_c = arr.reshape(2, 3, order='C')

print("Reshaped Array (order='C'):")
print(reshaped_c)
print("Shape:", reshaped_c.shape)

# Row-wise filling
# [[1 2 3]
#  [4 5 6]]

print("-" * 60)

# --------------------------------------------------
# Reshape using column-major order (order='F')
# --------------------------------------------------
reshaped_f = arr.reshape(2, 3, order='F')

print("Reshaped Array (order='F'):")
print(reshaped_f)
print("Shape:", reshaped_f.shape)

# Column-wise filling
# [[1 3 5]
#  [2 4 6]]

print("-" * 60)

# --------------------------------------------------
# Automatic dimension inference using -1
# --------------------------------------------------
auto_reshape = arr.reshape(-1, 2)

print("Reshape using -1 (automatic dimension):")
print(auto_reshape)
print("Shape:", auto_reshape.shape)

print("-" * 60)

# --------------------------------------------------
# Important Rule
# --------------------------------------------------
print("Rule: Total number of elements must remain the same during reshape.")

"""
File: numpy_matrix_creation_and_operations.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates how to create NumPy matrices of choice
and perform common matrix operations using NumPy.
"""

import numpy as np

print("=" * 70)
print("NUMPY MATRIX CREATION AND OPERATIONS")
print("=" * 70)

# --------------------------------------------------
# 1. MATRIX WITH USER-DEFINED VALUES (MOST IMPORTANT)
# --------------------------------------------------
print("\n1. MATRIX WITH CHOSEN VALUES")

A = np.array([[1, 2, 3],
              [4, 5, 6]])
print("Matrix A:\n", A)

# --------------------------------------------------
# 2. MATRIX USING arange() + reshape()
# --------------------------------------------------
print("\n2. MATRIX USING arange() + reshape()")

B = np.arange(1, 13).reshape(3, 4)
print("Matrix B:\n", B)

# --------------------------------------------------
# 3. SPECIAL MATRICES
# --------------------------------------------------
print("\n3. SPECIAL MATRICES")

zeros_mat = np.zeros((2, 3))
ones_mat = np.ones((2, 3))
full_mat = np.full((2, 3), 9)

print("Zeros matrix:\n", zeros_mat)
print("Ones matrix:\n", ones_mat)
print("Full matrix (all 9s):\n", full_mat)

# --------------------------------------------------
# 4. IDENTITY & DIAGONAL MATRICES
# --------------------------------------------------
print("\n4. IDENTITY & DIAGONAL MATRICES")

identity = np.eye(3)
diagonal = np.diag([10, 20, 30])

print("Identity matrix:\n", identity)
print("Diagonal matrix:\n", diagonal)

# --------------------------------------------------
# 5. RANDOM MATRICES
# --------------------------------------------------
print("\n5. RANDOM MATRICES")

random_float = np.random.rand(3, 3)
random_int = np.random.randint(1, 10, (3, 3))

print("Random float matrix:\n", random_float)
print("Random integer matrix:\n", random_int)

# --------------------------------------------------
# 6. BASIC MATRIX OPERATIONS
# --------------------------------------------------
print("\n6. BASIC MATRIX OPERATIONS")

C = np.array([[1, 2],
              [3, 4]])
D = np.array([[5, 6],
              [7, 8]])

print("Matrix C:\n", C)
print("Matrix D:\n", D)

print("Addition (C + D):\n", C + D)
print("Subtraction (C - D):\n", C - D)
print("Element-wise multiplication:\n", C * D)

# --------------------------------------------------
# 7. MATRIX MULTIPLICATION (DOT PRODUCT)
# --------------------------------------------------
print("\n7. MATRIX MULTIPLICATION")

dot_product = np.dot(C, D)
print("Dot product (C · D):\n", dot_product)

# --------------------------------------------------
# 8. TRANSPOSE, INVERSE, DETERMINANT
# --------------------------------------------------
print("\n8. ADVANCED MATRIX OPERATIONS")

print("Transpose of C:\n", C.T)
print("Determinant of C:", np.linalg.det(C))
print("Inverse of C:\n", np.linalg.inv(C))

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
print("\nSUMMARY:")
print("Use np.array() to create matrices of your choice.")
print("Use arange()+reshape() for patterns.")
print("NumPy supports powerful matrix operations.")

print("\nMatrix program execution completed.")

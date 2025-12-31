"""
File: math_random_statistics_numpy.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates commonly used mathematical operations
using Python's math, random, statistics modules and NumPy basics.
"""

import math
import random
import statistics
import numpy as np

print("=" * 70)
print("PYTHON MATH, RANDOM, STATISTICS AND NUMPY FUNCTIONS")
print("=" * 70)

# --------------------------------------------------
# 1. MATH MODULE
# --------------------------------------------------
print("\n1. MATH MODULE")

x = 16
y = 3.7

print("Square root of 16:", math.sqrt(x))
print("Ceiling of 3.7:", math.ceil(y))
print("Floor of 3.7:", math.floor(y))
print("Power (2^3):", math.pow(2, 3))
print("Absolute value of -25:", math.fabs(-25))
print("Value of pi:", math.pi)

# --------------------------------------------------
# 2. RANDOM MODULE
# --------------------------------------------------
print("\n2. RANDOM MODULE")

print("Random float between 0 and 1:", random.random())
print("Random integer between 1 and 10:", random.randint(1, 10))

numbers = [10, 20, 30, 40, 50]
print("Random choice from list:", random.choice(numbers))

random.shuffle(numbers)
print("Shuffled list:", numbers)

# --------------------------------------------------
# 3. STATISTICS MODULE
# --------------------------------------------------
print("\n3. STATISTICS MODULE")

data = [10, 20, 30, 40, 50, 50]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Variance:", statistics.variance(data))
print("Standard Deviation:", statistics.stdev(data))

# --------------------------------------------------
# 4. NUMPY MATH BASICS
# --------------------------------------------------
print("\n4. NUMPY MATH BASICS")

arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)

print("Array sum:", np.sum(arr))
print("Array mean:", np.mean(arr))
print("Array max:", np.max(arr))
print("Array min:", np.min(arr))
print("Square root of array:", np.sqrt(arr))

# Matrix operations
matrix = np.array([[1, 2], [3, 4]])
print("\nMatrix:\n", matrix)
print("Matrix transpose:\n", matrix.T)

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
print("\nSUMMARY:")
print("math      -> basic mathematical functions")
print("random    -> random number generation")
print("statistics-> data analysis functions")
print("numpy     -> fast numerical computations")

print("\nProgram execution completed.")

"""
File: math_functions.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates commonly used mathematical functions
from the math module in Python with simple examples.
"""

import math

print("=" * 60)
print("PYTHON MATH FUNCTIONS")
print("=" * 60)

# -----------------------------
# BASIC MATHEMATICAL FUNCTIONS
# -----------------------------

x = 16
y = 3.7

print("\nBasic Math Functions")
print("Square root of 16:", math.sqrt(x))
print("Ceiling of 3.7:", math.ceil(y))
print("Floor of 3.7:", math.floor(y))
print("Power (2^3):", math.pow(2, 3))
print("Absolute value of -10:", math.fabs(-10))

print("-" * 60)

# -----------------------------
# TRIGONOMETRIC FUNCTIONS
# -----------------------------

angle = math.radians(30)

print("\nTrigonometric Functions")
print("sin(30°):", math.sin(angle))
print("cos(30°):", math.cos(angle))
print("tan(30°):", math.tan(angle))

print("-" * 60)

# -----------------------------
# LOGARITHMIC FUNCTIONS
# -----------------------------

print("\nLogarithmic Functions")
print("log base e of 10:", math.log(10))
print("log base 10 of 100:", math.log10(100))
print("log base 2 of 8:", math.log2(8))

print("-" * 60)

# -----------------------------
# CONSTANTS IN MATH MODULE
# -----------------------------

print("\nMath Constants")
print("Value of pi:", math.pi)
print("Value of e:", math.e)

print("-" * 60)

# -----------------------------
# SUMMARY
# -----------------------------

print("\nSUMMARY:")
print("The math module provides mathematical functions and constants.")
print("It is widely used in scientific computing, data science, and AI.")

print("\nMath functions demonstration completed.")

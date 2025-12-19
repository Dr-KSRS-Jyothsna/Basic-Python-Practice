"""
File: variables.py
Author: Dr. K.S.R.S. Jyothsna
Description:
This program demonstrates the concept of variables in Python,
including variable assignment, multiple assignment, and dynamic typing.
"""

# 1. Variable Assignment
x = 10
y = 3.5
name = "Python"

print("Integer value:", x)
print("Float value:", y)
print("String value:", name)

# 2. Dynamic Typing in Python
x = "Data Science"
print("Updated x value:", x)

# 3. Multiple Variable Assignment
a, b, c = 1, 2, 3
print("a:", a, "b:", b, "c:", c)

# 4. Assigning Same Value to Multiple Variables
p = q = r = 100
print("p:", p, "q:", q, "r:", r)

# 5. Variable Naming Rules (Examples)
valid_variable = 10
_valid_variable = 20
variable123 = 30

print("Valid variable examples:",
      valid_variable, _valid_variable, variable123)

# 6. Using Variables in Expressions
length = 10
width = 5
area = length * width

print("Area of rectangle:", area)

# 7. Checking Variable Data Types
print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of name:", type(name))

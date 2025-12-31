"""
File: eval_function_examples.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates the usage of eval() function in Python
from simple to slightly complex examples.
"""

print("=" * 70)
print("PYTHON eval() FUNCTION : SIMPLE TO COMPLEX EXAMPLES")
print("=" * 70)

# --------------------------------------------------
# 1. SIMPLE MATHEMATICAL EXPRESSION
# --------------------------------------------------
result = eval("10 + 20 + 30")
print("Result of '10 + 20 + 30':", result)

print("-" * 60)

# --------------------------------------------------
# 2. USING eval() WITH USER INPUT
# --------------------------------------------------
expr = eval(input("Enter a mathematical expression (e.g., 5*4): "))
print("Evaluated result:", expr)

print("-" * 60)

# --------------------------------------------------
# 3. eval() WITH VARIABLES
# --------------------------------------------------
a = 10
b = 5
expression = "a * b + 20"
print("Expression:", expression)
print("Result:", eval(expression))

print("-" * 60)

# --------------------------------------------------
# 4. eval() RETURNING DIFFERENT DATA TYPES
# --------------------------------------------------
x = eval("100")
y = eval("3.14")
z = eval("'Python'")

print("x:", x, "Type:", type(x))
print("y:", y, "Type:", type(y))
print("z:", z, "Type:", type(z))

print("-" * 60)

# --------------------------------------------------
# 5. eval() FOR LIST INPUT
# --------------------------------------------------
numbers = eval(input("Enter a list (e.g., [1, 2, 3]): "))
print("List entered:", numbers)
print("Sum of list:", sum(numbers))

print("-" * 60)

print("eval() function demonstration completed.")

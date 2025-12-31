"""
File: input_function_simple_to_complex.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates the usage of input() function in Python
starting from very simple examples to slightly complex ones.
"""

print("=" * 70)
print("PYTHON input() FUNCTION : SIMPLE TO COMPLEX EXAMPLES")
print("=" * 70)

# --------------------------------------------------
# 1. SIMPLE STRING INPUT
# --------------------------------------------------
name = input("Enter your name: ")
print("Hello,", name)

print("-" * 60)

# --------------------------------------------------
# 2. INTEGER INPUT WITH TYPE CASTING
# --------------------------------------------------
age = int(input("Enter your age: "))
print("Your age after 10 years will be:", age + 10)

print("-" * 60)

# --------------------------------------------------
# 3. FLOAT INPUT
# --------------------------------------------------
salary = float(input("Enter your monthly salary: "))
print("Your annual salary is:", salary * 12)

print("-" * 60)

# --------------------------------------------------
# 4. MULTIPLE INPUTS IN ONE LINE
# --------------------------------------------------
a, b = input("Enter two numbers separated by space: ").split()
a = int(a)
b = int(b)

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

print("-" * 60)

# --------------------------------------------------
# 5. LIST INPUT FROM USER
# --------------------------------------------------
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("List of numbers:", numbers)
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

print("-" * 60)

# --------------------------------------------------
# 6. CONDITIONAL LOGIC WITH INPUT
# --------------------------------------------------
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("-" * 60)

# --------------------------------------------------
# 7. LOOP WITH INPUT
# --------------------------------------------------
n = int(input("Enter how many subjects: "))
total = 0

for i in range(n):
    mark = int(input(f"Enter marks of subject {i+1}: "))
    total += mark

print("Total marks:", total)
print("Average marks:", total / n)

print("-" * 60)

# --------------------------------------------------
# 8. SIMPLE REAL-WORLD EXAMPLE
# --------------------------------------------------
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width
print("Area of rectangle:", area)

print("-" * 60)

print("Input function demonstration completed successfully.")

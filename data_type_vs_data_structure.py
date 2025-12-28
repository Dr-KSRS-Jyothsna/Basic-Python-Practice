"""
File: data_type_vs_data_structure.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program explains the difference between Data Types and
Data Structures in Python using simple examples.
"""

print("=" * 60)
print("DATA TYPE vs DATA STRUCTURE IN PYTHON")
print("=" * 60)

# -----------------------------
# DATA TYPES (Single Value)
# -----------------------------
print("\nDATA TYPES (Store ONE value)")

a = 10              # int
b = 3.14            # float
c = "Python"        # string
d = True            # boolean

print("Integer:", a, "Type:", type(a))
print("Float:", b, "Type:", type(b))
print("String:", c, "Type:", type(c))
print("Boolean:", d, "Type:", type(d))

# -----------------------------
# DATA STRUCTURES (Multiple Values)
# -----------------------------
print("\nDATA STRUCTURES (Store MULTIPLE values)")

# List
my_list = [10, 20, 30]
print("List:", my_list, "Type:", type(my_list))

# Tuple
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple, "Type:", type(my_tuple))

# Set
my_set = {10, 20, 30}
print("Set:", my_set, "Type:", type(my_set))

# Dictionary
my_dict = {"a": 1, "b": 2}
print("Dictionary:", my_dict, "Type:", type(my_dict))

print("\nSUMMARY:")
print("Data Type  -> Stores a single value")
print("Data Structure -> Stores multiple values")

print("\nProgram execution completed.")

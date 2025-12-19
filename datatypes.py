"""
File: data_types.py
Author: Dr. K.S.R.S. Jyothsna
Description:
This program demonstrates the built-in data types in Python
with simple and clear examples.
"""

# 1. Numeric Data Types
integer_value = 25
float_value = 3.14
complex_value = 2 + 3j

print("Integer:", integer_value, "Type:", type(integer_value))
print("Float:", float_value, "Type:", type(float_value))
print("Complex:", complex_value, "Type:", type(complex_value))

# 2. Boolean Data Type
is_active = True
print("Boolean:", is_active, "Type:", type(is_active))

# 3. String Data Type
language = "Python for Data Science"
print("String:", language, "Type:", type(language))

# 4. List Data Type (Mutable)
numbers_list = [1, 2, 3, 4]
numbers_list.append(5)
print("List:", numbers_list, "Type:", type(numbers_list))

# 5. Tuple Data Type (Immutable)
coordinates = (10, 20)
print("Tuple:", coordinates, "Type:", type(coordinates))

# 6. Set Data Type (No Duplicates)
unique_values = {1, 2, 2, 3}
print("Set:", unique_values, "Type:", type(unique_values))

# 7. Dictionary Data Type (Key-Value Pairs)
student = {
    "name": "Jyothsna",
    "role": "AI Learner",
    "experience": "Teaching"
}
print("Dictionary:", student, "Type:", type(student))

# 8. None Data Type
result = None
print("None value:", result

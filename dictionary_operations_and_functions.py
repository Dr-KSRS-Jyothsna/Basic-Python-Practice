"""
File: dictionary_operations_and_functions.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates dictionary operations and
commonly used dictionary functions in Python with simple examples.
"""

print("=" * 60)
print("PYTHON DICTIONARY OPERATIONS AND FUNCTIONS")
print("=" * 60)

# -----------------------------
# CREATING A DICTIONARY
# -----------------------------
student = {
    "name": "Jyothsna",
    "qualification": "PhD",
    "domain": "AI",
    "experience": 20
}

print("\nOriginal Dictionary:")
print(student)

print("-" * 60)

# -----------------------------
# DICTIONARY OPERATIONS
# -----------------------------

# 1. Accessing values using keys
print("Name:", student["name"])

# 2. Using get() (safe access)
print("Domain:", student.get("domain"))
print("Age (using get):", student.get("age", "Not Available"))

# 3. Adding a new key-value pair
student["location"] = "India"
print("After adding location:", student)

# 4. Updating an existing value
student["experience"] = 22
print("After updating experience:", student)

# 5. Deleting a key-value pair
del student["qualification"]
print("After deleting qualification:", student)

print("-" * 60)

# -----------------------------
# DICTIONARY FUNCTIONS (METHODS)
# -----------------------------

# 6. keys() – returns all keys
print("Keys:", student.keys())

# 7. values() – returns all values
print("Values:", student.values())

# 8. items() – returns key-value pairs
print("Items:", student.items())

# 9. pop() – removes and returns value of a key
removed_value = student.pop("location")
print("Popped value:", removed_value)
print("After pop:", student)

# 10. popitem() – removes last inserted item
last_item = student.popitem()
print("Popitem result:", last_item)
print("After popitem:", student)

# 11. update() – updates dictionary with another dictionary
student.update({"skills": "Python, ML, AI", "role": "Educator"})
print("After update():", student)

# 12. copy() – creates a shallow copy
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# 13. clear() – removes all items
student.clear()
print("After clear():", student)

print("\nDictionary operations and functions demonstration completed.")

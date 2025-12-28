"""
File: string_operations_and_backslash.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates basic string operations in Python
and explains the importance of backslash (\) using simple examples.
"""

print("=" * 60)
print("PYTHON STRING OPERATIONS AND BACKSLASH USAGE")
print("=" * 60)

# -----------------------------
# STRING BASICS
# -----------------------------
text = "Hello Python"
print("\nOriginal String:", text)

# Length of string
print("Length of string:", len(text))

# Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("Substring (0:5):", text[0:5])
print("Reverse string:", text[::-1])

print("-" * 60)

# -----------------------------
# COMMON STRING OPERATIONS
# -----------------------------

# Concatenation
s1 = "Hello"
s2 = "World"
print("Concatenation:", s1 + " " + s2)

# Repetition
print("Repetition:", s1 * 3)

# Membership
print("'Py' in text:", "Py" in text)
print("'Java' not in text:", "Java" not in text)

# Case conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

print("-" * 60)

# -----------------------------
# IMPORTANCE OF BACKSLASH (\)
# -----------------------------

print("\nIMPORTANCE OF BACKSLASH (\\)")

# 1. Escape characters
print("New line example:")
print("Hello\nPython")

print("Tab space example:")
print("Hello\tPython")

# 2. Printing quotes inside strings
print("Using single quotes:")
print('Python is a "programming" language')

print("Using backslash to escape quotes:")
print("Python is a \"programming\" language")

# 3. Printing backslash itself
print("Printing backslash:")
print("C:\\Users\\Admin")

# 4. Raw string (r prefix)
print("Raw string example:")
path = r"C:\Users\Admin\Documents"
print(path)

print("-" * 60)

# -----------------------------
# SUMMARY
# -----------------------------
print("\nSUMMARY:")
print("Strings store text data in Python.")
print("Backslash (\\) is used for escape sequences and special characters.")
print("Raw strings help avoid escape issues in file paths.")

print("\nString operations and backslash demonstration completed.")

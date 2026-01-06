"""
File: matrix_reverse_operations.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program creates a 10x10 matrix and demonstrates various
reverse operations using Python slicing.
It also explains the usage of ':' and '::' in slicing.
"""

# --------------------------------------------------
# PART 1: Understanding ':' and '::'
# --------------------------------------------------
# data[start : stop : step]
#
# ':'   -> selects a range
# '::'  -> controls direction and jump (step)
#
# Examples:
# a[:]      -> full list
# a[::2]    -> every second element
# a[::-1]   -> reverse
# a[::-2]   -> reverse and skip one

# --------------------------------------------------
# PART 2: Create a 10 x 10 Matrix
# --------------------------------------------------

matrix = []
value = 1

for i in range(10):
    row = []
    for j in range(10):
        row.append(value)
        value += 1
    matrix.append(row)

print("Original 10 x 10 Matrix:")
for row in matrix:
    print(row)

print("-" * 60)

# --------------------------------------------------
# PART 3: Reverse Operations
# --------------------------------------------------

# 1. Reverse each row (horizontal flip)
print("Reverse each row:")
for row in matrix:
    print(row[::-1])

print("-" * 60)

# 2. Reverse row order (vertical flip)
print("Reverse row order:")
for row in matrix[::-1]:
    print(row)

print("-" * 60)

# 3. Full reverse (180-degree rotation)
print("Fully reversed matrix:")
for row in matrix[::-1]:
    print(row[::-1])

print("-" * 60)

# 4. Every alternate element in each row
print("Every alternate element in each row:")
for row in matrix:
    print(row[::2])

print("-" * 60)

# 5. Reverse and skip one element
print("Reverse and skip one element:")
for row in matrix:
    print(row[::-2])

print("-" * 60)

# 6. Reverse only first 5 columns
print("Reverse first 5 columns:")
for row in matrix:
    print(row[:5][::-1])

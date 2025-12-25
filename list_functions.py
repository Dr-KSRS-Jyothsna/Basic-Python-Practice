"""
File: list_functions.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates Python list data structure and
commonly used list functions with simple examples.
"""

# Creating a list
numbers = [10, 20, 30, 40, 10]
print("Original list:", numbers)

print("-" * 50)

# 1. append() – adds one element at the end
numbers.append(50)
print("After append(50):", numbers)

print("-" * 50)

# 2. extend() – adds multiple elements
numbers.extend([60, 70])
print("After extend([60, 70]):", numbers)

print("-" * 50)

# 3. insert() – inserts element at a specific index
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

print("-" * 50)

# 4. remove() – removes first occurrence of a value
numbers.remove(10)
print("After remove(10):", numbers)

print("-" * 50)

# 5. pop() – removes and returns element (default: last)
removed_item = numbers.pop()
print("Popped element:", removed_item)
print("After pop():", numbers)

print("-" * 50)

# 6. index() – returns index of first occurrence
index_value = numbers.index(30)
print("Index of 30:", index_value)

print("-" * 50)

# 7. count() – counts occurrences of an element
count_10 = numbers.count(10)
print("Count of 10:", count_10)

print("-" * 50)

# 8. reverse() – reverses the list
numbers.reverse()
print("After reverse():", numbers)

print("-" * 50)

# 9. sort() – sorts the list in ascending order
numbers.sort()
print("After sort():", numbers)

print("-" * 50)

# 10. copy() – creates a shallow copy of the list
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)

print("-" * 50)

# 11. clear() – removes all elements from the list
numbers.clear()
print("After clear():", numbers)

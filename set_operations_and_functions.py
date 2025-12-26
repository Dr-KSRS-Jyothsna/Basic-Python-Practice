"""
File: set_operations_and_functions.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates Python set operations and
commonly used set functions with simple examples.
"""

print("=" * 60)
print("PYTHON SET OPERATIONS AND FUNCTIONS")
print("=" * 60)

# -----------------------------
# SET OPERATIONS
# -----------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nSet A:", A)
print("Set B:", B)

print("\n--- Set Operations ---")

# Union
print("Union (A | B):", A | B)

# Intersection
print("Intersection (A & B):", A & B)

# Difference
print("Difference (A - B):", A - B)
print("Difference (B - A):", B - A)

# Symmetric Difference
print("Symmetric Difference (A ^ B):", A ^ B)

# Subset & Superset
C = {1, 2}
print("Set C:", C)
print("C is subset of A:", C.issubset(A))
print("A is superset of C:", A.issuperset(C))

# Disjoint
D = {7, 8}
print("A and D are disjoint:", A.isdisjoint(D))

print("-" * 60)

# -----------------------------
# SET FUNCTIONS (METHODS)
# -----------------------------

my_set = {10, 20, 30}
print("\nOriginal set:", my_set)

print("\n--- Set Functions ---")

# add()
my_set.add(40)
print("After add(40):", my_set)

# update()
my_set.update([50, 60])
print("After update([50, 60]):", my_set)

# remove()
my_set.remove(20)
print("After remove(20):", my_set)

# discard() – no error if element not present
my_set.discard(100)
print("After discard(100):", my_set)

# pop()
removed_element = my_set.pop()
print("Popped element:", removed_element)
print("After pop():", my_set)

# clear()
my_set.clear()
print("After clear():", my_set)

print("\nSet operations and functions demonstration completed.")

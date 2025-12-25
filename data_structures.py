"""
File: data_structures.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates the basic data structures in Python
such as List, Tuple, Set, Dictionary, and String with simple examples.
"""

print("=" * 60)
print("PYTHON DATA STRUCTURES")
print("=" * 60)

# 1. List
print("\n1. LIST (Ordered, Mutable)")
my_list = [10, 20, 30, 10]
print("Original list:", my_list)

my_list.append(40)
print("After append:", my_list)

print("Count of 10:", my_list.count(10))

# 2. Tuple
print("\n2. TUPLE (Ordered, Immutable)")
my_tuple = (1, 2, 3, 1)
print("Tuple:", my_tuple)
print("Count of 1:", my_tuple.count(1))

# 3. Set
print("\n3. SET (Unordered, No Duplicates)")
my_set = {10, 20, 30, 10}
print("Set:", my_set)

my_set.add(40)
print("After add:", my_set)

# 4. Dictionary
print("\n4. DICTIONARY (Key-Value Pairs)")
my_dict = {
    "name": "Jyothsna",
    "domain": "AI",
    "experience": "Teaching"
}
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])

# 5. String
print("\n5. STRING (Immutable Sequence)")
my_string = "PYTHON"
print("String:", my_string)
print("First character:", my_string[0])
print("Reverse string:", my_string[::-1])

print("\nData Structures demonstration completed.")

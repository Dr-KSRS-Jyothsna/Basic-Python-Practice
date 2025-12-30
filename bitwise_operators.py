"""
File: bitwise_operators.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates all bitwise operators in Python
using clear examples and binary explanations.
"""

# Bitwise operators work on binary representation of integers

# 1. Bitwise AND (&)
a = 5      # Binary: 0101
b = 3      # Binary: 0011
print("Bitwise AND (&)")
print("5 & 3 =", a & b)   # 0001 -> 1

print("-" * 50)

# 2. Bitwise OR (|)
print("Bitwise OR (|)")
print("5 | 3 =", a | b)   # 0111 -> 7

print("-" * 50)

# 3. Bitwise XOR (^)
print("Bitwise XOR (^)")
print("5 ^ 3 =", a ^ b)   # 0110 -> 6

print("-" * 50)

# 4. Bitwise NOT (~)
print("Bitwise NOT (~)")
print("~5 =", ~a)         # -(5 + 1) = -6

print("-" * 50)

# 5. Left Shift (<<)
print("Left Shift (<<)")
print("5 << 1 =", a << 1)   # 5 * 2 = 10
print("5 << 2 =", a << 2)   # 5 * 4 = 20

print("-" * 50)

# 6. Right Shift (>>)
print("Right Shift (>>)")
print("5 >> 1 =", a >> 1)   # 5 // 2 = 2
print("5 >> 2 =", a >> 2)   # 5 // 4 = 1

print("-" * 50)

# Summary
print("Summary:")
print("AND (&)  -> Both bits must be 1")
print("OR (|)   -> Any bit is 1")
print("XOR (^)  -> Bits must be different")
print("NOT (~)  -> Inverts all bits")
print("<<       -> Multiply by powers of 2")
print(">>       -> Divide by powers of 2")

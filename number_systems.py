"""
File: number_systems.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates different number systems in Python
and their representations: Decimal, Binary, Octal, and Hexadecimal.
It also shows conversions between these number systems.
"""

# 1. Decimal Number System (Base-10)
decimal_num = 10
print("Decimal number:", decimal_num)

print("-" * 50)

# 2. Binary Number System (Base-2)
binary_num = 0b1010
print("Binary (0b1010) in decimal:", binary_num)

print("-" * 50)

# 3. Octal Number System (Base-8)
octal_num = 0o12
print("Octal (0o12) in decimal:", octal_num)

print("-" * 50)

# 4. Hexadecimal Number System (Base-16)
hexadecimal_num = 0xA
print("Hexadecimal (0xA) in decimal:", hexadecimal_num)

print("-" * 50)

# 5. Decimal to Other Number Systems
num = 25
print("Decimal:", num)
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))

print("-" * 50)

# 6. Other Number Systems to Decimal
binary_to_decimal = int("1010", 2)
octal_to_decimal = int("12", 8)
hex_to_decimal = int("A", 16)

print("Binary to Decimal:", binary_to_decimal)
print("Octal to Decimal:", octal_to_decimal)
print("Hexadecimal to Decimal:", hex_to_decimal)

print("-" * 50)

# 7. Summary Output
print("All number systems are internally stored as binary in Python.")

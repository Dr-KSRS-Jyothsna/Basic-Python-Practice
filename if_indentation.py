"""
File: if_indentation_demo.py
Description: Demonstrates how if-else conditions and indentation work in Python.
Author: Dr. KSRS Jyothsna
"""

def example_one():
    print("Example 1: if True")
    if True:   # indentation is always 4 spaces
        print("Data Science")
    print("-" * 30)


def example_two():
    print("Example 2: if False")
    if False:
        print("Data Science")
    print("bye for now")
    print("-" * 30)


def example_three():
    print("Example 3: if True with extra print")
    if True:
        print("Data science")
    print("bye for now")
    print("-" * 30)


if __name__ == "__main__":
    print("Python If-Indentation Demonstration\n")
    example_one()
    example_two()
    example_three()

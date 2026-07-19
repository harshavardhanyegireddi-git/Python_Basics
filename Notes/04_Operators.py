"""
=========================================================
Topic      : Operators in Python
File       : 04_Operators.py
=========================================================

What are Operators?
-------------------
Operators are special symbols used to perform operations
on variables and values.

Types of Operators:
1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators
"""

print("=" * 50)
print("OPERATORS IN PYTHON")
print("=" * 50)

# ======================================================
# Example 1 : Arithmetic Operators
# ======================================================

a = 20
b = 10

print("Arithmetic Operators")
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponent       :", a ** b)

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Comparison Operators
# ======================================================

x = 15
y = 20

print("Comparison Operators")
print("x == y :", x == y)           # x is equal to y.
print("x != y :", x != y)           # x is not equal to y.
print("x > y  :", x > y)            # x is greater than y.
print("x < y  :", x < y)            # x is less than y.
print("x >= y :", x >= y)           # x greater than or equal to y.
print("x <= y :", x <= y)           # x less than or equal to y.

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Assignment Operators
# ======================================================

num = 10

print("Assignment Operators")

num += 5
print("num += 5 :", num)

num -= 2
print("num -= 2 :", num)

num *= 3
print("num *= 3 :", num)

num //= 2
print("num //= 2:", num)

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Logical Operators
# ======================================================

a = True
b = False

print("Logical Operators")
print("a and b :", a and b)
print("a or b  :", a or b)
print("not a   :", not a)

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Membership Operators
# ======================================================

languages = ["Python", "Java", "C"]

print("Membership Operators")
print("'Python' in languages      :", "Python" in languages)
print("'JavaScript' in languages  :", "JavaScript" in languages)
print("'Java' not in languages    :", "Java" not in languages)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Identity Operators
# ======================================================

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("Identity Operators")
print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 == list3     :", list1 == list3)

print("\n" + "=" * 50)

# ======================================================
# Practice Questions
# ======================================================

# 1. Perform all arithmetic operations on two numbers.
#
# 2. Compare two numbers using all comparison operators.
#
# 3. Use +=, -=, *= and //= operators.
#
# 4. Check whether both conditions are True using logical operators.
#
# 5. Check whether "Python" exists in a list.
#
# 6. Compare two lists using is and ==.

print("\n" + "=" * 50)

# ======================================================
# Mini Challenge
# ======================================================

# Student Marks Calculator
#
# Take marks of two subjects as input.
#
# Display:
# - Addition
# - Difference
# - Multiplication
# - Division
#
# Compare the marks using comparison operators.
#
# Check whether both marks are greater than or equal to 35.
#
# Print whether the student passed both subjects.
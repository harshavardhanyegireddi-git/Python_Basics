"""
=========================================================
Topic : Modules
=========================================================

What are Modules?
-----------------
A module is a Python file that contains functions,
variables, or classes that can be reused in
other Python programs.

Python provides:
1. Built-in Modules
2. User-Defined Modules

Common built-in modules:
- math
- random
"""

print("=" * 50)
print("MODULES")
print("=" * 50)

# ======================================================
# Example 1 : Importing a Module
# ======================================================

# Imports the math module.
import math

# Returns the square root.
print("Square Root of 25 :", math.sqrt(25))

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Using math Module
# ======================================================

print("Value of Pi :", math.pi)

print("Power :", math.pow(2, 5))

print("Ceiling :", math.ceil(5.2))

print("Floor :", math.floor(5.8))

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Importing Specific Functions
# ======================================================

from math import sqrt, factorial

# Uses imported functions directly.
print("Square Root :", sqrt(64))

print("Factorial :", factorial(5))

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Using Alias
# ======================================================

import math as m

# Uses alias instead of module name.
print("Square Root :", m.sqrt(81))

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Random Module
# ======================================================

import random

# Generates a random integer.
print("Random Number :", random.randint(1, 100))

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Random Choice
# ======================================================

colors = ["Red", "Green", "Blue", "Yellow"]

# Selects a random element.
print("Random Color :", random.choice(colors))

print("\n" + "=" * 50)

# ======================================================
# Example 7 : User-Defined Module
# ======================================================

"""
Suppose there is another file named:

calculator.py

def add(a, b):
    return a + b

Then you can use:

import calculator

print(calculator.add(10, 20))
"""

print("User-defined modules help reuse code.")

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. A module is a Python file.

2. Modules help reuse code.

3. import imports an entire module.

4. from imports specific functions.

5. as creates an alias.

6. math is used for mathematical operations.

7. random is used to generate random values.

8. User-defined modules are Python files
   created by programmers.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Import the math module.
#
# 2. Print the value of pi.
#
# 3. Find the square root of 100.
#
# 4. Find 3 raised to the power of 4.
#
# 5. Import sqrt() directly.
#
# 6. Import math as m.
#
# 7. Generate a random number between 1 and 50.
#
# 8. Select a random fruit from a list.


# ======================================================
# Mini Challenge
# ======================================================

# Lucky Number Generator
#
# Take the student's name as input.
#
# Generate:
# - A lucky number between 1 and 100.
# - A lucky color from a list.
#
# Display:
#
# Student Name
# Lucky Number
# Lucky Color
#
# Hint:
# Use:
# import random
# random.randint()
# random.choice()
"""
=========================================================
Topic      : Input and Output
File       : 03_Input_Output.py
=========================================================

What is Input?
--------------
Input is the data entered by the user during program execution.

What is Output?
---------------
Output is the result displayed to the user.

Real-Life Example:
------------------
ATM Machine
Input  -> Enter PIN
Output -> Account Details
"""

print("=" * 50)
print("INPUT AND OUTPUT IN PYTHON")
print("=" * 50)

# ======================================================
# Example 1 : Simple Output
# ======================================================

print("Hello, World!")

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Printing Variables
# ======================================================

name = "Harsha"
age = 18

print("Name :", name)
print("Age :", age)

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Taking String Input
# ======================================================

name = input("Enter your name: ")

print("Welcome", name)

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Taking Integer Input
# ======================================================

age = int(input("Enter your age: "))

print("Your age is", age)

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Taking Float Input
# ======================================================

height = float(input("Enter your height: "))

print("Your height is", height)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Multiple Inputs
# ======================================================

name = input("Enter your name: ")
city = input("Enter your city: ")

print(name, "lives in", city)

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Input + Calculation
# ======================================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)

print("\n" + "=" * 50)

# ======================================================
# Example 8 : Formatted Output
# ======================================================

name = "Harsha"
college = "NIAT"

print(f"My name is {name}")
print(f"I study at {college}")

print("\n" + "=" * 50)

# ======================================================
# Practice Questions
# ======================================================

# 1. Take your name as input and print a welcome message.
#
# 2. Take your age as input and print it.
#
# 3. Take two numbers and print their sum.
#
# 4. Take your city and state as input and print them.
#
# 5. Take your height as input and print it.
#
# 6. Take your favourite programming language and print it.


# ======================================================
# Mini Challenge
# ======================================================

# Create a Student Information Form.
#
# Take input for:
# - Name
# - Age
# - College
# - Branch
# - City
#
# Display the information in a neat format.

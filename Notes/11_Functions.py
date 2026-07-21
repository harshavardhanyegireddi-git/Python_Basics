"""
=========================================================
Topic : Functions
=========================================================

What are Functions?
-------------------
A function is a reusable block of code that performs
a specific task.

Functions help us:
- Avoid writing the same code multiple times.
- Make programs easier to read.
- Make programs easier to maintain.

Syntax:

def function_name():
    # Code
"""

print("=" * 50)
print("FUNCTIONS")
print("=" * 50)

# ======================================================
# Example 1 : Creating and Calling a Function
# ======================================================

def greet():
    # Prints a welcome message.
    print("Welcome to Python!")

greet()                          # Calls the function.

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Function with One Parameter
# ======================================================

def greet_user(name):
    # Prints a greeting using the given name.
    print("Hello,", name)

greet_user("Harsha")             # Passes "Harsha" as an argument.

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Function with Multiple Parameters
# ======================================================

def student(name, branch):
    # Displays student details.
    print("Name   :", name)
    print("Branch :", branch)

student("Harsha", "CSE (AI & ML)")      # Passes two arguments.

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Function Returning a Value
# ======================================================

def add(a, b):
    # Returns the sum of two numbers.
    return a + b

result = add(10, 20)             # Stores the returned value.

print("Sum:", result)

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Function with Default Parameter
# ======================================================

def country(name="India"):
    # Uses "India" if no argument is provided.
    print("Country:", name)

country()                         # Uses the default value.
country("USA")                    # Overrides the default value.

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Function Returning Multiple Values
# ======================================================

def calculate(a, b):
    # Returns addition and multiplication.
    return a + b, a * b

addition, multiplication = calculate(5, 4)

print("Addition       :", addition)
print("Multiplication :", multiplication)

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Calling One Function Inside Another
# ======================================================

def line():
    # Prints a separator line.
    print("=" * 30)

def welcome():
    # Calls another function.
    line()
    print("Welcome to Python Functions")
    line()

welcome()

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. A function is created using the def keyword.

2. A function runs only when it is called.

3. Parameters receive values passed to the function.

4. A function can return one or more values.

5. Functions improve code reusability.

6. Functions make programs easier to read and maintain.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Create a function that prints your name.
#
# 2. Create a function that greets a user.
#
# 3. Create a function that adds two numbers.
#
# 4. Create a function that returns the square of a number.
#
# 5. Create a function that prints a multiplication table.
#
# 6. Create a function with a default parameter.
#
# 7. Create a function that returns two values.
#
# 8. Create one function that calls another function.


# ======================================================
# Mini Challenge
# ======================================================

# Student Result Calculator
#
# Create a function named calculate_result().
#
# The function should:
# - Take the student's name.
# - Take marks of three subjects.
# - Calculate the total marks.
# - Calculate the average marks.
# - Print whether the student passed.
#
# A student passes only if all subject marks
# are greater than or equal to 35.
#
# Hint:
# Use functions, parameters, return statement,
# and if-else conditions.
"""
=========================================================
Topic : Exceptions
=========================================================

What are Exceptions?
--------------------
An exception is an error that occurs during the
execution of a program.

Python provides exception handling to prevent
the program from crashing.

Keywords used:
- try
- except
- else
- finally
"""

print("=" * 50)
print("EXCEPTIONS")
print("=" * 50)

# ======================================================
# Example 1 : Exception Without Handling
# ======================================================

# This code will cause an error.
# Uncomment it to see the exception.

# number = 10 / 0

print("Division by zero causes an exception.")

print("\n" + "=" * 50)

# ======================================================
# Example 2 : try and except
# ======================================================

try:

    number = 10 / 0

except ZeroDivisionError:

    # Executes if ZeroDivisionError occurs.
    print("Cannot divide a number by zero.")

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Handling ValueError
# ======================================================

try:

    age = int(input("Enter Your Age : "))

    print("Age :", age)

except ValueError:

    # Executes if the user enters invalid data.
    print("Please enter a valid integer.")

print("\n" + "=" * 50)

# ======================================================
# Example 4 : try, except and else
# ======================================================

try:

    number = int(input("Enter a Number : "))

except ValueError:

    print("Invalid Input.")

else:

    # Executes only if no exception occurs.
    print("You Entered :", number)

print("\n" + "=" * 50)

# ======================================================
# Example 5 : try, except and finally
# ======================================================

try:

    result = 20 / 2

    print("Result :", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    # Executes whether an exception occurs or not.
    print("Program Finished.")

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Multiple Exceptions
# ======================================================

try:

    number = int(input("Enter a Number : "))

    result = 100 / number

    print("Result :", result)

except ValueError:

    print("Please enter a valid integer.")

except ZeroDivisionError:

    print("Division by zero is not allowed.")

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Raising an Exception
# ======================================================

age = -5

try:

    if age < 0:

        raise ValueError("Age cannot be negative.")

except ValueError as error:

    print(error)

print("\n" + "=" * 50)

# ======================================================
# Example 8 : Exception Object
# ======================================================

try:

    number = int(input("Enter a Number : "))

except ValueError as error:

    # Prints the exception message.
    print("Error :", error)

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. Exceptions are runtime errors.

2. try contains the risky code.

3. except handles the exception.

4. else executes only if no exception occurs.

5. finally always executes.

6. A program does not crash if an exception
   is handled properly.

7. raise is used to create custom exceptions.

8. Exception objects provide error details.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Handle ZeroDivisionError.
#
# 2. Handle ValueError while taking integer input.
#
# 3. Use try, except and else.
#
# 4. Use try, except and finally.
#
# 5. Handle multiple exceptions.
#
# 6. Raise a ValueError if age is negative.
#
# 7. Print the exception object.
#
# 8. Create your own exception handling example.


# ======================================================
# Mini Challenge
# ======================================================

# Simple Calculator
#
# Take two numbers from the user.
#
# Take an operator (+, -, *, /).
#
# Display the result.
#
# Handle:
# - Division by zero
# - Invalid number input
# - Invalid operator
#
# Hint:
# Use:
# try
# except
# if-elif-else
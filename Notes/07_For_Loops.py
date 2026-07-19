"""
=========================================================
Topic : For Loops
File  : 07_For_Loops.py
=========================================================

What is a For Loop?
-------------------
A for loop is used to repeat a block of code a fixed
number of times or to iterate over a sequence.

Syntax:
for variable in sequence:
    # Code to execute
"""

print("=" * 50)
print("FOR LOOPS")
print("=" * 50)

# ======================================================
# Example 1 : Print Numbers from 1 to 5
# ======================================================

for number in range(1, 6):
    print(number)                    # Prints numbers from 1 to 5.

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Print Your Name 5 Times
# ======================================================

for count in range(5):
    print("Harsha")                  # Prints the name 5 times.

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Print Even Numbers
# ======================================================

for number in range(2, 11, 2):
    print(number)                    # Prints even numbers from 2 to 10.

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Print Odd Numbers
# ======================================================

for number in range(1, 10, 2):
    print(number)                    # Prints odd numbers from 1 to 9.

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Iterate Through a String
# ======================================================

language = "Python"

for letter in language:
    print(letter)                    # Prints one character at a time.

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Iterate Through a List
# ======================================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)                     # Prints each item in the list.

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Calculate the Sum of Numbers
# ======================================================

total = 0

for number in range(1, 6):
    total += number                  # Adds each number to total.

print("Sum:", total)

print("\n" + "=" * 50)

# ======================================================
# Example 8 : Multiplication Table
# ======================================================

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n" + "=" * 50)

# ======================================================
# Practice Questions
# ======================================================

# 1. Print numbers from 1 to 10.
#
# 2. Print numbers from 10 to 1.
#
# 3. Print even numbers from 2 to 20.
#
# 4. Print odd numbers from 1 to 19.
#
# 5. Print your name 10 times.
#
# 6. Print each character of your name.
#
# 7. Find the sum of numbers from 1 to 100.
#
# 8. Print the multiplication table of any number.


# ======================================================
# Mini Challenge
# ======================================================

# Number Statistics
#
# Take a number as input.
#
# Print:
# - Numbers from 1 to the given number.
# - Sum of all numbers.
# - Even numbers.
# - Odd numbers.
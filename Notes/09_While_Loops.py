"""
=========================================================
Topic : While Loops
=========================================================

What is a While Loop?
---------------------
A while loop repeatedly executes a block of code
as long as the given condition is True.

Syntax:

while condition:
    # Code to execute

The condition is checked before every iteration.
If the condition becomes False, the loop stops.
"""

print("=" * 50)
print("WHILE LOOPS")
print("=" * 50)

# ======================================================
# Example 1 : Print Numbers from 1 to 5
# ======================================================

count = 1

while count <= 5:
    print(count)                    # Prints numbers from 1 to 5.
    count += 1                      # Increases the value by 1.

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Print Even Numbers
# ======================================================

number = 2

while number <= 10:
    print(number)                   # Prints even numbers from 2 to 10.
    number += 2                     # Increases the value by 2.

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Print Odd Numbers
# ======================================================

number = 1

while number <= 9:
    print(number)                   # Prints odd numbers from 1 to 9.
    number += 2                     # Increases the value by 2.

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Countdown
# ======================================================

count = 5

while count >= 1:
    print(count)                    # Prints numbers from 5 to 1.
    count -= 1                      # Decreases the value by 1.

print("Blast Off!")

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Multiplication Table
# ======================================================

number = 5
count = 1

while count <= 10:
    print(f"{number} x {count} = {number * count}")
    count += 1

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Sum of Numbers
# ======================================================

count = 1
total = 0

while count <= 5:
    total += count                  # Adds the current number to total.
    count += 1

print("Sum:", total)

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Infinite Loop (Commented)
# ======================================================

# while True:
#     print("This loop runs forever.")

print("Infinite loop example is commented.")

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. A while loop executes as long as the condition is True.

2. Always update the loop variable inside the loop.

3. If the loop variable is not updated,
   the loop may run forever (Infinite Loop).

4. Use a while loop when the number of
   iterations is not known in advance.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Print numbers from 1 to 20.
#
# 2. Print numbers from 20 to 1.
#
# 3. Print even numbers from 2 to 20.
#
# 4. Print odd numbers from 1 to 19.
#
# 5. Print the multiplication table of any number.
#
# 6. Find the sum of numbers from 1 to 100.
#
# 7. Print numbers divisible by 5 from 1 to 50.
#
# 8. Print the square of numbers from 1 to 10.


# ======================================================
# Mini Challenge
# ======================================================

# Password Verification System
#
# Correct Password:
# python123
#
# Ask the user to enter the password.
#
# Keep asking until the correct password is entered.
#
# If the password is correct:
#     Print "Access Granted!"
#
# Hint:
# Use a while loop.
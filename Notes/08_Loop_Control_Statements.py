"""
=========================================================
Topic : Loop Control Statements
File : 08_Loop_Control_Statements.py
=========================================================

What are Loop Control Statements?
---------------------------------
Loop control statements are used to control the flow of
execution inside a loop.

Types of Loop Control Statements:
1. break    - Terminates the loop immediately.
2. continue - Skips the current iteration and moves to
              the next iteration.
3. pass     - Does nothing. It acts as a placeholder.
"""
   
print("=" * 50)
print("LOOP CONTROL STATEMENTS")
print("=" * 50)

# ======================================================
# Example 1 : break Statement
# ======================================================

print("Break Statement")

for number in range(1, 11):

    if number == 6:
        break                      # Terminates the loop when number becomes 6.

    print(number)

print("\n" + "=" * 50)

# ======================================================
# Example 2 : continue Statement
# ======================================================

print("Continue Statement")

for number in range(1, 11):

    if number == 6:
        continue                   # Skips printing the number 6.

    print(number)

print("\n" + "=" * 50)

# ======================================================
# Example 3 : pass Statement
# ======================================================

print("Pass Statement")

for number in range(1, 6):

    if number == 3:
        pass                       # Does nothing.

    print(number)

print("\n" + "=" * 50)

# ======================================================
# Example 4 : break with while Loop
# ======================================================

print("Break with While Loop")

count = 1

while True:

    if count == 6:
        break                      # Stops the infinite loop.

    print(count)
    count += 1

print("\n" + "=" * 50)

# ======================================================
# Example 5 : continue with while Loop
# ======================================================

print("Continue with While Loop")

count = 0

while count < 10:

    count += 1

    if count == 5:
        continue                   # Skips printing 5.

    print(count)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : pass inside if Statement
# ======================================================

print("Pass inside If Statement")

marks = 75

if marks >= 35:
    pass                           # Placeholder for future code.

print("Student Passed")

print("\n" + "=" * 50)

# ======================================================
# Practice Questions
# ======================================================

# 1. Print numbers from 1 to 20.
#    Stop the loop when the number becomes 12.
#
# 2. Print numbers from 1 to 20.
#    Skip printing the number 10.
#
# 3. Print only odd numbers using continue.
#
# 4. Use break to stop an infinite while loop.
#
# 5. Use continue in a while loop to skip multiples of 3.
#
# 6. Create an empty if block using pass.
#
# 7. Print numbers from 1 to 50.
#    Stop when the number becomes divisible by 17.
#
# 8. Skip all even numbers between 1 and 20.


# ======================================================
# Mini Challenge
# ======================================================

# Guess the Secret Number
#
# Secret Number = 7
#
# Ask the user to guess the secret number continuously.
#
# If the guess is correct:
#     Print "Congratulations! You guessed it."
#     Stop the loop using break.
#
# If the guess is incorrect:
#     Print "Wrong Guess! Try Again."
#
# If the user enters 0:
#     Print "Game Exited."
#     Stop the loop.
"""
=========================================================
Topic : If Else Statements
File : 06_If_Else.py
=========================================================

What is If Else?
----------------
If Else statements are used to make decisions in a program.

Python checks a condition.
- If the condition is True, the 'if' block executes.
- Otherwise, the 'else' block executes.

Keywords:
- if
- elif
- else
"""

print("=" * 50)
print("IF ELSE STATEMENTS")
print("=" * 50)

# ======================================================
# Example 1 : Simple If Statement
# ======================================================

age = 18

if age >= 18:
    print("You are eligible to vote.")    # Executes only if the condition is True.

print("\n" + "=" * 50)

# ======================================================
# Example 2 : If Else Statement
# ======================================================

marks = 32

if marks >= 35:
    print("Pass")                         # Executes when marks are 35 or above.
else:
    print("Fail")                         # Executes when marks are below 35.

print("\n" + "=" * 50)

# ======================================================
# Example 3 : If Elif Else Statement
# ======================================================

score = 87

if score >= 90:
    print("Grade A")                      # Highest grade.
elif score >= 75:
    print("Grade B")                      # Second highest grade.
elif score >= 50:
    print("Grade C")                      # Passing grade.
else:
    print("Grade F")                      # Failing grade.

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Check Even or Odd
# ======================================================

number = 15

if number % 2 == 0:
    print(number, "is Even")              # Even numbers are divisible by 2.
else:
    print(number, "is Odd")               # Odd numbers are not divisible by 2.

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Check Positive, Negative or Zero
# ======================================================

num = -10

if num > 0:
    print("Positive Number")              # Number is greater than zero.
elif num < 0:
    print("Negative Number")              # Number is less than zero.
else:
    print("Zero")                         # Number is exactly zero.

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Largest of Two Numbers
# ======================================================

a = 45
b = 80

if a > b:
    print(a, "is greater")                # Prints 'a' if it is larger.
else:
    print(b, "is greater")                # Prints 'b' if it is larger or equal.

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Check Leap Year
# ======================================================

year = 2024

# A leap year is divisible by 4,
# but not divisible by 100,
# unless it is also divisible by 400.

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

print("\n" + "=" * 50)

# ======================================================
# Practice Questions
# ======================================================

# 1. Check whether a person is eligible to vote.
#
# 2. Check whether a number is positive,
#    negative or zero.
#
# 3. Check whether a number is even or odd.
#
# 4. Find the largest of two numbers.
#
# 5. Find the largest of three numbers.
#
# 6. Check whether a student passed or failed.
#
# 7. Print the grade based on marks.
#
# 8. Check whether a year is a leap year.


# ======================================================
# Mini Challenge
# ======================================================

# ATM Withdrawal System
#
# Take the account balance as input.
# Take the withdrawal amount as input.
#
# If the withdrawal amount is less than or equal
# to the balance:
#     Print "Transaction Successful"
#     Print the remaining balance.
#
# Otherwise:
#     Print "Insufficient Balance"
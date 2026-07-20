"""
=========================================================
Topic : Nested Loops
File : 10_Nested_Loops.py
=========================================================

What are Nested Loops?
----------------------
A nested loop is a loop inside another loop.

The inner loop executes completely for every
iteration of the outer loop.

Nested loops are commonly used for:
- Printing patterns
- Working with tables
- Traversing matrices
- Comparing data

Syntax:

for variable1 in sequence:
    for variable2 in sequence:
        # Code to execute
"""

print("=" * 50)
print("NESTED LOOPS")
print("=" * 50)

# ======================================================
# Example 1 : Simple Nested Loop
# ======================================================

for row in range(1, 4):                 # Outer loop controls the rows.
    for column in range(1, 4):          # Inner loop controls the columns.
        print(f"Row {row} Column {column}")

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Square Star Pattern
# ======================================================

for row in range(4):                    # Executes 4 rows.
    for column in range(4):             # Prints 4 stars in each row.
        print("*", end=" ")
    print()                             # Moves to the next line.

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Right Triangle Pattern
# ======================================================

for row in range(1, 6):                 # Controls the number of rows.
    for column in range(row):           # Prints stars equal to the current row.
        print("*", end=" ")
    print()                             # Moves to the next line.

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Number Pattern
# ======================================================

for row in range(1, 6):                 # Controls the number of rows.
    for column in range(1, row + 1):    # Prints numbers from 1 to the current row.
        print(column, end=" ")
    print()                             # Moves to the next line.

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Multiplication Tables
# ======================================================

for table in range(1, 4):               # Prints tables from 1 to 3.

    print(f"\nMultiplication Table of {table}")

    for number in range(1, 11):         # Prints multiplication from 1 to 10.
        print(f"{table} x {number} = {table * number}")

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Alphabet Pattern
# ======================================================

for row in range(5):                    # Controls the number of rows.
    for column in range(row + 1):       # Prints 'A' based on the current row.
        print("A", end=" ")
    print()                             # Moves to the next line.

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Rectangle of Numbers
# ======================================================

for row in range(3):                    # Executes 3 rows.
    for column in range(5):             # Prints numbers from 1 to 5.
        print(column + 1, end=" ")
    print()                             # Moves to the next line.

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. A nested loop is a loop inside another loop.

2. The inner loop completes all its iterations
   before the outer loop moves to the next iteration.

3. Nested loops are commonly used for
   printing patterns.

4. They are useful for working with
   tables, matrices and two-dimensional data.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Print a 5 × 5 star square.
#
# 2. Print a right triangle using stars.
#
# 3. Print an inverted triangle using stars.
#
# 4. Print a number triangle.
#
# 5. Print multiplication tables from 1 to 5.
#
# 6. Print a rectangle of numbers.
#
# 7. Print a rectangle of alphabets.
#
# 8. Print the following pattern:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# ======================================================
# Mini Challenge
# ======================================================

# Pattern Generator
#
# Take the number of rows as input.
#
# Print the following pattern:
#
# Example:
#
# Enter rows: 5
#
# *
# * *
# * * *
# * * * *
# * * * * *
#
# Hint:
# Use nested for loops.
"""
=========================================================
Topic : Tuples
=========================================================

What are Tuples?
----------------
A tuple is a collection of multiple items stored
in a single variable.

Tuples are:
- Ordered
- Immutable (cannot be modified after creation)
- Allow duplicate values
- Can store different data types

Syntax:

tuple_name = (item1, item2, item3)
"""

print("=" * 50)
print("TUPLES")
print("=" * 50)

# ======================================================
# Example 1 : Creating a Tuple
# ======================================================

fruits = ("Apple", "Banana", "Mango")

# Prints the entire tuple.
print("Fruits :", fruits)

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Accessing Tuple Elements
# ======================================================

languages = ("Python", "Java", "C++", "JavaScript")

# Accesses the first element.
print("First Language :", languages[0])

# Accesses the second element.
print("Second Language:", languages[1])

# Accesses the last element.
print("Last Language  :", languages[-1])

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Tuple Slicing
# ======================================================

numbers = (10, 20, 30, 40, 50)

# Prints elements from index 1 to 3.
print(numbers[1:4])

# Prints the first three elements.
print(numbers[:3])

# Prints elements from index 2 to the end.
print(numbers[2:])

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Tuple Length
# ======================================================

students = ("Harsha", "Rahul", "Priya")

# Returns the number of elements.
print("Length :", len(students))

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Checking an Element
# ======================================================

languages = ("Python", "Java", "C++")

# Checks whether "Python" exists in the tuple.
print("Python in Tuple :", "Python" in languages)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Looping Through a Tuple
# ======================================================

subjects = ("Python", "Maths", "Physics")

# Prints every element in the tuple.
for subject in subjects:
    print(subject)

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Counting Elements
# ======================================================

numbers = (10, 20, 10, 30, 10)

# Counts how many times 10 appears.
print("Count of 10 :", numbers.count(10))

print("\n" + "=" * 50)

# ======================================================
# Example 8 : Finding an Element
# ======================================================

fruits = ("Apple", "Banana", "Mango")

# Returns the index of "Banana".
print("Index of Banana :", fruits.index("Banana"))

print("\n" + "=" * 50)

# ======================================================
# Example 9 : Tuple Packing
# ======================================================

# Stores multiple values in one tuple.
student = ("Harsha", 18, "Python")

print(student)

print("\n" + "=" * 50)

# ======================================================
# Example 10 : Tuple Unpacking
# ======================================================

student = ("Harsha", 18, "Python")

# Stores each tuple value into separate variables.
name, age, course = student

print("Name   :", name)
print("Age    :", age)
print("Course :", course)

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. Tuples store multiple values.

2. Tuples are ordered.

3. Tuples are immutable.
   Their elements cannot be changed.

4. Tuples allow duplicate values.

5. Indexing starts from 0.

6. Slicing works the same as lists.

7. count() returns the number of occurrences
   of an element.

8. index() returns the position of an element.

9. Tuple packing stores multiple values.

10. Tuple unpacking separates tuple values
    into individual variables.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Create a tuple of five fruits.
#
# 2. Print the first and last element.
#
# 3. Print the length of a tuple.
#
# 4. Check whether "Python" exists in a tuple.
#
# 5. Print all elements using a for loop.
#
# 6. Count how many times a number appears.
#
# 7. Find the index of an element.
#
# 8. Create a tuple with different data types.
#
# 9. Perform tuple unpacking.
#
# 10. Slice a tuple.


# ======================================================
# Mini Challenge
# ======================================================

# Student Information System
#
# Create a tuple containing:
# - Student Name
# - Age
# - Branch
# - CGPA
#
# Display:
# - Complete Tuple
# - Student Name
# - Branch
# - Length of the Tuple
#
# Then unpack the tuple into
# separate variables and print them.
#
# Hint:
# Use indexing, len(), and tuple unpacking.
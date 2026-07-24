"""
=========================================================
Topic : Dictionaries
=========================================================

What are Dictionaries?
----------------------
A dictionary is a collection of key-value pairs.

Dictionaries are:
- Ordered
- Mutable (can be modified)
- Keys are unique
- Values can be duplicated
- Store different data types

Syntax:

dictionary_name = {
    "key1": value1,
    "key2": value2
}
"""

print("=" * 50)
print("DICTIONARIES")
print("=" * 50)

# ======================================================
# Example 1 : Creating a Dictionary
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Prints the complete dictionary.
print("Student :", student)

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Accessing Values
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Accesses values using keys.
print("Name   :", student["Name"])
print("Age    :", student["Age"])

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Using get()
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18
}

# Returns the value of the key.
print(student.get("Name"))

# Returns None because the key does not exist.
print(student.get("City"))

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Modifying Values
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18
}

# Changes the value of Age.
student["Age"] = 19

print(student)

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Adding a New Key
# ======================================================

student = {
    "Name": "Harsha"
}

# Adds a new key-value pair.
student["College"] = "NRI University"

print(student)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Removing an Item
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Removes the specified key.
student.pop("Age")

print(student)

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Dictionary Length
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Returns the number of key-value pairs.
print("Length :", len(student))

print("\n" + "=" * 50)

# ======================================================
# Example 8 : Looping Through Keys
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Prints all keys.
for key in student:
    print(key)

print("\n" + "=" * 50)

# ======================================================
# Example 9 : Looping Through Values
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Prints all values.
for value in student.values():
    print(value)

print("\n" + "=" * 50)

# ======================================================
# Example 10 : Looping Through Items
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Prints keys and values.
for key, value in student.items():
    print(key, ":", value)

print("\n" + "=" * 50)

# ======================================================
# Example 11 : Dictionary Keys
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "Branch": "CSE"
}

# Returns all keys.
print(student.keys())

print("\n" + "=" * 50)

# ======================================================
# Example 12 : Dictionary Values
# ======================================================

# Returns all values.
print(student.values())

print("\n" + "=" * 50)

# ======================================================
# Example 13 : Dictionary Items
# ======================================================

# Returns all key-value pairs.
print(student.items())

print("\n" + "=" * 50)

# ======================================================
# Example 14 : Clearing a Dictionary
# ======================================================

student.clear()

# Removes all key-value pairs.
print(student)

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. Dictionaries store data as key-value pairs.

2. Keys must be unique.

3. Values can be duplicated.

4. Dictionaries are mutable.

5. Values are accessed using keys.

6. get() safely returns a value.

7. pop() removes a key-value pair.

8. keys() returns all keys.

9. values() returns all values.

10. items() returns key-value pairs.

11. clear() removes all items.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Create a dictionary for a student.
#
# 2. Print the student's name.
#
# 3. Change the student's age.
#
# 4. Add a new key called "City".
#
# 5. Remove one key using pop().
#
# 6. Print all keys.
#
# 7. Print all values.
#
# 8. Print all key-value pairs.
#
# 9. Print the length of the dictionary.
#
# 10. Clear the dictionary.


# ======================================================
# Mini Challenge
# ======================================================

# Student Information Manager
#
# Take input for:
# - Name
# - Age
# - Branch
# - CGPA
#
# Store the data in a dictionary.
#
# Display:
# - Complete Dictionary
# - Student Name
# - Branch
# - All Keys
# - All Values
# - Total Number of Entries
#
# Hint:
# Use:
# get()
# keys()
# values()
# len()
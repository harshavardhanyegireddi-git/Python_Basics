"""
=========================================================
Topic : Lists
=========================================================

What are Lists?
---------------
A list is a collection of multiple items stored
in a single variable.

Lists are:
- Ordered
- Mutable (can be modified)
- Allow duplicate values
- Can store different data types

Syntax:

list_name = [item1, item2, item3]
"""

print("=" * 50)
print("LISTS")
print("=" * 50)

# ======================================================
# Example 1 : Creating a List
# ======================================================

fruits = ["Apple", "Banana", "Mango"]

# Prints the entire list.
print("Fruits :", fruits)

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Accessing List Elements
# ======================================================

languages = ["Python", "Java", "C++", "JavaScript"]

# Accesses the first element.
print("First Language :", languages[0])

# Accesses the second element.
print("Second Language:", languages[1])

# Accesses the last element.
print("Last Language  :", languages[-1])

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Modifying a List
# ======================================================

colors = ["Red", "Green", "Blue"]

# Changes the second element.
colors[1] = "Yellow"

print("Modified List :", colors)

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Adding Elements
# ======================================================

numbers = [10, 20, 30]

# Adds an element at the end of the list.
numbers.append(40)

print("After append() :", numbers)

# Inserts an element at index 1.
numbers.insert(1, 15)

print("After insert() :", numbers)

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Removing Elements
# ======================================================

animals = ["Dog", "Cat", "Rabbit", "Tiger"]

# Removes "Rabbit" from the list.
animals.remove("Rabbit")

print("After remove() :", animals)

# Removes the last element.
animals.pop()

print("After pop()    :", animals)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : List Length
# ======================================================

students = ["Harsha", "Rahul", "Priya"]

# Returns the number of elements.
print("Length :", len(students))

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Checking an Element
# ======================================================

languages = ["Python", "Java", "C++"]

# Checks whether "Python" is present.
print("Python in list :", "Python" in languages)

print("\n" + "=" * 50)

# ======================================================
# Example 8 : List Slicing
# ======================================================

numbers = [10, 20, 30, 40, 50]

# Elements from index 1 to 3.
print(numbers[1:4])

# First three elements.
print(numbers[:3])

# Elements from index 2 to the end.
print(numbers[2:])

print("\n" + "=" * 50)

# ======================================================
# Example 9 : Looping Through a List
# ======================================================

subjects = ["Maths", "Physics", "Python"]

# Prints every element in the list.
for subject in subjects:
    print(subject)

print("\n" + "=" * 50)

# ======================================================
# Example 10 : Sorting a List
# ======================================================

marks = [85, 72, 95, 60]

# Sorts the list in ascending order.
marks.sort()

print("Sorted Marks :", marks)

print("\n" + "=" * 50)

# ======================================================
# Example 11 : Reversing a List
# ======================================================

numbers = [1, 2, 3, 4, 5]

# Reverses the order of elements.
numbers.reverse()

print("Reversed List :", numbers)

print("\n" + "=" * 50)

# ======================================================
# Example 12 : Clearing a List
# ======================================================

cities = ["Delhi", "Mumbai", "Hyderabad"]

# Removes all elements from the list.
cities.clear()

print("After clear() :", cities)

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. Lists store multiple values in one variable.

2. Lists are ordered.

3. Lists are mutable, so elements can be changed.

4. Lists allow duplicate values.

5. Lists can contain different data types.

6. append() adds an element at the end.

7. insert() adds an element at a specific position.

8. remove() deletes an element by value.

9. pop() removes an element by index
   (last element by default).

10. sort() arranges elements in ascending order.

11. reverse() reverses the list.

12. clear() removes all elements from the list.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Create a list of five fruits.
#
# 2. Print the first and last element.
#
# 3. Change one element in the list.
#
# 4. Add a new element using append().
#
# 5. Insert an element at index 2.
#
# 6. Remove an element using remove().
#
# 7. Remove the last element using pop().
#
# 8. Print the length of a list.
#
# 9. Check whether "Python" exists in a list.
#
# 10. Sort a list of numbers.
#
# 11. Reverse a list.
#
# 12. Print every element using a for loop.


# ======================================================
# Mini Challenge
# ======================================================

# Student Marks Manager
#
# Create an empty list named marks.
#
# Take marks of five subjects from the user
# and store them in the list.
#
# Display:
# - All Marks
# - Highest Mark
# - Lowest Mark
# - Total Marks
# - Average Marks
#
# Hint:
# Use:
# append()
# max()
# min()
# sum()
# len()
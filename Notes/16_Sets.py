"""
=========================================================
Topic : Sets
=========================================================

What are Sets?
--------------
A set is a collection of unique items stored
in a single variable.

Sets are:
- Unordered
- Mutable (can be modified)
- Do not allow duplicate values
- Can store different data types

Syntax:

set_name = {item1, item2, item3}
"""

print("=" * 50)
print("SETS")
print("=" * 50)

# ======================================================
# Example 1 : Creating a Set
# ======================================================

fruits = {"Apple", "Banana", "Mango"}

# Prints the complete set.
print("Fruits :", fruits)

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Duplicate Values
# ======================================================

numbers = {10, 20, 30, 20, 10, 40}

# Duplicate values are automatically removed.
print("Numbers :", numbers)

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Adding an Element
# ======================================================

languages = {"Python", "Java"}

# Adds a new element to the set.
languages.add("C++")

print("After add() :", languages)

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Updating a Set
# ======================================================

colors = {"Red", "Green"}

# Adds multiple elements.
colors.update(["Blue", "Yellow"])

print("After update() :", colors)

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Removing an Element
# ======================================================

animals = {"Dog", "Cat", "Rabbit"}

# Removes "Cat" from the set.
animals.remove("Cat")

print("After remove() :", animals)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Discarding an Element
# ======================================================

cities = {"Delhi", "Mumbai", "Hyderabad"}

# Removes the element if it exists.
cities.discard("Mumbai")

print("After discard() :", cities)

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Length of a Set
# ======================================================

students = {"Harsha", "Rahul", "Priya"}

# Returns the number of elements.
print("Length :", len(students))

print("\n" + "=" * 50)

# ======================================================
# Example 8 : Checking an Element
# ======================================================

languages = {"Python", "Java", "C++"}

# Checks whether "Python" exists.
print("Python in Set :", "Python" in languages)

print("\n" + "=" * 50)

# ======================================================
# Example 9 : Looping Through a Set
# ======================================================

subjects = {"Python", "Maths", "Physics"}

# Prints every element in the set.
for subject in subjects:
    print(subject)

print("\n" + "=" * 50)

# ======================================================
# Example 10 : Set Union
# ======================================================

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Combines both sets and removes duplicates.
print("Union :", set1.union(set2))

print("\n" + "=" * 50)

# ======================================================
# Example 11 : Set Intersection
# ======================================================

# Returns common elements.
print("Intersection :", set1.intersection(set2))

print("\n" + "=" * 50)

# ======================================================
# Example 12 : Set Difference
# ======================================================

# Returns elements present in set1 but not in set2.
print("Difference :", set1.difference(set2))

print("\n" + "=" * 50)

# ======================================================
# Example 13 : Clearing a Set
# ======================================================

countries = {"India", "USA", "Japan"}

# Removes all elements.
countries.clear()

print("After clear() :", countries)

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. Sets store unique values.

2. Sets are unordered.

3. Sets do not allow duplicate values.

4. Sets are mutable.

5. add() adds one element.

6. update() adds multiple elements.

7. remove() deletes an element.
   It raises an error if the element does not exist.

8. discard() deletes an element.
   It does not raise an error if the element does not exist.

9. union() combines two sets.

10. intersection() returns common elements.

11. difference() returns different elements.

12. clear() removes all elements.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Create a set of five fruits.
#
# 2. Create a set with duplicate values.
#
# 3. Add one element using add().
#
# 4. Add multiple elements using update().
#
# 5. Remove an element using remove().
#
# 6. Remove an element using discard().
#
# 7. Print the length of a set.
#
# 8. Check whether "Python" exists in a set.
#
# 9. Print all elements using a for loop.
#
# 10. Find the union of two sets.
#
# 11. Find the intersection of two sets.
#
# 12. Find the difference of two sets.

# ======================================================
# Mini Challenge
# ======================================================

# Student Club Registration
#
# Two clubs organize registrations.
#
# Club A Students:
# Take 5 student names as input.
#
# Club B Students:
# Take another 5 student names as input.
#
# Display:
# - Students registered in Club A
# - Students registered in Club B
# - Students registered in both clubs
# - Students registered in either club
#
# Hint:
# Use:
# add()
# intersection()
# union()
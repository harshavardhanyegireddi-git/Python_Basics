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

print("\n" + "=" * 50)

#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

fruits = {"Mango", "Orange", "Papaya", "Banana", "Apple"}

print("Fruits :", fruits)

print("\n" + "=" * 50)


# ---- 2.Solution ----

numbers = {10, 20, 10, 30, 10}

print("Numbers :", numbers)

print("\n" + "=" * 50)


# ---- 3.Solution ----

names = {"Harsha", "Rahul"}

names.add("Keerthana")

print("After add() :", names)

print("\n" + "=" * 50)


# ---- 4.Solution ----

subjects = {"Python", "Maths"}

subjects.update("C++", "Java")

print("After update() :", subjects)

print("\n" + "=" * 50)


# ---- 5.Solution ----

numbers = {10, 20, 30, 40, 50}

numbers.remove(40)

print("After remove() :", numbers)

print("\n" + "=" * 50)


# ---- 6.Solution ----

animals = {"Cat", "Dog", "Monkey"}

animals.discard("Dog")

print("After discard() :", animals)

print("\n" + "=" * 50)


# ---- 7.Solution ----

numbers = {10, 20, 30, 40, 50}

print("Lnegth of numbers :", len(numbers))

print("\n" + "=" * 50)


# ---- 8.Solution ----

languages = {"Python", "Java", "C++"}

print("Python in Set :", "Python" in languages)

print("\n" + "=" * 50)


# ---- 9.Solution ----

fruits = {"Mango", "Orange", "Papaya", "Banana", "Apple"}

for i in fruits:
    print(i)

print("\n" + "=" * 50)


# ---- 10.Solution ----

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union :", set1.union(set2))

print("\n" + "=" * 50)


# ---- 11.Solution ----

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Intersection :", set1.intersection(set2))

print("\n" + "=" * 50)


# ---- 12.Solution ----

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Intersection :", set1.intersection(set2))

print("\n" + "=" * 50)
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

print("\n" + "=" * 50)

#=============================================
#---------------- Solutions ------------------
#=============================================



# ---- 1.Solution ----

fruits = ["Apple","Papaya","Banana","Mango","Grapes"]

print("Fruits :", fruits)

print("\n" + "=" * 50)


# ---- 2.Solution ---- 

numbers = [1, 2, 3, 4, 5]

print("First Element :", numbers[0])

print("Last Element :", numbers[-1])

print("\n" + "=" * 50)


# ---- 3.Solution ----

animals = ["Tiger", "Lion", "Elephant"]

print("Before Replacing :", animals)

animals[2] = "Monkey"

print("After Replacing :", animals)

print("\n" + "=" * 50)


# ---- 4.Solution ----

nums = [10, 20, 30]

print("Before Adding :", nums)

nums.append(40)

print("After Adding :", nums)

print("\n" + "=" * 50)


# ---- 5.Solution ----

numbers = [10, 20, 30, 40]

print("Before Insert :", numbers)

print("After Insert :", numbers.insert(2, 50))

print("\n" + "=" * 50)


# ---- 6.Solution ----

names = ["Harsha", "Rahul", "Sandeep", "Keerthana"]

print("Before Removing :", names)

names.remove("Sandeep")

print("After Removing :", names)

print("\n" + "=" * 50)


# ---- 7.Solution ----

animals = ["Tiger", "Lion", "Elephant", "Monkey"]

print("Before pop() :", animals)

animals.pop()

print("After pop() :", animals)

print("\n" + "=" * 50)


# ---- 8.Solution ----

names = ["Harsha", "Rahul", "Sandeep", "Keerthana"]

print(len(names))

print("\n" + "=" * 50)
 

# ---- 9.Solution ----

languages = ["Java", "Python", "C++"]

print("Python in languages :","Python" in languages)

names = ["Harsha", "Rahul", "Sandeep", "Keerthana"]

print("\n" + "=" * 50)


# ---- 10.Solution ----

numbers = [85, 70, 62, 92]

numbers.sort()

print("Sorted Numbers :", numbers)

print("\n" + "=" * 50)


# ---- 11.Solution ----

numbers = [10, 20, 30, 40]

numbers.reverse()

print("Reverse Numbers :", numbers)

print("\n" + "=" * 50)


# ---- 12.Solution ----

fruits = ["Apple","Papaya","Banana","Mango","Grapes"]

for i in fruits:
    print(i)

print("\n" + "=" * 50)
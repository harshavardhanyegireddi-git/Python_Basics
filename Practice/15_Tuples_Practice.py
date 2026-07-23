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


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ---- 

fruits = ("Mango", "Orange", "Papaya", "Banana", "Apple")

print(fruits)

print("\n" + "=" * 50)


# ---- 2.Solution ----

numbers = (10, 20, 30, 40)

print("First Element :", numbers[0])

print("\n" + "=" * 50)


# ---- 3.Solution ---- 

fruits = ("Mango", "Orange", "Papaya", "Banana", "Apple")

print("Length :", len(fruits))

print("\n" + "=" * 50)


# ---- 4.Solution ----

languages = ("Python", "Java", "C++")

print("Python in Languages :", "Python" in languages)

print("\n" + "=" * 50)


# ---- 5.Solution ----

students = ("Harsha", "Rahul", "Priya", "Keerthana")

for i in students:
    print(i)

print("\n" + "=" * 50)


# ---- 6.Solution ---- 

numbers = (10, 30, 20, 30, 40)

print("Count of 30 :", numbers.count(30))

print("\n" + "=" * 50)


# ---- 7.Solution ---- 

numbers = (10, 20, 30, 40)

print("Index of 30 :", numbers.index(30))

print("\n" + "=" * 50)


# ---- 8.Solution ---- 

student = ("Harsha", 17, 78.5, True)

print(student)

print("\n" + "=" * 50)


# ---- 9.Solution ----

student = ("Harsha", 17, 78.5, True)

name, age, percentage, is_student = student

print("Name       :", name)
print("Age        :", age)
print("Percentage :", percentage)
print("Is Student :", is_student)

print("\n" + "=" * 50)


# ---- 10.Solution ----

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

print("\n" + "=" * 50)
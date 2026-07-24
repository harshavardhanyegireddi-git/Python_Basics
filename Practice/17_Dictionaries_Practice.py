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

print("\n" + "=" * 50)

#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT",
    "Branch" : "CSE (AI & ML)"
}

print("Student :",student)

print("\n" + "=" * 50)


# ---- 2.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT",
    "Branch" : "CSE (AI & ML)"
}

print("Name :", student["Name"])

print("\n" + "=" * 50)


# ---- 3.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT",
    "Branch" : "CSE (AI & ML)"
}

print("Age :", student["Age"])

print("\n" + "=" * 50)


# ---- 4.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT"
}

student["City"] = "Visakhapatnam"

print("Student :", student)

print("\n" + "=" * 50)


# ---- 5.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT",
}

student.pop("College")

print(student)

print("\n" + "=" * 50)


# ---- 6.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT"
}

print("Keys :", student.keys())

print("\n" + "=" * 50)


# ---- 7.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT"
}

print("Values :", student.values())

print("\n" + "=" * 50)


# ---- 8.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT"
}

print("Student :", student)

print("\n" + "=" * 50)


# ---- 9.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT"
}

print("Length :", len(student))

print("\n" + "=" * 50)


# ---- 10.Solution ----

student = {
    "Name" : "Harsha",
    "Age" : 17,
    "College" : "NIAT"
}

student.clear()

print("Student :", student)

print("\n" + "=" * 50)
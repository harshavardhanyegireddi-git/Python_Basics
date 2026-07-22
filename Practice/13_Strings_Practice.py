# ======================================================
# Practice Questions
# ======================================================

# 1. Create and print a string.
#
# 2. Print the first and last character of a string.
#
# 3. Print the length of a string.
#
# 4. Convert a string to uppercase.
#
# 5. Convert a string to lowercase.
#
# 6. Replace one word with another.
#
# 7. Join two strings together.
#
# 8. Print a string three times.
#
# 9. Use an f-string to print your name and age.
#
# 10. Check whether a string starts with "P".

print("\n" + "=" * 50)

#=============================================
#---------------- Solutions ------------------
#=============================================

# ---- 1.Solution ----

name = "Harsha"

print("Name :",name)

print("\n" + "=" * 50)


# ---- 2.Solution ----

name = "Harsha"

print("First Character :",name[0])

print("Last Character :",name[-1])

print("\n" + "=" * 50)

# ---- 3.Solution ----

college = "NRI University"

length = len(college)

print("Length :",length)

print("\n" + "=" * 50)

# ---- 4.Solution ----

language = "python"

print("Uppercase :",language.upper())

print("\n" + "=" * 50)

# ---- 5.Solution ----

language = "PYTHON"

print("Lowercase :",language.lower())

print("\n" + "=" * 50)

# ---- 6.Solution ----

text = "C++ Programming"

print("Before replacing :",text)

print("After Replacing :",text.replace("C++", "Python"))

print("\n" + "=" * 50)

# ---- 7.Solution ---- 

first_name = "Harsha"
second_name = "Vardhan"

full_name = first_name + " " + second_name

print("Full Name :",full_name)

print("\n" + "=" * 50)

# ---- 8.Solution ----

print("Harsha " * 3)

print("\n" + "=" * 50)


# ---- 9.Solution ----

name = "Harsha"
age = 17

print(f"My name is {name}. I'm {age} years old.")

print("\n" + "=" * 50)

# ---- 10.Solution ----

language = "Python"

print("Language starts with P :",language.startswith("P"))

print("\n" + "=" * 50)

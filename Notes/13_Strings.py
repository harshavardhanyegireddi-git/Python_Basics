"""
=========================================================
Topic : Strings
=========================================================

What are Strings?
-----------------
A string is a sequence of characters enclosed in
single quotes (' '), double quotes (" "), or
triple quotes (''' ''' or \"\"\" \"\"\").

Strings are used to store text data.

Examples:
"Python"
'Hello'
"123"
"""

print("=" * 50)
print("STRINGS")
print("=" * 50)

# ======================================================
# Example 1 : Creating Strings
# ======================================================

name = "Harsha"                 # String using double quotes.
city = 'Vijayawada'             # String using single quotes.

print("Name :", name)
print("City :", city)

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Multiline String
# ======================================================

message = """
Welcome
to
Python
"""

# Prints a multiline string.
print(message)

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Accessing Characters
# ======================================================

language = "Python"

# Index starts from 0.
print("First Character :", language[0])

# Index 1.
print("Second Character:", language[1])

# Last character.
print("Last Character  :", language[-1])

print("\n" + "=" * 50)

# ======================================================
# Example 4 : String Slicing
# ======================================================

text = "Programming"

# Characters from index 0 to 5.
print("0:6  ->", text[0:6])

# Characters from index 3 to end.
print("3:   ->", text[3:])

# Characters from beginning to index 5.
print(":6   ->", text[:6])

print("\n" + "=" * 50)

# ======================================================
# Example 5 : String Length
# ======================================================

course = "Python"

# Returns the number of characters.
print("Length :", len(course))

print("\n" + "=" * 50)

# ======================================================
# Example 6 : String Methods
# ======================================================

text = "python programming"

# Converts to uppercase.
print("Upper      :", text.upper())

# Converts to lowercase.
print("Lower      :", text.lower())

# Capitalizes the first letter.
print("Capitalize :", text.capitalize())

# Replaces one word with another.
print("Replace    :", text.replace("python", "Java"))

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Checking Strings
# ======================================================

message = "Python"

# Checks whether the string starts with "Py".
print("Starts With 'Py' :", message.startswith("Py"))

# Checks whether the string ends with "on".
print("Ends With 'on'   :", message.endswith("on"))

print("\n" + "=" * 50)

# ======================================================
# Example 8 : String Concatenation
# ======================================================

first_name = "Harsha"
last_name = "Vardhan"

# Joins two strings.
full_name = first_name + " " + last_name

print("Full Name :", full_name)

print("\n" + "=" * 50)

# ======================================================
# Example 9 : Repeating Strings
# ======================================================

# Repeats the string three times.
print("Python " * 3)

print("\n" + "=" * 50)

# ======================================================
# Example 10 : f-Strings
# ======================================================

name = "Harsha"
age = 18

# Inserts variables into a string.
print(f"My name is {name} and I am {age} years old.")

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. Strings store text data.

2. Strings are immutable, which means
   they cannot be changed after creation.

3. Indexing starts from 0.

4. Negative indexing starts from -1.

5. Slicing extracts part of a string.

6. Python provides many useful string methods.

7. f-Strings are the preferred way to format strings.
"""

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


# ======================================================
# Mini Challenge
# ======================================================

# Student ID Generator
#
# Take the student's:
# - First Name
# - Last Name
# - Birth Year
#
# Create a Student ID in the following format:
#
# Example:
#
# First Name : Harsha
# Last Name  : Vardhan
# Birth Year : 2008
#
# Student ID : HARVAR2008
#
# Hint:
# - Use string slicing.
# - Use upper().
# - Use string concatenation.
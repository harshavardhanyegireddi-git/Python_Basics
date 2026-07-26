"""
=========================================================
Topic : File Handling
=========================================================

What is File Handling?
----------------------
File handling allows a program to create, read,
write, append, and manage files stored on a computer.

Common File Modes:

"r"  -> Read
"w"  -> Write
"a"  -> Append
"x"  -> Create

Using 'with open()' automatically closes the file.
"""

print("=" * 50)
print("FILE HANDLING")
print("=" * 50)

# ======================================================
# Example 1 : Writing to a File
# ======================================================

# Creates a file if it does not exist.
# Overwrites the file if it already exists.

with open("student.txt", "w") as file:

    file.write("Harsha\n")
    file.write("CSE (AI & ML)\n")
    file.write("NRI University")

print("Data written successfully.")

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Reading a File
# ======================================================

# Opens the file in read mode.

with open("student.txt", "r") as file:

    content = file.read()

print(content)

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Reading Line by Line
# ======================================================

with open("student.txt", "r") as file:

    # Reads one line at a time.
    for line in file:

        print(line.strip())

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Appending Data
# ======================================================

# Adds data at the end of the file.

with open("student.txt", "a") as file:

    file.write("\nPython Developer")

print("Data appended successfully.")

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Reading After Appending
# ======================================================

with open("student.txt", "r") as file:

    print(file.read())

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Creating a New File
# ======================================================

# Creates a new file.
# Raises an error if the file already exists.

try:

    with open("notes.txt", "x") as file:

        file.write("Welcome to Python!")

    print("File created successfully.")

except FileExistsError:

    print("File already exists.")

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Different File Modes
# ======================================================

"""
r -> Read only

w -> Write (Creates a file if it doesn't exist.
             Overwrites existing content.)

a -> Append (Adds data without deleting
             existing content.)

x -> Create (Creates a new file only.)
"""

print("Common File Modes:")
print("r -> Read")
print("w -> Write")
print("a -> Append")
print("x -> Create")

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. open() opens a file.

2. with open() automatically closes the file.

3. read() reads the entire file.

4. write() writes data to a file.

5. append mode (a) adds new data.

6. write mode (w) overwrites old data.

7. create mode (x) creates a new file.

8. File handling is useful for storing
   permanent data.
"""

# ======================================================
# Practice Questions
# ======================================================

# 1. Create a file and write your name.
#
# 2. Read data from a file.
#
# 3. Append your college name.
#
# 4. Read the file line by line.
#
# 5. Create a new file using "x".
#
# 6. Display the difference between
#    "r", "w", "a", and "x".
#
# 7. Write three lines into a file.
#
# 8. Read and print the complete file.


# ======================================================
# Mini Challenge
# ======================================================

# Student Record System
#
# Take the following input:
# - Name
# - Age
# - Branch
#
# Save the data into a file named
# "student_record.txt"
#
# Then read the file and display
# all the stored information.
#
# Hint:
# Use:
# with open()
# write()
# read()
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

print("\n" + "=" * 50)

#=============================================
#---------------- Solutions ------------------
#=============================================

# ---- 1. Solution ----

# Creates a file and writes your name into it.
with open("my_name.txt", "w") as file:

    file.write("Harsha Vardhan")

print("Name written successfully.")

print("\n" + "=" * 50)

# ---- 2. Solution ----

# Reads data from the file.
with open("my_name.txt", "r") as file:

    print(file.read())

print("\n" + "=" * 50)

# ---- 3. Solution ----

# Appends college name to the file.
with open("my_name.txt", "a") as file:

    file.write("\nNRI University")

print("College name appended successfully.")

print("\n" + "=" * 50)

# ---- 4. Solution ----

# Reads the file line by line.
with open("my_name.txt", "r") as file:

    for line in file:

        print(line.strip())

print("\n" + "=" * 50)

# ---- 5. Solution ----

# Creates a new file using "x" mode.
try:

    with open("python_notes.txt", "x") as file:

        file.write("Welcome to Python!")

    print("File created successfully.")

except FileExistsError:

    print("File already exists.")

print("\n" + "=" * 50)

# ---- 6. Solution ----

print("File Modes")
print("r : Read")
print("w : Write")
print("a : Append")
print("x : Create")

print("\n" + "=" * 50)

# ---- 7. Solution ----

# Writes three lines into a file.
with open("student.txt", "w") as file:

    file.write("Name : Harsha\n")
    file.write("Branch : CSE (AI & ML)\n")
    file.write("College : NRI University")

print("Three lines written successfully.")

print("\n" + "=" * 50)

# ---- 8. Solution ----

# Reads and prints the complete file.
with open("student.txt", "r") as file:

    print(file.read())

print("\n" + "=" * 50)


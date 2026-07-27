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


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("          STUDENT RECORD SYSTEM")
print("=" * 50)


name = input("Enter Student Name : ")
age = int(input("Enter Student Age : "))
branch = input("Enter Student Branch : ")


with open("student_record.txt", "w") as file:

    file.write(f"Name   : {name}\n")
    file.write(f"Age    : {age}\n")
    file.write(f"Branch : {branch}")


print("\nStudent record saved successfully.")

print("\n" + "=" * 50)

print("Student Record")

with open("student_record.txt", "r") as file:

    print(file.read())

print("\n" + "=" * 50)
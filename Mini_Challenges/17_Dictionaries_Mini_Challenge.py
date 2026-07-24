# ======================================================
# Mini Challenge
# ======================================================

# Student Information Manager
#
# Take input for:
# - Name
# - Age
# - Branch
# - CGPA
#
# Store the data in a dictionary.
#
# Display:
# - Complete Dictionary
# - Student Name
# - Branch
# - All Keys
# - All Values
# - Total Number of Entries
#
# Hint:
# Use:
# get()
# keys()
# values()
# len()


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("         STUDENT INFORMATION MANAGER")
print("=" * 50)


name = input("\nEnter your name   : ")
age = int(input("Enter your age    : "))
branch = input("Enter your branch : ")
cgpa = float(input("Enter your cgpa   : "))


student = {
    "Name" : name,
    "Age" : age,
    "Branch" : branch,
    "CGPA" : cgpa
}


print("\nStudent       :", student)
print("Name          :", student["Name"])
print("Branch        :", student["Branch"])
print("CGPA          :", student["CGPA"])
print("All Keys      :", student.keys())
print("All Values    :", student.values())
print("Total Entries :", len(student))

print("\n" + "=" * 50)
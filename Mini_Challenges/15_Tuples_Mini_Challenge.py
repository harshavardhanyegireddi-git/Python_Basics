# ======================================================
# Mini Challenge
# ======================================================

# Student Information System
#
# Create a tuple containing:
# - Student Name
# - Age
# - Branch
# - CGPA
#
# Display:
# - Complete Tuple
# - Student Name
# - Branch
# - Length of the Tuple
#
# Then unpack the tuple into
# separate variables and print them.
#
# Hint:
# Use indexing, len(), and tuple unpacking.

# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================

print("=" * 50)
print("        STUDENT INFORMATION SYSTEM")
print("=" * 50)


student = (
    input("Enter Student Name : "),
    int(input("Enter Age          : ")),
    input("Enter Branch       : "),
    float(input("Enter CGPA         : "))
)


print("\nComplete Tuple :", student)
print("Student Name  :", student[0])
print("Branch        :", student[2])


print("Tuple Length  :", len(student))

print("\n" + "=" * 50)


name, age, branch, cgpa = student

print("After Tuple Unpacking")
print("Name   :", name)
print("Age    :", age)
print("Branch :", branch)
print("CGPA   :", cgpa)

print("\n" + "=" * 50)
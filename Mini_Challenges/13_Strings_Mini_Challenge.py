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


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================

print("=" * 50)
print("          STUDENT ID GENERATOR")
print("=" * 50)

first_name = input("Enter First Name : ")
last_name = input("Enter Last Name  : ")
birth_year = input("Enter Birth Year : ")

student_id = (
    first_name[:3].upper()
    + last_name[:3].upper()
    + birth_year
)

print("\nStudent ID :", student_id)

print("\n" + "=" * 50)


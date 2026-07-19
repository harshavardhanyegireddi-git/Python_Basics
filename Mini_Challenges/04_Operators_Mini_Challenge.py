# ======================================================
# Mini Challenge
# ======================================================

# Student Marks Calculator
#
# Take marks of two subjects as input.
#
# Display:
# - Addition
# - Difference
# - Multiplication
# - Division
#
# Compare the marks using comparison operators.
#
# Check whether both marks are greater than or equal to 35.
#
# Print whether the student passed both subjects.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


"""
=========================================
Mini Challenge : Student Marks Calculator
=========================================
"""

# Taking input from the user
subject1 = float(input("Enter Subject 1 Marks: "))
subject2 = float(input("Enter Subject 2 Marks: "))

print("\n" + "=" * 50)
print("          STUDENT MARKS CALCULATOR")
print("=" * 50)

# Arithmetic Operators
print("Addition       :", subject1 + subject2)
print("Difference     :", subject1 - subject2)
print("Multiplication :", subject1 * subject2)
print("Division       :", subject1 / subject2)

print("\n" + "=" * 50)

# Comparison Operators
print("Subject 1 > Subject 2  :", subject1 > subject2)
print("Subject 1 < Subject 2  :", subject1 < subject2)
print("Subject 1 == Subject 2 :", subject1 == subject2)
print("Subject 1 != Subject 2 :", subject1 != subject2)
print("Subject 1 >= Subject 2 :", subject1 >= subject2)
print("Subject 1 <= Subject 2 :", subject1 <= subject2)

print("\n" + "=" * 50)

# Logical Operator
passed = subject1 >= 35 and subject2 >= 35

print("Passed Both Subjects:", passed)
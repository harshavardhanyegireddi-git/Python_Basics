# ======================================================
# Mini Challenge
# ======================================================

# Student Result Calculator
#
# Create a function named calculate_result().
#
# The function should:
# - Take the student's name.
# - Take marks of three subjects.
# - Calculate the total marks.
# - Calculate the average marks.
# - Print whether the student passed.
#
# A student passes only if all subject marks
# are greater than or equal to 35.
#
# Hint:
# Use functions, parameters, return statement,
# and if-else conditions.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


"""
======================================================
Mini Challenge
Topic: Functions
======================================================

Student Grade Calculator

Create a function named calculate_grade().

The function should:
1. Take the student's name.
2. Take marks of three subjects.
3. Calculate the total marks.
4. Calculate the average.
5. Display:
   - Student Name
   - Total Marks
   - Average
   - Result (Pass if average >= 35, otherwise Fail)
"""

# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================

print("=" * 50)
print("          STUDENT GRADE CALCULATOR")
print("=" * 50)


def calculate_grade(name, mark1, mark2, mark3):

    total = mark1 + mark2 + mark3
    average = total / 3

    print("\nStudent Name :", name)
    print("Total Marks  :", total)
    print("Average      :", average)

    if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
        print("Result       : Pass")
    else:
        print("Result       : Fail")


student_name = input("Enter student name : ")
subject1 = float(input("Enter Subject 1 marks : "))
subject2 = float(input("Enter Subject 2 marks : "))
subject3 = float(input("Enter Subject 3 marks : "))


calculate_grade(student_name, subject1, subject2, subject3)

print("\n" + "=" * 50)
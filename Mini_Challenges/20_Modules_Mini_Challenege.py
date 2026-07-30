# ======================================================
# Mini Challenge
# ======================================================

# Lucky Number Generator
#
# Take the student's name as input.
#
# Generate:
# - A lucky number between 1 and 100.
# - A lucky color from a list.
#
# Display:
#
# Student Name
# Lucky Number
# Lucky Color
#
# Hint:
# Use:
# import random
# random.randint()
# random.choice()


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


import random

print("=" * 50)
print("          LUCKY NUMBER GENERATOR")
print("=" * 50)

student_name = input("Enter Student Name : ")

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

lucky_number = random.randint(1, 100)

lucky_color = random.choice(colors)

print("\n" + "=" * 50)

print("Student Name :", student_name)
print("Lucky Number :", lucky_number)
print("Lucky Color  :", lucky_color)

print("\n" + "=" * 50)
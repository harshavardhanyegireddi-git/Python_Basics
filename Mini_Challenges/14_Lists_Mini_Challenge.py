# ======================================================
# Mini Challenge
# ======================================================

# Student Marks Manager
#
# Create an empty list named marks.
#
# Take marks of five subjects from the user
# and store them in the list.
#
# Display:
# - All Marks
# - Highest Mark
# - Lowest Mark
# - Total Marks
# - Average Marks
#
# Hint:
# Use:
# append()
# max()
# min()
# sum()
# len()


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("          STUDENT MARKS MANAGER")
print("=" * 50)

marks = []

subjects = ["Python", "M1", "M2", "Physics", "English"]


for subject in subjects:

    mark = int(input(f"Enter your {subject} marks : "))

    marks.append(mark)


total_marks = sum(marks)

average_marks = total_marks / len(marks)


print("\nAll Marks     :", marks)
print("Highest mark  :", max(marks))
print("Lowest Mark   :", min(marks))
print("Total Marks   :", total_marks)
print("Average Marks :", average_marks, 2)

print("\n" + "=" * 50)
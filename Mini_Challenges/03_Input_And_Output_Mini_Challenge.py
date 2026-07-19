# ======================================================
# Mini Challenge
# ======================================================

# Create a Student Information Form.
#
# Take input for:
# - Name
# - Age
# - College
# - Branch
# - City
#
# Display the information in a neat format.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================

name = input("Enter your name :")
age = int(input("Enter your age :"))
college = input("Enter your collage :")
branch = input("Enter your branch :")
city = input("Enter your city :")

print("\n" + "=" * 40)
print("      STUDENT PROFILE")
print("=" * 40)

print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"College : {college}")
print(f"Branch  : {branch}")
print(f"City    : {city}")

print("=" * 40)
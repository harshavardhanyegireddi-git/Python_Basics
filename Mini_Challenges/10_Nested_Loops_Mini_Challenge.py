# ======================================================
# Mini Challenge
# ======================================================

# Pattern Generator
#
# Take the number of rows as input.
#
# Print the following pattern:
#
# Example:
#
# Enter rows: 5
#
# *
# * *
# * * *
# * * * *
# * * * * *
#
# Hint:
# Use nested for loops.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("               PATTERN GENERATOR")
print("=" * 50)

print()

rows = int(input("Enter number of rows : "))

print()

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end= ' ')
    print()

print("\n" + "=" * 50)
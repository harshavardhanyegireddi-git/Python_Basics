# ======================================================
# Mini Challenge
# ======================================================

# Student Club Registration
#
# Two clubs organize registrations.
#
# Club A Students:
# Take 5 student names as input.
#
# Club B Students:
# Take another 5 student names as input.
#
# Display:
# - Students registered in Club A
# - Students registered in Club B
# - Students registered in both clubs
# - Students registered in either club
#
# Hint:
# Use:
# add()
# intersection()
# union()


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("       STUDENT CLUB REGISTRATION")
print("=" * 50)


club_a = set()
club_b = set()

print("\nEnter names for Club A")


for student in range(1, 6):

    name = input(f"Enter Student {student} Name : ")

    club_a.add(name)


print("\nEnter names for Club B")

for student in range(1, 6):

    name = input(f"Enter Student {student} Name : ")

    club_b.add(name)

print("\n" + "=" * 50)


print("Club A Students           :", club_a)
print("Club B Students           :", club_b)

print("Common Students           :", club_a.intersection(club_b))

print("All Registered Students   :", club_a.union(club_b))

print("\n" + "=" * 50)
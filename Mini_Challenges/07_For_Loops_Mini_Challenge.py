# ======================================================
# Mini Challenge
# ======================================================

# Number Statistics
#
# Take a number as input.
#
# Print:
# - Numbers from 1 to the given number.
# - Sum of all numbers.
# - Even numbers.
# - Odd numbers.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("          NUMBER STATISTICS")
print("=" * 50)

number = int(input("Enter a number : "))

print("\n" + "=" * 50)
print("             All Numbers")
print("=" * 50)


for i in range(1, number + 1):
    print(i)


print("\n" + "=" * 50)
print("          Sum Of All Numbers")
print("=" * 50)


total = 0

for i in range(1, number + 1):
    total += i
print("Sum:",total)


print("\n" + "=" * 50)
print("           All Even Numbers")
print("=" * 50)


for i in range(2, number + 1, 2):
    print(i)


print("\n" + "=" * 50)
print("           All Odd Numbers")
print("=" * 50)

for i in range(1, number + 1, 2):
    print(i)

print("\n" + "=" * 50)
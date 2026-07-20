# ======================================================
# Practice Questions
# ======================================================

# 1. Print numbers from 1 to 20.
#
# 2. Print numbers from 20 to 1.
#
# 3. Print even numbers from 2 to 20.
#
# 4. Print odd numbers from 1 to 19.
#
# 5. Print the multiplication table of any number.
#
# 6. Find the sum of numbers from 1 to 100.
#
# 7. Print numbers divisible by 5 from 1 to 50.
#
# 8. Print the square of numbers from 1 to 10.


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----
number = 1

while number <= 20:
    print(number)
    number += 1

print("\n" + "=" * 50)

# ---- 2.Solution ----
num = 20

while num >= 1:
    print(num)
    num -= 1

print("\n" + "=" * 50)

# ---- 3.Solution ----
even = 2

while even <= 20:
    print(even)
    even += 2

print("\n" + "=" * 50)

# ---- 4.Solution ----
odd = 1
while odd <= 20:
    print(odd)
    odd += 2

print("\n" + "=" * 50)

# ---- 5.Solution ----
table = int(input("Enter a number :"))
count = 1

while count <= 10:
    print(f"{table} x {count} = {table*count}")
    count += 1

print("\n" + "=" * 50)

# ---- 6.Solution ----
count = 1
total = 0

while count <= 100:
    total += count
    count += 1
print("Sum :",total)

print("\n" + "=" * 50)

# ---- 7.Solution ----
num = 0

while num <= 50:
    num += 1
    if num % 5 != 0:
        continue

    print(num)

print("\n" + "=" * 50)


# ---- 8.Solution ----
num = 1

while num <= 10:
    print(num**2)

    num += 1

print("\n" + "=" * 50)

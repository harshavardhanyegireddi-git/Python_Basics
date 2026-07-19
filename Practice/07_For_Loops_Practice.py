# ======================================================
# Practice Questions
# ======================================================

# 1. Print numbers from 1 to 10.
#
# 2. Print numbers from 10 to 1.
#
# 3. Print even numbers from 2 to 20.
#
# 4. Print odd numbers from 1 to 19.
#
# 5. Print your name 10 times.
#
# 6. Print each character of your name.
#
# 7. Find the sum of numbers from 1 to 100.
#
# 8. Print the multiplication table of any number.


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

for number in range(1,11):
    print(number)

print("\n" + "=" * 50)


# ---- 2.Solution ----

for num in range(10,0,-1):
    print(num)

print("\n" + "=" * 50)


# ---- 3.Solution ----

for even in range(2,21,2):
    print(even)

print("\n" + "=" * 50)


# ---- 4.Solution ----

for odd in range(1,20,2):
    print(odd)

print("\n" + "=" * 50)


# ---- 5.Solution -----

name = input('Enter your name: ')

for j in range(10):
    print(name)

print("\n" + "=" * 50)


# ---- 6.Solution ----

_name = input("Enter your name : ")

for i in _name:
    print(i)

print("\n" + "=" * 50)


# ---- 7.Solution ----

total = 0

for k in range (1,101):
    total += k
print("Sum:",total)

print("\n" + "=" * 50)


# ---- 8.Solution ----

number = int(input("Enter a number : "))

for table in range(1,11):
    print(f"{number} x {table} = {number * table}")

print("\n" + "=" * 50)
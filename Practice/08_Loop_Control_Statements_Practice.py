# ======================================================
# Practice Questions
# ======================================================

# 1. Print numbers from 1 to 20.
#    Stop the loop when the number becomes 12.
#
# 2. Print numbers from 1 to 20.
#    Skip printing the number 10.
#
# 3. Print only odd numbers using continue.
#
# 4. Use break to stop an infinite while loop.
#
# 5. Use continue in a while loop to skip multiples of 3.
#
# 6. Create an empty if block using pass.
#
# 7. Print numbers from 1 to 50.
#    Stop when the number becomes divisible by 17.
#
# 8. Skip all even numbers between 1 and 20.


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

for i in range(1, 21):
    if i == 12:
        break

    print(i)

print("\n" + "=" * 50)

# ---- 2.Solution ----

for i in range(1, 21):
    if i == 10:
        continue

    print(i)

print("\n" + "=" * 50)

# ---- 3.Solution ----

for i in range(1, 21):
    if i % 2 == 0:
        continue

    print(i)

print("\n" + "=" * 50)

# ---- 4.Solution ----

num = 1

while num < 11 :
    if num == 6:
        break

    print(num)
    num += 1

print("\n" + "=" * 50)

# ---- 5.Solution ----

number = 0

while number < 20:
    number += 1

    if number % 3 == 0:
        continue

    print(number)
    

print("\n" + "=" * 50)

# ---- 6.Solution ----

marks = 85

if marks >= 35:
    pass

print("Student Passed")

print("\n" + "=" * 50)

# ---- 7.Solution ----

for i in range(1,51):
    if i % 17 == 0:
        continue

    print(i)

print("\n" + "=" * 50)

# ---- 8.Solution ----

for i in range(1, 21):
    if i % 2 == 0:
        continue

    print(i)

print("\n" + "=" * 50)
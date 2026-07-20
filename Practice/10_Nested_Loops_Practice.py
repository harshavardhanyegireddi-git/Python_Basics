# ======================================================
# Practice Questions
# ======================================================

# 1. Print a 5 × 5 star square.
#
# 2. Print a right triangle using stars.
#
# 3. Print an inverted triangle using stars.
#
# 4. Print a number triangle.
#
# 5. Print multiplication tables from 1 to 5.
#
# 6. Print a rectangle of numbers.
#
# 7. Print a rectangle of alphabets.
#
# 8. Print the following pattern:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

for rows in range(5):
    for columns in range(5):
        print("*",end=" ")
    print()

print ("\n" + "=" * 50)

# ---- 2.Solution ----

for rows in range(1, 6):
    for columns in range(rows):
        print("*", end=" ")
    print()

print ("\n" + "=" * 50)

# ---- 3.Solution ----

for rows in range(5, 0, -1):
    for columns in range(rows):
        print("*", end=" ")
    print()

print ("\n" + "=" * 50)

# ---- 4.Solution ----
count = 1

for rows in range(1,5):
    for columns in range (rows):
        print(count, end= " ")
        count += 1
    print()

print ("\n" + "=" * 50)

# ---- 5.Solution ---- 

for tables in range(1,6):
    print(f"Multipication table of {tables}")
    for count in range (1,11):
        print(f"{tables} x {count} = {tables*count}")
    print()

print ("\n" + "=" * 50)

# ---- 6.Solution ----

for rows in range(1,4):
    for columns in range(1,6):
        print(columns, end= " ")
    print()

print ("\n" + "=" * 50)

# ---- 7.Solution ----

for rows in range(1,5):
    for colums in range(rows):
        print("A", end= " ")
    print()

print ("\n" + "=" * 50)

# ---- 8.Solution ----

for rows in range(1,6):
    for columns in range(rows):
        print(columns + 1, end = " ")
    print()
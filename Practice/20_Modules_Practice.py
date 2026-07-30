# ======================================================
# Practice Questions
# ======================================================

# 1. Import the math module.
#
# 2. Print the value of pi.
#
# 3. Find the square root of 100.
#
# 4. Find 3 raised to the power of 4.
#
# 5. Import sqrt() directly.
#
# 6. Import math as m.
#
# 7. Generate a random number between 1 and 50.
#
# 8. Select a random fruit from a list.


print("\n" + "=" * 50)


# ======================================================
#                      Solutions
# ======================================================

# ---- 1. Solution ----

import math

print("Math module imported successfully.")

print("\n" + "=" * 50)

# ---- 2. Solution ----

print("Value of Pi :", math.pi)

print("\n" + "=" * 50)

# ---- 3. Solution ----

print("Square Root of 100 :", math.sqrt(100))

print("\n" + "=" * 50)

# ---- 4. Solution ----

print("3 Raised to the Power of 4 :", math.pow(3, 4))

print("\n" + "=" * 50)

# ---- 5. Solution ----

from math import sqrt

print("Square Root of 144 :", sqrt(144))

print("\n" + "=" * 50)

# ---- 6. Solution ----

import math as m

print("Square Root of 81 :", m.sqrt(81))

print("\n" + "=" * 50)

# ---- 7. Solution ----

import random

print("Random Number :", random.randint(1, 50))

print("\n" + "=" * 50)

# ---- 8. Solution ----

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Random Fruit :", random.choice(fruits))

print("\n" + "=" * 50)
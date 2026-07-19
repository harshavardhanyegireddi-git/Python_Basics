# ======================================================
# Practice Questions
# ======================================================

# 1. Perform all arithmetic operations on two numbers.
#
# 2. Compare two numbers using all comparison operators.
#
# 3. Use +=, -=, *= and //= operators.
#
# 4. Check whether both conditions are True using logical operators.
#
# 5. Check whether "Python" exists in a list.
#
# 6. Compare two lists using is and ==.


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----
a = 10
b = 2

print("Arithmetic Operators")
print("Addition       :", a + b)            # Adds two numbers.
print("Subtraction    :", a - b)            # Subtracts one number from another.
print("Multiplication :", a * b)            # Multiplies two numbers.
print("Division       :", a / b)            # Returns the quotient.
print("Floor Division :", a // b)           # Returns integer quotient.
print("Modulus        :", a % b)            # Returns the reminder.
print("Exponent       :", a ** b)           # Raises a number to power.

print("\n" + "=" * 50)

# ---- 2.Solution ----
x = 17
y = 26

print("Comparison Operators")
print("x == y :", x == y)           # x is equal to y.
print("x != y :", x != y)           # x is not equal to y.
print("x > y  :", x > y)            # x is greater than y.
print("x < y  :", x < y)            # x is less than y.
print("x >= y :", x >= y)           # x greater than or equal to y.
print("x <= y :", x <= y)           # x less than or equal to y.

print("\n" + "=" * 50)

# ---- 3.Solution ----
num = 10

print("Assignment Operators")

num += 5
print("num += 5 :", num)            # Performs addition and stores the result in the same variable.

num -= 2
print("num -= 2 :", num)            # Performs subtraction and stores the result in the same variable.

num *= 3
print("num *= 3 :", num)            # Performs multiplication and stores the result in the same variable.

num //= 2
print("num //= 2:", num)            # Performs floor division and stores the result in the same variable.

print("\n" + "=" * 50)

# ---- 4.Solution ----

a = False
b = True

print("Logical Operators")
print("a and b :", a and b)         # Returns True only if both values are True.
print("a or b  :", a or b)          # Returns True if atleast one value is True.
print("not a   :", not a)           # Reverses the boolean value.

print("\n" + "=" * 50)

# ---- 5.Solution ----
languages = ["Python", "Java", "C"]
print("Python in languages :","Python" in languages)     # Checks whether "Python" exists in the list.

print("\n" + "=" * 50)

# ---- 6.Solution ----
list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("Identity Operators")
print("list1 is list2     :", list1 is list2)               # Output: True
print("list1 is list3     :", list1 is list3)               # Output: False 
print("list1 == list3     :", list1 == list3)               # Output: True 

print("\n" + "=" * 50)
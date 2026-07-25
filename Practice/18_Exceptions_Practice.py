# ======================================================
# Practice Questions
# ======================================================

# 1. Handle ZeroDivisionError.
#
# 2. Handle ValueError while taking integer input.
#
# 3. Use try, except and else.
#
# 4. Use try, except and finally.
#
# 5. Handle multiple exceptions.
#
# 6. Raise a ValueError if age is negative.
#
# 7. Print the exception object.
#
# 8. Create your own exception handling example.

print("\n" + "=" * 50)

#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Can't divide a number by zero.")

print("\n" + "=" * 50)


# ---- 2.Solution ----

try:

    num = int(input("Enter a number :"))

except ValueError:

    print("Invalid, please enter an integer.")

print("\n" + "=" * 50)


# ---- 3.Solution ----

try:

    num = int(input("Enter a number :"))

except ValueError:

    print("Invalid, please enter an integer.")

else:

    print("You Entered :", num)

print("\n" + "=" * 50)


# ---- 4.Solution ----

try:

    result = 20 / 2

    print("Result :", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("Program Finished.")

print("\n" + "=" * 50)


# ---- 5.Solution ----

try:

    number = int(input("Enter a number :"))

    result = 100 / number

    print("Result :", result)

except ValueError:

    print("Please enter a valid integer.")

except ZeroDivisionError:

    print("Division with zero not allowed.")


print("\n" + "=" * 50)


# ---- 6.Solution ----

age = int(input("Enter your age :"))

try:

    if age < 0:

        raise ValueError("Age can't be negative.")

except ValueError as error:

    print(error)

print("\n" + "=" * 50)


# ---- 7.Solution ----

try:

    num = int(input("Enter a number :"))

except ValueError as error:

    print("Error :", error)

print("\n" + "=" * 50)


# ---- 8.Solution ----

age = int(input("Enter your age :"))

try:

    if age < 0:

        raise ValueError("Age can't be negative.")

except ValueError as error:

    print(error)

print("\n" + "=" * 50)
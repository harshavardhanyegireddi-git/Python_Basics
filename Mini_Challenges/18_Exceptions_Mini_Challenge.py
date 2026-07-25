# ======================================================
# Mini Challenge
# ======================================================

# Simple Calculator
#
# Take two numbers from the user.
#
# Take an operator (+, -, *, /).
#
# Display the result.
#
# Handle:
# - Division by zero
# - Invalid number input
# - Invalid operator
#
# Hint:
# Use:
# try
# except
# if-elif-else


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("               SIMPLE CALCULATOR ")
print("=" * 50)


num1 = int(input("Enter a number :"))
num2 = int(input("Enter another number"))
operator = input("Enter an operator (+, -, *, / ):")


try :
    num1 = int(input("Enter a number :"))
    num2 = int(input("Enter another number"))
    operator = input("Enter an operator (+, -, *, / ):")


    if operator == "+" :
        print(num1, "+", num2, "=", num1 + num2)

    elif operator == "-" :
        print(num1, "-", num2, "=", num1 - num2)

    elif operator == "*" :
        print(num1, "*", num2, "=", num1 * num2)

    elif operator == "/" :
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Invalid Operator!")


except ValueError :

    print("Enter a valid integer")

except ZeroDivisionError :

    print("Division by zero is not allowed.")

print("\n" + "=" * 50)
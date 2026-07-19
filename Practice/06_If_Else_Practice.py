# ======================================================
# Practice Questions
# ======================================================

# 1. Check whether a person is eligible to vote.
#
# 2. Check whether a number is positive,
#    negative or zero.
#
# 3. Check whether a number is even or odd.
#
# 4. Find the largest of two numbers.
#
# 5. Find the largest of three numbers.
#
# 6. Check whether a student passed or failed.
#
# 7. Print the grade based on marks.
#
# 8. Check whether a year is a leap year.


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Soltion ----

age = int(input("Enter your age :"))

if age >= 18:
    print("You are eligible to vote.")    # Executes only if the condition is True.
else:
    print("You are not eligible to vote.")   # Executes when the if condition is False

print("\n" + "=" * 50)


# ---- 2.Solution ----

number = int(input("Enter any number :"))

if number > 0:
    print(f"{number} is a Positive number.")            # Number is greater than zero
elif number < 0:
    print(f"{number} is a Negative number.")            # Number is less than zero.
else:
    print("It is Zero.")                                # Number is exactly zero.

print("\n" + "=" * 50)


# ---- 3.Solution ----

num = int(input("Enter a number : "))

if num == 0:
    print("It is Zero.")                    
elif num % 2 == 0:
    print(f"{num} is Even.")                # Even numbers are divisible by 2.
else:
    print(f"{num} is Odd.")                 # Odd numbers are not divisible by 2.

print("\n" + "=" * 50)


# ---- 4.Solution ----

num1 = int(input("Enter a number :"))
num2 = int(input("Enter another number :"))

if num1 > num2:
    print(f"{num1} is greater.")                    
elif num2 > num1:
    print(f"{num2} is greater.")
else:
    print("Both numbers are equal.")

print("\n" + "=" * 50)


# ---- 5.Solution ----

a = int(input("Enter a number :"))
b = int(input("Enter another number :"))
c = int(input("Enter another number :"))

if a > b and a > c:
    print(a,"is greater.")
elif b > c :  
    print(b,"is greater.")
elif a == b == c :
    print(" All numbers are Equal")
else:
    print(c,"is greater.")

print("\n" + "=" * 50)


# ---- 6.Solution ----

marks = int(input("Enter your marks: "))

if marks >= 35:
    print("You're Passed.")
else:
    print("You're Failed.")

print("\n" + "=" * 50)


# ---- 7.Solution ----
score = int(input("Enter your marks:"))

if score >= 90:
    print("Grade A")                      # Highest grade.
elif score >= 75:
    print("Grade B")                      # Second highest grade.
elif score >= 50:
    print("Grade C")                      # Passing grade.
else:
    print("Grade F")                      # Failing grade.

print("\n" + "=" * 50)


# ---- 8.Solution ----
year = int(input("Enter a year :"))

# A leap year is divisible by 4,
# but not divisible by 100,
# unless it is also divisible by 400.

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

print("\n" + "=" * 50)
# ======================================================
# Practice Questions
# ======================================================

# 1. Take your name as input and print a welcome message.
#
# 2. Take your age as input and print it.
#
# 3. Take two numbers and print their sum.
#
# 4. Take your city and state as input and print them.
#
# 5. Take your height as input and print it.
#
# 6. Take your favourite programming language and print it.

#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----
name = input("Enter your name : ")
print("Hello",name,"Welcome to python.")
print("\n"+"="*50)

# ---- 2.Solution ----
age = int(input("Enter your age : "))
print("Your age is",age )
print("\n"+"="*50)

# ---- 3.Solution ----
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
sum_result = num1 + num2
print("sum of given numbers is",sum_result)
print("\n"+"="*50)

# ---- 4.Solution ----
city = input("Enter Your City : ")
state = input("Enter Your State : ")
print(city,"is in",state)
print("\n"+"="*50)

# ---- 5.Solution ----
height = float(input("Enter your height : "))
print("Your Height Is",height)
print("\n"+"="*50)

# ---- 6.Solution ----
fav_programming_language = input("Enter your favorite programming language :")
print("Your Favourite Programming Language is",fav_programming_language)
print("\n"+"="*40)
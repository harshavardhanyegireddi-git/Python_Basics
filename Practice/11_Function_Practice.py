# ======================================================
# Practice Questions
# ======================================================

# 1. Create a function that prints your name.
#
# 2. Create a function that greets a user.
#
# 3. Create a function that adds two numbers.
#
# 4. Create a function that returns the square of a number.
#
# 5. Create a function that prints a multiplication table.
#
# 6. Create a function with a default parameter.
#
# 7. Create a function that returns two values.
#
# 8. Create one function that calls another function.


#=============================================
#---------------- Solutions ------------------
#=============================================

print("\n" + "=" * 50)

# ---- 1.Solution ----

def student(name):
    print("Name :",name)

student("Harsha")

print("\n" + "=" * 50)


# ---- 2.Solution ----

def greet(name):
    print("Hello",name)

greet("Harsha")

print("\n" + "=" * 50)


# ---- 3.Solution ----

def add(a, b):
    return a + b

result = add(5, 10)
print("Sum :",result)

print("\n" + "=" * 50)


# ---- 4.Solution ----

def square(a):
    return a ** 2

result = square(5)
print(result)

print("\n" + "=" * 50)


# ---- 5.solution ----
table = int(input("Enter a number :"))
multiple = 1

while multiple <= 10:
    
    def tables(count):
        print(f"{table} x {count} = {table * count}")

    tables(multiple)
    multiple += 1

print("\n" + "=" * 50)

# ---- 6.Solution ----

def country(name = "India"):
    print("Country :",name)

country()

print("\n" + "=" * 50)

# ---- 7.Solution ----

def calculate(a, b):
    return a + b, a * b

addition,multipication = calculate(5, 4)

print("Addition :", addition)
print("Multipication :", multipication)

print("\n" + "=" * 50)


# ---- 8.Solution ----

def line():
    print("=" * 30)

def welcome():
    
    line()
    print("Welcome To Python")
    line()

welcome()

print("\n" + "=" * 50)


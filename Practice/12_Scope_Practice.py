# ======================================================
# Practice Questions
# ======================================================

# 1. Create a local variable inside a function.
#
# 2. Create a global variable and print it inside a function.
#
# 3. Create a local and global variable with the same name.
#
# 4. Modify a global variable using the global keyword.
#
# 5. Create two functions with different local variables.
#
# 6. Pass a variable as a function parameter.
#
# 7. Print a global variable from multiple functions.
#
# 8. Create your own example of local and global scope.

print("\n" + "=" * 50)

#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

def college():

    name = "NIAT"

    print("College :",name)

college()

print("\n" + "=" * 50)


# ---- 2.Solution ----

name = "Harsha"

def student():
    
    print("Name :",name)

student()

print("\n" + "=" * 50)


# ---- 3.Solution ---- 

city = "Visakhapatnam"

def location():

    city = "Vijayawada"

    print("Inside Function :", city)

location()

print("Outside Function:", city)

print("\n" + "=" * 50)


# ---- 4.Solution ----

count = 0

def counting():

    global count

    count += 1

    print("Count :",count)

counting()

print("\n" + "=" * 50)


# ---- 5.Solution ---- 

def first():

    country = "India"

    print("First Function :", country)


def second():

    country = "USA"

    print("Second Function :", country)


print("\n" + "=" * 50)


# ---- 6.Solution ---- 

name = "Harsha"

def greet(a):

    print("Hello",a)

greet(name)

print("\n" + "=" * 50)


# ---- 7. Solution ----

company = "OpenAI"

def employee():
    print("Employee works at", company)


def manager():
    print("Manager works at", company)


def intern():
    print("Intern works at", company)

employee()
manager()
intern()

print("\n" + "=" * 50)


# ---- 8. Solution ----

country = "India"

def display_country():

    state = "Andhra Pradesh"

    print("Country :", country)
    print("State   :", state)

display_country()

print("Country :", country)

print("\n" + "=" * 50)
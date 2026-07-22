"""
=========================================================
Topic : Scope
=========================================================

What is Scope?
--------------
Scope determines where a variable can be accessed
in a program.

There are mainly two types of scope:

1. Local Scope
2. Global Scope

Local Variable:
A variable created inside a function.
It can only be accessed inside that function.

Global Variable:
A variable created outside a function.
It can be accessed anywhere in the program.
"""

print("=" * 50)
print("SCOPE")
print("=" * 50)

# ======================================================
# Example 1 : Local Variable
# ======================================================

def student():

    name = "Harsha"             # Local variable.

    print("Student Name:", name)

student()

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Global Variable
# ======================================================

college = "NRI University"      # Global variable.

def display_college():

    print("College:", college)

display_college()

print("\n" + "=" * 50)

# ======================================================
# Example 3 : Local and Global Variables
# ======================================================

city = "Visakhapatnam"          # Global variable.

def location():

    city = "Vijayawada"          # Local variable.

    print("Inside Function :", city)

location()

print("Outside Function:", city)

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Accessing Global Variable
# ======================================================

language = "Python"

def programming():

    print("Programming Language:", language)

programming()

print("\n" + "=" * 50)

# ======================================================
# Example 5 : Using global Keyword
# ======================================================

count = 0

def increase():

    global count                # Refers to the global variable.

    count += 1

increase()

print("Count:", count)

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Function Parameters
# ======================================================

def greet(name):

    print("Hello,", name)

greet("Harsha")

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Different Local Variables
# ======================================================

def first():

    number = 10

    print("First Function:", number)


def second():

    number = 20

    print("Second Function:", number)

first()
second()

print("\n" + "=" * 50)

# ======================================================
# Key Points
# ======================================================

"""
1. Variables created inside a function
   are called local variables.

2. Local variables can only be used
   inside that function.

3. Variables created outside functions
   are called global variables.

4. Global variables can be accessed
   anywhere in the program.

5. Use the global keyword only when
   you need to modify a global variable.
"""

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


# ======================================================
# Mini Challenge
# ======================================================

# Visitor Counter
#
# Create a global variable named visitors
# and initialize it with 0.
#
# Create a function named visit().
#
# Every time the function is called:
# - Increase visitors by 1.
# - Print the total number of visitors.
#
# Call the function 5 times.
#
# Hint:
# Use the global keyword.

'''
==================================
Topic : Variables in Python
File  : 01_Variables.py
==================================

What is a Variable?
-------------------
Answer :

Variable is a name used to store data in memory.


--- Real life Example ---

if we have three boxes

Box 1 📦---> name 
Box 2 📦---> age
Box 3 📦---> marks

each box carries values 
In Python, these boxes are called Variables.
'''

print("=" * 40)
print("VARIABLES IN PYTHON")
print("=" * 40)

# ================================================
# Example 1: Storing different types of data
# ================================================

name = "Harsha"
age = 17
height = 5.7
is_student = True

print(name)             # Output : Harsha
print(age)              # Output : 17
print(height)           # Output : 5.7
print(is_student)       # Output : True

print("\n"+"="*40)      # \n gives a gap line.


# ================================================
# Example 2: Printing Multiple Variables
# ================================================

collage = "NIAT"
course = "BTech CSE(AI & ML)"

print("Name:",name)             # Output:   Name: Harsha
print("Collage",collage)        # Output:   Collage: NIAT
print("Course:",course)         # Output:   Course: BTech CSE(AI & ML)

print("\n"+"="*40)              # \n gives a gap line.


# ================================================
# Example 3: Changing Variable Values
# ================================================

score = 80
print("Old Score:",score)       # Output :   Old Score: 80

score = 90
print("New score:",score)       # Output :   New Score: 90

print("\n"+"="*40)              # \n gives a gap line.


# ================================================
# Example 4: Assigning Multiple Values
# ================================================

x,y,z = 1,2,3

print(x)                        # Prints the first value in multiple values.
print(y)                        # Prints the second value in multiple values.
print(z)                        # Prints the third value in multiple values.

print("\n"+"="*40)              # \n gives a gap line.


# ================================================
# Example 5: Same Value To Multiple Variables
# ================================================

a = b = c = 100
print(a)
print(b)
print(c)

print("\n"+"="*40)


# ================================================
# Example 6: Variable Naming Rules
# ================================================

student_name = "Harsha"     # Correct
studentAge = 17             # Correct
_marks = 95                 # Correct

print(student_name)
print(studentAge)
print(_marks)

    # --- Invalid Variable Names ---
# 2name = "Harsha"
# my-name = "Harsha"
# class = "Python"

print("\n"+"="*40)


# ================================================
# Example 7: Using Variables In Caluculations
# ================================================

math = 90
science = 95
english = 88

total = math + science + english
average = total/3

print("Total:",total)
print("Average:",average)

print("\n"+"="*40)


# ================================================
# Example 8: Swapping Two Variables
# ================================================

a = 5
b = 10

print("Before swap")
print(a,b)                  # Output: 5,10

a,b = b,a
print("After Swap")
print(a,b)                  # Output: 10,5

print("\n"+"="*40)


# ==========================================
# ---- Practice Questions ----
# ==========================================

# 1. Create variables for your:
# - Name
# - Age
# - City
# - Favourite Language

# 2. Print them.

# 3. Create variables for marks in
# Maths, Physics and Chemistry.

# 4. Find Total and Average.




"""
===========================================
Mini Challenge: Student Profile
Topic: Variables
===========================================

Create variables to store a student's details
and display them in a neat format.
"""
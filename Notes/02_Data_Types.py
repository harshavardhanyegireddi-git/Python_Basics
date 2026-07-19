"""
=========================================================
Topic      : Data Types in Python
File       : 02_Data_Types.py
=========================================================

What are Data Types?
--------------------
Data types define the type of value stored in a variable.


--- Real life Example ---

Think of data types like different containers.

🥤 Bottle  -> Water
📦 Box     -> Books
💰 Wallet  -> Money

Similarly, Python stores different types of data using
different data types.

Common Python Data Types:
1. int    -> Integer numbers
2. float  -> Decimal numbers
3. str    -> Text or characters
4. bool   -> True or False
5. list   -> Ordered collection
6. tuple  -> Ordered, immutable collection
7. set    -> Unordered unique collection
8. dict   -> Key-Value pairs
"""

print("=" * 50)
print("PYTHON DATA TYPES")
print("=" * 50)

# ======================================================
# Example 1 : Integer (int)
# ======================================================

age = 18

print("Integer Example")
print(age)
print(type(age))

print("\n" + "=" * 50)

# ======================================================
# Example 2 : Float
# ======================================================

height = 5.8

print("Float Example")
print(height)
print(type(height))

print("\n" + "=" * 50)

# ======================================================
# Example 3 : String
# ======================================================

name = "Harsha"

print("String Example")
print(name)
print(type(name))

print("\n" + "=" * 50)

# ======================================================
# Example 4 : Boolean
# ======================================================

is_student = True

print("Boolean Example")
print(is_student)
print(type(is_student))

print("\n" + "=" * 50)

# ======================================================
# Example 5 : List
# ======================================================

fruits = ["Apple", "Banana", "Mango"]

print("List Example")
print(fruits)
print(type(fruits))

print("\n" + "=" * 50)

# ======================================================
# Example 6 : Tuple
# ======================================================

colors = ("Red", "Green", "Blue")

print("Tuple Example")
print(colors)
print(type(colors))

print("\n" + "=" * 50)

# ======================================================
# Example 7 : Set
# ======================================================

numbers = {10, 20, 30, 40}

print("Set Example")
print(numbers)
print(type(numbers))

print("\n" + "=" * 50)

# ======================================================
# Example 8 : Dictionary
# ======================================================

student = {
    "Name": "Harsha",
    "Age": 18,
    "College": "NIAT"
}

print("Dictionary Example")
print(student)
print(type(student))

print("\n" + "=" * 50)

# ======================================================
# Example 9 : Checking Data Type
# ======================================================

marks = 95

print("Checking Data Type")
print(type(marks))

print("\n" + "=" * 50)

# ======================================================
# Example 10 : Multiple Data Types Together
# ======================================================

name = "Harsha"
age = 18
cgpa = 8.9
hosteller = True

print("Student Details")
print(name)
print(age)
print(cgpa)
print(hosteller)

print(type(name))
print(type(age))
print(type(cgpa))
print(type(hosteller))

print("\n" + "=" * 50)




# ======================================================
# Practice Questions
# ======================================================

# 1. Create an integer variable for your age.

# 2. Create a float variable for your height.

# 3. Create a string variable for your name.

# 4. Create a boolean variable to indicate
#    whether you are a student.

# 5. Create a list of your favourite fruits.

# 6. Create a tuple of three colours.

# 7. Create a set of five numbers.

# 8. Create a dictionary containing your
#    Name, Age and City.


# 9. Print the data type of every variable.



# ======================================================
# Mini Challenge
# ======================================================

# Create a Student Information System.

# Store:
# - Name
# - Age
# - Height
# - Is Student
# - Favourite Subjects (List)
# - Favourite Colors (Tuple)
# - Lucky Numbers (Set)
# - Student Details (Dictionary)

# Print every value and its data type.
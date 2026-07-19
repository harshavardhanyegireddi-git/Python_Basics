# ======================================================
# Practice Questions
# ======================================================

# 1. Convert an integer into a float.
#
# 2. Convert a float into an integer.
#
# 3. Convert an integer into a string.
#
# 4. Convert a string into an integer.
#
# 5. Convert a string into a float.
#
# 6. Convert True into an integer.
#
# 7. Convert 0 into a boolean.
#
# 8. Add an integer and a float.
#    Print the result and its data type.


#=============================================
#---------------- Solutions ------------------
#=============================================


# ---- 1.Solution ----

num = 80

print("Before Conversion")
print("Value :", num)
print("Data Type :", type(num))

num = float(num)                      # Converts integer into float.

print("\nAfter Conversion")
print("Value :", num)
print("Data Type :", type(num))

print("\n" + "=" * 50)


# ---- 2.Solution ----

price = 36.9

print("Before Conversion")
print("Value :", price)
print("Data Type :", type(price))

price = int(price)                    # Converts float into integer.

print("\nAfter Conversion")
print("Value :", price)
print("Data Type :", type(price))

print("\n" + "=" * 50)


# ---- 3.Solution ----

age = 17

print("Before Conversion")
print("Value :", age)
print("Data Type :", type(age))

age = str(age)                        # Converts integer into string.

print("\nAfter Conversion")
print("Value :", age)
print("Data Type :", type(age))

print("\n" + "=" * 50)


# ---- 4.Solution ----

number = "108"

print("Before Conversion")
print("Value :", number)
print("Data Type :", type(number))

number = int(number)                  # Converts string into integer.

print("\nAfter Conversion")
print("Value :", number)
print("Data Type :", type(number))

print("\n" + "=" * 50)


# ---- 5.Solution ----

height = "5.7"

print("Before Conversion")
print("Value :", height)
print("Data Type :", type(height))

height = float(height)                # Converts string into float.

print("\nAfter Conversion")
print("Value :", height)
print("Data Type :", type(height))

print("\n" + "=" * 50)


# ---- 6.Solution ----
status = True

print("Before Conversion")
print("Value :", status)
print("Data Type :", type(status))

status = int(status)                  # Converts boolean into integer.

print("\nAfter Conversion")
print("Value :", status)
print("Data Type :", type(status))

print("\n" + "=" * 50)



# ---- 7.Solution ----

value = 0

print("Before Conversion")
print("Value :", value)
print("Data Type :", type(value))

value = bool(value)                   # Converts integer into boolean.

print("\nAfter Conversion")
print("Value :", value)
print("Data Type :", type(value))

print("\n" + "=" * 50)


# ---- 8.Solution ----

a = 10
b = 5.5

result = a + b                        # Python automatically converts integer into float.

print("Result :", result)
print("Data Type :", type(result))

print("\n" + "=" * 50)
# ======================================================
# Mini Challenge
# ======================================================

# Password Verification System
#
# Correct Password:
# python123
#
# Ask the user to enter the password.
#
# Keep asking until the correct password is entered.
#
# If the password is correct:
#     Print "Access Granted!"
#
# Hint:
# Use a while loop.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("          PASSWORD VERIFICATION SYSTEM")
print("=" * 50)

print()

correct_password = "python123"

while True :
    password = input("Enter your password : ")

    if correct_password == password:
        print("Access Granted!")
        break                                                   # Exit the loop after successful login.

    print("Incorrect password. Please try again.")

print("\n" + "=" * 50)
# ======================================================
# Mini Challenge
# ======================================================

# Guess the Secret Number
#
# Secret Number = 7
#
# Ask the user to guess the secret number continuously.
#
# If the guess is correct:""
#     Print "Congratulations! You guessed it."
#     Stop the loop using break.
#
# If the guess is incorrect:
#     Print "Wrong Guess! Try Again."
#
# If the user enters 0:
#     Print "Game Exited."
#     Stop the loop.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


print("=" * 50)
print("            Guess the Secret Number")
print("=" * 50)

secret_number = 7

while True:
    guess = int(input("Guess a number(0 to exit): "))

    if guess == 0:
        print("Game Exited.")
        break

    if guess == secret_number:
        print("Congratulations! You guessed it.")
        break

    print("Wrong Guess! Try Again.")

print("\n" + "=" * 50)

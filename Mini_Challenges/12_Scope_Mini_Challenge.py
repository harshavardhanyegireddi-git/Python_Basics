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


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================

print("=" * 50)
print("                VISITOR COUNTER")
print("=" * 50)


visitors = 0


def visit(name):

    global visitors

    visitors += 1

    print(f"{visitors}. {name}")

visit("Harsha")

visit("Yeswanth")

visit("Padma")

visit("Srinivas")

visit("Keerthana")


print("\n" + "=" * 50)

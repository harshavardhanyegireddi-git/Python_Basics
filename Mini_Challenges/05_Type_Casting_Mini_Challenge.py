# ======================================================
# Mini Challenge
# ======================================================

# Student Fee Calculator
#
# Take the student's fee as input.
#
# Convert the fee into float.
#
# Add a library fee of 500.
#
# Print:
# - Original Fee
# - Library Fee
# - Total Fee
# - Data type of Total Fee.


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================


'''
STUDENT FEE CALCULATOR
'''

print("=" * 50)
print("           STUDENT FEE CALCULATOR")
print("=" * 50)

original_fee = float(input("Enter Your Fee :"))
library_fee = 500

total_fee = original_fee + library_fee

print("Original Fee:", original_fee)
print("Library Fee:", library_fee)
print("Total Fee:", total_fee)
print("Type:", type(total_fee))

print("\n" + "=" * 50)
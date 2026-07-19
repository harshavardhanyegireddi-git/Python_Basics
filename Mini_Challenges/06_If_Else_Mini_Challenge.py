# ======================================================
# Mini Challenge
# ======================================================

# ATM Withdrawal System
#
# Take the account balance as input.
# Take the withdrawal amount as input.
#
# If the withdrawal amount is less than or equal
# to the balance:
#     Print "Transaction Successful"
#     Print the remaining balance.
#
# Otherwise:
#     Print "Insufficient Balance"


# ======================================================
# ---------------- Challenge Solution ------------------
# ======================================================

print("=" * 50)
print("            ATM MACHINE")
print("=" * 50)


account_balance = int(input("Enter account balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))

if account_balance >= withdrawal_amount:
    remaining_balance = account_balance - withdrawal_amount

    print("Transaction Successful")
    print("Remaining Balance:",remaining_balance)
else:
    print("Insufficient Balance")


print("\n" + "=" * 50)
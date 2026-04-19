def atm_withdrawal(withdrawal_amount):
    balance = 5000

    # Validation 1
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False

    # Validation 2
    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
        return False

    # Validation 3
    if withdrawal_amount > balance:
        print(f"Error: Insufficient balance. Available: {balance}")
        return False

    # If all validations pass
    remaining_balance = balance - withdrawal_amount
    print(f"Withdrawal successful. Amount: {withdrawal_amount}")
    print(f"Remaining balance: {remaining_balance}")
    return True


# Take input from user
amount = int(input("Enter withdrawal amount: "))

# Call function
result = atm_withdrawal(amount)

print("Return:", result)

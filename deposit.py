# deposit.py - deposit functionality

def deposit(account, amount: float):
    """
    Deposit money into account with validation.
    """
    if amount <= 0:
        print("Invalid deposit amount ❌")
        return account.balance

    account.update_balance(amount)

    print(f"Deposited: {amount} EGP ✔")
    print(f"New Balance: {account.balance} EGP")

    return account.balance
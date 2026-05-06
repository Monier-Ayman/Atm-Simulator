# account.py - manages account balance operations

class Account:
    def __init__(self, owner: str, initial_balance: float = 0):
        self.owner = owner
        self.balance = initial_balance

    def get_balance(self) -> float:
        return self.balance

    def update_balance(self, amount: float):
        self.balance += amount

    def show_account_info(self):
        print("\n--- Account Info ---")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance} EGP")
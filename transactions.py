# transactions.py - stores transaction history

from datetime import datetime

class TransactionManager:
    def __init__(self):
        self.history = []

    def add_transaction(self, action: str, amount: float):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.history.append({
            "action": action,
            "amount": amount,
            "time": timestamp
        })

    def show_history(self):
        print("\n--- Transaction History ---")

        if not self.history:
            print("No transactions yet.")
            return

        for t in self.history:
            print(f"{t['time']} | {t['action']} | {t['amount']} EGP")

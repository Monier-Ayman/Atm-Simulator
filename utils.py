# utils.py - helper functions

def format_currency(amount: float) -> str:
    return f"{amount:.2f} EGP"


def print_line():
    print("-" * 40)


def validate_amount(amount: float) -> bool:
    return amount > 0

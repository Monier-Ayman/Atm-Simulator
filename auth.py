# auth.py - handles user authentication logic

MAX_ATTEMPTS= 3


def check_pin(input_pin: str, correct_pin: str) -> bool:
    """
    Compare user PIN with stored PIN.
    """
    return input_pin == correct_pin


def login_system(correct_pin: str) -> bool:
    """
    Handles login attempts with limited tries.
    """
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        pin = input("Enter your PIN: ")

        if check_pin(pin, correct_pin):
            print("Login successful ✔")
            return True

        attempts += 1
        print(f"Wrong PIN ❌ Attempts left: {MAX_ATTEMPTS - attempts}")

    print("Account locked due to too many attempts ❌")
    return False

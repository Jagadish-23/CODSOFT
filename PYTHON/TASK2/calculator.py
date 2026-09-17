"""
Simple Calculator
CodSoft Python Programming Internship - Task 2

Prompts the user for two numbers and an operation, performs the
calculation, and displays the result. Runs in a loop so the user can
perform multiple calculations in one session.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("Addition (+)", add),
    "2": ("Subtraction (-)", subtract),
    "3": ("Multiplication (*)", multiply),
    "4": ("Division (/)", divide),
}


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number, please try again.")


def print_menu():
    print("\n===== SIMPLE CALCULATOR =====")
    for key, (label, _) in OPERATIONS.items():
        print(f"{key}. {label}")
    print("5. Exit")


def main():
    print("Welcome to the Python Calculator!")
    while True:
        print_menu()
        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        label, func = OPERATIONS[choice]

        try:
            result = func(num1, num2)
            print(f"\nResult: {num1} {label.split('(')[-1].strip(')')} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

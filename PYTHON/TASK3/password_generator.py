"""
Password Generator
CodSoft Python Programming Internship - Task 3

Generates a strong, random password of a user-specified length,
optionally including uppercase letters, digits, and symbols.
Uses the `secrets` module (rather than `random`) for cryptographically
strong randomness, which is best practice for password generation.
"""

import secrets
import string


def build_character_pool(use_upper, use_digits, use_symbols):
    pool = string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%^&*()-_=+[]{};:,.<>?"
    return pool


def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    pool = build_character_pool(use_upper, use_digits, use_symbols)
    if not pool:
        raise ValueError("Character pool is empty — enable at least one character type.")

    password = "".join(secrets.choice(pool) for _ in range(length))
    return password


def ask_yes_no(prompt, default=True):
    suffix = " [Y/n]: " if default else " [y/N]: "
    answer = input(prompt + suffix).strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes")


def main():
    print("===== PASSWORD GENERATOR =====")
    while True:
        try:
            length = int(input("Enter desired password length (min 4): "))
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        use_upper = ask_yes_no("Include uppercase letters?")
        use_digits = ask_yes_no("Include digits?")
        use_symbols = ask_yes_no("Include symbols?")

        try:
            password = generate_password(length, use_upper, use_digits, use_symbols)
            print(f"\nGenerated Password: {password}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
            continue

        again = input("Generate another password? [y/N]: ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

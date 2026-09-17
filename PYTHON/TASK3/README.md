# Task 3 — Password Generator

A command-line password generator built in Python for the **CodSoft
Python Programming Internship**. It creates strong, random passwords of a
user-specified length, with optional uppercase letters, digits, and
symbols.

## Features
- User specifies password length (minimum 4 characters)
- Optional inclusion of uppercase letters, digits, and symbols
- Uses Python's `secrets` module for cryptographically secure randomness
  (safer than the standard `random` module for security-sensitive uses)
- Generate multiple passwords in one session

## How to Run
```bash
python password_generator.py
```
No external libraries are required — uses only `secrets` and `string`
from the Python standard library.

## Example Session
```
===== PASSWORD GENERATOR =====
Enter desired password length (min 4): 12
Include uppercase letters? [Y/n]: y
Include digits? [Y/n]: y
Include symbols? [Y/n]: y

Generated Password: aQ8!fL2#zK9$
```

## Files
| File | Description |
|------|-------------|
| `password_generator.py` | Main application source code |
| `README.md` | This file |

---
Part of the **#codsoft** Python Programming virtual internship.

"""
Write a Python program to create a simple password validation system.

The program should repeatedly ask the user to enter a password until a
valid password is entered. A password is considered valid only if it has
at least 8 characters and contains the @ symbol.

Once the user enters a valid password, display "Password accepted." and
stop. Otherwise, display "Weak password. Try again." and ask again.
"""

while True:
    password = input("Enter password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted.")
        break
    else:
        print("Weak password. Try again.")
# 2. Write a Python program to simulate a digital lock system. The lock should ask the user to enter a 4-digit PIN.
# If the entered PIN does not contain exactly 4 digits, the program should display an error message and ask again.
# If the entered PIN is correct, the lock should open. Otherwise, the program should ask the user to try again

pin = input("Enter 4 digit PIN: ")
correct_pin = "1234"

valid = len(pin) == 4 and pin.isdigit()
correct = pin == correct_pin

print("Valid PIN:", valid)
print("Lock opened:", valid and correct)
#  Write a Python program to take a password and check whether it contains @ and has at least 8 characters.
password = input("Enter password: ")
is_valid = ("@" in password) and (len(password) >= 8)
print("Is password valid?", is_valid)
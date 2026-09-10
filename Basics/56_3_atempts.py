# Write a Python program that asks the user to enter a username and password.
# The user should get only 3 attempts. If the correct credentials are entered,
# display "Login Successful" and stop the loop. If all attempts are used,
# display "Account Locked".

username1 = "admin"
password1 = "1234"

for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == username1 and password == password1:
        print("Login Successful")
        break
    else:
        print("Account Locked")
# Take a password and check length , presence of @ and whether first and last character are different

password = input("Enter Password: ")
print(len(password) >= 8)
print("@" in password)
print(password[0] != password[-1])
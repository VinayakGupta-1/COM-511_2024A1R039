#  Write a Python program to take first name and last name and print initials.
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
initials = first_name[0].upper() + "." + last_name[0].upper() + "."
print("Initials:", initials)

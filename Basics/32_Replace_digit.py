# Write a python program to take a 10 digit mobile number and display only the last 4 digit. Replace the first 6 digit with ********
mobile = input("Enter 10 digit mobile number: ")

print("Masked number:", "*" * 6 + mobile[-4:])
print("Last 4 digits:", mobile[-4:])                   

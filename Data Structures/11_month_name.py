# Write a Python program to store all month names in a tuple. Input a month number and display the corresponding month name.

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

num = int(input("Enter month number (1-12): "))

if 1 <= num <= 12:
    print("Month name:", months[num - 1])
else:
    print("Invalid month number.")

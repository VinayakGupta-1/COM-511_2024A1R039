# Program to calculate the number of ₹500 and ₹100 notes required

amount = int(input("Enter amount in rupees: "))

notes_500 = amount // 500
remaining = amount % 500

notes_100 = remaining // 100

print("Number of ₹500 notes:", notes_500)
print("Number of ₹100 notes:", notes_100)
# Write a Python program to input a list of numbers and create a new list containing only unique elements.

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

    unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)
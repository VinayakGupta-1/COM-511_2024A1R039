# Write a Python program to input numbers in a list and find the second largest number.

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

    numbers = list(set(numbers))
    numbers.sort()

print("Second largest number:", numbers[-2])
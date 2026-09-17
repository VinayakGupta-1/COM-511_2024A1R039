# Write a Python program to count how many times a particular element appears in a list.

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

element = int(input("Enter element to search: "))

count = numbers.count(element)

print("Element appears", count, "times.")
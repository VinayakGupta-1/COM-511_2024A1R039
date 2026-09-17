# Write a Python program to rotate a list one position to the right.

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

last = numbers.pop()
numbers.insert(0, last)

print("Rotated list:", numbers)
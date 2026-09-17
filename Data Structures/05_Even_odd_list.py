# Write a Python program to input numbers in a list and create two separate lists for even and odd numbers.

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

    even = []
    odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

# Write a Python program to repeatedly calculate the sum of digits of a
# number until the result becomes a single digit.
# Example: 9875 -> 29 -> 11 -> 2

num = int(input("Enter a number: "))

while num >= 10:
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    num = sum

print("Result =", num)
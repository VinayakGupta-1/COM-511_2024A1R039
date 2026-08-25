# Program to find the sum of digits of a two-digit number

num = int(input("Enter a two-digit number: "))

tens = num // 10
ones = num % 10

sum_digits = tens + ones

print("Sum of digits:", sum_digits)
# Write a Python program to check whether a number is a perfect number.
# A number is perfect if the sum of its proper divisors is equal to
# the number itself.

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
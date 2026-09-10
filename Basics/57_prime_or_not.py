# Write a Python program to input a number and check whether it is prime or not.
# A number is prime if it has no divisor other than 1 and itself.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
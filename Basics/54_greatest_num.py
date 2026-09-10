"""
Write a Python program to input four numbers from the user and find
the greatest number among them.
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

greatest = a

if b > greatest:
    greatest = b

if c > greatest:
    greatest = c

if d > greatest:
    greatest = d

print("Greatest number =", greatest)
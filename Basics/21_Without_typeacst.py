# 21. write a Python program to take input from the user without typecasting and multiply it by 3. Then typecast the same input to int and multiply it by 3. Print both results to show thw difference.

user = int(input("Enter input :"))

result1 = user * 3
print("Without typecasting:", result1)

user = int(user)

result2 = user * 3
print("After typecasting:", result2)
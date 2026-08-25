# 19. Write a Python program to take marks of three subjects out of 100. Print True if the student scored at least 40 in all three subjects and average marks at least 50.
a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))

if a and b and c>= 40 and (a+b+c)/3 >= 50:
    print("True")
else:
    print("False")
# Write a python program that accepts the length of three sides of a triangle as inputs.
# The program should indicate whether or not the triangle is a right-angled triangle.
# (Use Pythagorean theorem) Also find out its area using Heron's formula.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:

    sides = sorted([a, b, c])

    if abs((sides[0]**2 + sides[1]**2) - sides[2]**2) < 1e-9:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")

    s = (a + b + c) / 2

    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

    print("Area:", area)

else:
    print("Invalid triangle")

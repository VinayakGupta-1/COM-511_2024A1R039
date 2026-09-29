# Write a Python program to store two points as tuples and calculate the distance between them.

import math

x1 = float(input("Enter x coordinate of first point: "))
y1 = float(input("Enter y coordinate of first point: "))
x2 = float(input("Enter x coordinate of second point: "))
y2 = float(input("Enter y coordinate of second point: "))

p1 = (x1, y1)
p2 = (x2, y2)

distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print("First point:", p1)
print("Second point:", p2)
print("Distance between points:", distance)

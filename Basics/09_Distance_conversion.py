# Program to take distance in kilometer and convert it into meters, centimeters and millimeters
km = float(input("Enter distance in kilometers: "))

meters = km * 1000
centimeters = km * 100000
millimeters = km * 1000000

print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)
print("Distance in millimeters =", millimeters)
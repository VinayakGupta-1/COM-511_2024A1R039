# Write a Python program to store repeated values in a tuple and count how many times a given value appears.

values = (1, 2, 3, 2, 4, 2, 5, 3, 1, 2)

print("Tuple:", values)

value = int(input("Enter value to count: "))

count = values.count(value)

print(value, "appears", count, "times.")

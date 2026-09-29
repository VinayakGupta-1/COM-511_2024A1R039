# Write a Python program to check whether a given value is present in a tuple. If present, display its position.

values = (10, 25, 30, 45, 50, 65)

print("Tuple:", values)

value = int(input("Enter value to search: "))

if value in values:
    print(value, "is present at position", values.index(value) + 1)
else:
    print(value, "is not present in the tuple.")

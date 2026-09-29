# Write a Python program to show that tuple values cannot be changed directly. Convert tuple into list, update it, and convert it back into tuple.

numbers = (10, 20, 30, 40, 50)

print("Original tuple:", numbers)

index = int(input("Enter index to update (0-4): "))
value = int(input("Enter new value: "))

# Trying to change a tuple directly gives an error
try:
    numbers[index] = value
except TypeError as e:
    print("Error:", e)

if 0 <= index < len(numbers):
    temp = list(numbers)
    temp[index] = value
    numbers = tuple(temp)
    print("Updated tuple:", numbers)
else:
    print("Invalid index.")

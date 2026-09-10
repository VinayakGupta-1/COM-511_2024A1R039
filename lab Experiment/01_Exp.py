# Write a program to demonstrate type checking of various data types
# and demonstrate the use of built-in functions:
# abs(), len(), min(), round(), isalnum(), type()

# Different data types

num = 25
decimal = 15.786
text = "Python123"
result = True
my_list = [1, 2, 3, 4, 5]
my_list2 = ["apple", "banana", "cherry"]

# Type checking
print("Type of num:", type(num))
print("Type of decimal:", type(decimal))
print("Type of text:", type(text))
print("Type of result:", type(result))
print("Type of my_list:", type(my_list))
print("Type of my_list2:", type(my_list2))

#print("\n--- Built-in Functions Demonstration ---")

# abs()
negative_num = -45
positive_num = 45
print("Absolute value of", negative_num, "is:", abs(negative_num))
print("Absolute value of", positive_num, "is:", abs(positive_num))

# len()
print("Length of text:", len(text))
print("Length of list:", len(my_list))

# min()
print("Minimum value in list:", min(my_list))
print("Minimum value in list of strings:", min(my_list2))

# round()
print("Rounded value of", decimal, "is:", round(decimal))
print("Rounded value to 2 decimal places:", round(decimal, 2))

# isalnum()
print("Is 'Python123' alphanumeric?", text.isalnum())
print("Is 'Python 123' alphanumeric?", "Python 123".isalnum())

# type()
print("Type of decimal variable:", type(decimal))
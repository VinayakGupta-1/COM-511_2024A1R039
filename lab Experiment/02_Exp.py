# Write a program to illustrate iteration over the list and dictionary.
# Iteration over a list
my_list = [10, 20, 30, 40, 50]

print("Elements of the list:")
for item in my_list:
    print(item, end=" ")


# Iteration over a dictionary
my_dict = {
    "Name": "Vinayak",
    "Subject": "Python Programming",
    "Course": "B.Tech CSE"
    }

print("\nElements of the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)
    
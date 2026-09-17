# Write a Python program to input two lists and create a third list containing common elements.

list1 = []
list2 = []
common = []

n1 = int(input("Enter number of elements in first list: "))

for i in range(n1):
    num = int(input("Enter number: "))
    list1.append(num)

    n2 = int(input("Enter number of elements in second list: "))

for i in range(n2):
    num = int(input("Enter number: "))
    list2.append(num)

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("First list:", list1)
print("Second list:", list2)
print("Common elements:", common)
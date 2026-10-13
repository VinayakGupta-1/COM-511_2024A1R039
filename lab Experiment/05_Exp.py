# Write a program to perform searching activity using linear search and binary search.

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = int(input("Enter the value to search: "))

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Linear Search result
pos = linear_search(list1, target)
if pos != -1:
    print("Linear Search: Element found at index", pos)
else:
    print("Linear Search: Element not found")

# Binary Search result (list must be sorted)
pos = binary_search(list1, target)
if pos != -1:
    print("Binary Search: Element found at index", pos)
else:
    print("Binary Search: Element not found")

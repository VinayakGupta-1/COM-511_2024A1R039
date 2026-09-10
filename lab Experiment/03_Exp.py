# Consider the string "Welcome to Python world".
# Perform the following operations:
    # 1. Count the number of alphabets in the given string.
    # 2. Extract characters in the given range from the string.
    # 3. Check if the string is alphanumeric or not.

string = "Welcome to Python world"

# 1. Count the number of alphabets
count = 0
for ch in string:
    if ch.isalpha():
        count += 1  
print("Number of alphabets:", count)

# 2. Extract characters in a given range
# Extract characters from index 0 to 6
print("Characters from index 0 to 6:", string[0:7])

# 3. Check whether the string is alphanumeric
print("Is the string alphanumeric?", string.isalnum())
# Program to reverse kth row in matrix
# (Reverses every kth row: row k, 2k, 3k, ...)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24]
]

print("Original Matrix:")
for row in matrix:
    print(row)

k = int(input("Enter the value of k: "))

if k <= 0:
    print("k must be a positive number")
else:
    for i in range(len(matrix)):
        if (i + 1) % k == 0:
            matrix[i] = matrix[i][::-1]

    print("Matrix after reversing every", k, "th row:")
    for row in matrix:
        print(row)

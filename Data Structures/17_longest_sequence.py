"""Find the longest consecutive sequence of strictly improving test marks."""

n = int(input("Enter number of tests: "))
while n < 1:
    print("Enter at least one test.")
    n = int(input("Enter number of tests: "))

marks = []
for test_number in range(1, n + 1):
    mark = int(input(f"Enter marks for test {test_number}: "))
    marks.append(mark)

best_start = 0
best_length = 1
current_start = 0
current_length = 1

for index in range(1, n):
    if marks[index] > marks[index - 1]:
        current_length += 1
        if current_length > best_length:
            best_start = current_start
            best_length = current_length
    else:
        current_start = index
        current_length = 1

best_end = best_start + best_length - 1
longest_sequence = marks[best_start:best_end + 1]

print("Marks:", marks)
print("Longest improving sequence:", longest_sequence)
print("Number of tests:", best_length)
print("Test range:", (best_start + 1, best_end + 1))

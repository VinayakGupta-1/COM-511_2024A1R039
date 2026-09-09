"""
Write a Python program to input marks of 5 students.

For each student, check whether the entered marks are valid or invalid.
Marks are considered valid only if they are between 0 and 100.

If the marks are invalid, display "Invalid marks skipped" and move to
the next student without printing those marks.

If the marks are valid, display the marks as valid.
"""

for i in range(1, 6):
    marks = float(input(f"Enter marks of student {i}: "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped")
        continue

    print("Valid marks:", marks)
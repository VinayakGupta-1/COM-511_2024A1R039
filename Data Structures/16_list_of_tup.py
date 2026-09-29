# Write a Python program to store multiple student records as a list of tuples. Each tuple should contain name, roll number, and marks. Display students who scored above 75.

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    students.append((name, roll, marks))

print("Students who scored above 75:")

found = False

for student in students:
    if student[2] > 75:
        print("Name:", student[0], "Roll number:", student[1], "Marks:", student[2])
        found = True

if not found:
    print("No student scored above 75.")

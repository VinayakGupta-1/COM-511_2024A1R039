# Write a Python program to store one student data as a tuple: name, roll number, and marks. Display grade based on marks.

name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student = (name, roll, marks)

if student[2] >= 90:
    grade = "A"
elif student[2] >= 75:
    grade = "B"
elif student[2] >= 60:
    grade = "C"
elif student[2] >= 40:
    grade = "D"
else:
    grade = "F"

print("Name:", student[0])
print("Roll number:", student[1])
print("Marks:", student[2])
print("Grade:", grade)

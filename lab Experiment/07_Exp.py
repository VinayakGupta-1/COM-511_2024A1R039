# Write a Python program to create records of n students.
# Store each student record as a dictionary containing roll number, name, branch, and marks.
# Store all records in a list and search for a student using roll number.
# (Condition: Roll numbers must be unique.)

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    # Roll number must be unique
    while True:
        roll = int(input("Roll Number: "))
        duplicate = False
        for s in students:
            if s["roll"] == roll:
                duplicate = True
                break
        if duplicate:
            print("Roll number already exists! Enter a unique roll number.")
        else:
            break

    name = input("Name: ")
    branch = input("Branch: ")
    marks = float(input("Marks: "))

    student = {"roll": roll, "name": name, "branch": branch, "marks": marks}
    students.append(student)

# Display all records
print("\nAll Student Records:")
for s in students:
    print(s)

# Search by roll number
search_roll = int(input("\nEnter roll number to search: "))
found = False
for s in students:
    if s["roll"] == search_roll:
        print("Student Found:")
        print("Roll Number:", s["roll"])
        print("Name:", s["name"])
        print("Branch:", s["branch"])
        print("Marks:", s["marks"])
        found = True
        break

if not found:
    print("Student with roll number", search_roll, "not found")

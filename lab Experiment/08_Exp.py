# Create a database using lists and tuples. Each student record must contain
# roll number, name, branch, and CGPA. Store each record as a tuple inside a list.
# Display all records and search for a student using roll number.
# Conditions:
#   - Each record should be stored as a tuple.
#   - The complete database should be stored as a list.
#   - Roll numbers must be unique.

database = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    # Roll number must be unique
    while True:
        roll = int(input("Roll Number: "))
        duplicate = False
        for record in database:
            if record[0] == roll:
                duplicate = True
                break
        if duplicate:
            print("Roll number already exists! Enter a unique roll number.")
        else:
            break

    name = input("Name: ")
    branch = input("Branch: ")
    cgpa = float(input("CGPA: "))

    record = (roll, name, branch, cgpa)   # each record is a tuple
    database.append(record)                # database is a list

# Display all records
print("\nAll Student Records:")
print("Roll No\tName\tBranch\tCGPA")
for record in database:
    print(record[0], "\t", record[1], "\t", record[2], "\t", record[3])

# Search by roll number
search_roll = int(input("\nEnter roll number to search: "))
found = False
for record in database:
    if record[0] == search_roll:
        print("Student Found:", record)
        found = True
        break

if not found:
    print("Student with roll number", search_roll, "not found")

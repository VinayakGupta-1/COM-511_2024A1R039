# Write a program to implement an employee management system using classes, instances and inheritance.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


name = input("Enter name: ")
emp_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))
department = input("Enter department: ")

m = Manager(name, emp_id, salary, department)

print("\nEmployee Details:")
m.display()
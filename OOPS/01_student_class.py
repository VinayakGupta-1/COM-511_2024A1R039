"""
Create a class and object: Student details
Problem: Create a student class to store a student's name, roll number.
Create an object of the class and display the details of
"""
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

# Create an object of the Student class
student1 = Student("Vinayak",39)
student2 = Student("Pushkar", 45)

# Display the details of the students
student1.display_details()
student2.display_details()
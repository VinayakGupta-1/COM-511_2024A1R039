# Program to take student details like name, roll numer and hostel status from user. Typecast them into appropriate types and print them along with their detected type
name = input("Enter Name : ")
roll = input("Enter roll no : ")
cgpa = input("Enter CGPA : ")
hostel = input("Enter Hostel Status : ")

print(f"Name : {name} {type(str(name))}, Roll no : {roll} {type(int(roll))}, CGPA : {cgpa} {type(float(cgpa))}, Hostel Status : {hostel} {type(str(hostel))}")
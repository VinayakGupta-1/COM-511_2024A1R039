# Write a python program to take a student name and roll number , then generarte a user name using the first 3 letters of the name and lst 2 digit of the roll number
name = input("Enter student name: ")
roll = input("Enter roll number: ")

username = name[:3] + roll[-2:]

print("Username:", username)
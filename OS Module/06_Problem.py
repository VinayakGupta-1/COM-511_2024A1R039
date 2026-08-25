# Write a program to check if file / folder exist or not
import os

if os.path.isfile("01_Problem.py"):
    print("File Exist")
else:
    print("File does not exist")

if os.path.isdir("Practice"):
    print("Folder exist")
else:
    print("Folder does not exist")
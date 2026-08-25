# Write a python program to print the contents of a directory uding the os module. Search online for function which does that.
import os

folder = os.listdir(".")

for file in folder:
    print(file)

#Write a python program to take a student full name and display
 # Total number of characters, last characters, first character, Name in uppercase

name = input("Enter student full name: ")

print("Total number of characters:", len(name))
print("Last character:", name[-1])
print("First character:", name[0])
print("Name in uppercase:", name.upper())
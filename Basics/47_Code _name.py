# take name , ranch and year . Generate a code name using string concatenation , slicing and repetation
name = input("Enter your name: ")
branch = input("Enter your branch: ")   
year = input("Enter your year: ")

code_name = name[:3].lower() + branch[:3].lower() + year[-2:].lower()
print("Generated code name:", code_name) 
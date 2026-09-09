# Take student full name and roll number. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll number.43

full_name = input("Enter your full name: ")
roll_number = input("Enter your roll number: ")
first_letter = full_name.split()[0][:3].lower()
last_letter = full_name.split()[-1][:3].lower()
roll_suffix = roll_number[-3:].lower()

email = first_letter + last_letter + roll_suffix
print("Generated email:", email)
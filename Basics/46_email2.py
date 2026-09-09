# Take an email address and print username , domain , and reserved domain.

email = input("Enter your email address: ")

at_position = email.find("@")
username = email[:at_position]
domain = email[at_position + 1:]
reserved_domain = domain.split(".")[0]

print("Username:", username)
print("Domain:", domain)
print("Reserved Domain:", reserved_domain)
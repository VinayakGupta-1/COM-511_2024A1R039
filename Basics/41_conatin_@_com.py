#  Take an email address and check whether it contains @ and .com.
email = input("Enter an email address: ")
is_valid_email = ("@" in email) and (".com" in email)
print("Is email valid?", is_valid_email)
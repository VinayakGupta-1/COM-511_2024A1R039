"""
Write a Python program to manage a small library using a dictionary. The program must repeatedly allow the user to add books, issue books, return books, and display the current book record.

Conditions
    Store book title as the key and available copies as the value.
    A book can be issued only if it exists and at least one copy is available.
    Return a book only if it already exists in the library record.
    Book names should work regardless of uppercase or lowercase letters.

"""

library = {}

while True:
    print("\n1. Add book")
    print("2. Issue book")
    print("3. Return book")
    print("4. Display books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ").strip().lower()
        copies = int(input("Enter number of copies: "))
        while copies < 1:
            print("Copies must be at least 1.")
            copies = int(input("Enter number of copies: "))

        library[title] = library.get(title, 0) + copies
        print("Book added successfully.")

    elif choice == "2":
        title = input("Enter book title to issue: ").strip().lower()

        if title not in library:
            print("Book not found in library.")
        elif library[title] == 0:
            print("No copies available right now.")
        else:
            library[title] -= 1
            print("Book issued successfully.")

    elif choice == "3":
        title = input("Enter book title to return: ").strip().lower()

        if title in library:
            library[title] += 1
            print("Book returned successfully.")
        else:
            print("This book does not belong to the library.")

    elif choice == "4":
        if not library:
            print("Library is empty.")
        else:
            print("Book record:")
            for title, copies in library.items():
                print(title.title(), ":", copies)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")

# Library Management System (CLI)

books = {}  # {book_name: status}

def add_book():
    name = input("Enter book name: ").strip().lower()
    if name in books:
        print("Book already exists!")
    else:
        books[name] = "available"
        print("Book added successfully!")

def view_books():
    if not books:
        print("No books available.")
        return

    print("\n--- Book List ---")
    for book, status in books.items():
        print(f"{book} -> {status}")

def issue_book():
    name = input("Enter book name to issue: ").strip().lower()

    if name not in books:
        print("Book not found!")
    elif books[name] == "issued":
        print("Book already issued!")
    else:
        books[name] = "issued"
        print("Book issued successfully!")

def return_book():
    name = input("Enter book name to return: ").strip().lower()

    if name not in books:
        print("Book not found!")
    elif books[name] == "available":
        print("Book was not issued!")
    else:
        books[name] = "available"
        print("Book returned successfully!")

def menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Exiting system... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
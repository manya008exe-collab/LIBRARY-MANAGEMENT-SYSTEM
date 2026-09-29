print("===== LIBRARY MANAGEMENT SYSTEM =====")

books = []

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Display Available Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Display All Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = [book_id, title, author, "Available"]
        books.append(book)

        print("Book added successfully.")

    elif choice == "2":
        search = input("Enter title or author to search: ").lower()
        found = False

        for book in books:
            if search in book[1].lower() or search in book[2].lower():
                print(book[0], "|", book[1], "|", book[2], "|", book[3])
                found = True

        if found == False:
            print("Book not found.")

    elif choice == "3":
        found = False

        print("\n===== AVAILABLE BOOKS =====")

        for book in books:
            if book[3] == "Available":
                print(book[0], "|", book[1], "|", book[2])
                found = True

        if found == False:
            print("No available books.")

    elif choice == "4":
        book_id = input("Enter book ID to issue: ")
        student = input("Enter student name: ")

        found = False

        for book in books:
            if book[0] == book_id:
                found = True

                if book[3] == "Available":
                    book[3] = "Issued to " + student
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

        if found == False:
            print("Book not found.")

    elif choice == "5":
        book_id = input("Enter book ID to return: ")
        found = False

        for book in books:
            if book[0] == book_id:
                found = True

                if book[3] != "Available":
                    book[3] = "Available"
                    print("Book returned successfully.")
                else:
                    print("This book is already available.")

        if found == False:
            print("Book not found.")

    elif choice == "6":
        if len(books) == 0:
            print("No books found.")
        else:
            print("\n===== ALL BOOKS =====")

            for book in books:
                print(book[0], "|", book[1], "|", book[2], "|", book[3])

    elif choice == "7":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")

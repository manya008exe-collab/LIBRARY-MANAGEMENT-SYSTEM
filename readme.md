# Library Management System

## Project Overview

The **Library Management System** is a simple beginner-friendly Python command-line project designed to manage basic library activities.

The program allows the user to add books, search for books, display available books, issue books to students, return books, and display all books. The project uses a list to store book information while the program is running.

This project is created using basic Python concepts and is suitable for understanding how conditional statements, loops, lists, strings, and user input can be combined to build a practical application.

## Aim

The aim of this project is to create a simple Python-based library system that can manage basic book records and operations such as adding, searching, issuing, returning, and displaying books.

## Objectives

- Add new books to the library.
- Store book ID, title, author, and availability status.
- Search for a book using its title or author.
- Display currently available books.
- Issue a book to a student.
- Return an issued book.
- Display all books and their current status.
- Provide a simple menu-driven interface.

## Features

### 1. Add Book

The user can add a new book by entering:

- Book ID
- Book title
- Author name

The book is added to the library with the status **Available**.

### 2. Search Book

The user can search for a book using:

- Book title
- Author name

The search is not case-sensitive.

If a matching book is found, its ID, title, author, and status are displayed.

### 3. Display Available Books

This option displays only the books whose current status is **Available**.

If there are no available books, the program displays a suitable message.

### 4. Issue Book

A book can be issued by entering:

- Book ID
- Student name

If the book is available, its status changes to:

```text
Issued to <student name>
```

If the book is already issued, the program informs the user.

### 5. Return Book

The user can return an issued book by entering its Book ID.

After returning, the status of the book changes back to:

```text
Available
```

If the book is already available, the program displays a message.

### 6. Display All Books

This option displays all books stored in the system along with:

- Book ID
- Book title
- Author
- Current status

If no books have been added, the program displays a message saying that no books were found.

## Menu

The program provides the following menu:

```text
1. Add Book
2. Search Book
3. Display Available Books
4. Issue Book
5. Return Book
6. Display All Books
7. Exit
```

## Data Stored

Each book is stored as a list containing four values:

```text
[Book ID, Book Title, Author, Status]
```

For example:

```text
["B101", "Python Basics", "John Smith", "Available"]
```

When the book is issued, the status changes to:

```text
"Issued to Rahul"
```

## Python Concepts Used

This project uses basic Python programming concepts:

- `input()` for user input
- `print()` for displaying information
- Variables
- Lists
- Strings
- `while` loop
- `for` loop
- `if`, `elif`, and `else`
- Comparison operators
- String methods such as `.lower()`
- `len()` for checking the number of books

## Requirements

- Python 3.x
- No external Python libraries are required.

## Environment Setup

1. Install Python 3 on your computer.
2. Open the project folder in VS Code or a terminal.
3. Make sure `main.py` is present in the project folder.
4. Run the program using the command given below.

## How to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## How the Program Works

The program runs continuously using a `while` loop and displays the main menu.

The user selects an option:

1. **Add Book** — adds a new book to the list.
2. **Search Book** — searches books by title or author.
3. **Display Available Books** — shows books whose status is Available.
4. **Issue Book** — changes the selected book's status to the student who received it.
5. **Return Book** — changes an issued book's status back to Available.
6. **Display All Books** — displays every book and its status.
7. **Exit** — stops the program.

If an invalid menu option is entered, the program displays:

```text
Invalid choice.
```

## Example

### Adding a Book

```text
1. Add Book
2. Search Book
3. Display Available Books
4. Issue Book
5. Return Book
6. Display All Books
7. Exit

Enter your choice: 1
Enter book ID: B101
Enter book title: Python Basics
Enter author name: John Smith

Book added successfully.
```

### Issuing a Book

```text
Enter your choice: 4
Enter book ID to issue: B101
Enter student name: Rahul

Book issued successfully.
```

The book status becomes:

```text
Issued to Rahul
```

### Returning a Book

```text
Enter your choice: 5
Enter book ID to return: B101

Book returned successfully.
```

The status changes back to:

```text
Available
```

## Testing

The program can be tested using different operations and inputs, such as:

- Adding one or multiple books.
- Searching for an existing book.
- Searching for a book that does not exist.
- Displaying available books.
- Issuing an available book.
- Trying to issue an already issued book.
- Returning an issued book.
- Trying to return an already available book.
- Displaying all books.
- Selecting an invalid menu option.

## Error and Status Messages

The program provides basic messages for different situations:

- `Book added successfully.`
- `Book not found.`
- `No available books.`
- `Book issued successfully.`
- `Book is already issued.`
- `Book returned successfully.`
- `This book is already available.`
- `No books found.`
- `Invalid choice.`

## Limitations

- Book data is stored only while the program is running.
- Data is not saved permanently to a file or database.
- The project uses a command-line interface.
- There is no separate login system for students or librarians.
- The system handles basic library operations only.

## Future Scope

The project can be improved in the future by adding:

- Permanent file storage.
- Database support.
- Student records.
- Librarian login.
- Due dates and return dates.
- Fine calculation.
- Graphical user interface.
- More advanced search options.
- Book categories and author management.

## Project Structure

```text
Library_Management_System/
│
├── main.py
└── README.md
```

### `main.py`

Contains the complete Python program and all library management operations.

### `README.md`

Contains information about the project, its features, requirements, working, testing, and future scope.

## Conclusion

The **Library Management System** demonstrates how basic Python programming concepts can be used to create a useful command-line application.

The project provides the basic operations required to manage books, including adding, searching, issuing, returning, and displaying books. It is designed as a simple Python project for learning and practicing fundamental programming concepts.

## Author

**Name:** Manya Singh   
**Academic Number:** 26BCE10914
**Course:** Python Essentials

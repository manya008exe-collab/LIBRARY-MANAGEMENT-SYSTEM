# Library Management System

## 1. Project Overview

Library Management System is a simple Python program made to manage books. It allows the user to add books, search for books, check available books, issue books, return books, and see all books.

The project uses basic Python concepts like lists, loops, conditions, strings, and user input.

## 2. Features

- Add a new book with book ID, title, and author.
- Search for a book using its title or author.
- Display all available books.
- Issue a book to a student.
- Return an issued book.
- Display all books with their current status.
- Shows simple messages for wrong or invalid choices.

## 3. Technologies / Tools Used

- **Programming Language:** Python 3
- **Editor:** VS Code
- **Version Control:** Git and GitHub
- **Libraries:** No external libraries are used.

## 4. Installation and Running

### Step 1: Install Python

Install Python 3 on the computer.

### Step 2: Open the Project

Open the project folder in VS Code or a terminal.

### Step 3: Check the Files

Make sure the project contains:

```text
Library_Management_System/
│
├── main.py
└── README.md
```

### Step 4: Run the Program

Open the terminal in the project folder and run:

```bash
python main.py
```

If `python` does not work, use:

```bash
python3 main.py
```

## 5. Testing

The program can be tested using the following operations:

- Add one or more books.
- Search for an existing book.
- Search for a book that does not exist.
- Check the available books.
- Issue an available book.
- Try to issue a book that is already issued.
- Return an issued book.
- Try to return a book that is already available.
- Display all books.
- Enter an invalid menu choice.

### Example

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



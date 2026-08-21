class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}")
        print(f"Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books: None")
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully!")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully!")

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found!")
            return

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.available:
            book.available = False
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print("Book is already borrowed!")

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found!")
            return

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)
            book.available = True
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This patron did not borrow this book.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\n----- Library Books -----")
            for book in self.books.values():
                book.display()

    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
        else:
            print("\n----- Registered Patrons -----")
            for patron in self.patrons.values():
                patron.display()


# ---------------- Main Program ----------------

library = Library()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Books")
    print("2. Register Patrons")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("How many books do you want to add? "))
        for i in range(n):
            print(f"\nEnter details for Book {i+1}")
            book_id = input("Book ID: ")
            title = input("Book Title: ")
            author = input("Author Name: ")
            library.add_book(Book(book_id, title, author))

    elif choice == 2:
        n = int(input("How many patrons do you want to register? "))
        for i in range(n):
            print(f"\nEnter details for Patron {i+1}")
            patron_id = input("Patron ID: ")
            name = input("Patron Name: ")
            library.register_patron(Patron(patron_id, name))

    elif choice == 3:
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.borrow_book(patron_id, book_id)

    elif choice == 4:
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.return_book(patron_id, book_id)

    elif choice == 5:
        library.display_books()

    elif choice == 6:
        library.display_patrons()

    elif choice == 7:
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

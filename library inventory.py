import json
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(filename="library.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def to_dict(self):
        return self.__dict__

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"

class LibraryInventory:
    def __init__(self, catalog_file="catalog.json"):
        self.catalog_file = Path(catalog_file)
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if self.catalog_file.exists():
                with open(self.catalog_file, "r") as f:
                    data = json.load(f)
                self.books = [Book(**book) for book in data]
                logging.info("Catalog loaded successfully.")
            else:
                self.books = []
        except Exception as e:
            self.books = []
            logging.error(f"Error loading catalog: {e}")

    def save_books(self):
        try:
            with open(self.catalog_file, "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
            logging.info("Catalog saved successfully.")
        except Exception as e:
            logging.error(f"Error saving catalog: {e}")

    def add_book(self, title, author, isbn):
        if any(book.isbn == isbn for book in self.books):
            print("Book with this ISBN already exists.")
            return False
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        print("Book added successfully.")
        return True

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)

    def display_all(self):
        if not self.books:
            print("No books in the catalog.")
        for book in self.books:
            print(book)

def main():
    inventory = LibraryInventory()
    while True:
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book by Title")
        print("6. Search Book by ISBN")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            inventory.add_book(title, author, isbn)
        elif choice == "2":
            isbn = input("Enter ISBN to issue: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_books()
                print("Book issued successfully.")
            else:
                print("Book not found or already issued.")
        elif choice == "3":
            isbn = input("Enter ISBN to return: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_books()
                print("Book returned successfully.")
            else:
                print("Book not found or not issued.")
        elif choice == "4":
            inventory.display_all()
        elif choice == "5":
            title = input("Enter title to search: ").strip()
            books = inventory.search_by_title(title)
            if books:
                for book in books:
                    print(book)
            else:
                print("No book found with the title.")
        elif choice == "6":
            isbn = input("Enter ISBN to search: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book:
                print(book)
            else:
                print("No book found with the ISBN.")
        elif choice == "7":
            print("Exiting the Library Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

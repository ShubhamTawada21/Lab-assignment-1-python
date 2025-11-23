class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.borrowed_count = 0

    def is_available(self):
        return self.quantity > self.borrowed_count

    def borrow(self):
        if self.is_available():
            self.borrowed_count += 1
            return True
        return False

    def return_book(self):
        if self.borrowed_count > 0:
            self.borrowed_count -= 1
            return True
        return False

    def display_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.quantity - self.borrowed_count}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available right now.")

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} doesn't have '{book.title}' borrowed.")

    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                book.display_info()
        else:
            print(f"{self.name} has no borrowed books.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered.")

    def find_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                book.display_info()
        else:
            print("No books in the library.")

    def list_users(self):
        if self.users:
            print("Registered Users:")
            for user in self.users:
                print(f"ID: {user.user_id}, Name: {user.name}")
        else:
            print("No registered users.")


def main():
    library = Library()

    # Adding sample books
    library.add_book(Book(1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 5))
    library.add_book(Book(2, "The Hobbit", "J.R.R. Tolkien", 3))
    library.add_book(Book(3, "1984", "George Orwell", 2))

    # Registering users
    library.register_user(User(1, "Alice"))
    library.register_user(User(2, "Bob"))

    while True:
        print("\nLibrary Management System Menu")
        print("1. List all books")
        print("2. List all users")
        print("3. Search book by title")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. View borrowed books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.list_books()

        elif choice == '2':
            library.list_users()

        elif choice == '3':
            title = input("Enter book title to search: ")
            found_books = library.find_book_by_title(title)
            if found_books:
                for book in found_books:
                    book.display_info()
            else:
                print("No books found with that title.")

        elif choice == '4':
            try:
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID to borrow: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                book = next((b for b in library.books if b.book_id == book_id), None)
                if user and book:
                    user.borrow_book(book)
                else:
                    print("Invalid user ID or book ID.")
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")

        elif choice == '5':
            try:
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID to return: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                book = next((b for b in library.books if b.book_id == book_id), None)
                if user and book:
                    user.return_book(book)
                else:
                    print("Invalid user ID or book ID.")
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")

        elif choice == '6':
            try:
                user_id = int(input("Enter user ID to view borrowed books: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                if user:
                    user.view_borrowed_books()
                else:
                    print("Invalid user ID.")
            except ValueError:
                print("Invalid input. Please enter numeric user ID.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

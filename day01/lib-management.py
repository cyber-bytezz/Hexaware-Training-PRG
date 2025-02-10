import time

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print(f'\n"{title}" is already in the library.')
        else:
            self.books[title] = {"author": author, "available": True}
            print(f'\nBook "{title}" by {author} has been added successfully.')

    def view_books(self):
        if not self.books:
            print("\nThe library is currently empty. Add some books first.")
            return

        print("\nLibrary Collection:")
        for title, details in self.books.items():
            status = "Available" if details["available"] else "Borrowed"
            print(f'- "{title}" by {details["author"]} ({status})')
        print()

    def borrow_book(self, title):
        if title in self.books and self.books[title]["available"]:
            self.books[title]["available"] = False
            print(f'\nYou have borrowed "{title}". Enjoy your reading.')
        elif title in self.books:
            print(f'\nSorry, "{title}" is already borrowed.')
        else:
            print(f'\nThe book "{title}" does not exist in the library.')

    def return_book(self, title):
        if title in self.books and not self.books[title]["available"]:
            self.books[title]["available"] = True
            print(f'\nThank you for returning "{title}".')
        elif title in self.books:
            print(f'\n"{title}" was not borrowed.')
        else:
            print(f'\n"{title}" is not in the library.')

def main():
    library = Library()

    print("\nWelcome to the Library Management System!")
    time.sleep(1)

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a Book")
        print("2. View Available Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("\nEnter book title: ").strip()
            author = input("Enter author's name: ").strip()
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            title = input("\nEnter the title of the book you want to borrow: ").strip()
            library.borrow_book(title)

        elif choice == "4":
            title = input("\nEnter the title of the book you want to return: ").strip()
            library.return_book(title)

        elif choice == "5":
            print("\nExiting Library System. Have a great day!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

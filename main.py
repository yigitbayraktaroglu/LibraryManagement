class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            book_info = book.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for book in books:
            if title_to_remove not in book:
                self.file.write(book)

        print(f"Book '{title_to_remove}' removed successfully.")

# Create an object named "lib" with the Library class
lib = Library()

# Create a menu to interact with the "lib" object
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

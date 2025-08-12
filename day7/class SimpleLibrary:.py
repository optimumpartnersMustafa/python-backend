class SimpleLibrary:
    def __init__(self):
        self.books = {} 

    def add_book(self, title):
        if title not in self.books:
            self.books[title] = False 
            print(f"'{title}' added.")
        else:
            print(f"'{title}' already exists.")

    def borrow_book(self, title):
        if title in self.books and not self.books[title]:
            self.books[title] = True
            print(f"'{title}' borrowed.")
        elif title in self.books and self.books[title]:
            print(f"'{title}' is already borrowed.")
        else:
            print(f"'{title}' not found.")

    def return_book(self, title):
        if title in self.books and self.books[title]:
            self.books[title] = False
            print(f"'{title}' returned.")
        elif title in self.books and not self.books[title]:
            print(f"'{title}' was not borrowed.")
        else:
            print(f"'{title}' not found.")

    def list_books(self):
        print("\nCurrent Library Books:")
        if not self.books:
            print("  No books in library.")
        for title, is_borrowed in self.books.items():
            status = "Borrowed" if is_borrowed else "Available"
            print(f"  - {title} ({status})")

if __name__ == "__main__":
    library = SimpleLibrary()
    library.add_book("The Cat in the Hat")
    library.add_book("Puss in the boots")

    library.list_books()

    library.borrow_book("The Cat in the Hat")
    library.borrow_book("The Cat in the Hat") 
    library.borrow_book("The Lorax") 

    library.list_books()

    library.return_book("Puss in the boots")
    library.return_book("The Cat in the Hat")

    library.list_books()

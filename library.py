class Library:
    # Stores all books using a dictionary with ISBN as the key (O(1) average lookup)
    def __init__(self):
        #Dictionary acts as a hash table for book storage
        self.books = {}

    def add_book(self, book):
        self.books[book.isbn] = book
    
    def display_books(self):
        if not self.books:
            print("No books available.")
            return        
        for book in self.books.values():
            status = "Available" if book.available else "Not Available"
            print(f"{book.title} - {book.author} ({book.year}) - {status}")

    def search_book(self, isbn):
        #Finds books from their ISBN number
        found_book = self.books.get(isbn)
        if found_book:
            print(f"\nBook found: {found_book.title} by {found_book.author}") 
        else:
            print("\nBook not found.")
        return found_book

    def borrow_book(self, isbn):
        #Allows a user to borrow a book if it is available
        book = self.search_book(isbn)
        if book and book.available:
            book.available = False
            print("You have borrowed the book:", book.title)
        else:
            print("Book is not available for borrowing.")
        return book

    def return_book(self, isbn):
        #User can return a borrowed book, making it available again.
        book = self.search_book(isbn)
        if book and not book.available:
            book.available = True
            print("You have returned the book:", book.title)
        elif book and book.available:
            print("This book was not borrowed.")
        return book
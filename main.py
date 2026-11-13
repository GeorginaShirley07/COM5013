class Book:
    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True

class Library:
    # Stores all books using a dictionary with ISBN as the key (O(1) average case)
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
            print(book.title)

    def search_book(self, isbn):
        #Finds books from their ISBN number
        return self.books.get(isbn, None)

    def borrow_book(self, isbn):
        #Allows a user to borrow a book if it is available
        book = self.search_book(isbn)
        if book and book.available:
            book.available = False
            print("You have borrowed the book:", book.title)
        else:
            print("Book is not available for borrowing.")

    def return_book(self, isbn):
        #User can return a borrowed book, making it available again.
        book = self.search_book(isbn)
        if book and not book.available:
            book.available = True
            print("You have returned the book:", book.title)
        else:
            print("This book was not borrowed or does not exist in the library.")

#Testing the Library and Book classes so far
library = Library()
book1 = Book("001", "Python Programming", "John Doe", 2020)
book2 = Book("002", "Data Structures", "Jane Smith", 2019)
library.add_book(book1)
library.add_book(book2)
library.display_books()
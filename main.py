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
        for book in self.books.values():
            print(book.title,book.author)

#Testing the Library and Book classes so far
library = Library()
book1 = Book("001", "Python Programming", "John Doe", 2020)
book2 = Book("002", "Data Structures", "Jane Smith", 2019)
library.add_book(book1)
library.add_book(book2)
library.display_books()
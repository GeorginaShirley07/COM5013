class Book:
    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True

book1 = Book("001", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book1.title)
print(book1.author)
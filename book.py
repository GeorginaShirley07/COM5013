from collections import deque

class Book:
    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True

        # Queue available for books currently unavailable
        self.waiting_list = deque()
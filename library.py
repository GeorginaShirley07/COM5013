from sorting import merge_sort
from datetime import datetime, timedelta

class Library:
    #Stores all books using a dictionary with ISBN as the key (O(1) average lookup)
    def __init__(self):
        #Dictionary acts as a hash table for book storage
        self.books = {}
        self.sorted_books = []

    def add_book(self,book):
        self.books[book.isbn] = book

    def add_new_book(self, book):
        #adds a book to the library, validating the isbn beforehand
        if not book.isbn:
            print("ISBN cannot be empty.")
            return False
        
        if book.isbn in self.books:
            print("A book with that ISBN already exists.")
            return False
        
        if len(book.isbn) != 10:
            print("ISBN has to be 10 digits.")
            return False
        
        self.books[book.isbn] = book
        self.insert_sorted(book)
        print(f"{book.title} added succesfully")
        return True

    def insert_sorted(self, new_book):
        #inserts the new book into the correct place in the library
        self.sorted_books.append(new_book)

        i = len(self.sorted_books) - 2
        while(i >= 0 and self.sorted_books[i].title.lower() > new_book.title.lower()):
            self.sorted_books[i + 1] = self.sorted_books[i]
            i -= 1
        self.sorted_books[i + 1] = new_book

    def display_books(self):
        if not self.books:
            print("No books available.")
            return        
        for book in self.books.values():
            status = "Available" if book.available else "Not Available"
            print(f"{book.isbn} - {book.title} - {book.author} ({book.year}) - {status}")
        print(f"Loaded {len(self.books)} books")

    def search_book(self, isbn):
        #Finds books from their ISBN number
        #avg time complexity O(1)
        #Hash table search is used since the books are stored in a dictionary. 
        found_book = self.books.get(isbn)
        if found_book:
            status = "available" if found_book.available else "not Available"
            print(f"\n{found_book.isbn} - {found_book.title} - {found_book.author} - {found_book.year} - {status}")
        else:
            print("\nBook not found.")
        return found_book

    def search_book_title(self, title_search):
        #Finds books from their title and adds them to a list to print
        #linear search used to check each book in the library for a match.
        #avg time complexity O(n)
        searched_books = []
        if title_search != "":
            for book in self.books.values():
                if title_search.lower() in book.title.lower():
                    searched_books.append(book)
            if searched_books:
                print(f"\n{len(searched_books)} books found:")
                for book in searched_books:
                    status = "Available" if book.available else "Not Available"
                    print(f"{book.isbn}: {book.title} - {book.author} ({book.year}) - {status}")
        else:
            print("\nNo books found with that title.")

    def borrow_book(self, isbn):
        #Allows a user to borrow a book if it is available
        book = self.search_book(isbn)
        if book and book.available:
            book.available = False
            book.due_date = datetime.now() + timedelta(days=14)
            print("You have borrowed the book:", book.title)
            print(f"Due Date: {book.due_date.strftime('%d/%m/%Y')}")
        else:
            print("Book is not available for borrowing.")
        return book

    def return_book(self, isbn):
        #User can return a borrowed book, making it available again.
        book = self.search_book(isbn)
        if book and not book.available:
            book.available = True
            print("You have returned the book:", book.title)
            print(f"Waiting list for {book.title}: {list(book.waiting_list)}")
            #check if there is a waiting list.
            if book.waiting_list:
                next_student = book.waiting_list.popleft()
                book.due_date = datetime.now() + timedelta(days=14)
                print(f"{next_student} has automatically been assigned {book.title} with a due date of {book.due_date.strftime('%d/%m/%Y')}")
                book.available = False  # The book is now borrowed by the next student
        elif book and book.available:
            print("This book was not borrowed.")

    def reserve_book(self, isbn, student_name):
        #allows a user to reserve a book if currently unavailable.
        book = self.search_book(isbn)
        if book and not book.available:
            book.waiting_list.append(student_name)
            print(f"{student_name} has reserved {book.title} and is added to the waiting list.")
        elif book and book.available:
            self.borrow_book(isbn)
        return book

    def view_waiting_list(self, isbn):
        #allows veiwing of the waiting list for a specific book.
        book = self.search_book(isbn)
        if book and not book.available:
            print(f"Waiting list for {book.title}: \n{list(book.waiting_list)}")
        return book

    def sort_books_by_title(self):
        #sorts the books using the merge sort from sorting.py
        book_list = list(self.books.values())
        searched_books = merge_sort(book_list)
        print("\nBooks sorted by author:")
        for book in searched_books:
            status = "Available" if book.available else "Not Available"
            print(f"{book.isbn} - {book.title} - {book.author} ({book.year}) - {status}")
        print("Books sorted alphabetically")
        return searched_books
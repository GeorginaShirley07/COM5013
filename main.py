from book import Book
from library import Library
from test_data import load_books

library = Library()
for book in load_books():
    library.add_book(book)

while True:
    print("\nLibrary Menu:")
    print("1. Display all books")
    print("2. Search for a book by ISBN")
    print("3. Search for a book by title")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Reserve a book")
    print("7. View waiting list for a book")
    print("8. Sort books by title")
    print("9. Add a book")
    print("10. Exit")
    choice = input("Enter your choice (1-9):")
  
    match choice:
        case "1":
            library.display_books()

        case "2":
            isbn = input("Enter ISBN to search: ")
            library.search_book(isbn)

        case "3":
            title = input("Enter title to search: ")
            library.search_book_title(title)

        case "4":
            isbn = input("Enter ISBN to borrow: ")
            library.borrow_book(isbn)

        case "5":
            isbn = input("Enter ISBN to return: ")
            library.return_book(isbn)

        case "6":
            isbn = input("Enter ISBN to reserve: ")
            student_name = input("Enter your name: ")
            library.reserve_book(isbn, student_name)

        case "7":
            isbn = input("Enter ISBN to view waiting list: ")
            library.view_waiting_list(isbn)

        case "8":
            library.sort_books_by_title()

        case "9":
            while True:
                #.strip() takes away any spaces in the input
                isbn = input("Enter ISBN:").strip()
                title = input("Enter title:").strip()
                authors = input("Enter authors:").strip()
                publication_date = int(input("Enter publication year:"))

                new_book = Book(isbn,title,authors,publication_date)
                if library.add_new_book(new_book):
                    break

        case "10":
            print("Exiting the library system.")
            break

        case _:
            print("Invalid choice. Please try again.")

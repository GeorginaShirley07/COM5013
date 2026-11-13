from book import Book
from library import Library
from test_data import sample_books

library = Library()
for book in sample_books:
    library.add_book(book)
library.display_books()

library.return_book("001")
print("\nAfter returning 'Python Programming':")
library.display_books()


from book import Book
from library import Library
from test_data import sample_books

library = Library()
for book in sample_books:
    library.add_book(book)




library.borrow_book("001")

library.reserve_book("001", "izzy")
library.reserve_book("001", "georgina")

library.return_book("001")
library.view_waiting_list("001")

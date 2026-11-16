import csv
from book import Book

def load_books():
    #loads books from a csv file and creates a list of book objects
    books = []
    with open("Library_test_data.csv", newline = "", encoding="utf-8") as csv_file:
        #reads each row using column headings
        reader = csv.DictReader(csv_file)

        #processes each row in file
        for row in reader:
            books.append(Book(
                row["isbn"],
                row["title"],
                row["authors"],
                row["publication_date"][-4:]))

    return books

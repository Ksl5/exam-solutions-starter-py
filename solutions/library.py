
books = [
    {"id": 1, "title": "Book A", "color": "green", "year": 1901},
    {"id": 2, "title": "Book B", "color": "red", "year": 1957},
    {"id": 3, "title": "Book C", "color": "green", "year": 1988},
    {"id": 4, "title": "Book D", "color": "blue", "year": 1923},
    {"id": 5, "title": "Book E", "color": "yellow", "year": 2017},
    {"id": 6, "title": "Book F", "color": "orange", "year": 2028}
]

if __name__ == "__main__":

    print("------------------")
    print("PROCESSING LIBRARY DATA...")
    print("------------------")
    #print(books)
    # breakpoint()

    #
    # QUESTION A
    #
    # Assuming the identifier, or "id" attribute, of each book is and will always be unique,
    # ... and assuming the order of books may vary,
    # ... "print" the title of the book whose identifier is equal to 4 (i.e. "Book D"):
for book in books:
    if book["id"] == 4:
        print(book["title"]) 


    #
    # QUESTION B
    #
    # Assuming the "year" attribute represents the year a given book was published,
    # ... "print" the number of books published before the year 1990 (i.e. 4):
early_books = [book for book in books if book["year"] < 1990]
print(len(early_books))
import csv

def get_books():
    books = []
    try:
        with open("books_list.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append({
                    "Title": row["Title"].lower(), 
                    "Author": row["Author"],
                    "Status": "available"
                })
    except FileNotFoundError:
        print("Error: The file books_list.csv was not found.")
    return books
def borrow_book(books, title):
    title = title.lower()
    for book in books:
        if book["Title"] == title:
            if book["Status"] == "available":
                book["Status"] = "borrowed"
                print(f"Success: You have borrowed '{title.title()}'.")
                return
            else:
                print(f"Error: '{title.title()}' is already borrowed.")
                return
    print(f"Error: '{title.title()}' not found in our library.")

def return_book(books, title):
    title = title.lower()
    for book in books:
        if book["Title"] == title:
            if book["Status"] == "borrowed":
                book["Status"] = "available"
                print(f"Success: You have returned '{title.title()}'.")
                return
            else:
                print(f"Note: '{title.title()}' was already in the library.")
                return
    print(f"Error: '{title.title()}' does not belong to this library.")
my_library = get_books()
borrow_book(my_library, "the great gatsby")
borrow_book(my_library, "the great gatsby")
return_book(my_library, "the great gatsby")
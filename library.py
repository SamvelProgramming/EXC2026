import csv
books = []
with open("books_list.csv", mode="r") as f:
    for row in csv.DictReader(f):
        books.append({"Title": row["Title"], "Author": row["Author"], "Status": "available"})

while True:
    user_input = input("[Search/Borrow/Return/Exit]: ").strip().lower()
    
    if user_input == 'exit':
        break
        
    if user_input in ['search', 'borrow', 'return']:
        query = input("Enter title or author: ").lower()
        matches = [b for b in books if query in b['Title'].lower() or query in b['Author'].lower()]
        
        if not matches:
            print("No matches found.")
            continue

        for i, b in enumerate(matches, 1):
            print(f"{i}) {b['Title']} - {b['Author']} [{b['Status']}]")
        
        if user_input == 'search':
            continue

        try:
            idx = int(input(f"Number to {user_input}: ")) - 1
            book = matches[idx]
            
            if user_input == 'borrow':
                if book['Status'] == 'available':
                    book['Status'] = 'borrowed'
                    print(f"Done. Borrowed '{book['Title']}'.")
                else:
                    print("Already out.")
            
            elif user_input == 'return':
                if book['Status'] == 'borrowed':
                    book['Status'] = 'available'
                    print(f"Done. '{book['Title']}' is back.")
                else:
                    print("Not currently borrowed.")
        except:
            print("Invalid selection.")
    else:
        print("Unknown command.")

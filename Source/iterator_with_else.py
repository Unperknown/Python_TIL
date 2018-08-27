books = []
exist = False

def store_status(book):
    for book in books:
        exist = True
        print("Just noticed that there's a lot of books in there!")
        break
    else:
        print("How dare they don't have any books?")

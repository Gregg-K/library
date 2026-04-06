# --- DATA ---
books = {}    # stores all books
members = {}  # stores all members

book_count = 1
member_count = 1

# CRUD 1 - Add a book
def add_book():
    global book_count

    print("\n-- Add Book --")
    title = input("Title: ")
    author = input("Author: ")

    book_id = "B" + str(book_count)
    books[book_id] = {
        "id": book_id,
        "title": title,
        "author": author,
        "borrowed_by": None   # RELATIONSHIP: stores a member ID when borrowed
    }

    book_count += 1
    print("Book added! ID:", book_id)




# Task 03 - Replace a Book Title
# Write a function called replace_book(books, old_book, new_book)
# that takes a list of book titles.
#
# If old_book is in the list, replace ONLY the first occurrence
# with new_book and return the updated list.
#
# If old_book is not in the list, return the original list unchanged.
#
# Example:
# replace_book(["Wonder", "Holes", "Matilda"], "Holes", "Hatchet")
# returns ["Wonder", "Hatchet", "Matilda"]

def replace_book(books, old_book, new_book):
    replace_book = [new_book if book == old_book else book for book in books]
    return replace_book
    pass


def main():
    books_input = input("Enter book titles separated by commas: ")
    books = [b.strip() for b in books_input.split(",") if b.strip() != ""]
    old_book = input("Enter the book to replace: ")
    new_book = input("Enter the new book title: ")

    updated_books = replace_book(books, old_book, new_book)
    print(updated_books)


if __name__ == "__main__":
    main()

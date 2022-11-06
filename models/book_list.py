from models.book import Book

book1 = Book("The Gruffalo", "J. Donaldson", "Children fantasy")
book2 = Book("Anne of The Green Gables", "L. M. Montgomery", "Novel")
book3 = Book("Naruto vol.1", "M. Kishimoto", "Adventure/ Fantasy/ Comedy/ Martial arts")

book_list = [book1, book2, book3]

def add_new_book(book):
    book_list.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in book_list:
        if book.title == book_title:
            book_to_delete = book
            break

    book_list.remove(book_to_delete)

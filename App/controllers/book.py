from App.models import Book
from App.database import db

def add_book(isbn, title, authorFname, authorLname, publiYear):
    newbook = Book(isbn = isbn, title = title, authorFname = authorFname, authorLname = authorLname, publiYear = publiYear):
    db.session.add(newbook)
    db.session.commit()
    return newbook

def get_all_books():
    return Book.query.all()


def get_all_book_by_title(title):
    books = Book.query.all()
    if not books:
        return []
    haul = [book.toJSON() for title in books]
    return haul

                                
def get_book_by_isbn(isbn):
    return Book.query.filter_by(isbn= isbn).first()

def get_book_by_Year

def get_book_author_by_Year(publiYear):
    books = Book.query.all()
    if not books:
        return []
    haul = [book.toJSON() for (publiYear && authorFname && authorLname) in books]
    return haul

def get_all_authors_json():
    books = Book.query.all()
    if not books:
        return []
    haul = [book.toJSON() for (authorFname && authorLname)  in books]
    return haul

#Not too sure about how to implement
def update_book(ISBN):
    book = get_book(ISBN)
    if book:
        book.ISBN = ISBN
        db.session.add(book)
        return db.session.commit()
    return None

from App.models import Book
from App.database import db

def add_book(authorFname, authorLname, title, publiYear, ISBN):
    newbook = Book(authorFname = authorFname, authorLname = authorLname, title = title, publiYear = publiYear, ISBN = ISBN):
    db.session.add(newbook)
    db.session.commit()
    return newbook

def get_book_by_author(authorFname, authorLname):
    return Book.query.filter_by(authorFname=authorFname && authorLname = authorLname).first()

def get_book(ISBN):
    return Book.query.get(ISBN)

def get_all_books():
    return Book.query.all()

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

from App.models import Book, Author
from sqlalchemy.exc import IntegrityError
from App.database import db

def add_book(isbn, title, authorName, publiYear, coAuthor):
    newbook = Book(isbn = isbn, title = title, authorName = authorName, publiYear = publiYear, coAuthor = coAuthor)
    try:
        db.session.add(newbook)
        db.session.commit()
    except IntegrityError: # attempted to insert a duplicate ISBN/Book
        db.session.rollback()
        return None
#    return 'Book added' 
    return newbook

def get_all_books():
    return Book.query.all()


def get_all_book_by_title(title):
    books = Book.query.all()
    if not books:
        return []
    haul = [book.toJSON() for title in books]
    return haul

def get_all_books_json():
    books = Book.query.all()
    if not books:
        return []
    books = [Book.toJSON() for Book in books]
    return books
                                
def get_book_by_isbn(isbn):
    books = Book.query.filter_by(isbn= isbn).first()
    if not books:
        return "Error: Book not found"
    return books.toJSON()


def get_book_by_Year(publiYear):
    books = Book.query.all()
    if not books:
        return []
    haul = [book.toJSON() for authorName in books]
    authorSort = [haul.toJSON() for publiYear in haul]
    return authorSort


def get_all_author_book_by_Year(publiYear, authorName):
    books = Book.query.all()
    if not books:
        return None
    haul = Book.query.filter(Book.publiYear == publiYear, Book.authorName == authorName).first()
    return ("Title: " + haul.title + "\n" + "ISBN: " + str(haul.isbn) + "\n" + "Author: " + haul.authorName + "\n" + "Co-Author/s: " + haul.coAuthor)

def get_all_author_book(author):
    books = Book.query.all()
    dump = []
    if not books:
        return None
    authorbooks = Book.query.filter_by(authorName = author).all()
    for authorbook in authorbooks:
        haul = ["Title: " + authorbook.title + " " + "ISBN: " + str(authorbook.isbn) + " " + "Author: " + authorbook.authorName + " " + "Co-Author/s: " + authorbook.coAuthor]
        dump.append(haul)
    if not dump:
        return None
    return dump

def specialFeature(author):
    books = Book.query.all()
    dump = []
    x = 0
    count = Book.query.count()
    if not books:
        return None

    authorbooks = Book.query.filter_by(authorName = author).all()
    for authorbook in authorbooks:

        haul = ["Title: " + authorbook.title + " " + "ISBN: " + str(authorbook.isbn) + " " + "Author: " + authorbook.authorName + " " + "Co-Author/s: " + authorbook.coAuthor]
        dump.append(haul)

        authorbooks = Book.query.filter_by(authorName = authorbook.coAuthor).all()
        if not authorbooks:
            continue
        for authorbook in authorbooks:
            haul = ["Title: " + authorbook.title + " " + "ISBN: " + str(authorbook.isbn) + " " + "Author: " + authorbook.authorName + " " + "Co-Author/s: " + authorbook.coAuthor]
            dump.append(haul)
            while x <= count:
                x = x + 1
                authorbooks = Book.query.filter_by(authorName = authorbook.coAuthor).all()
                if not authorbooks:
                    continue
                for authorbook in authorbooks:
                    haul = ["Title: " + authorbook.title + " " + "ISBN: " + str(authorbook.isbn) + " " + "Author: " + authorbook.authorName + " " + "Co-Author/s: " + authorbook.coAuthor]
                    dump.append(haul)
                
    if not dump:
        return None
    sorted = []
    for i in dump:
        if i not in sorted:
            sorted.append(i)
    return sorted

def get_all_authors_json():
    books = Book.query.all()
 
    dump = []
    sorted = []
    if not books:
        return None
    for book in books:
        haul = [book.authorName] #working now, just need to search list to remove duplicates
        dump.append(haul)
    sorted = []
    for i in dump:
        if i not in sorted:
            sorted.append(i)
    return sorted



def add_coAuthor(coAuthor, isbn): #not working how it's supposed to, it just replaces the author, if I try to add it will just make a string
    change = Book.query.filter_by(isbn = isbn).first()
    change.coAuthor = coAuthor
    db.session.commit()


#Not too sure about how to implement
def update_book(ISBN):
    book = get_book(ISBN)
    if book:
        book.ISBN = ISBN
        db.session.add(book)
        return db.session.commit()
    return None

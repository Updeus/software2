from App.database import db

class Book(db.Model):
    isbn = db.Column('isbn', db.Integer, primary_key=True)
    title =  db.Column('title', db.String(120), nullable=False)
    author = db.Column('authorName', db.String(120), db.ForeignKey('Author.authorName'))
    publiYear = db.Column(db.Integer, nullable=False)

    def toDict(self):
        return{
            "isbn":self.isbn,
            "title":self.title.toDict(),
            "author":self.author.toDict(),
            "publiYear":self.publiYear.toDict()
        }


class Author(db.Model):
    authorName = db.Column(db.String(120), primary_key=True)
    
    def toDict(self):
        return{
            "authorName":self.authorName.toDict()
        }

""" def __init__(self, isbn, title, authorFname, authorLname, publiYear):
        self.isbn = isbn
        self.title = title
        self.authorFname = authorFname
        self.authorLname = authorLname
        self.publiYear = publiYear """

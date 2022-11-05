from App.database import db

class Book(db.Model):
    isbn = db.Column('isbn', db.Integer, primary_key=True)
    title =  db.Column('title', db.String(120), nullable=False)
    authorName = db.Column('authorName', db.String(120), db.ForeignKey('author.authorName'))
    coAuthor = db.Column('coAuthor', db.String(120), db.ForeignKey('author.authorName'))
    publiYear = db.Column(db.Integer, nullable=False)


    def __init__(self, isbn, title, authorName, coAuthor, publiYear):
        self.isbn = isbn
        self.title = title
        self.authorName = authorName
        self.coAuthor = coAuthor
        self.publiYear = publiYear


    def toJSON(self):
        return{
            "isbn":self.isbn,
            "title":self.title,
            "authorName":self.authorName,
            "coAuthor":self.coAuthor,
            "publiYear":self.publiYear
        }

"""     def addAuthor(self, author):
        self.coAuthor.append(author)

 """

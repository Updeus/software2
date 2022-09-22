from App.database import db

class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String, nullable=False)
    authorFname = db.Column(db.String, nullable=False)
    authorLname = db.Column(db.String, nullable=False)
    publiYear = db.Column(db.Integer, nullable=False)
 
def __init__(self, isbn, title, authorFname, authorLname, publiYear):
        self.isbn = isbn
        self.title = title
        self.authorFname = authorFname
        self.authorLname = authorLname
        self.publiYear = publiYear

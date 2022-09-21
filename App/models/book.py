from App.database import db

class Book(db.Model):
    ISBN = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String, nullable=False)
    authorFname = db.Column(db.String, nullable=False)
    authorLname = db.Column(db.String, nullable=False)
    publiYear = db.Column(db.Date, nullable=False)
 
def __init__(self, ISBN, title, authorFname, authorLname, publiYear):
        self.ISBN = ISBN
        self.title = title
        self.authorFname = authorFname
        self.authorLname = authorLname
        self.publiYear = publiYear

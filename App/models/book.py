from App.database import db

class Book(db.Model):
    isbn = db.Column('isbn', db.Integer, primary_key=True)
    title =  db.Column('title', db.String(120), nullable=False)
    authorName = db.Column('authorName', db.String(120), nullable=False)
    publiYear = db.Column(db.Integer, nullable=False)
   
    def toDict(self):
        return{
            "isbn":self.isbn,
            "title":self.title.toDict(),
            "authorName":self.authorName.toDict(),
            "publiYear":self.publiYear.toDict()
        }


""" class Author(db.Model): #facing errors with this
    authorName = db.Column(db.String(120), primary_key=True)

    def toDict(self):
        return{
            "authorName":self.authorName.toDict()
        } """


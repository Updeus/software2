from App.database import db

class Author(db.Model): #facing errors with this
    authorName = db.Column(db.String(120), primary_key=True)
 #   coAuthor = db.Column(db.String(120), unique=True, nullable=True)

    def toJSON(self):
        return{
            "authorName":self.authorName.toJSON(),
    #        "coAuthor":self.coAuthor.toJSON()
        }
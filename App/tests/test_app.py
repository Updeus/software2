import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User, Book, Author
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user,
    add_book,
    get_all_authors_json,
    get_all_books_json,
    get_book_by_isbn,
    get_all_author_book,
    specialFeature
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass")
        assert user.username == "bob"

    # pure function no side effects or integrations called
    def test_toJSON(self):
        user = User("bob", "bobpass")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None, "username":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

class BookUnitTests(unittest.TestCase):
    def test_new_book(self):
        book = Book(100, "Science", "Jarod", "Henry", 2022)
        assert book.isbn == 100 and book.title ==  "Science" and book.authorName ==  "Jarod" and book.publiYear == 2022 and book.coAuthor == "Henry"

    def test_new_book_toJSON(self):
        book = Book(100, "Science", "Jarod", "Henry", 2022 )
        book_json = book.toJSON()
        self.assertDictEqual(book_json, {
            "isbn": 100,
            "title": "Science",
            "authorName": "Jarod",
            "publiYear": 2022,
            "coAuthor": "Henry"     
        })



"""
    Integration Tests
"""

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert authenticate("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)
    
    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"

class BooksIntegrationTests(unittest.TestCase):

    def test_create_book(self):
        book = add_book(100, "Science", "Jarod", 2022, "Henry") 
        assert book.isbn == 100 and book.title ==  "Science" and book.authorName ==  "Jarod" and book.publiYear == 2022 and book.coAuthor == "Henry"
    
    def test_get_all_authors_json(self):
        authors = get_all_authors_json();
        self.assertListEqual([['Jarod']], authors) 

    def test_get_all_books(self):
        books_json = get_all_books_json()
        self.assertListEqual([{"isbn":100, "title":"Science", "authorName":"Jarod", "publiYear": 2022, "coAuthor": "Henry"}], books_json)

    def test_get_books_by_isbn(self):
        books_json = get_book_by_isbn(100)
        assert books_json == {
            "authorName": "Jarod",
            "coAuthor": "Henry",
            "isbn": 100,
            "publiYear": 2022,
            "title": "Science"
            }

    def test_get_books_by_author(self):
        authorBooks = specialFeature("Jarod")
        self.assertListEqual([['Title: Science ISBN: 100 Author: Jarod Co-Author/s: Henry']], authorBooks)

    def test_specialfeature(self):
        authorBooks = get_all_author_book("Jarod")
        self.assertListEqual([['Title: Science ISBN: 100 Author: Jarod Co-Author/s: Henry']], authorBooks)

    
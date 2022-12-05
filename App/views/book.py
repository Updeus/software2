import json
from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
  add_book,
  get_all_books,
  get_all_books_json,
  get_all_book_by_title,
  get_book_by_isbn,
  get_book_by_Year,
  get_all_author_book_by_Year,
  get_all_authors_json,
  get_all_author_book,
  specialFeature,
  update_book
)

book_views = Blueprint('book_views', __name__, template_folder='../templates')

@book_views.route('/api/books', methods=['GET'])
def book_page():
    books = get_all_books_json()
    return jsonify(books) #Jsonify might not work for some things, may have to import a new library called jsonpickle
    

@book_views.route('/api/books/authors', methods=['GET'])
def authors_page():
    authors = get_all_authors_json()
    return jsonify(authors)

@book_views.route('/api/books/authors/', methods=['POST'])
@jwt_required()
def show_Author_Books():
    data = request.get_json()
    authorName =  data['authorName']
    authorBooks = get_all_author_book(authorName)
    if authorBooks is None:
        return jsonify('No books by this author!')
    return jsonify(authorBooks)

@book_views.route('/api/specialFeature/', methods=['POST'])
@jwt_required()
def showSpecialFeature():
    data = request.get_json()
    authorName =  data['authorName']
    authorBooks = specialFeature(authorName)
    if authorBooks is None:
        return jsonify('No books by this author!')
    return jsonify(authorBooks)

@book_views.route('/api/books/', methods=['POST'])
@jwt_required()
def showBook():
    data = request.get_json()
    isbn = data['isbn']
    response = jsonify(get_book_by_isbn(isbn))
    return jsonify('Error: Book not found') if response is None else response

@book_views.route('/api/books/createbook', methods=['POST'])  #Create book route
@jwt_required() #remove if there's problems
def createbook():
    data = request.get_json()
    if book := add_book(
        isbn=data['isbn'],
        title=data['title'],
        authorName=data['authorName'],
        publiYear=data['publiYear'],
        coAuthor=data['coAuthor'],
    ):
        returnString = data['title'] + " added!"
        return returnString, 201
    return jsonify({"error": "Book not added"}), 400

@book_views.route('/static/books')
def static_book_page():
  return send_from_directory('static', 'static-book.html')

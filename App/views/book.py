import json
from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
  add_book,
  get_all_books,
  get_all_book_by_title,
  get_book_by_isbn,
  get_book_by_Year,
  get_all_author_book_by_Year,
  get_all_authors_json,
  update_book
)

book_views = Blueprint('book_views', __name__, template_folder='../templates')

@book_views.route('/books', methods=['GET'])
def book_page():
    books = get_all_books()
    return json.dumps(books)

@book_views.route('/api/books')
def client_app():
    books = get_all_books()
    return books
  
@book_views.route('/static/books')
def static_book_page():
  return send_from_directory('static', 'static-book.html')

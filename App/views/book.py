from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
  
)

book_views = Blueprint('book_views', __name__, template_folder='../templates')


@book_views.route('/books', methods=['GET'])
def book_page():
    books = get_all_books()
    return render_template('users.html', books=books)

@user_views.route('/api/books')
def client_app():
    books = get_all_books_json()
    return jsonify(books)

@user_views.route('/static/books')
def static_book_page():
  return send_from_directory('static', 'static-book.html')

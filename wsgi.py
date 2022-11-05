import click, pytest, sys
from flask import Flask, jsonify
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( 
    create_user, 
    get_all_users_json, 
    get_all_users, 
    add_book, 
    get_all_books_json,
    get_all_book_by_title,
    get_book_by_isbn,
    get_book_by_Year,
    get_all_books,
    get_all_author_book_by_Year,
    get_all_authors_json,
    get_all_author_book,
    add_coAuthor
    )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 
# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
 #   if format == 'string':
  #      print(get_all_users())
  #  else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)




book_cli = AppGroup("book", help='Book object commands')

@book_cli.command("create", help="Creates a book entry")
@click.argument("isbn")
@click.argument("title")
@click.argument("author")
@click.argument("year")
@click.argument("coauthor")

def add_book_com(isbn, title, author, year, coauthor): #For some god forsaken reason the cli commands dont work if you have a capital letter in the variable name, so remember this :(
    add_book(isbn, title, author, year, coauthor)
    print(f'{title} added!')

@book_cli.command("get-books")
def get_books_com():
    print(get_all_books_json())

@book_cli.command("get-authorBookByYear")
@click.argument("publiYear")
@click.argument("authorName")

def get_all_author_book_by_Year_com(publiyear, authorname):
    print(get_all_author_book_by_Year(publiyear, authorname))

@book_cli.command("add_coAuthor")
@click.argument("coauthor")
@click.argument("isbn")

def add_coAuthor_com(coauthor, isbn):
    add_coAuthor(coauthor, isbn)
    print(f'{coauthor} added!')

app.cli.add_command(book_cli)

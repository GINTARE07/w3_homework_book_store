from flask import render_template

from app import app
from models.book import Book
from models.book_list import book_list

@app.route('/book')
def index():
    return render_template("index.html", book_list= book_list)


@app.route('/book/<index>')
def children_book():
  children_book = book1
  
  return render_template('order.html', book=children_book)


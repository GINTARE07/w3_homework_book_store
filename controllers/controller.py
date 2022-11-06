from flask import render_template, request, redirect

from app import app
from models.book import Book
from models.book_list import book_list, add_new_book, delete_book

@app.route('/book')
def index():
    return render_template("index.html", book_list= book_list)


@app.route('/book/<index>')
def book(index):
  return render_template('book1.html', book = book_list[int(index)])
  
  return render_template('order.html', book=children_book)

@app.route('/book', methods = ['POST'])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_new_book(new_book)

    return  redirect('/books') 
    # return render_template('index.html', title='Library', book=book)
@app.route('/events/delete/<title>', methods=['POST'])
def delete(title):
  delete_book(title)
  return redirect('/events')
   


 






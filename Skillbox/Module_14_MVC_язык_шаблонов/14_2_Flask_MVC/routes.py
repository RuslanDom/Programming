from flask import Flask, render_template, request
from models import get_all_books
from typing import List


app = Flask(__name__)


@app.route('/books')
def all_books():
    return render_template("index.html", books=get_all_books())

@app.route('/books/form', methods=['GET', 'POST'])
def books_form():
    if request.method == "POST":
        ...
    else:
        return render_template("add_book.html")


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
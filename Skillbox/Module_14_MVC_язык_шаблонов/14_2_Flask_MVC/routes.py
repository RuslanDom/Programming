from flask import Flask, render_template, request, url_for, redirect
from models import get_all_books, set_book
from typing import List

app = Flask(__name__)

# def get_html_table(books: List[dict]):
#     table = """
#     <table class="customTable">
#         <thead>
#             <tr>
#                 <th>ID</th>
#                 <th>Title</th>
#                 <th>Author</th>
#             </tr>
#         </thead>
#         <tbody>
#             {books_row}
#         </tbody>
#     </table>
#     """
#     rows = ""
#     for book in books:
#         rows += "<tr><td>{id}</td><td>{title}</td><td>{author}</td></tr>".format(
#             id=book["id"],
#             title=book["title"],
#             author=book["author"],
#         )
#     return table.format(books_row=rows)


@app.route('/books')
def all_books():
    return render_template("index.html", books=get_all_books())


@app.route('/books/form', methods=['GET', 'POST'])
def books_form():
    if request.method == "POST":
        form = request.form
        print(f"{form['book_title']}\n{form['author_name']}")
        # if (form["book_title"] and form["author_name"]):
        #     set_book(form["book_title"], form["author_name"])
        return redirect(url_for("books_form"))
    return render_template("add_book.html")


if __name__ == '__main__':
    # app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
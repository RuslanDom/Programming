from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{self.author}: {self.title} - {self.description}"


@app.route('/books/', methods=['GET'])
def get_books():
    books = Book.query.all()
    response = [{
                 "id": book.id,
                 "author": book.author,
                 "title": book.title,
                 "description": book.description}
                for book in books]
    return jsonify({"success": True, "books": response}), 200, {"Content-Type": "application/json"}


@app.route('/books/<string:title>',methods=['GET'])
def get_book(title):
    book = Book.query.filter_by(title=title).first()
    return jsonify({"id": book.id, "title": book.title, "author": book.author}), 200, {"Content-Type": "application/json"}


@app.route('/books/<int:id>',methods=['GET'])
def get_book_with_id(id):
    book = Book.query.get_or_404(id)
    return jsonify({"id": book.id, "title": book.title, "author": book.author}), 200, {"Content-Type": "application/json"}


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json(force=True)
    book = Book(author=data['author'],
             title=data['title'],
             description=data["description"]
             )
    db.session.add(book)
    db.session.commit()
    return {"success": f"Added book: id = {book.id}"}, 201, {"Content-Type": "application/json"}


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book not found"}, 404
    db.session.delete(book)
    db.session.commit()
    return {"success": f"book {book.id} is delete"}, 200, {"Content-Type": "application/json"}


@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    data = request.get_json(force=True)
    book = Book.query.get_or_404(id)
    if data.get("title"):
        book.title = data['title']
    if data.get("author"):
        book.author = data['author']
    if data.get("description"):
        book.description = data['description']
    db.session.commit()
    return jsonify({"success": f"book: {book.id} update"}), 202, {"Content-Type": "application/json"}


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
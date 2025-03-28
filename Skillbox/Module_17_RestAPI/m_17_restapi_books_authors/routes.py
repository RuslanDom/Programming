import sqlite3
from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError

from models import (
    DATA,
    get_all_books,
    init_db,
    init_author_table,
    add_book,
    update_book_by_id,
    delete_book_by_id,
    gets_the_book_by_id,
    patch_book,
    get_all_authors,
    add_author,
    get_all_books_by_author_id,
    delete_author_with_books,
    refactoring_author_name
)
from schemas import BookSchema, AuthorSchema

app = Flask(__name__)
api = Api(app)


class BookList(Resource):
    def get(self) -> tuple[list[dict], int]:
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self) -> tuple[dict, int]:
        data = request.json
        schema = BookSchema()
        try:
            data['author'] = refactoring_author_name(data['author'])
            book = schema.load(data)
            post_book = add_book(book)
            return schema.dump(post_book), 201
        except ValidationError as exc:
            return exc.messages, 400


class BookID(Resource):
    def get(self, id: int) -> tuple[dict, int]:
        schema = BookSchema()
        return schema.dump(gets_the_book_by_id(id)), 200

    def put(self, id: int) -> tuple[dict, int]:
        data = request.json
        schema = BookSchema()
        try:
            data['author'] = refactoring_author_name(data['author'])
            book = schema.load(data)
            book = update_book_by_id(book, id)
            return schema.dump(book), 200
        except ValidationError as exc:
            return exc.messages, 400

    def patch(self, id: int) -> tuple[dict, int]:
        data = request.json

        schema = BookSchema()
        if "author" in data.keys():
            print("IF AUTHOR")
            data["author"] = refactoring_author_name(data["author"])

        book = schema.load(data, partial=True)
        response = patch_book(book, id)
        if response:
            return schema.dump(response), 200
        else:
            return {"error": "Not found"}, 404


    def delete(self, id: int) -> tuple[str, int]:
        response = delete_book_by_id(id)
        return response


class AuthorList(Resource):
    def get(self) -> tuple[list[dict], int]:
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True), 200

    def post(self) -> tuple[dict, int]:
        data = request.json
        schema = AuthorSchema()
        try:
            author = schema.load(data)
            post_author = add_author(author)
            return schema.dump(post_author), 201
        except ValidationError as exc:
            return exc.messages, 400

class AuthorID(Resource):
    def get(self, id: int) -> tuple[dict, int]:
        schema = BookSchema()
        return schema.dump(get_all_books_by_author_id(id), many=True), 200

    def delete(self, id: int) -> tuple[dict, int]:
        response = delete_author_with_books(id)
        return response



api.add_resource(BookList, '/api/books')
api.add_resource(BookID, '/api/books/<int:id>')
api.add_resource(AuthorList, '/api/authors')
api.add_resource(AuthorID, '/api/authors/<int:id>')

if __name__ == '__main__':
    try:
        init_author_table(initial_records=DATA)
        init_db(initial_records=DATA)
    except sqlite3.Error as exc:
        print(exc)
    app.run(debug=True)

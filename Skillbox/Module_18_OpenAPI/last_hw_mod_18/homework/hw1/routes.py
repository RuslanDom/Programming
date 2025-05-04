import functools
import json
from typing import Callable

from flask import Flask, request
from flask_restx import Api, Resource
from models import *
from schemas import BookSchema, AuthorSchema, ValidationError
from flasgger import Swagger, APISpec, swag_from
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from swagger_files.spec_dict import *
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)
api = Api(app)
spec = APISpec(
    title='Books API',
    version='1.0.0',
    openapi_version='2.0.0',
    plugins=[
        MarshmallowPlugin(),
        FlaskPlugin()
    ]
)

def swagger_decorator(_func=None, *, path) -> Callable:
    def wrapper(func: Callable) -> Callable:
        with open(path, 'r') as f:
            new_file = json.load(f)
        @swag_from(new_file)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapped
    if _func is None:
        return wrapper
    return wrapper(_func)




@api.route('/api/books', endpoint='books')
class Books(Resource):
    @swag_from("swagger_files/get_books.yml")
    def get(self):
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True)

    @swag_from("swagger_files/add_book.yml")
    def post(self):
        data = request.json
        schema = BookSchema()
        data["author"]: int = exists_author(refactoring_author_name(data['author']))
        try:
            book = schema.load(data)
            result = add_book(book)
            return schema.dump(result), 201
        except ValidationError as e:
            return schema.dump(e), 400


@api.route('/api/books/<int:id>', endpoint='books/id')
class Book(Resource):
    @swag_from("swagger_files/get_book_by_id.yml")
    def get(self, id: int):
        schema = BookSchema()
        return schema.dump(get_book_by_id(id)), 200

    @swag_from("swagger_files/put_book.yml")
    def put(self, id: int):
        schema = BookSchema()
        data: Book = schema.load(request.json)  # Десериализовали в объект python
        book = put_updated_book(data, id)
        return schema.dump(book), 200  # Сериализуем python объект в потоковые данные

    @swag_from("swagger_files/patch_book.yml")
    def patch(self, id: int):
        schema = BookSchema()
        data: Book = schema.load(request.json, partial=True)
        book = patch_book(data, id)
        return schema.dump(book), 200

    @swag_from("swagger_files/delete_book.yml")
    def delete(self, id: int):
        result = delete_book(id)
        if result:
            return result, 404
        return {}, 204


@api.route('/api/authors', endpoint='authors')
class Authors(Resource):
    @swagger_decorator(path="swagger_files/get_authors.json")
    def get(self):
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True), 200

    @swagger_decorator(path="swagger_files/add_author.json")
    def post(self):
        data = request.json
        schema = AuthorSchema()
        try:
            author: Author = schema.load(data)  # Десериализация потоковых данных в объект python
            result = add_author(author)
            return schema.dump(result), 201
        except ValidationError as e:
            return schema.dump(e), 400


@api.route('/api/authors/<int:id>', endpoint='author/id')
class Author(Resource):
    @swagger_decorator(path="swagger_files/get_author_by_id.json")
    def get(self, id: int):
        schema = BookSchema()
        return schema.dump(get_all_books_by_author_id(id), many=True), 200

    @swagger_decorator(path="swagger_files/delete_author_by_id.json")
    def delete(self, id: int):
        result = delete_author(id)
        if result:
            return result, 404
        return {}, 204


template = spec.to_flasgger(
                            app=app,
                            definitions=[BookSchema, AuthorSchema]
                            )
swagger = Swagger(app=app, template=template)


if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    init_authors_table(DATA)
    init_books_table(DATA)
    app.run(debug=True)



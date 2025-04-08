from flask import Flask, request
from flask_restx import Api, Resource
from models import *
from schemas import BookSchema, AuthorSchema, ValidationError
from flasgger import Swagger, APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

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


@api.route('/api/books')
class Books(Resource):
    def get(self):
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True)

    def post(self):
        """
        Add book
        ---
        tags:
          - books
        parameters:
          - in: body
            name: new_book
            required: true
            schema:
              $ref: '#/definitions/Book'
        responses:
          201:
            description: Book added
            schema:
              type: object
              $ref: '#/definitions/Book'
        """
        data = request.json
        schema = BookSchema()
        data["author"]: int = exists_author(refactoring_author_name(data['author']))
        try:
            book = schema.load(data)
            result = add_book(book)
            return schema.dump(result), 201
        except ValidationError as e:
            return schema.dump(e), 400


@api.route('/api/books/<int:id>')
class Book(Resource):
    def get(self, id: int):
        schema = BookSchema()
        return schema.dump(get_book_by_id(id)), 200

    def put(self, id: int):
        schema = BookSchema()
        data: Book = schema.load(request.json)  # Десериализовали в объект python
        book = put_updated_book(data, id)
        return schema.dump(book), 200  # Сериализуем python объект в потоковые данные

    def patch(self, id: int):
        schema = BookSchema()
        data: Book = schema.load(request.json, partial=True)
        book = patch_book(data, id)
        return schema.dump(book), 200

    def delete(self, id: int):
        result = delete_book(id)
        if result:
            return result, 404
        return {}, 204


@api.route('/api/authors')
class Authors(Resource):
    def get(self):
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True), 200

    def post(self):
        data = request.json
        schema = AuthorSchema()
        try:
            author: Author = schema.load(data)  # Десериализация потоковых данных в объект python
            result = add_author(author)
            return schema.dump(result), 201
        except ValidationError as e:
            return schema.dump(e), 400


@api.route('/api/authors/<int:id>')
class Author(Resource):
    def get(self, id: int):
        schema = BookSchema()
        return schema.dump(get_all_books_by_author_id(id), many=True), 200

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
    init_authors_table(DATA)
    init_books_table(DATA)
    app.run(debug=True)




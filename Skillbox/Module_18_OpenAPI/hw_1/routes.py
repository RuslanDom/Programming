from flask import Flask, request
from flask_restx import Api, Resource
from flasgger import Swagger, APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from models import *
from schemas import *



app = Flask(__name__)
api = Api(app)
spec = APISpec(
    title= "Books api",
    version="1.0",
    openapi_version="2.0",
    plugins=[
        MarshmallowPlugin(),
        FlaskPlugin()
    ]
)

@api.route('/api/books')
class Books(Resource):
    def get(self):
        """
        Get all books
        ---
        tags:
          - books
        responses:
          200:
            description: Successfully get all books
            schema:
              type: array
              items:
                $ref: '#/definitions/Book'
        """
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True)

    def post(self):
        """
        Create a new book
        ---
        tags:
          - books
        parameters:
          - in: body
            name: new_book
            schema:
              $ref: '#/definitions/Book'
        responses:
          201:
            description: Successfully create a new book
            schema:
              type: object
              $ref: '#/definitions/Book'
        """
        ...


@api.route('/api/authors')
class Authors(Resource):
    def get(self):
        """
        Get all authors
        ---
        tags:
          - authors
        responses:
          200:
            description: Successfully get all authors
            schema:
              type: array
              items:
                $ref: '#/definitions/Author'
        """
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True)

    def post(self):
        """
        Create a new author
        ---
        tags:
          - authors
        parameters:
          - in: body
            name: new_author
            schema:
              $ref: '#/definitions/Author'
        responses:
          201:
            description: Successfully create a new author
            schema:
              type: object
              $ref: '#/definitions/Author'
        """
        schema = AuthorSchema()
        author = schema.load(request.json)
        result = add_author(author)
        return schema.dump(result), 201


template = spec.to_flasgger(
    app=app,
    definitions=[
        BookSchema,
        AuthorSchema
    ]
)

swagger = Swagger(app=app, template=template)

if __name__ == '__main__':
    init_author_table(DATA)
    init_book_table(DATA)
    app.run(debug=True)
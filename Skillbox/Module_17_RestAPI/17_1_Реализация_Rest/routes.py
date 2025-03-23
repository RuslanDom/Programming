from dataclasses import asdict
from flask import Flask
from flask_restful import Resource, Api
from models import (
    DATA,
    get_all_records,
    get_record_by_author,
    init_db
)

app = Flask(__name__)
api = Api(app)


class BookResource(Resource):
    def get(self):
        return {'data': [asdict(book) for book in get_all_records()]}


class BookAuthorResource(Resource):
    def get(self, author):
        return {f'{author}': asdict(get_record_by_author(author))}

api.add_resource(BookResource, '/api/books')
api.add_resource(BookAuthorResource, '/api/books/<author>')


if __name__ == '__main__':

    init_db(initial_records=DATA)
    app.run(debug=True)

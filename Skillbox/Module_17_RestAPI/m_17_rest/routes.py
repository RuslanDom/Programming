from dataclasses import asdict
from flask import Flask, request
from flask_restful import Resource, Api
from schemas import BookSchema
from marshmallow import ValidationError
from models import (
    DATA,
    get_all_records,
    get_record_by_author,
    add_record,
    init_db,
    Book
)

app = Flask(__name__)
api = Api(app)


class BookResource(Resource):
    # def get(self):
    #     return {'data': [asdict(book) for book in get_all_records()]}

    # Другая реализация того же метода через метод marshmallow dump сериализатор
    def get(self):
        schema = BookSchema()
        return schema.dump(get_all_records(), many=True)

    def post(self):
        # модуль request позволяет получить самый последний запрос
        data = request.json
        # Валидация полученных данных
        schema = BookSchema()
        try:
            # load проводит валидацию и по умолчанию возвращает dict, но используя post_load можно преобразовать
            # к примеру сразу в объект Book
            book = schema.load(data)
        except ValidationError as err:
            return err.messages, 400

        post_book = add_record(book)

        return schema.dump(post_book), 201


class BookAuthorResource(Resource):
    def get(self, author):
        return {f'{author}': asdict(get_record_by_author(author))}

api.add_resource(BookResource, '/api/books')
api.add_resource(BookAuthorResource, '/api/books/<author>')


if __name__ == '__main__':

    init_db(initial_records=DATA)
    app.run(debug=True)

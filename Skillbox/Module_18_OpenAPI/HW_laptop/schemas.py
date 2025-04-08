from models import Author, Book, get_author_by_last_name, get_book_by_title
from marshmallow import post_load, validates
from flasgger import Schema, fields, ValidationError


class AuthorSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    middle_name = fields.String(default=None)

    @validates('last_name')
    def validate_last_name(self, last_name: str):
        if get_author_by_last_name(last_name):
            raise ValidationError('The last name is already exists')

    @post_load
    def make_author(self, data, **kwargs):
        return Author(**data)


class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    author = fields.Raw(required=True)

    @validates('title')
    def validate_title(self, title: str):
        if get_book_by_title(title):
            raise ValidationError(
                "This book is already registered with this title."
            )

    @post_load
    def make_book(self, data, **kwargs):
        if 'title' not in data.keys():
            return Book(title=None, author=data['author'])
        return Book(**data)


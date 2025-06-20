from marshmallow import Schema, fields, post_load, validate
from models import Book, Author, Student, ReceivingBook


class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(nullable=False)
    count = fields.Integer(default=1)
    release_date = fields.Date(nullable=False)
    author_id = fields.Integer(nullable=False)

    @post_load
    def get_book(self, data: dict, **kwargs):
        return Book(**data)


class AuthorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(nullable=False, validate=validate.Length(min=2, max=30))
    surname = fields.String(nullable=False, validate=validate.Length(min=2, max=30))

    @post_load
    def get_author(self, data: dict, **kwargs):
        return Author(**data)

class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(nullable=False, validate=validate.Length(min=2))
    surname = fields.String(nullable=False, validate=validate.Length(min=2))
    phone = fields.String(nullable=False, validate=validate.Length(min=7))
    email = fields.String(nullable=False, validate=validate.Email())
    average_score = fields.Float(nullable=False)
    scholarship = fields.Boolean(nullable=False)

    @post_load
    def get_student(self, data: dict, **kwargs):
        return Student(**data)


class ReceivedBookSchema(Schema):
    id = fields.Integer(dump_only=True)
    book_id = fields.Integer(nullable=False)
    student_id = fields.Integer(nullable=False)
    date_of_issue = fields.Date(nullable=False)
    date_of_return = fields.Date(nullable=True)

    @post_load
    def get_record_received_book(self, data: dict, **kwargs):
        return ReceivingBook(**data)
from marshmallow import Schema, fields, validates, ValidationError, post_load, validate, post_dump
from models import get_book_by_title, Book, Author
from models import DATABASE_NAME, add_author, get_author_id_use_name
import sqlite3


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True, validate=validate.Length(min=2))
    middle_name = fields.Str()

    @post_load
    def create_author(self, data: dict, **kwargs) -> Author:
        return Author(**data)


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    # author = fields.Raw(required=True)
    author = fields.Nested(AuthorSchema(), required=True)



    @validates('title')
    def validate_title(self, title: str) -> None:
        if get_book_by_title(title) is not None:
            raise ValidationError(
                'Book with title "{title}" already exists, '
                'please use a different title.'.format(title=title)
            )

    @post_load
    def create_book(self, data: dict, **kwargs) -> Book:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            if 'author' in data.keys():
                cursor.execute(
                    """
                    SELECT * FROM authors_table WHERE last_name = ? AND first_name = ?;
                    """,
                    (data['author']['last_name'], data['author']['first_name'])
                )
                author_record = cursor.fetchone()
                if author_record is None:
                    add_author(data['author'])
                    cursor.execute(
                        """
                        SELECT id FROM authors_table WHERE last_name = ? AND first_name = ?;
                        """,
                        (data['author']['last_name'], data['author']['first_name'])
                    )
                    author_record = cursor.fetchone()
                if 'title' not in data.keys():
                    return Book(title=None, author=author_record[0])
                return Book(title=data['title'], author=author_record[0])

            return Book(title=data['title'], author=None)

    @post_dump
    def dump_book(self, data: dict, **kwargs) -> dict:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    SELECT id FROM authors_table WHERE last_name = ? AND first_name = ?;
                    """,
                (data['author']['last_name'], data['author']['first_name'])
            )
            author_record = cursor.fetchone()
        return {"id": data['id'], "title": data['title'], "author": author_record[0]}








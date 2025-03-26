from marshmallow import Schema, fields, validates, ValidationError, post_load
from models import get_book_obj_from_row, Book



# Объект созданный для валидации с использованием marshmallow.Schema
class BookSchema(Schema):
    id = fields.Int(dump_only=True)  # dump_only
    title = fields.Str(required=True)  # required требуемое поле
    author = fields.Str(required=True)

    # Валидация на наличие имеющейся книги, если такая книга уже есть в БД то получим исключение
    @validates('title')
    def validate_title(self, title: str) -> None:
        if get_book_obj_from_row(title) is not None:
            raise ValidationError('Invalid title. This is title: {} exists'.format(title))

    # Выполняет постобработку (в данном случае преобразует полученный словарь в объект Book)
    @post_load
    def create_book(self, data: dict, **kwargs) -> Book:
        return Book(**data)


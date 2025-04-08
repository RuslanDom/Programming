from marshmallow import post_load, validates
from flasgger import ValidationError, Schema, fields
from models import Owner, Pet, DATABASE, OWNERS_TABLE
import sqlite3

class OwnerSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)

    @validates('name')
    def validate_name(self, name: str) -> None:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""SELECT id FROM '{OWNERS_TABLE}' WHERE name=?""", (name,))
            founded = cursor.fetchone()
        if founded is not None:
            raise ValidationError(
                'Owner with name "{name}" already exists, '
                'please use a different name.'.format(name=name)
            )

    @post_load
    def created_pet(self, data: dict, **kwargs):
        return Owner(**data)


class PetSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    kind = fields.String(required=True)
    age = fields.Integer(default=0)
    owner = fields.String(required=True)


    @post_load
    def created_pet(self, data: dict, **kwargs):
        return Pet(**data)





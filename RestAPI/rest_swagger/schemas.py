from marshmallow import Schema, fields, validate, post_load
from models import Pet, Owner



class PetSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    owner = fields.Raw(required=True)

    @post_load
    def load_pet(self, data, **kwargs):
        return Pet(**data)


class OwnerSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True, default=None)

    @post_load
    def load_owner(self, data, **kwargs):
        return Owner(**data)

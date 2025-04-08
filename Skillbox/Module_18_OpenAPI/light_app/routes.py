from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import APISpec, Swagger
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from models import (Pet, Owner, DATA, init_table_pets, init_table_owners,
                    get_all_pets, get_all_owners,
                    add_owner, add_pet
                    )

from schemas import PetSchema, OwnerSchema

app = Flask(__name__)
api = Api(app)
spec = APISpec(
    title="Pets api",
    version="1.0.0",
    openapi_version="2.0.0",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin()
    ]
)


class PetList(Resource):
    def get(self):
        """
        Get all pets
        ---
        tags:
          - pets
        responses:
          200:
            description: List of pets
            schema:
              type: array
              items:
                $ref: '#/definitions/Pet'
        """
        schema = PetSchema()
        return schema.dump(get_all_pets(), many=True), 200

    def post(self):
        """
        Create new pet
        ---
        tags:
          - pets
        parameters:
          - in: body
            name: new pet data
            schema:
              $ref: '#/definitions/Pet'
        responses:
          201:
            description: Pet created
            schema:
              type: object
              $ref: '#/definitions/Pet'
        """
        data = request.json
        schema = PetSchema()
        pet = schema.load(data)
        post_pet = add_pet(pet)
        return schema.dump(post_pet), 201

class OwnerList(Resource):
    def get(self):
        """
        Get all owners
        ---
        tags:
          - owners
        responses:
          200:
            description: List of owners
            schema:
              type: array
              items:
                $ref: '#/definitions/Owner'
        """
        schema = OwnerSchema()
        return schema.dump(get_all_owners(), many=True), 200

    def post(self):
        """
        Create new owner
        ---
        tags:
          - owners
        parameters:
          - in: body
            name: new owner data
            schema:
              $ref: '#/definitions/Owner'
        responses:
          201:
            description: Owner created
            schema:
              type: object
              $ref: '#/definitions/Owner'
        """
        schema = OwnerSchema()
        owner = schema.load(request.json)
        post_owner = add_owner(owner)
        return schema.dump(post_owner), 201

template = spec.to_flasgger(
    app=app,
    definitions=[PetSchema, OwnerSchema]
)
swagger = Swagger(app, template=template)

api.add_resource(PetList, '/api/v1/pets')
api.add_resource(OwnerList, '/api/v1/owners')

if __name__ == '__main__':
    init_table_owners(DATA)
    init_table_pets(DATA)
    app.run(debug=True)
from flasgger import APISpec, Swagger
from flask_restful import Api, Resource
from flask import request, Flask
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from Skillbox.Module_18_OpenAPI.rest_api_pets.schemas import PetSchema, OwnerSchema
from models import DATA, init_table_owner, add_owner, add_pet, init_table_pet, get_all_pets, get_all_owners, delete_pet



app = Flask(__name__)
api = Api(app)
spec = APISpec(
    title="Pets",
    version="0.0.1",
    openapi_version="2.0.0",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin()
    ]
)


class PetsList(Resource):
    def get(self):
        """
        Get all pets
        ---
        tags:
          - pets
        responses:
          200:
            description: List of all pets
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
            name: pet parameters
            schema:
              $ref: '#/definitions/Pet'
        responses:
          201:
            description: New pet created
            schema:
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
            description: List of all owners
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
            name: owner parameters
            schema:
              $ref: '#/definitions/Owner'
        responses:
          201:
            description: New owner created
            schema:
              $ref: '#/definitions/Owner'
        """
        data = request.json
        schema = OwnerSchema()
        owner_obj_after_valid = schema.load(data)
        post_owner = add_owner(owner_obj_after_valid)
        if post_owner is None:
            return {"ValueError": "This is name already exists"}, 404
        return schema.dump(post_owner), 201


class PetId(Resource):

    def delete(self, id: int):
        """
        Delete pet by id
        ---
        tags:
          - pets
        parameters:
          - in: path
            name: pet id
            schema:
              type: integer
              example: 5
        responses:
          204:
            description: Pet id deleted
            schema: {}
        """
        response = delete_pet(id)
        if response:
            return response, 204
        return None, 404




template = spec.to_flasgger(
    app,
    definitions=[PetSchema, OwnerSchema]
)
swagger = Swagger(app, template=template)
# swagger.json = Swagger(app, template_file='swagger.json.json')

api.add_resource(PetsList, '/api/v1/pets')
api.add_resource(OwnerList, '/api/v1/owners')
api.add_resource(PetId, '/api/v1/pets/<int:id>')



if __name__ == '__main__':
    init_table_owner(DATA)
    init_table_pet(DATA)
    app.run(debug=True)





from flask import Flask
from flask_restx import Api, Resource
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from schemas import PetSchema, OwnerSchema
import config
from models import init_table_owner, init_table_pet, DATA

app = Flask(__name__)
app.config.from_object(config.CONFIG)
api = Api(app)
spec = APISpec(
    version='1.0.0',
    title='RestAPI',
    openapi_version='2.0',
    plugins=[MarshmallowPlugin(),
             FlaskPlugin()]
)

@api.route("/pets")
class Pet(Resource):
    def get(self):
        schema = PetSchema()


if __name__ == "__main__":
    init_table_owner(DATA)
    init_table_pet(DATA)
    app.run(debug=True)


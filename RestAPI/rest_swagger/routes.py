from flask import Flask
from flask_restx import Api, Resource
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from schemas import PetSchema, OwnerSchema
import config

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

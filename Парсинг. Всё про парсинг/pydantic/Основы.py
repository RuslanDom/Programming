from pydantic import BaseModel, ValidationError, Field
from loguru import logger
from sys import stdout

logger.add(sink=stdout, format='{time} {level} {message}', level='DEBUG')


class Tags(BaseModel):
    view: str
    location: str


class City(BaseModel):
    city_id: int
    city_name: str
    population: int = Field(alias='people')
    tags: list[Tags]


json_file = '''
{   
    "city_id": 34,
    "city_name": "Volgograd",
    "people": "1000000",
    "tags": 
    [{
        "view": "Родина мать",
        "location": "центральный район"
    }]
}
'''

try:
    city_1 = City.model_validate_json(json_file)
except ValidationError as err:
    print(err.json())
    logger.debug(err.json())
else:
    logger.debug(city_1)
    logger.debug(city_1.city_name)
    logger.debug(city_1.tags[0].location)


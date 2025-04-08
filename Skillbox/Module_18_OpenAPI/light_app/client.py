import requests

from Skillbox.Module_18_OpenAPI.light_app.models import Pet


class PetClient:
    URL = "http://127.0.0.1:5000/api/v1/pets"
    TIMEOUT = 5

    def __init__(self):
        self._session = requests.Session()

    def get_all_pets(self):
        response = self._session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_pet(self, data_pet):
        response = self._session.post(self.URL, json=data_pet, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError("Wrong parameters. Response message: {}".format(response.json()))
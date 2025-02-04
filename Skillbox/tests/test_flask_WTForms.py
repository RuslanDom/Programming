import unittest
from Flask.Rest.flask_WTForms import *
import json



class TestFillFields(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        

    def setUp(self):
        self.app = app.test_client()
        self.base_url = "/registration"
        self.email = "test@example.com"
        self.phone = 9951010203
        self.name = "Скворцов Сергей"
        self.address = "Волгоград"
        self.index = 187110
        self.comment = "вход со двора"
        self.headers = {'Content-Type': 'application/json'}

    def test_phone(self):
        phone = '25test'
        data = {
            "email": self.email,
            "phone": phone,
            "name": self.name,
            "address": self.address,
            "index": self.index,
            "comment": self.comment}
        url = self.base_url
        response = self.app.post(url, data=json.dumps(data), headers=self.headers)
        print(response.status_code, response.text)
        self.assertEqual(400, response.status_code)
        
    def test_index(self):
        index = '123qwe'
        data = {
            "email": self.email,
            "phone": self.phone,
            "name": self.name,
            "address": self.address,
            "index": index,
            "comment": self.comment}
        url = self.base_url
        response = self.app.post(url, data=json.dumps(data), headers=self.headers)
        print(response.status_code, response.text)
        self.assertEqual(400, response.status_code)

    def test_email(self):
        email = None
        data = {
            "email": email,
            "phone": self.phone,
            "name": self.name,
            "address": self.address,
            "index": self.index,
            "comment": self.comment}
        url = self.base_url
        response = self.app.post(url, data=json.dumps(data), headers=self.headers)
        print(response.status_code, response.text)
        self.assertEqual(400, response.status_code)
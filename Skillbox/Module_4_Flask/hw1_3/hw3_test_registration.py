"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app
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
        self.data = {
            "email": "test@example.com",
            "phone": 9951010203,
            "name": "Скворцов Сергей",
            "address": "Волгоград",
            "index": 187110,
            "comment": "вход со двора"}


    def test_positive(self):
        response = self.app.post(self.base_url, data=self.data)
        print(response.status_code, response.text)
        self.assertEqual(200, response.status_code, msg="FAIL")

    def test_negative(self):
        negative_data = (("phone", "sgdfg8798"),
                         ("phone", None),
                         ("index", '123qwe'),
                         ("index", None),
                         ("email", "fsfsf@sdf."),
                         ("email", None),
                         ("name", None),
                         ("address", None))

        for i in range(len(negative_data)):
            with self.subTest(f"Негативный тест проверка поля: {negative_data[i][0]} со значением {negative_data[i][1]}", i=i):
                self.data[negative_data[i][0]] = negative_data[i][1]
                response = self.app.post(self.base_url, data=self.data)
                self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()

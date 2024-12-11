import unittest
from datetime import datetime
from freezegun import freeze_time
# from Unit_test.flask_tests.web_hello_weekday import app
from web_hello_weekday import app

DAYS = [
    "Понедельника",
    "Вторника",
    "Среды",
    "Четверга",
    "Пятницы",
    "Субботы",
    "Воскресенья"
]

@freeze_time("2024-10-29")
class TestHellWeekday(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello/'


    def test_has_name_in_webpage(self):
        username = 'user'
        url = self.base_url + username
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_check_weekday(self):
        username = 'user'
        date_test = datetime.today().weekday()
        url = self.base_url + username
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertIn(DAYS[date_test], response_text)
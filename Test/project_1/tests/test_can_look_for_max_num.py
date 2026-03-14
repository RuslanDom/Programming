import unittest
from Test.project_1.web_max_numbres import app


class TestMaxNum(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client
        self.base_url = "/max/"

    def test_can_look_for_max(self):
        numbers = 5, 10
        url = self.base_url + "/".join(num for num in numbers)
        response = self.app.get(url)
        response_text = response.data.decode()
        expected_answer = str(max(numbers))
        self.assertTrue(expected_answer in response_text)
        




import unittest

# 1-й вариант запуск из терминала
#from example_code import get_social_status

# 2-й вариант запуск из этого файла
from Unit_test.unit_tests.example_code import get_social_status


"""Для того чтобы вызвать тест
1. Переходим в директорию с нашими файлами (.venv) ruslan@PC:~/Programming/Unit_test/unit_tests$ 
затем пишем:  python -m unittest -v

test_can_get_child_age (tests.test_01_social_age.TestSocialAge.test_can_get_child_age) ... ok
test_cannot_pass_str_as_age (tests.test_01_social_age.TestSocialAge.test_cannot_pass_str_as_age) ... ok
----------------------------------------------------------------------
Ran 2 test in 0.000s

OK

2. Запускаем тест из самого файла

Ran 2 tests in 0.001s

OK

"""

class TestSocialAge(unittest.TestCase):

    def test_can_get_child_age(self):
        age = 8
        expected_res = 'Child'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_cannot_pass_str_as_age(self):
        age = '10'
        # Проверь что появилось исключение ValueError, если ДА то тест ОК
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_can_teenager_age(self):
        age = 14
        expected_res = 'Teenager'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_adult_age(self):
        age = 18
        expected_res = "Adult"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_elderly_age(self):
        age = 64.99
        expected_res = 'Elderly'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_pensioner_age(self):
        age = 99
        expected_res = 'Pensioner'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)
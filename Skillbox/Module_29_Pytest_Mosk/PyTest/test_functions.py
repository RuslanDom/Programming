import math
import pytest

# ЗАПУСКИ
# pytest -v - подробный тест
# pytest test_functions - определенный тест
# pytest -k math - тест со словом math в названии теста
# pytest -m str - тест с маркировкой указанной в декораторе @pytest.mark
@pytest.mark.math
def test_math_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.str
def test_uppercase():
    assert 'skillbox'.upper() == 'SKILLBOX'

def test_item_in_list():
    assert 777 in [item for item in [111, 222, 777, 888]]

@pytest.mark.math
def test_math_square():
    assert pow(7, 2) == 7 ** 2

@pytest.mark.math
def test_math_division():
    assert 9 / 3 == 3

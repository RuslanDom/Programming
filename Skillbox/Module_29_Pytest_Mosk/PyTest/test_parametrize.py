import pytest
import math


@pytest.mark.parametrize('digit, result', [(5, 25), (7, 49), (10, 100)])
def test_math_divide(digit, result):
    assert math.pow(digit, 2) == result

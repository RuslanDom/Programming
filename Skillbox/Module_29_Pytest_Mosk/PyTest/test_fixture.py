import pytest

@pytest.fixture
def input_value():
    input = 2
    return input


@pytest.mark.math
def test_math_add(input_value):
    x = input_value
    assert x + x == 4

@pytest.mark.str
def test_add_str(input_value):
    x = str(input_value)
    assert x + x == '22'










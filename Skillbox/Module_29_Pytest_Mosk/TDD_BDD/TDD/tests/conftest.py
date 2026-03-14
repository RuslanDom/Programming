import pytest
from TDD.main.app import create_app


@pytest.fixture
def app():
    __app = create_app()
    return __app

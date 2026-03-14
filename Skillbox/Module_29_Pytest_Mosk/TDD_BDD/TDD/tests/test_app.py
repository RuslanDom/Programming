import pytest
from flask import Flask
from .conftest import app

def test_app(app: Flask):
    assert isinstance(app, Flask)
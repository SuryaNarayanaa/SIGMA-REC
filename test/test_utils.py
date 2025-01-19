import pytest
from unittest.mock import patch
from flask import Flask
from app.utils import validate_user
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    with app.app_context():
        yield app

@patch("app.utils.validate_user")
def test_validate_user(mock_validate_user, app):
    with app.app_context():
        mock_validate_user.return_value = True
        data = {"username": "test", "email": "test@example.com", "password": "password"}
        assert validate_user(data) is True

import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token
from app.routes import user, BLOCKLIST
# def test_init_app():
#     app = Flask(__name__)
#     assert app is  None
# def test_user():
#     app = check_init_app()
#     app.register_blueprint(user)
#     client = app.test_client()
#     response = client.get('/user')
#     assert response.status_code == 200
#     assert response.json == {'message': 'User route'}

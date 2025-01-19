import pytest
from pydantic import ValidationError
from app.Schemas import UserRegistrationModel, UserLoginModel, UserUpdateModel

def test_user_registration_model_valid():
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword",
        "isadmin": False
    }
    model = UserRegistrationModel(**data)
    assert model.username == "testuser"
    assert model.email == "test@example.com"
    assert model.password == "securepassword"
    assert not model.isadmin 

def test_user_registration_model_invalid():
    with pytest.raises(ValidationError):
        UserRegistrationModel(username="tu", email="invalid-email", password="123")

def test_user_login_model_valid():
    data = {
        "email": "test@example.com",
        "password": "securepassword"
    }
    model = UserLoginModel(**data)
    assert model.email == "test@example.com"
    assert model.password == "securepassword"

def test_user_login_model_invalid():
    with pytest.raises(ValidationError):
        UserLoginModel(email="invalid-email", password="123")

def test_user_update_model_valid():
    data = {
        "username": "updateduser","email": "updated@example.com","password": "newpassword","isadmin": True
    }
    model = UserUpdateModel(**data)
    assert model.username  == "updateduser"
    assert model.email ==  "updated@example.com"
    assert model.password  ==  "newpassword"
    assert   model.isadmin is True

def test_user_update_model_partial():
    data = {
        "username": "updateduser"
    }
    model = UserUpdateModel(**data)
    assert model.username == "updateduser"
    assert model.email is None
    assert model.password is None
    assert model.isadmin  is False

def test_user_update_model_invalid():
    with pytest.raises(ValidationError):
        UserUpdateModel(username="up", email="invalid-email", password="123")
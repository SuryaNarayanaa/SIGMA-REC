from app.config import Config

def test_config():
    assert Config.PORT is not None, "PORT is not set"
    assert Config.SECRET_KEY is not None, "SECRET_KEY is not set"
    assert Config.MONGO_INITDB_ROOT_USERNAME is not None, "MONGO_INITDB_ROOT_USERNAME is not set"
    assert Config.MONGO_INITDB_ROOT_PASSWORD is not None, "MONGO_INITDB_ROOT_PASSWORD is not set"
    assert Config.JWT_SECRET_KEY is not None, "JWT_SECRET is not set"
from flask import Flask
from flask_jwt_extended import JWTManager

from .config import Config
from .db import init_db
from .routes import user
from .blocklist import BLOCKLIST

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return jti in BLOCKLIST

    db = init_db()
    app.db = db

    app.register_blueprint(user)
    return app

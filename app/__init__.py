from flask import Flask
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from .config import Config
from .db import init_db
from .routes import user
from .blocklist import BLOCKLIST

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=["200 per day", "20 per hour"]
    )
    # CSRFProtect(app=app)
    
    Talisman(app, strict_transport_security=True , force_https  = False, frame_options = "DENY", referrer_policy="no-referrer")

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return jti in BLOCKLIST

    db = init_db()
    app.db = db

    app.register_blueprint(user)
    return app

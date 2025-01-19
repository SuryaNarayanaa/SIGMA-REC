from app import create_app
app = create_app()

def test_init_app():
    assert app is not None
    assert app.config["TESTING"] is False

def test_database_initialization():
    assert hasattr(app, "db"), "App should have a database instance attached"
    assert app.db is not None, "Database instance should not be None"


def test_blueprint_registration():
    registered_blueprints = list(app.blueprints.keys())
    assert "user" in registered_blueprints, "User blueprint should be registered"

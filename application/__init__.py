from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def init_app():
    """Initialize the core application for test."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.TestConfig')

    # Initialize Plugins
    db.init_app(app)
    
    return add_blueprints(app)

def add_blueprints(app):
    with app.app_context():
        # Include our Routes
        from application.modules.home.home import home_bp
        from application.modules.create.create import create_bp

        # Register Blueprints
        app.register_blueprint(home_bp)
        app.register_blueprint(create_bp)
        
        db.create_all()
        
        return app
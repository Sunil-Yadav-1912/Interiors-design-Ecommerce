from flask import Flask
def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Configuration settings
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    # Add more configuration settings as needed

    # Initialize extensions, database, etc.
    # Example: db.init_app(app)

    # Import and register blueprints
    from .views import main_bp
    app.register_blueprint(main_bp)

    return app
from flask import Flask
from .routes import register_routes
from flask_cors import CORS
from .config import get_config
from .extensions import init_extensions

def create_app():
    app = Flask(__name__)
    # CORS(app)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
    app.config.from_object(get_config())

    register_routes(app)
    init_extensions(app)  
    

    return app
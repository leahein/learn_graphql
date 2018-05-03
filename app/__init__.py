from flask import Flask
from .routes import API

def create_app(config):
    app = Flask(__name__)
    app.config.update(config)
    app.register_blueprint(API, url_prefix='/')
    return app

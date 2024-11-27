from flask import Flask
from app.main import main_blueprint

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)


    app.register_blueprint(main_blueprint, url_prefix='/')

    return app

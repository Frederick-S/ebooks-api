from flask import Flask
from config import configs
from ebooks.api.api_blueprint import api_blueprint
from ebooks.api.api_bootstrap import init_api_routes


def create_app(config_name):
    config = configs[config_name]
    app = Flask(__name__, template_folder='static/dist',
                static_folder='static/dist', static_url_path='')
    app.config.from_object(config)

    init_api_routes()

    app.register_blueprint(api_blueprint, url_prefix='/v1.0')

    return app

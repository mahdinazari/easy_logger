import os
import importlib

from flask import Flask, jsonify

from .extentions import db
from .exceptions import ApplicationException


def create_app(config_filename):
    """
    Flask application factory
    """
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.config['JSON_AS_ASCII'] = False
    db.init_app(app)

    for installed_app in app.config['APPLICATION_VIEWS']:
        view = importlib.import_module('views.{}'.format(installed_app))
        app.register_blueprint(view.blueprint)

    with app.app_context():
        db.init_app(app)

    # Register the error handler
    @app.errorhandler(ApplicationException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app


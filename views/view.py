from threading import Thread

from flask import Blueprint, jsonify


blueprint = Blueprint('deleteme', __name__, url_prefix='/api/v1/')


@blueprint.route('/main')
def main():
    return jsonify("Hello World")


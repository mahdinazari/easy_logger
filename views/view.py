from threading import Thread

from flask import Blueprint, jsonify

from application.utils import Foo


blueprint = Blueprint('view', __name__, url_prefix='/api/v1')


@blueprint.route('/main')
def main():
    return jsonify("Hello World")


@blueprint.route('/hello')
def hello():
    Foo.exception_code = None
    Foo.exception_message = None
    foo = Foo()
    t = Thread(
        target = foo.say_hello,
        args=['mehdi']
    )
    t.start()
    t.join()
    if foo.exception_code and foo.exception_message:
        return jsonify(foo.exception_message), foo.exception_code

    return jsonify("Done"), 200


@blueprint.route('/hi')
def hi():
    foo = Foo()
    func = foo.say_hi('mehdi')
    return jsonify("Done"), 200


@blueprint.route('/is-integer')
def is_integer():
    foo = Foo()
    func = foo.is_integer('mehdi')
    return jsonify("Done"), 200


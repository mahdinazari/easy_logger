import sys
import threading

from flask import jsonify

from application.app import create_app
from application.exceptions import FooException, BarException, BazException


class Foo:
    def __init__(self):
        self.exception_code = None
        self.exception_message = None


    def say_hello(self, name):
        if name == 'mehdi':
            self.exception_code = FooException.status_code
            self.exception_message = FooException.message
            return

        else:
            self.exception_code = BarException.status_code
            self.exception_message = BarException.message
            return


    def say_hi(self, name):
        if name == 'mehdi':
            raise BarException()

        else:
            raise FooException()


    def is_integer(self, number):
        try:
            if number == '':
                raise FooException()
                return

            if number == 2:
                raise BarException()

            number + 1
            raise FooException()

        except:
            raise BazException()


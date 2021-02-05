from flask import jsonify


"""
Create A New Exception Example:
```
    class BarException(AppException):
        message = "This Is A Sample Error text"
        status_code = 423
        code = 1025
```

Usage of created exception in Views Example:
```
    from application import exc
    @app.route('/foo')
    def get_foo():
        raise exc.BarException
```
"""

class ApplicationException(Exception):
    status_code = 400
    message =  "Empty"
    payload = {}

    def __init__(self):
        Exception.__init__(self)

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class FooException(ApplicationException):
    status_code = 701
    message = '400 Foo Execution'


class BarException(ApplicationException):
    status_code = 702
    message = '400 Bar Execution'


class BazException(ApplicationException):
    status_code = 703
    message = '400 Baz Execution'


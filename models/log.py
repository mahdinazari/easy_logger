from mongoengine import *


class Log(Document):
    action = StringField(required=True, max_length=50)
    actor = StringField(required=True, max_length=50)
    level = StringField(required=True, max_length=50)
    code = IntField(required=True)
    message = StringField(required=True, max_length=50)
    _input = StringField(required=True, max_length=500)
    _output = StringField(required=True, max_length=500)
    created_at = DateTimeField(required=True)


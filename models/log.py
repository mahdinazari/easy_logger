from mongoengine import *


class Log(Document):
    verb = StringField(required=True, max_length=50)
    message = StringField(required=True, max_length=50)
    status_code = IntField(required=True)


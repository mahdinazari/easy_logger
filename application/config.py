import os


class Config(object):
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'postgres://postgres:postgres@localhost/flask_practice'
    )

    PRESERVE_CONTEXT_ON_EXCEPTION = False

    APPLICATION_VIEWS = [
        'view',
    ]


class DevelopmentConfig(Config):
     """
     Development Configuration
     """
     DEBUG = True


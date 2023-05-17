"""Flask configuration."""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class TestConfig(Config):
    FLASK_ENV = 'test'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, 'testing.sqlite')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
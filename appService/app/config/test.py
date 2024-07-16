from .base import BaseConfig

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    DEBUG = True
    TESTING = True

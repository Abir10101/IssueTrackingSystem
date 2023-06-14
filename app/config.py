import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Database configuration
    DB_USER = os.getenv('DB_USER', default = 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', default = 'mysql')
    DB_NAME = os.getenv('DB_NAME', default = 'myapp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Other configuration
    SECRET_KEY = os.getenv('SECRET_KEY', default = "terrible secret key")

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_HOST')

if os.getenv('FLASK_ENV') == 'prod':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()

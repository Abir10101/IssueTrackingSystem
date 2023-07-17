import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Database configuration
    DB_USER = os.getenv('DB_USER', default = 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', default = 'mysql')
    DB_NAME = os.getenv('DB_NAME', default = 'myapp')
    DB_HOST = os.getenv('DB_HOST', default = 'localhost')
    DB_PORT = os.getenv('DB_PORT', default = '3306')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Other configuration
    SECRET_KEY = os.getenv('SECRET_KEY', default = "terrible secret key")

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"

if os.getenv('FLASK_ENV') == 'prod':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()

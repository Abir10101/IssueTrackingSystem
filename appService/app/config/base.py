import os

class BaseConfig:

    # Database configuration
    DB_USER = os.getenv('DB_USER', default = 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', default = 'mysql')
    DB_NAME = os.getenv('DB_NAME', default = 'myapp')
    DB_HOST = os.getenv('DB_HOST', default = 'localhost')
    DB_PORT = os.getenv('DB_PORT', default = '3306')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

    # Other configuration
    SECRET_KEY = os.getenv('SECRET_KEY', default = "terrible secret key")

    # Auth Module
    AUTH_TOKEN_VALIDITY = 24 * 60 * 60 # one day in sec
    AUTH_TOKEN_REFRESH_RATE = 30 * 60 # 30 min in sec

    #Message Queue
    QUEUE_MASTER_HOST = os.getenv('QUEUE_MASTER_HOST', default = 'localhost')
    QUEUE_MASTER_PORT = os.getenv('QUEUE_MASTER_PORT', default = 6378)
    QUEUE_MASTER_PASSWORD = os.getenv('QUEUE_MASTER_PASSWORD', default = 'abir101')
    QUEUE_SLAVE_HOST = os.getenv('QUEUE_SLAVE_HOST', default = 'localhost')
    QUEUE_SLAVE_PORT = os.getenv('QUEUE_SLAVE_PORT', default = 6379)
    QUEUE_SLAVE_PASSWORD = os.getenv('QUEUE_SLAVE_PASSWORD', default = 'abir101')

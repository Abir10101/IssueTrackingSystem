from .base import BaseConfig

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{BaseConfig.DB_USER}:{BaseConfig.DB_PASSWORD}@{BaseConfig.DB_HOST}:{BaseConfig.DB_PORT}/{BaseConfig.DB_NAME}"
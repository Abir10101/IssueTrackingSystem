from .prod import ProductionConfig
from .dev import DevelopmentConfig

class AppConfig:
    _instance = None
    _configs = None
    _environment = None

    def __new__(cls, env=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._configs = None
            cls._instance._environment = env
        return cls._instance

    @staticmethod
    def get():
        if AppConfig._instance._configs is None:
            if AppConfig._instance._environment == "prod":
                AppConfig._instance._configs = ProductionConfig()
            else:
                AppConfig._instance._configs = DevelopmentConfig()
        return AppConfig._instance._configs

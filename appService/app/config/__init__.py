import threading
from .prod import ProductionConfig
from .dev import DevelopmentConfig
from .test import TestConfig


class AppConfig: 
    _instance = None
    _configs = None
    _environment = None
    _lock = threading.Lock()

    def __new__(cls, env=None):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._environment = env

                    if cls._instance._environment == "prod":
                        cls._instance._configs = ProductionConfig()
                    elif AppConfig._instance._environment == "test":
                        AppConfig._instance._configs = TestConfig()
                    else:
                        cls._instance._configs = DevelopmentConfig()

        return cls._instance

    @staticmethod
    def get():
        return AppConfig._instance._configs

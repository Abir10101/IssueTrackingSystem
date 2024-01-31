import os
from .prod import ProductionConfig
from .dev import DevelopmentConfig

if os.getenv('FLASK_ENV') == 'prod':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()

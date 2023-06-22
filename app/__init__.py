import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():

  app = Flask(__name__)

  CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='app.config.app_config')
  app.config.from_object(CONFIG_TYPE)

  db.init_app(app)
  migrate = Migrate(app, db)

  register_blueprints(app)
  configure_logging(app)


  return app


def register_blueprints(app):
    from .auth import auth_blueprint
    from .main import main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/users')
    app.register_blueprint(main_blueprint)


def configure_logging(app):
  import logging
  from flask.logging import default_handler
  from logging.handlers import RotatingFileHandler

  # Deactivate the default flask logger so that log messages don't get duplicated 
  app.logger.removeHandler(default_handler)

  if not os.path.exists('logs'):
    os.mkdir('logs')

  # Create a file handler object
  file_handler = RotatingFileHandler('logs/debug.log', maxBytes=625000, backupCount=20)

  # Set the logging level of the file handler object so that it logs INFO and up
  file_handler.setLevel(logging.INFO)

  # Create a file formatter object
  file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s %(name)s: %(lineno)d]')

  # Apply the file formatter object to the file handler object
  file_handler.setFormatter(file_formatter)

  # Add file handler object to the logger
  app.logger.addHandler(file_handler)
  app.logger.setLevel(logging.INFO)

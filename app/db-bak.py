# import pymysql
# from app.config import app_config
# from flask import current_app

# def db_connection():
#     current_app.logger.info( app_config.DB_HOST )
#     try:
#         con = pymysql.connect(  host = app_config.DB_HOST,
#                                 user = app_config.DB_USER,
#                                 password = app_config.DB_PASSWORD,
#                                 database = app_config.DB_NAME,
#                                 cursorclass = pymysql.cursors.DictCursor )
#     except pymysql.err.DatabaseError:
#         raise Exception('Cannot connect Database')
#     return con

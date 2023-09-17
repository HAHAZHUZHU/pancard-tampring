# 这个文件中通常包含不同环境的配置，如开发环境、生产环境等。
# 你可以使用不同的配置类来管理这些配置。

import os
from os import environ

class Config(object):

    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'pianalytix'

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "pianalytix"

    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "pianalytix"

    UPLOADS = "/home/username/app/app/static/uploads"
    
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "pianalytix"

    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIE_SECURE = False

 
class DebugConfig(Config):
    DEBUG = False

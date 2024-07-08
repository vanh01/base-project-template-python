import os

postgres_local_base = os.getenv('DATABASE_URL')
# postgres_local_base = "postgresql+psycopg2://postgres:123456@localhost/postgres"

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

    # Logging
    DATE_FMT = "%Y-%m-%d %H:%M:%S"
    LOG_FILE_API = f"{basedir}/logs/api.log"

    APP_ENV = ""


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

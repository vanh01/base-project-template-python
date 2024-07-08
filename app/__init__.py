import os
from flask import Flask
from dotenv import load_dotenv
import manage

load_dotenv()

from config import config_by_name

from .db import db
from .migrate import migrate
from .bcrypt import flask_bcrypt
from .logging import configure_logging
from .blueprint import blpv1
from .router import map_namespacev1


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    flask_bcrypt.init_app(app)

    manage.init_app(app)

    configure_logging(app)

    map_namespacev1(blpv1)
    app.register_blueprint(blpv1, url_prefix='/api/v1')

    return app

app = create_app(config_by_name[os.getenv('BOILERPLATE_ENV') or 'dev'])

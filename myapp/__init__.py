from flask import Flask


def create_app(config_file='settings.py'):

    app = Flask(__name__)
    # app = Flask(__name__, static_folder="static", template_folder="templates")

    app.config.from_pyfile(config_file)

    from .example.routes import example
    from .accounts.urls import accounts
    app.register_blueprint(example)
    app.register_blueprint(accounts)

    return app

from flask import Flask, redirect, url_for
# from markupsafe import escape


def create_app(test_config=None):
    # create and configure the app

    # app = Flask(__name__)
    app = Flask(__name__, static_folder="static", template_folder="templates")

    from .accounts.urls import accounts
    app.register_blueprint(accounts)

    @app.route('/')
    @app.route('/index')
    # *** CANNOT access the URL with trailing slash ***
    def index():
        return redirect(url_for("home"))

    @app.route('/home/')
    # *** CAN access the URL without trailing slash ***
    def home():
        return "HOME Page"

    # TESTING
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('accounts.show_user_profile', username='Prashanth', next='/'))

    return app

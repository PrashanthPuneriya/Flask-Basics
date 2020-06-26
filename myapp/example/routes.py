from flask import url_for, redirect, Blueprint, current_app, g

example = Blueprint('example', __name__)


@example.route('/')
@example.route('/index')
# *** CANNOT access the URL with trailing slash ***
def index():
    print(current_app.config)

    return redirect(url_for("example.home"))


@example.route('/home/')
# *** CAN access the URL without trailing slash ***
def home():
    return "HOME Page"

from flask import url_for, redirect, Blueprint, current_app, g, make_response, session

example = Blueprint('example', __name__)


@example.route('/')
@example.route('/index')
# *** CANNOT access the URL with trailing slash ***
def index():
    print(current_app)
    print(current_app.config)

    return "INDEX page"


@example.route('/home/')
# *** CAN access the URL without trailing slash ***
def home():
    return redirect(url_for("example.index"))


@example.route('/cookies-example/')
def cookie_example():
    # set a cookie for 30 seconds
    resp = make_response("See the cookies of this website")
    resp.set_cookie('test-cookie', '123', max_age=5)
    """
    Accessing the cookie:-
        request.cookies.get('key')
    Deleting the cookie:-
        resp.set_cookie('key', 'value', max_age=0)
    """
    return resp


@example.route('/session-example/')
def session_example():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    """
    Deleting the session:-
        session.pop('key', None)
    """
    return "Total visits: {}".format(session.get('visits'))

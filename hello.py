from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/index')
def index():
    # *** CANNOT access the URL with trailing slash ***
    return "Index Page"

@app.route('/home/')
@app.route('/home/<string:username>/')
def hello_world(username=None):
    # *** Can access the URL without trailing slash ***
    return render_template('hello.html', username=username)

@app.route('/profile/<string:username>')
def show_user_profile(username):
    return "Profile of user: %s" % username
    # return "Profile of user: %s" % escape(username)

@app.route('/post/<int:post_id>')
def show_single_post(post_id):
    return "Post ID is: %d" % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return "Subpath %s" % escape(subpath)

url_for('static', filename='base.css')

# TESTING
with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='Prashanth', next='/'))

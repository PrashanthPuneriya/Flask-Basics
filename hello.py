from flask import Flask
# from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/home')
def hello_world():
    return "Hello World"

@app.route('/profile/<string:username>/')
def show_user_profile(username):
    # Can access the URL without trailing slash
    return "Profile of user: %s" % username
    # return "Profile of user: %s" % escape(username)

@app.route('/post/<int:post_id>')
def show_single_post(post_id):
    return "Post ID is: %d" % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath
from flask import Flask, url_for, render_template
# from markupsafe import escape

app = Flask(__name__)

@app.route('/index')
# *** CANNOT access the URL with trailing slash ***
def index():
    return "Index Page"

@app.route('/home/')
# *** CAN access the URL without trailing slash ***
@app.route('/home/<string:username>/')
def hello_world(username=None):
    return render_template('hello.html', username=username)

@app.route('/profile/<string:username>')
def show_user_profile(username):
    return f"Profile of user: {username}"

@app.route('/post/<int:post_id>')
def show_single_post(post_id):
    return f"Post ID is: {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {subpath}"

# url_for('static', filename='base.css')

# TESTING
with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='Prashanth', next='/'))

if __name__ == "__main__":
    app.run(debug=True)
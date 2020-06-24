from flask import Flask, redirect, url_for, render_template
# from markupsafe import escape


app = Flask(__name__)

@app.route('/')
@app.route('/index')
# *** CANNOT access the URL with trailing slash ***
def index():
    return redirect(url_for("home"))


@app.route('/home/')
# *** CAN access the URL without trailing slash ***
def home():
    return "HOME Page"


@app.route('/profile/<string:username>')
def show_user_profile(username=None):
        return render_template('profile.html', username=username)


@app.route('/post/<int:post_id>')
def show_single_post(post_id):
    return f"Post ID is: {post_id}"


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {subpath}"


# TESTING
with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='Prashanth', next='/'))


if __name__ == "__main__":
    app.run(debug=True)
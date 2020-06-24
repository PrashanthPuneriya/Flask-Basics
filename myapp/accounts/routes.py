from flask import Blueprint, render_template


accounts = Blueprint(
    'accounts',
    __name__,
    template_folder='templates',
    url_prefix='/profile'
)


@accounts.route('/<string:username>')
def show_user_profile(username=None):
    return render_template('profile.html', username=username)


@accounts.route('/posts/<int:post_id>')
def show_single_post(post_id):
    return f"Post ID is: {post_id}"


@accounts.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {subpath}"

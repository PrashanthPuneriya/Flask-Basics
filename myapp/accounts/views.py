from flask import render_template


def show_user_profile(username=None):
    return render_template('profile.html', username=username)


def show_single_post(post_id):
    return f"Post ID is: {post_id}"


def show_subpath(subpath):
    return f"Subpath {subpath}"

from flask import Blueprint
from . import views


accounts = Blueprint(
    'accounts',
    __name__,
    template_folder='templates',
    url_prefix='/profile/'
)

accounts.add_url_rule('<string:username>/', view_func=views.show_user_profile)
accounts.add_url_rule('posts/<int:post_id>/', view_func=views.show_single_post)
accounts.add_url_rule('path/<path:subpath>/', view_func=views.show_subpath)

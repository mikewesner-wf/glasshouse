"""
decorators.py

Decorators for URL handlers

"""

from functools import wraps
from google.appengine.api import users
from flask import redirect, request, abort

# my requests library wrapper
from application import call

def login_required(func):
    """Requires standard login credentials"""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            return redirect(users.create_login_url(request.url))
        return func(*args, **kwargs)
    return decorated_view

def login_and_oauth2_required(func):
    """Requires oauth2 credentials"""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            return redirect(users.create_login_url(request.url))

        credentials = call._get_creds(users.get_current_user().user_id())
        if not credentials:
            return redirect('/signup')

        return func(*args, **kwargs)
    return decorated_view

def admin_required(func):
    """Requires App Engine admin credentials"""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if users.get_current_user():
            if not users.is_current_user_admin():
                abort(401)  # Unauthorized
            return func(*args, **kwargs)
        return redirect(users.create_login_url(request.url))
    return decorated_view

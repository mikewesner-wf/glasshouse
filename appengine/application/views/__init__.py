"""
views.py

URL route handlers
"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect
from application import app

from flask_cache import Cache


from application.decorators import login_required, admin_required, login_and_oauth2_required
# from application.forms import ExampleForm
# from application.models import ExampleModel

# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


from application.views.signup import *

@app.route('/')
def home():
    user = users.get_current_user()
    credentials = None
    if user:
        credentials = call._get_creds(user.user_id())

    return render_template('home.html', user=user, credentials=credentials)

@app.route('/logout')
def logout():
    return redirect(users.create_logout_url('/'))


@app.route('/myhome')
@login_and_oauth2_required
def myhome():
    credentials = call._get_creds(users.get_current_user().user_id())

    context = {}

    # Does user have a home setup?



    return render_template('myhome.html', **context)

@app.route('/addhome')
@login_and_oauth2_required
def addhome():
    user = users.get_current_user()
    credentials = call._get_creds(user.user_id())
    if not credentials:
        return redirect(url_for(signup))

    context = {}



    return render_template('myhome.html', **context)

# @login_required
# def list_examples():
#     """List all examples"""
#     examples = ExampleModel.query()
#     form = ExampleForm()
#     if form.validate_on_submit():
#         example = ExampleModel(
#             example_name = form.example_name.data,
#             example_description = form.example_description.data,
#             added_by = users.get_current_user()
#         )
#         try:
#             example.put()
#             example_id = example.key.id()
#             flash(u'Example %s successfully saved.' % example_id, 'success')
#             return redirect(url_for('list_examples'))
#         except CapabilityDisabledError:
#             flash(u'App Engine Datastore is currently in read-only mode.', 'info')
#             return redirect(url_for('list_examples'))
#     return render_template('list_examples.html', examples=examples, form=form)


# @login_required
# def edit_example(example_id):
#     example = ExampleModel.get_by_id(example_id)
#     form = ExampleForm(obj=example)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             example.example_name = form.data.get('example_name')
#             example.example_description = form.data.get('example_description')
#             example.put()
#             flash(u'Example %s successfully saved.' % example_id, 'success')
#             return redirect(url_for('list_examples'))
#     return render_template('edit_example.html', example=example, form=form)


# @login_required
# def delete_example(example_id):
#     """Delete an example object"""
#     example = ExampleModel.get_by_id(example_id)
#     try:
#         example.key.delete()
#         flash(u'Example %s successfully deleted.' % example_id, 'success')
#         return redirect(url_for('list_examples'))
#     except CapabilityDisabledError:
#         flash(u'App Engine Datastore is currently in read-only mode.', 'info')
#         return redirect(url_for('list_examples'))


@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


# @cache.cached(timeout=60)
# def cached_examples():
#     """This view should be cached for 60 sec"""
#     examples = ExampleModel.query()
#     return render_template('list_examples_cached.html', examples=examples)

@app.route('/_ah/warmup')
def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''


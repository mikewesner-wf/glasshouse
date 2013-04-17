"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb


class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)


class IndigoHouse(ndb.Model):
    owner = ndb.StringProperty()
    host = ndb.StringProperty()
    apikey = ndb.StringProperty()


class Devices(ndb.Model):
    pass

class Variables(ndb.Model):
    pass

class Actions(ndb.Model):
    pass



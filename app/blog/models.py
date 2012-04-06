import ndbunq
from google.appengine.ext import ndb


class User(ndbunq.Model):
    username = ndb.StringProperty(required=True)

    class Meta:
        unique = (('username',),)

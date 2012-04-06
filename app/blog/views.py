from google.appengine.ext import ndb

from . import blog
from .models import User


@blog.route('/init/')
@ndb.toplevel
def user_init():
    u1 = User(username='foobar')
    u1.put()

    u2 = User(username='foobar')
    u2.put()

    raise ndb.Return('OK')

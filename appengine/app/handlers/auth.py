#!/usr/bin/env python
from ._jinja import JinjaHandler
from .constants import PATH_LOGIN

from google.appengine.api import users
from app.models import User

def do_login(self):
    email = users.get_current_user().email() if users.get_current_user() else None
    if not email:
        self.redirect(users.create_login_url(PATH_LOGIN), abort=True)

    user = User.get_by_id(email)
    if not user:
        user = User(id=email, name=email)
        user.put()

    user.update_last_login()

    return user.key.urlsafe()

class AuthenticationHandler(JinjaHandler):
    def get(self):
        token = do_login(self)
        props = {
            'token': token
        }
        self.render('login', **props)


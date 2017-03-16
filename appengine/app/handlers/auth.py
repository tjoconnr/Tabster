import os
import logging
from datetime import datetime
from google.appengine.api import users

from app.models import User

from .constants import TOKEN_HEADER, PATH_DEFAULT

#------------------------------------------------------------------------------
#
#    User Authentication
#
#------------------------------------------------------------------------------
def get_logged_in_user(self):
    if not users.get_current_user():
        return None

    return users.get_current_user().email()

def get_app_user(self):
    user_email = get_logged_in_user(self)
    if not user_email:
        return None

    return User.get_or_create_user(email=user_email)

def do_login(self):
    user = get_app_user(self)
    user.last_login = str(datetime.now())
    user.logins += 1
    user.put_async()

    self.redirect(PATH_DEFAULT, abort=True)

#------------------------------------------------------------------------------
#
#    API Authentication
#
#------------------------------------------------------------------------------
def get_auth_token(self):
    return self.request.headers.get(TOKEN_HEADER, None)

def authorize_api(self):
    user = get_api_user(self)
    if not user:
        self.error(401)
        self.response.out.write("User not authorized.")
        return

    user.api_last_login = str(datetime.now())
    user.api_logins += 1
    user.put_async()

    return user

def get_api_user(self, app_state={}):
    token = get_auth_token(self)
    if not token:
        return None

    user = User.get_user_by_token(token=token)
    if not user:
        return None

    return user

#------------------------------------------------------------------------------
#
#    AppEngine State
#
#------------------------------------------------------------------------------
def get_app_state(self):
    return {
        'home': PATH_DEFAULT,
        'loggedInUser': get_logged_in_user(self),
        'loginUrl': users.create_login_url('/login'),
        'logoutUrl': users.create_logout_url('/'),
        'isAdmin': users.is_current_user_admin(),
        'version': os.environ['CURRENT_VERSION_ID']
    }



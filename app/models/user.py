import logging
from google.appengine.ext import ndb

from app.utils.gravatar import gravatar

from ._model import BaseModel

class User(BaseModel):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    avatar = ndb.ComputedProperty(lambda self: gravatar(self.email))
    last_login = ndb.StringProperty()
    logins = ndb.IntegerProperty(default=0)
    api_last_login = ndb.StringProperty()
    api_logins = ndb.IntegerProperty(default=0)

    @staticmethod
    def get_user(email):
        return User.query(User.email==email).get()

    @staticmethod
    def get_user_by_token(token):
        try:
            return ndb.Key(urlsafe=token).get()
        except:
            logging.info('Invalid token: %s' % token)
            return None


    @staticmethod
    def get_or_create_user(email):
    	user = User.get_user(email=email)
    	if not user:
            user = User(email=email, name=email)
            user.put()
    	return user

    @staticmethod
    def update_last_login(email):
        user = User.get_or_create_user(email=email)
        user.last_login = str(datetime.now())
        user.logins += 1
        user.put()

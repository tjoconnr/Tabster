import logging
from datetime import datetime, time

from google.appengine.ext import ndb
from app.utils.gravatar import gravatar

from ._model import BaseModel

def date_now():
    return datetime.now()

class User(BaseModel):
    name = ndb.StringProperty(required=True)
    avatar = ndb.ComputedProperty(lambda self: gravatar(self.key.id()))
    last_login = ndb.DateTimeProperty()
    logins = ndb.IntegerProperty(default=1)
    api_last_hit = ndb.DateTimeProperty()
    api_hits = ndb.IntegerProperty(default=1)

    def track_api_hit(self):
        self.api_last_hit = date_now()
        self.api_hits += 1

        future = self.put_async()
        future.get_result()

    def update_last_login(self):
        self.last_login = date_now()
        self.logins += 1

        future = self.put_async()
        future.get_result()

    @staticmethod
    def get_user(email):
        return User.get_by_id(email)

    @staticmethod
    def get_user_by_token(token):
        try:
            return ndb.Key(urlsafe=token).get()
        except:
            logging.info('Invalid token: %s' % token)
            return None


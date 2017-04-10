#!/usr/bin/env python
import logging
import json
import webapp2

from app.models import User, model_from_string
from ._jinja import get_app_state

TOKEN_HEADER = 'Authorization'

def do_api_login(self):
    self.response.headers['Content-Type'] = 'application/json'
    token = self.request.headers.get(TOKEN_HEADER, None)
    user = User.get_user_by_token(token)
    if not user:
        self.error(401)
        return

    user.track_api_hit()
    return user

def json_dump(s):
    return json.dumps(s, indent=5, sort_keys=True)

class ApiHandler(webapp2.RequestHandler):

    def get(self, endpoint):
        if endpoint == "status":
            self.response.out.write("OK")
            return

        user = do_api_login(self)
        if not user:
            return

        item_id = None
        if endpoint.find("/") > 0:
            item_id = endpoint.split('/')[1]
            endpoint = endpoint.split('/')[0]

        resp = {}
        if endpoint == "me":
            resp = user.to_dict()
        else:
            MyModel = model_from_string(endpoint)
            if not MyModel:
                self.error(500)
                self.response.out.write("Model not found: %s" % endpoint)
                return

            if item_id:
                resp = MyModel.get_by_id(int(item_id)).to_dict()
            else:
                resp = [j.to_dict() for j in MyModel.query().order(MyModel.name).fetch(None)]

        self.response.out.write(json_dump(resp))


    def post(self, endpoint):
        logging.info("ApiHandler - POST /%s" % (endpoint))

        user = do_api_login(self)
        if not user:
            return

        # Parse string into Model name
        MyModel = model_from_string(endpoint)
        db_item = MyModel(**self.request.POST)
        db_item.put()
        self.response.write(json_dump(db_item.to_dict()))

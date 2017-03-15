#!/usr/bin/env python
import logging
import json
import webapp2

from app.tests import run_tests
from .constants import TOKEN_HEADER
from .auth import authorize_api, get_app_state

def string_to_model_class(s):
    return eval(s.title())

class ApiHandler(webapp2.RequestHandler):

    def add_cors_headers(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.headers.add_header("Access-Control-Allow-Headers", "%s, if-none-match" % TOKEN_HEADER)
        self.response.headers.add_header("Access-Control-Allow-Methods", "GET,POST")

    def options(self, endpoint):
        self.add_cors_headers()

    def get(self, endpoint):
        self.add_cors_headers()

        if endpoint == "status":
            self.response.out.write("OK")
            return

        user = authorize_api(self)
        if not user:
            return

        if endpoint == "user":
            self.response.out.write(json.dumps(user.to_dict(), indent=5))
            return

        if endpoint == "authorize":
            self.response.out.write(json.dumps(get_app_state(self), indent=5))
            return

        if endpoint == "test":
            run_tests(self)

    def post(self, endpoint):
        logging.info("ApiHandler - POST /%s" % (endpoint))
        self.add_cors_headers()

        user = authorize_api(self)
        if not user:
            return

        # Parse string into Model name
        MyModel = model_from_string(endpoint)
        db_item = MyModel(**self.request.POST)
        db_item.put()
        self.response.write(json.dumps(db_item.to_dict()))

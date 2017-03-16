#!/usr/bin/env python
import logging
import json
import webapp2

from app.tests import run_tests
from .constants import TOKEN_HEADER
from .auth import authorize_api, get_app_state

from app.models import *
def string_to_model_class(s):
    try:
        return eval(s.title())
    except:
        pass

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

        if endpoint == "test":
            run_tests(self)
            return

        user = authorize_api(self)
        if not user:
            return

        item_id = None
        if endpoint.find("/") > 0:
            item_id = endpoint.split('/')[1]
            endpoint = endpoint.split('/')[0]

        logging.info(item_id)

        resp = {}
        if endpoint == "user":
            resp = user.to_dict()
        elif endpoint == "authorize":
            resp = get_app_state(self)
        else:
            MyModel = string_to_model_class(endpoint)
            if not MyModel:
                self.error(500)
                self.response.out.write("Model not found: %s" % endpoint)
                return

            if item_id:
                resp = MyModel.get_by_id(int(item_id)).to_dict()
            else:
                resp = [j.to_dict() for j in MyModel.query().order(MyModel.name).fetch(None)]

        self.response.out.write(json.dumps(resp, indent=5))


    def post(self, endpoint):
        logging.info("ApiHandler - POST /%s" % (endpoint))
        self.add_cors_headers()

        user = authorize_api(self)
        if not user:
            return

        # Parse string into Model name
        MyModel = string_to_model_class(endpoint)
        db_item = MyModel(**self.request.POST)
        db_item.put()
        self.response.write(json.dumps(db_item.to_dict()))

#!/usr/bin/env python
from ._jinja import JinjaHandler

from .constants import VALID_PAGES
from .auth import do_login

class PageHandler(JinjaHandler):
    def get(self, endpoint):

        if endpoint == "":
            endpoint = "index"

        if endpoint == "login":
            do_login(self)

        if endpoint.find('a/') == 0:
            endpoint = "react"

        self.render(endpoint)


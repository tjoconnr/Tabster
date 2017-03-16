#!/usr/bin/env python
from ._jinja import JinjaHandler

from .constants import VALID_PAGES
from .auth import do_login

class PageHandler(JinjaHandler):
    def get(self, endpoint):
        if endpoint == "":
            endpoint = "index"
        elif endpoint == "login":
            do_login(self)
        elif endpoint.find('a/') == 0:
            endpoint = "react"
        elif not endpoint in VALID_PAGES:
            self.redirect('/404?msg=%s' % endpoint)
        self.render(endpoint)

#!/usr/bin/env python
from ._jinja import JinjaHandler

VALID_PAGES = ['index', 'admin', '401', '404', '500']

class PageHandler(JinjaHandler):
    def get(self, endpoint):
        if endpoint == "":
            endpoint = "index"
        elif endpoint.find('a/') == 0:
            endpoint = "react"
        elif not endpoint in VALID_PAGES:
            self.redirect('/404?msg=%s' % endpoint)
        self.render(endpoint)

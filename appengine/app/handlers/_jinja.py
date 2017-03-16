#!/usr/bin/env python
import json
import webapp2
from webapp2_extras import jinja2
from jinja2.exceptions import TemplateNotFound

from .auth import get_app_state, get_app_user

class JinjaHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        jinja_obj = jinja2.get_jinja2(app=self.app)
        jinja_obj.environment.filters.update({
            "json": json.dumps
        })
        return jinja_obj

    def render(self, _template, **context):
        obj = {}
        user = get_app_user(self)
        obj['appState'] = {
            "auth": get_app_state(self),
            "user": user.to_dict() if user else None
        }
        obj['page'] = _template
        obj['msg'] = self.request.get('msg')
        obj.update(context)

        try:
            rv = self.jinja2.render_template("%s.html" % _template, **obj)
            self.response.write(rv)
        except TemplateNotFound:
            if _template != '404':
                self.redirect('/404?msg=%s' % self.request.url, abort=True)

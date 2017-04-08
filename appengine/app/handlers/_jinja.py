#!/usr/bin/env python
import json
import os
import webapp2

from webapp2_extras import jinja2
from jinja2.exceptions import TemplateNotFound
from google.appengine.api import users

from .constants import PATH_LOGIN, PATH_DEFAULT

def get_app_state():
    return {
        'home': PATH_DEFAULT,
        'loginUrl': users.create_login_url(PATH_LOGIN),
        'logoutUrl': users.create_logout_url('/'),
        'userEmail': users.get_current_user().email() if users.get_current_user() else None,
        'userIsAdmin': users.is_current_user_admin(),
        'version': os.environ['CURRENT_VERSION_ID']
    }

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
        obj['appState'] = get_app_state()
        obj['page'] = _template
        obj['msg'] = self.request.get('msg')
        obj.update(context)

        try:
            rv = self.jinja2.render_template("%s.html" % _template, **obj)
            self.response.write(rv)
        except TemplateNotFound:
            if _template != '404':
                self.redirect('/404?msg=%s' % self.request.url, abort=True)

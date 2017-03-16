#!/usr/bin/env python
import webapp2
from app.handlers import ApiHandler, PageHandler

#-----------------------------------------------------------------------------
#
#   ** START APPLICATION **
#
#-----------------------------------------------------------------------------

ROUTES = [
    ("/api/v1/(.*)", ApiHandler),
    ("/(.*)", PageHandler)
]
app = webapp2.WSGIApplication(ROUTES, debug=True)

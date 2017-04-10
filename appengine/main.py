#!/usr/bin/env python
import webapp2
from app.handlers import *

#-----------------------------------------------------------------------------
#
#   ** START APPLICATION **
#
#-----------------------------------------------------------------------------

ROUTES = [
    ("/login", AuthenticationHandler),
    ("/migrate-db", DatabaseMigrationHandler),
    ("/api/v1/(.*)", ApiHandler),
    ("/(.*)", PageHandler)
]
app = webapp2.WSGIApplication(ROUTES, debug=True)

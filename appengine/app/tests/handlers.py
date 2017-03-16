#!/usr/bin/env python
from _test import BaseTestCase
import webapp2
import json
import logging

from app.handlers.constants import TOKEN_HEADER

TEST_VALID_TOKEN = "ahFkZXZ-b21lZ2EtdGFic3RlcnIRCxIEVXNlchiAgICAgODXCAw"

URL_AUTH = "/api/v1/authorize"
URL_USER = "/api/v1/user"
URL_STATUS = "/api/v1/status"

class HandlersTestCase(BaseTestCase):
    def testPublicWebsite(self):
        resp = self.app.get_response("/")
        self.assertEqual(resp.status_int, 200)

    def testPublicWebsiteNotFoundRedirect(self):
        resp = self.app.get_response("/somefakepagethatwillneverexist")
        self.assertEqual(resp.status_int, 302)

    def testApiStatus(self):
        resp = self.app.get_response(URL_STATUS)
        self.assertEqual(resp.status_int, 200)
        self.assertEqual(resp.body, "OK")

    def testApiAuthorizeNoTokenReturns401(self):
        resp = self.app.get_response(URL_AUTH)
        self.assertEqual(resp.status_int, 401)

    def testApiAuthorizeInvalidTokenRequestReturns401(self):
        req = webapp2.Request.blank(URL_AUTH)
        req.headers.update({
            TOKEN_HEADER: 'ahFkZ'
        })
        resp = req.get_response(self.app)
        self.assertEqual(resp.status_int, 401)

    def testApiAuthorizeValidRequest(self):
        req = webapp2.Request.blank(URL_AUTH)
        req.headers.update({
            TOKEN_HEADER: TEST_VALID_TOKEN
        })
        resp = req.get_response(self.app)
        obj = json.loads(resp.body)
        self.assertEqual(resp.status_int, 200)

    def testApiAuthorizeValidUserRequest(self):
        req = webapp2.Request.blank(URL_USER)
        req.headers.update({
            TOKEN_HEADER: TEST_VALID_TOKEN
        })
        resp = req.get_response(self.app)
        obj = json.loads(resp.body)

        self.assertEqual(resp.status_int, 200)
        self.assertEqual(obj['_urlsafe'], TEST_VALID_TOKEN)

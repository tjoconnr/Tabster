#!/usr/bin/env python
import unittest
from google.appengine.api import memcache

from handlers import HandlersTestCase

def get_test_suite():
    TEST_ARRAY = [
        HandlersTestCase
    ]
    arr = []
    for t in TEST_ARRAY:
        arr.append(unittest.TestLoader().loadTestsFromTestCase(t))
    return unittest.TestSuite(arr)

def flush():
    '''Fake method allowing Response to be passed into TestRunner'''
    pass

def run_tests(webapp2_obj):
    memcache.flush_all()
    full_suite = get_test_suite()

    # Run test
    webapp2_obj.response.flush = flush
    webapp2_obj.response.headers['Content-Type'] = "text/plain"
    runner = unittest.TextTestRunner(stream=webapp2_obj.response, verbosity=3)
    runner.run(full_suite)

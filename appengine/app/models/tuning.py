#!/usr/bin/env python
from google.appengine.ext import ndb
from _model import BaseModel

class Tuning(BaseModel):
    name = ndb.StringProperty(required=True)
    interval = ndb.IntegerProperty(repeated=True)
    root = ndb.IntegerProperty(required=True, choices=[0,1,2,3,4,5,6,7,8,9,10,11]) # C, Db, D, Eb, ..., Bb, B

    @staticmethod
    def populate():
        t = Tuning(key_name="standard", name="Guitar - Standard Tuning", interval=[0,5,5,5,4,5], root=4)
        t.put()


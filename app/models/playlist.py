#!/usr/bin/env python
from google.appengine.ext import ndb
from _model import BaseModel

class Playlist(BaseModel):
    name = ndb.StringProperty(required=True, default="New Playlist")
    songs = ndb.KeyProperty(repeated=True)
    views = ndb.IntegerProperty(default=0)

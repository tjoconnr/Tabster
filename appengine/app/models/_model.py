#!/usr/bin/env python
import json
from google.appengine.ext import ndb

class BaseModel(ndb.Model):
    def to_json(self, exclude=None, include=None):
        return json.dumps(self.to_dict(exclude=exclude, include=include))

    def to_dict(self, **kwargs):
        obj = super(BaseModel, self).to_dict(**kwargs)
        obj['_id'] = self.key.id()
        obj['_urlsafe'] = self.key.urlsafe()
        for key in obj:
            val = obj[key]
            if isinstance(val, ndb.Key):
                obj[key] = val.id()
        return obj

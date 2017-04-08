#!/usr/bin/env python
import json
from google.appengine.ext import ndb
from datetime import datetime

class BaseModel(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)

    def to_json(self):
        return json.dumps(self.to_dict(sort_keys=True, indent=5))

    def to_dict(self, **kwargs):
        obj = super(BaseModel, self).to_dict(**kwargs)
        obj['_id'] = self.key.id()
        for key in obj:
            val = obj[key]
            if isinstance(val, ndb.Key):
                obj[key] = val.id()
            elif isinstance(val, datetime):
                obj[key] = str(val)
        return obj

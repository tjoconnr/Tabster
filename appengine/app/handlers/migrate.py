#!/usr/bin/env python
import json
import webapp2
import logging
from datetime import datetime

from google.appengine.api import urlfetch, memcache, users, taskqueue
from app.models import SongItem
from app.utils.spotify import search_track

class DatabaseMigrationHandler(webapp2.RequestHandler):
    def get(self):
        queue_import()
        self.response.out.write("OK")

    def post(self):
        sync_song(self.request.get('id'))

def load_songs_cached():
    data = memcache.get('songs')
    if not data:
        url = "https://omega-tabster.appspot.com/api/json/song"
        data = json.loads(urlfetch.fetch(url).content)
        memcache.set('songs', data)
    return data

def sync_song(s):
    logging.info(s)
    song = json.loads(urlfetch.fetch("https://omega-tabster.appspot.com/api/song/%s" % s).content)
    s = SongItem(
        id=s,
        name=song['name'],
        artist=song['artist']['name'],
        song_key=song['song_key'],
        tab=song['tab'],
        modified = datetime.now()
    )
    meta = search_track(song['name'] + ' ' + song['artist']['name'])
    if meta:
        for k, v in meta.iteritems():
            setattr(s, k, v)
    future = s.put_async()
    future.get_result()

def queue_import():
    songs = load_songs_cached()
    for s in songs:
        queue = taskqueue.Queue(name='default')
        task = taskqueue.Task(
            url='/migrate-db',
            target='beta',
            params={'id': s})

        rpc = queue.add_async(task)

        # Wait for the rpc to complete and return the queued task.
        task = rpc.get_result()
        logging.info('Task %s enqueued, ETA %s.' % (task.name, task.eta))

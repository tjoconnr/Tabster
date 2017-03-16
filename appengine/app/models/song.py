#!/usr/bin/env python
import math
import logging

from google.appengine.ext import ndb
from google.appengine.api import memcache

from _model import BaseModel

class Song(BaseModel):
    name = ndb.StringProperty(required=True)
    artist = ndb.StringProperty()
    album = ndb.StringProperty()
    tuning = ndb.StringProperty()
    image_url = ndb.StringProperty()
    song_key = ndb.StringProperty(choices=["A","Ab","B","Bb","C","D","Db","E","Eb","F","G","Gb"])
    tab = ndb.TextProperty()
    views = ndb.IntegerProperty(default=0)

    @staticmethod
    def get_song_cached(slug, cache_seconds=60*60*24):
        cache_key = "get_song_cached: %s" % slug
        data = memcache.get(cache_key)
        if data is None:
            data = Song.get_song(slug)
            if data:
                memcache.add(cache_key, data, cache_seconds)
        return data

    @staticmethod
    def get_song(slug):
        return Song.get_by_key_name(slug)

    @staticmethod
    def update_song(name, slug, tab, song_key, modified_by, artist_slug, artist_name, album_slug, album_name):
        dt_now = datetime.datetime.now()
        song = get_song(slug)
        if not song:
            song = Song(key_name=slug,name=name,created_by=modified_by,created_on=dt_now)

        if artist_slug:
            song.artist = create_artist(artist_slug, artist_name)

        if album_slug:
            song.album = create_album(album_slug, album_name, artist_slug, artist_name)

        song.name = name
        song.tab = tab
        song.song_key = song_key
        song.modified_by = modified_by
        song.modified_on = dt_now
        song.put()

        logging.info("update_song(%s)" % slug)

    @staticmethod
    def get_songs_cached(sort_order="name", page=0, limit=50, cache_seconds=60*60*24):
        cache_key = "get_songs_cached: %s,%s,%s" % (sort_order, page, limit)
        data = memcache.get(cache_key)
        if data is None:
            data = Song.get_songs(sort_order, page, limit)
            if data:
                memcache.add(cache_key, data, cache_seconds)
        return data

    @staticmethod
    def get_songs(sort_order="name", page=0, limit=50):

        # Begin query
        q = Song.query()

        # Get total count
        total_records = q.count()

        # Get pages/page
        pages = int(math.ceil(float(total_records)/float(limit)))

        # Get offset
        offset = 0
        if page>0:
            offset = (page * limit)

        # Parse sort order
        if sort_order.find(",") > 0:
            for s in sort_order.split(','):
                q.order(s)
        else:
            q.order(sort_order)

        # Run query
        songs = q.run(limit=limit, offset=offset, batch_size=20)

        # Prev/next URLs
        url = "/a/songs?offset=%s&order=%s"
        if pages > 0:
            if page > 0:
                prev_page = url % (str(page - 1), sort_order)
            else:
                prev_page = "#"

            if page < pages-1:
                next_page = url % (str(page + 1), sort_order)
            else:
                next_page = "#"
        else:
            prev_page = "#"
            next_page = "#"

        ret = {}
        ret['data'] = list(songs)
        ret['pages'] = pages
        ret['sort_order'] = sort_order
        ret['current_page'] = page
        ret['limit'] = limit
        ret['total_records'] = total_records
        ret['next_page'] = next_page
        ret['prev_page'] = prev_page
        return ret

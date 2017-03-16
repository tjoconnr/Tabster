import json
import urllib
from google.appengine.api import urlfetch

def search_track(q):
	params = {
	    'type': 'track',
	    'q': q
	}
	result = urlfetch.fetch("https://api.spotify.com/v1/search?%s" % urllib.urlencode(params))
	try:
		obj = json.loads(result.content)
		item = obj['tracks']['items'][0]
		return {
			'album': item['album']['name'],
			'image_url': item['album']['images'][0]['url']
		}
	except:
		return None



# def append_meta(s, include_artist=True):
#     q = s.name
#     if include_artist:
#         q += " " + s.artist
#     meta = search_track(q)
#     if not meta:
#         print "track not found: %s" % s.name
#         return s

#     for k, v in meta.iteritems():
#         setattr(s, k, v)
#     s.put()
#     return s



# songs = Song.query(Song.image_url == None).fetch(None)
# for s in songs:
#     print s.name.r
#     #newSong = append_meta(s, False)
#     #print json.dumps(newSong.to_dict(exclude=['tab']), indent=5)

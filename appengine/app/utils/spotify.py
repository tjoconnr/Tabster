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

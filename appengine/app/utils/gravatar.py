import urllib, hashlib

def gravatar(email,img_size=100):
    gravatar_url = "http://gravatar.com/avatar/"
    gravatar_url += hashlib.md5(email.lower()).hexdigest()
    gravatar_url += "?"
    gravatar_url += urllib.urlencode({
        's': img_size,
        'd': "mm",
    })
    return gravatar_url

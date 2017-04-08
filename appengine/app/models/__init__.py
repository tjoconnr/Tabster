from user import User
from song import SongItem

__all__ = ['User', 'SongItem']

def model_from_string(s):
    try:
        return eval(s.replace('-', ' ').title().replace(' ', ''))
    except:
        pass


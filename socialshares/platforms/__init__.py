import urlparse
import delicious, facebook, google, linkedin, pinterest, reddit, twitter

default = [
    'facebook', 
    'twitter', 
    ]

supported = default + [
    #'delicious', 
    'google', 
    #'linkedin', 
    'pinterest', 
    'reddit', 
    ]

_platforms = globals()

def get(name):
    if name in supported:
        platform = _platforms[name]
        platform.name = name
        return platform
    else:
        raise ValueError("Could not find a platform matching " + domain)

def find(domain):
    hostname = urlparse.urlparse(domain).hostname
    name = hostname.split('.')[-2]
    return get(name)
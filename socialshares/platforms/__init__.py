from . import delicious, facebook, facebookfql, google, linkedin, pinterest, reddit, twitter

default = [
    'facebook', 
    'twitter', 
    ]

supported = default + [
    # 'delicious', 
    'facebookfql', 
    'google', 
    'linkedin', 
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
        raise ValueError("Could not find a platform matching " + name)

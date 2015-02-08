import pkg_resources

from . import utils
from . import command
from . import platforms


__version__ = pkg_resources.get_distribution("socialshares").version


headers = {
    'User-Agent': 'Pollster <https://github.com/debrouwere/pollster>',
}

fetchers = platforms    

def fetch_once(session, url, platforms):
    handlers = []
    requests = []

    for platform in platforms:
        if platform in fetchers.supported:
            handler = fetchers.get(platform)
            handlers.append(handler)
            requests.append(handler.fetch(session, url))
        else:
            raise ValueError()
        
    responses = utils.get_responses(requests)

    counts = {}
    for handler, response in zip(handlers, responses):
        # * ValueErrors indicate no JSON could be decoded
        # * KeyErrors and IndexErrors indicate the JSON didn't 
        #   contain the data we were looking for
        # * IOErrors are raised on purpose for all other
        #   error conditions
        try:
            counts[handler.name] = handler.parse(response)
        except (IOError, ValueError, KeyError, IndexError):
            pass

    return counts


def fetch(url, platforms=platforms.default, attempts=2, strict=False, concurrent=None):
    session = utils.create_session(concurrent=concurrent, headers=headers)
    counts = {}
    attempt = 0
    todo = set(platforms)
    while len(todo) and attempt < attempts:
        attempt = attempt + 1
        partial = fetch_once(session, url, todo)
        todo = todo.difference(partial)
        counts.update(partial)

    if strict and len(counts) < len(platforms):
        failures = ", ".join(todo)
        raise IOError("Could not fetch all requested sharecounts. Failed: " + failures)

    session.close()
    return counts

try:
    import grequests
    request = grequests.map
except ImportError:
    import requests
    request = lambda responses: responses
import command
import platforms


fetchers = platforms

def fetch_once(url, platforms):
    handlers = []
    requests = []

    for platform in platforms:
        if platform in fetchers.supported:
            handler = fetchers.get(platform)
            handlers.append(handler)
            requests.append(handler.fetch(url))
        else:
            raise ValueError()
        
    responses = request(requests)

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


def fetch(url, platforms=platforms.default, attempts=2, strict=False):
    counts = {}
    attempt = 0
    todo = set(platforms)
    while len(todo) and attempt < attempts:
        attempt = attempt + 1
        partial = fetch_once(url, todo)
        todo = todo.difference(partial)
        counts.update(partial)

    if strict and len(counts) < len(platforms):
        failures = ", ".join(todo)
        raise IOError("Could not fetch all requested sharecounts. Failed: " + failures)

    return counts

import grequests
import command
import platforms

requests = []

def fetch(url, requested_platforms):
    for platform in requested_platforms:
        if not platform in platforms.supported:
            raise ValueError()

        handler = platforms.get(platform)
        requests.append(handler.fetch(url))

    responses = grequests.map(requests)

    counts = {}
    for response in responses:
        handler = platforms.find(response.url)
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

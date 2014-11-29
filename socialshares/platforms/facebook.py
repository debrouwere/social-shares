import grequests

def fetch(url):
    return grequests.get('https://graph.facebook.com/', params={'id': url})

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()
    return data['shares']
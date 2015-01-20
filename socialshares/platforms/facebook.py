try:
    import grequests as requests
except ImportError:
    import requests

def fetch(url):
    return requests.get('https://graph.facebook.com/', params={'id': url})

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()
    return data['shares']
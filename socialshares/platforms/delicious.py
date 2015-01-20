try:
    import grequests as requests
except ImportError:
    import requests

def fetch(url):
    return requests.get('http://feeds.delicious.com/v2/json/urlinfo/data', params={'url': url})

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()
    return data[0]['total_posts']
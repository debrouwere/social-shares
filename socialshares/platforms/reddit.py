try:
    import grequests as requests
except ImportError:
    import requests

def fetch(url):
    return requests.get('http://buttons.reddit.com/button_info.json',
        params={'format': 'json', 'url': url})

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()
    ups = 0
    downs = 0
    for child in data['data']['children']:
        ups = ups + child['data']['ups']
        downs = downs + child['data']['downs']
        
    return {
        'ups': ups, 
        'downs': downs, 
        }
try:
    import grequests as requests
except ImportError:
    import requests

def fetch(url):
    return requests.get('http://www.linkedin.com/countserv/count/share', 
        params={'url': url, 'format': 'json'})

def parse(response):
    if response.status_code != 200:
        raise IOError()
        
    result = response.json()
    return result['count']
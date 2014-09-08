import grequests

def fetch(url):
    return grequests.get('http://www.linkedin.com/countserv/count/share', params={'url': url})

def parse(response):
    if response.status_code != 200:
        raise IOError()
        
    result = response.json()
    return result['count']
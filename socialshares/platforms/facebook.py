import grequests

def fetch(url):
    return grequests.get('https://graph.facebook.com/', params={'ids': url})

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json().values()[0]
    return data['shares']
import grequests

def fetch(url):
    # twitter doesn't like urlencoded querystring arguments
    return grequests.get('http://urls.api.twitter.com/1/urls/count.json?url=' + url)

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()
    return data['count']
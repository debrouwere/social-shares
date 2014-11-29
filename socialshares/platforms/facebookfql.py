import grequests
from urllib import urlencode

query = 'SELECT comment_count, like_count, share_count FROM link_stat WHERE url = "{}"'

def fetch(url):
    return grequests.get('https://graph.facebook.com/fql', params={
        'q': query.format(url), 
        })

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()['data'][0]
    social = {
        'comments': data['comment_count'], 
        'shares': data['share_count'], 
        'likes': data['like_count'], 
        }

    return social

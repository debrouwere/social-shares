from collections import OrderedDict

query = 'SELECT comment_count, like_count, share_count FROM link_stat WHERE url = "{}"'

def fetch(session, url):
    return session.get('https://graph.facebook.com/fql', params={
        'q': query.format(url), 
        })

def parse(response):
    if response.status_code != 200:
        raise IOError()

    # for --plain output on the command-line, it is essential
    # that the order in which counts are output doesn't change
    # around, hence the ordered dictionary
    data = response.json()['data'][0]
    social = OrderedDict((
        ('likes', data['like_count']), 
        ('shares', data['share_count']), 
        ('comments', data['comment_count']), 
        ))

    return social

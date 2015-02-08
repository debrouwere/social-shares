import re
import json

def fetch(session, url):
    # pinterest doesn't like it when we urlencode the url
    return session.get('http://api.pinterest.com/v1/urls/count.json?url=' + url)

def parse_jsonp(response):
    text = response.text
    if not re.match(r'[_a-zA-Z]', text):
        raise ValueError("Cannot unwrap incorrect JSONP.")

    start = text.index('(') + 1
    stop = text.rindex(')')
    data = text[start:stop]
    return json.loads(data)

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = parse_jsonp(response)
    return data['count']
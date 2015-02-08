import json

def fetch(session, url):
    body = json.dumps({
        'method': 'pos.plusones.get', 
        'id': 'p', 
        'key': 'p', 
        'params': { 
            'nolog': True, 
            'id': url, 
            'source': 'widget', 
            },
        'jsonrpc': '2.0', 
        'apiVersion': 'v1'
        })
    return session.post('https://clients6.google.com/rpc', data=body)

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()
    return int(data['result']['metadata']['globalCounts']['count'])
"""Social shares.

A command-line utility and Python library to access the social share counts for a particular URL.

### Usage

Usage:
  socialshares <url> [<platforms>...] [options]

Options:
  -h, --help  Show this screen.
  -p, --plain  Plain output.
  -r <attempts>, --retry <attempts>  Retry fetching up to <attempt> times [default: 1]
  -e, --exit  Exit with an error code when not all counts could be fetched.

Some examples:

```sh
# fetch count for all supported platforms, try up to three times
$ socialshares http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/

# fetch only facebook and twitter
$ socialshares http://www.theguardian.com/politics facebook twitter \
    --retry 2
```

### Supported platforms

Platform   | Description
---------- | -----------
google     | google +1's
facebook   | facebook likes
pinterest  | pinterest pins
reddit     | reddit ups and downs (summed across posts)
twitter    | twitter tweets and retweets containing the URL

Platforms are fetched in parallel and retried (once by default).
If no platforms are specified, just facebook and twitter will be returned.

### Output

By default, `socialshares` outputs JSON:

```json
{
  "reddit": {
    "downs": 0, 
    "ups": 6
  }, 
  "google": 20, 
  "facebook": 1498, 
  "twitter": 300, 
  "pinterest": 1
}
```

Use the `--plain` flag if instead you'd like space-separated output.

```sh
$ socialshares http://www.theguardian.com/politics twitter
57
```

### Usage from Python

```python
import socialshares
counts = socialshares.fetch(url, ['facebook', 'pinterest'])
```

### Installation

```sh
pip install socialshares
```
"""

import sys
from docopt import docopt
import json
import socialshares


def main():
    arguments = docopt(__doc__, version='Social shares 0.1')
    url = arguments['<url>']
    attempts = int(arguments['--retry']) + 1
    plain = arguments['--plain']
    strict = arguments['--exit']
    platforms = arguments['<platforms>'] or socialshares.platforms.default
    todo = set(platforms)

    counts = {}
    attempt = 0
    while len(todo) and attempt < attempts:
        attempts = attempts + 1
        partial = socialshares.fetch(url, platforms)
        todo = todo.difference(partial)
        counts.update(partial)

    if strict and len(counts) < len(platforms):
        sys.exit(1)
    elif plain:
        print " ".join(map(str, counts.values()))
    else:
        print json.dumps(counts, indent=2)

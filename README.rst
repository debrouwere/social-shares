Social shares
=============

A command-line utility and Python library to access the social share
counts for a particular URL.

Usage
~~~~~

::

    Usage:
      socialshares <url> [<platforms>...] [options]

    Options:
      -h, --help  Show this screen.
      -p, --plain  Plain output.
      -r <attempts>, --retry <attempts>  Retry fetching up to <attempt> times [default: 1]
      -e, --exit  Exit with an error code when not all counts could be fetched.

Some examples:

.. code:: sh

    # fetch count for all supported platforms, 
    # try again once (the default) for platforms that fail
    $ socialshares http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/

    # fetch only facebook and twitter
    $ socialshares http://www.theguardian.com/politics facebook twitter     --retry 2

Supported platforms
~~~~~~~~~~~~~~~~~~~

+---------------+------------------------------------------------------------------------------------------------+
| Platform      | Description                                                                                    |
+===============+================================================================================================+
| twitter       | twitter tweets and retweets containing the URL                                                 |
+---------------+------------------------------------------------------------------------------------------------+
| facebook      | facebook likes                                                                                 |
+---------------+------------------------------------------------------------------------------------------------+
| facebookfql   | facebook likes, shares and comments (in that order; deprecated but supported until mid-2016)   |
+---------------+------------------------------------------------------------------------------------------------+
| linkedin      | linkedin shares                                                                                |
+---------------+------------------------------------------------------------------------------------------------+
| google        | google +1's                                                                                    |
+---------------+------------------------------------------------------------------------------------------------+
| pinterest     | pinterest pins                                                                                 |
+---------------+------------------------------------------------------------------------------------------------+
| reddit        | reddit ups and downs (summed across posts)                                                     |
+---------------+------------------------------------------------------------------------------------------------+

Platforms are fetched in parallel and retried (once by default.) If no
platforms are specified, just facebook and twitter will be returned.

Output
~~~~~~

By default, ``socialshares`` outputs JSON:

.. code:: json

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

Use the ``--plain`` flag if instead you'd like space-separated output.

.. code:: sh

    $ socialshares http://www.theguardian.com/politics twitter
    57

Usage from Python
~~~~~~~~~~~~~~~~~

.. code:: python

    import socialshares
    counts = socialshares.fetch(url, ['facebook', 'pinterest'])

Installation
~~~~~~~~~~~~

.. code:: sh

    pip install socialshares


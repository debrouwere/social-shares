from requests import Session
from textwrap import dedent


def check_concurrency():
    try:
        import requests_futures
        return True
    except ImportError:
        return False

def create_session(concurrent=None, **options):
    """
    Concurrency can be required (True), desired (None) or disabled (False)
    we only throw an import error if concurrency is required yet cannot be
    satisfied.
    """

    if concurrent is False:
        session = Session()
    else:
        try:
            from requests_futures.sessions import FuturesSession
            session = FuturesSession()
        except ImportError:
            if concurrent is True:
                raise ImportError(dedent("""
                    Could not find requests_futures.
                    Please disable concurrency or install this package.
                    If using Python 2.x, additionally install the futures package.
                    """))
            else:
                session = Session()

    for key, value in options.items():
        setattr(session, key, value)

    return session


# provide a single interface futures and synchronous requests
# (which we pass through untouched)
def get_response(response):
    if hasattr(response, 'result'):
        return response.result()
    else:
        return response

def get_responses(futures):
    return [get_response(future) for future in futures]

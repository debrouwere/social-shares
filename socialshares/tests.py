import os
import unittest
import subprocess
import json
import socialshares


url = 'http://www.theguardian.com/politics/2014/sep/08/pound-slumps-scottish-yes-campaign-poll-lead'


# share counts can differ on repeated fetches, but not by much
def is_close(a, b):
    return 0 <= abs(b - a) <= 5


class VerboseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls.CONCURRENT:
            print('Running tests with concurrency.')
        else:
            print('Running tests without concurrency.')


class PythonTestCase(object):
    @property
    def defaults(self):
        return dict(
            attempts=3, 
            concurrent=self.CONCURRENT, 
            )

    @property
    def lax_defaults(self):
        return dict(
            attempts=9, 
            concurrent=self.CONCURRENT, 
            )

    def test_facebook(self):
        counts = socialshares.fetch(url, ['facebook'], **self.defaults)
        self.assertIn('facebook', counts)
        self.assertIsInstance(counts['facebook'], int)

    def test_facebookfql(self):
        counts = socialshares.fetch(url, ['facebookfql'], )
        self.assertIn('facebookfql', counts)
        self.assertIsInstance(counts['facebookfql'], dict)

    def test_google(self):
        counts = socialshares.fetch(url, ['google'], **self.defaults)
        self.assertIn('google', counts)
        self.assertIsInstance(counts['google'], int)

    def test_linkedin(self):
        counts = socialshares.fetch(url, ['linkedin'], **self.defaults)
        self.assertIn('linkedin', counts)
        self.assertIsInstance(counts['linkedin'], int)

    def test_pinterest(self):
        counts = socialshares.fetch(url, ['pinterest'], **self.defaults)
        self.assertIn('pinterest', counts)
        self.assertIsInstance(counts['pinterest'], int)

    def test_reddit(self):
        counts = socialshares.fetch(url, ['reddit'], **self.defaults)
        self.assertIn('reddit', counts)
        self.assertIsInstance(counts['reddit'], dict)

    def test_twitter(self):
        counts = socialshares.fetch(url, ['twitter'], **self.defaults)
        self.assertIn('twitter', counts)
        self.assertIsInstance(counts['twitter'], int)

    def test_default(self):
        counts = socialshares.fetch(url, **self.lax_defaults)
        self.assertEqual(set(counts.keys()), set(socialshares.platforms.default))

    def test_all(self):
        counts = socialshares.fetch(url, socialshares.platforms.supported, **self.lax_defaults)
        self.assertTrue(len(counts.keys()))

    # requires stubs / spies
    def test_attempts(self):
        pass

    def test_strict(self):
        pass


class PythonSynchronousTestCase(VerboseTestCase, PythonTestCase):
    CONCURRENT = False


class PythonAsynchronousTestCase(VerboseTestCase, PythonTestCase):
    CONCURRENT = True


class CLITestCase(unittest.TestCase):
    def test_cli_json(self):
        py = socialshares.fetch(url)
        cli_raw = subprocess.check_output('socialshares {url}'.format(url=url), shell=True)
        cli = json.loads(cli_raw.decode('utf-8'))

        for k, v in py.items():
            self.assertIn(k, cli)
            self.assertIsInstance(v, int)
            self.assertTrue(is_close(py[k], cli[k]))

    def test_cli_plain(self):
        py = socialshares.fetch(url, ['twitter'])
        cli_raw = subprocess.check_output('socialshares {url} twitter --plain'.format(url=url), shell=True)
        cli = int(cli_raw)
        self.assertEqual(py['twitter'], cli)


# some platforms are banned or otherwise don't work reliably in our CI environment
SKIP_PLATFORMS = os.environ.get('SKIP_PLATFORMS', '').split(' ')
for platform in filter(None, SKIP_PLATFORMS):
    delattr(PythonTestCase, 'test_' + platform)

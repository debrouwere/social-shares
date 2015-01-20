import socialshares
import unittest
import subprocess
import json


url = 'http://www.theguardian.com/politics/2014/sep/08/pound-slumps-scottish-yes-campaign-poll-lead'


# share counts can differ on repeated fetches, but not by much
def is_close(a, b):
    return 0 <= abs(b - a) <= 5


class PythonTestCase(unittest.TestCase):
    def test_facebook(self):
        counts = socialshares.fetch(url, ['facebook'])
        self.assertIn('facebook', counts)
        self.assertIsInstance(counts['facebook'], int)

    def test_facebookfql(self):
        counts = socialshares.fetch(url, ['facebookfql'])
        self.assertIn('facebookfql', counts)
        self.assertIsInstance(counts['facebookfql'], dict)

    def test_google(self):
        counts = socialshares.fetch(url, ['google'])
        self.assertIn('google', counts)
        self.assertIsInstance(counts['google'], int)

    def test_linkedin(self):
        counts = socialshares.fetch(url, ['linkedin'])
        self.assertIn('linkedin', counts)
        self.assertIsInstance(counts['linkedin'], int)

    def test_pinterest(self):
        counts = socialshares.fetch(url, ['pinterest'])
        self.assertIn('pinterest', counts)
        self.assertIsInstance(counts['pinterest'], int)

    def test_reddit(self):
        counts = socialshares.fetch(url, ['reddit'])
        self.assertIn('reddit', counts)
        self.assertIsInstance(counts['reddit'], dict)

    def test_twitter(self):
        counts = socialshares.fetch(url, ['twitter'])
        self.assertIn('twitter', counts)
        self.assertIsInstance(counts['twitter'], int)

    def test_default(self):
        counts = socialshares.fetch(url)
        self.assertEquals(set(counts.keys()), set(['facebook', 'twitter']))

    def test_all(self):
        all_counts = socialshares.fetch(url, socialshares.platforms.supported)
        
    # requires stubs / spies
    def test_retry(self):
        pass

    def test_strict(self):
        pass


class CLITestCase(object):
    def test_cli_json(self):
        py = socialshares.fetch(url)
        cli_raw = subprocess.check_output('socialshares {url}'.format(url), shell=True)
        cli = json.loads(cli_raw)

        for k, v in py.items():
            self.assertIn(k, cli)
            self.assertIsInstance(v, int)
            self.assertTrue(is_close(py[k], cli[k]))

    def test_cli_plain(self):
        py = socialshares.fetch(url, ['twitter'])
        cli_raw = subprocess.check_output('socialshares {url} twitter --plain'.format(url), shell=True)
        cli = int(cli_raw)
        self.assertEquals(py['twitter'], cli)

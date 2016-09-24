import unittest
import httpretty
from types import SimpleNamespace

from . import find_target_ref


class TestFindTargetRef(unittest.TestCase):

    @httpretty.activate
    def test_get_target_ref(self):
        with open('pullrequest-6.json') as f:
            response = f.read()

        rest_url = 'https://api.bitbucket.org/2.0/repositories/the_org/the_project/pullrequests/6'
        pr_url = 'https://bitbucket.org/the_org/the_project/pull-requests/6'
        httpretty.register_uri(httpretty.GET, rest_url, body=response)

        args = SimpleNamespace(auth_user='user', auth_password='password', pr_url=pr_url)
        actual = find_target_ref.get_target_ref(args)
        self.assertEqual('the_target_hash', actual)

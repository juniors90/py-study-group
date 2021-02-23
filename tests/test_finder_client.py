"""

PROJECT: "Imagine a Github Profile Finder"

AUTHOR: juniors

CREATED AT: 22/02/2021

"""

from . import BaseTestClass

class FinderClientTestCase(BaseTestClass):

    def test_index_with_no_finder(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'GitHub Profile Not Fin', res.data)

    def test_redirect_to_error(self):
        res = self.client.get('/error')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Error', res.data)

    def test_undefined_endpoint(self):
        res = self.client.get('/undefined')
        self.assertEqual(404, res.status_code)
        self.assertIn(b'Error', res.data)

    def test_access_to_finder(self):
        user_data = self.finder_user(dict(username='juniors90',))
        res = self.client.get('/')
        self.assertEqual(200, user_data.status_code)
        self.assertIn(b'juniors90', user_data.data)
        self.assertIn(b'Public: 16', user_data.data)
        self.assertIn(b'Followers: 3', user_data.data)

    def test_access_to_undefinde_finder(self):
        first_user_indefined = self.finder_user(dict(username='----jkgfjkasgjfs',))
        sec_user_indefined = self.finder_user(dict(username='--jgadjkgdsfjgfsj--',))
        third_user_indefined = self.finder_user(dict(username='jkgfjkasgjfs----',))
        self.assertEqual(200, first_user_indefined.status_code)
        self.assertIn(b'Error', first_user_indefined.data)
        self.assertEqual(200, sec_user_indefined.status_code)
        self.assertIn(b'Error', sec_user_indefined.data)
        self.assertEqual(200, third_user_indefined.status_code)
        self.assertIn(b'Error', third_user_indefined.data)

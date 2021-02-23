"""

PROJECT: "Imagine a Github Profile Finder"

AUTHOR: juniors

CREATED AT: 22/02/2021

"""

import unittest

from main import app

class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        app.config['WTF_CSRF_ENABLED'] = False

    def finder_user(self, username):
        return self.client.post('/', data=dict(username, ), follow_redirects=True)
    

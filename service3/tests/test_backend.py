from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_phrase(self):
        response = self.client.get(url_for('phrase'))
        self.assertEqual(response.status_code, 200)
        with self.client:
            response = self.client.get(url_for('phrase'))
            self.assertEqual(response.status_code, 200)
        with self.client:
            response = self.client.get(url_for('phrase'))
            self.assertEqual(response.status_code, 200)
        with self.client:
            response = self.client.get(url_for('phrase'))
            self.assertEqual(response.status_code, 200)

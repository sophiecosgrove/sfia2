import unittest
from unittest.mock import Mock
from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class FakeResponse(object):
    text = 'In the next few weeks you will recieve some good news'


class TestRoutes(TestBase):
    def test_sentence(self):
        with patch('requests.get') as mock_request:
            fake_response = FakeResponse()
            mock_request.return_value = fake_response
            response = self.client.get(url_for('sentence'))
            self.assertIn(b'In the next few weeks you will recieve some good news', response.data)
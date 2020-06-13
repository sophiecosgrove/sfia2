import unittest
from unittest.mock import Mock
from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Fortunes
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        fortune = Fortunes(fortune = 'Next month you will recieve some good news')


        db.session.add(fortune)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestModels(TestBase):
    def test_repr(self):
        fortune = Fortunes(fortune = 'Next month you will recieve some good news')
        print(repr(fortune))

class FakeResponse(object):
    status_code = 200
    text = 'In the next few weeks you will recieve some good news'

class TestRoutes(TestBase):
    def test_home(self):
        with patch('requests.get') as mock_request:
            fake_response = FakeResponse()
            mock_request.return_value = fake_response
            response = self.client.get(url_for('home'))
            self.assertIn(b'In the next few weeks you will recieve some good news', response.data)
    
    def test_fortunes(self):
        response = self.client.get(url_for('fortunes'))
        self.assertIn(b'Next month you will recieve some good news', response.data)

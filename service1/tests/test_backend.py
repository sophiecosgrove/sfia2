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
            SECRET_KEY=getenv('TEST_SECRET_KEY'),
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

class TestRoutes(TestBase):
    def test_home(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            assert get_mock() == 200
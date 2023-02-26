# This file is for setting up the tests

import pytest
from tutor_service import create_app

@pytest.fixture()
def app():
    app = create_app()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
# This file is for setting up the tests

import pytest
from tutor_service import app


@pytest.fixture()
def client():
    return app.test_client()

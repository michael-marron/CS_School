# This file is for setting up the tests

import pytest
from project import create_app, db

@pytest.fixture()
def app():
  app = create_app("sqlite://") # create an app with a temporary sqlite db
  with app.app_context():
    # create the tables in the DB
    db.create_all()
  
  # code after this line will be ran once tests are finished
  yield app
  
@pytest.fixture()
def client(app):
  # is used to simulate requests to the client
  return app.test_client()

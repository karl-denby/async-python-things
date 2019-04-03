import pytest
from bocadillo import provider
from bocadillo.testing import create_client

from app import app

@provider
def diego():
    class EchoDiego:
        def get_response(self, query):
            return query

    return EchoDiego()

@pytest.fixture
def client():
    return create_client(app)

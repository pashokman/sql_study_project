import pytest

from .modules.database import Database


@pytest.fixture
def database():
    db = Database()
    yield db
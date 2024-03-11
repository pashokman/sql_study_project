import pytest

from .modules.movies_base import Movies

from .modules.students_base import Students

from .modules.marvels_base import Marvels

from .modules.database import Database


@pytest.fixture
def marverls():
    db = Marvels()
    yield db


@pytest.fixture
def students():
    db = Students()
    yield db


@pytest.fixture
def movies():
    db = Movies()
    yield db
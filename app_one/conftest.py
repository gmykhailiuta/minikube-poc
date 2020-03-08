import pytest


@pytest.fixture
def app():
    from app_one import app_one
    yield app_one

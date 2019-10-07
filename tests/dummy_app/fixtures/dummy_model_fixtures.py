import pytest
from pytest_factoryboy import register

from tests.dummy_app.factories.dummy_model_factories import DummyModelFactory

register(DummyModelFactory)

@pytest.fixture(name='dummy_model_build')
def fixture_dummy_model_build():
    return DummyModelFactory.build()

@pytest.fixture(name='dummy_model_created')
def fixture_dummy_model_create(db):
    return DummyModelFactory.create()


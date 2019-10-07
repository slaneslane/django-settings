import factory

from tests.dummy_app.models import DummyModel
from tests.base_factories import BaseFactory

class DummyModelFactory(BaseFactory):
    class Meta:
        model = DummyModel

    name = factory.Sequence(lambda n: 'name{0}'.format(n))


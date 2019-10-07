import pytest

from .dummy_app.models import DummyModel 

def first_test(db):
    DummyModel.objects.create(name='DummyM')
    obj = DummyModel.objects.first()
    assert obj.name == 'DummyM'

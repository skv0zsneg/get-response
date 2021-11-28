import pytest

from src.get_response import get_response
from src.get_response.core.exceptions import WrongApiType


def test_get_wrong_api_type_str():
    with pytest.raises(WrongApiType):
        get_response('', 'GyGy', {'name': ['name']})


def test_get_wrong_api_type_int():
    with pytest.raises(WrongApiType):
        get_response('', 123, {'name': ['name']})


def test_get_wrong_api_type_float():
    with pytest.raises(WrongApiType):
        get_response('', 12.3, {'name': ['name']})


def test_get_wrong_api_type_bool():
    with pytest.raises(WrongApiType):
        get_response('', False, {'name': ['name']})
        get_response('', True, {'name': ['name']})


def test_get_wrong_api_type_some_class():
    with pytest.raises(WrongApiType):
        get_response('', Exception, {'name': ['name']})


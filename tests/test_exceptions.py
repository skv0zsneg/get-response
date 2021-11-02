import unittest

from src.get_response import get_response
from src.get_response.core.exceptions import WrongApiType


class TestsForExceptions(unittest.TestCase):
    def test_get_wrong_api_type_str(self):
        self.assertRaises(WrongApiType, get_response, '', 'GyGy', {'name': ['name']})

    def test_get_wrong_api_type_int(self):
        self.assertRaises(WrongApiType, get_response, '', 123, {'name': ['name']})

    def test_get_wrong_api_type_float(self):
        self.assertRaises(WrongApiType, get_response, '', 12.3, {'name': ['name']})

    def test_get_wrong_api_type_bool(self):
        self.assertRaises(WrongApiType, get_response, '', False, {'name': ['name']})
        self.assertRaises(WrongApiType, get_response, '', True, {'name': ['name']})

    def test_get_wrong_api_type_some_class(self):
        self.assertRaises(WrongApiType, get_response, '', Exception, {'name': ['name']})

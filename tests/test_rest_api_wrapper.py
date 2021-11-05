import unittest

from src.get_response import get_response
from samples_for_test import SIMPLE_REST_RESPONSE


class TestRestWrapper(unittest.TestCase):
    def test_get_rest_response_as_text_find_all_str_values(self):
        _obj = SIMPLE_REST_RESPONSE
        _api_type = 'REST'
        _to_find = {'found_name': ['name']}

        gr = get_response(_obj, _api_type, _to_find)
        self.assertEqual(gr.found_name, 'Mike')

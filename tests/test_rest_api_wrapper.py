import unittest

from src.get_response import get_response
from samples_for_test import SIMPLE_REST_RESPONSE


class TestRestWrapper(unittest.TestCase):
    def setUp(self):
        self.api_type = 'REST'

    def test_get_rest_response_as_text_find_all_str_values(self):
        obj = SIMPLE_REST_RESPONSE
        to_find = {'found_name': ['name']}

        gr = get_response(obj, self.api_type, to_find)
        gr.parse_rest_response()
        # self.assertEqual(gr.found_name, 'Mike')
        self.assertEqual(gr['found_name'], 'Mike')

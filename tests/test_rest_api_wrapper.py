import unittest

from src.get_response import get_response
from samples_for_test import SIMPLE_REST_RESPONSE, ALL_TYPE_REST_RESPONSE


API_TYPE = 'REST'


class TestRestWrapperSimpleResponse(unittest.TestCase):
    def setUp(self):
        self.simple_rest_response_nt = SIMPLE_REST_RESPONSE
        self.obj = SIMPLE_REST_RESPONSE.rest_body

    def test_get_rest_response_as_text_find_all_str_values(self):
        to_find = {'found_name': ['name']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertEqual(gr['found_name'], self.simple_rest_response_nt.name)

    def test_get_rest_response_as_int_find_all_int_values(self):
        to_find = {'found_age': ['age']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertEqual(gr['found_age'], self.simple_rest_response_nt.age)

    def test_get_rest_response_as_list_find_all_list_values(self):
        to_find = {'found_books': ['books']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertEqual(gr['found_books'], self.simple_rest_response_nt.books)

    def test_get_rest_response_as_dict_find_all_dict_values(self):
        to_find = {'found_family': ['family']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertEqual(gr['found_family'], self.simple_rest_response_nt.family)


class TestRestWrapperAllTypes(unittest.TestCase):
    def setUp(self):
        self.all_type_rest_response_nt = ALL_TYPE_REST_RESPONSE
        self.obj = ALL_TYPE_REST_RESPONSE.rest_body

    def test_get_dict_py_from_objects_js(self):
        to_find = {'found_dict': ['js_object']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsInstance(gr['found_dict'], dict)
        self.assertEqual(gr['found_dict'], self.all_type_rest_response_nt.pi_dict)

    def test_get_list_py_from_array_js(self):
        to_find = {'found_list': ['js_array']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsInstance(gr['found_list'], list)
        self.assertEqual(gr['found_list'], self.all_type_rest_response_nt.pi_list)

    def test_get_str_py_from_string_js(self):
        to_find = {'found_str': ['js_string']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsInstance(gr['found_str'], str)
        self.assertEqual(gr['found_str'], self.all_type_rest_response_nt.pi_str)

    def test_get_int_py_from_int_js(self):
        to_find = {'found_int': ['js_int']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsInstance(gr['found_int'], int)
        self.assertEqual(gr['found_int'], self.all_type_rest_response_nt.pi_int)

    def test_get_float_py_from_real_js(self):
        to_find = {'found_float': ['js_real']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsInstance(gr['found_float'], float)
        self.assertEqual(gr['found_float'], self.all_type_rest_response_nt.pi_float)

    def test_get_True_py_from_true_js(self):
        to_find = {'found_True': ['js_true']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsInstance(gr['found_True'], bool)
        self.assertEqual(gr['found_True'], self.all_type_rest_response_nt.pi_True)

    def test_get_False_py_from_false_js(self):
        to_find = {'found_False': ['js_false']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsInstance(gr['found_False'], bool)
        self.assertEqual(gr['found_False'], self.all_type_rest_response_nt.pi_False)

    def test_get_None_py_from_null_js(self):
        to_find = {'found_None': ['js_null']}
        gr = get_response(self.obj, API_TYPE, to_find)

        self.assertIsNone(gr['found_None'], None)
        self.assertEqual(gr['found_None'], self.all_type_rest_response_nt.pi_None)

import pytest

from src.get_response import get_response
from tests.utils.samples_for_test import SIMPLE_REST_RESPONSE, ALL_TYPE_REST_RESPONSE

API_TYPE = 'REST'


# -- setUp --
@pytest.fixture()
def simple_rest_response_nt():
    simple_rest_response_nt = SIMPLE_REST_RESPONSE
    return simple_rest_response_nt


@pytest.fixture()
def simple_rest_obj():
    obj = SIMPLE_REST_RESPONSE.rest_body
    return obj


@pytest.fixture()
def all_type_rest_response_nt():
    simple_rest_response_nt = ALL_TYPE_REST_RESPONSE
    return simple_rest_response_nt


@pytest.fixture()
def all_type_rest_obj():
    obj = ALL_TYPE_REST_RESPONSE.rest_body
    return obj


# -- tests --
def test_get_rest_response_as_text_find_all_str_values(simple_rest_response_nt, simple_rest_obj):
    to_find = {'found_name': ['name']}
    gr = get_response(simple_rest_obj, API_TYPE, to_find)

    assert gr['found_name'] == simple_rest_response_nt.name


def test_get_rest_response_as_int_find_all_int_values(simple_rest_response_nt, simple_rest_obj):
    to_find = {'found_age': ['age']}
    gr = get_response(simple_rest_obj, API_TYPE, to_find)

    assert gr['found_age'] == simple_rest_response_nt.age


def test_get_rest_response_as_list_find_all_list_values(simple_rest_response_nt, simple_rest_obj):
    to_find = {'found_books': ['books']}
    gr = get_response(simple_rest_obj, API_TYPE, to_find)

    assert gr['found_books'] == simple_rest_response_nt.books


def test_get_rest_response_as_dict_find_all_dict_values(simple_rest_response_nt, simple_rest_obj):
    to_find = {'found_family': ['family']}
    gr = get_response(simple_rest_obj, API_TYPE, to_find)

    assert gr['found_family'] == simple_rest_response_nt.family


def test_get_dict_py_from_objects_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_dict': ['js_object']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert isinstance(gr['found_dict'], dict)
    assert gr['found_dict'] == all_type_rest_response_nt.pi_dict


def test_get_list_py_from_array_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_list': ['js_array']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert isinstance(gr['found_list'], list)
    assert gr['found_list'] == all_type_rest_response_nt.pi_list


def test_get_str_py_from_string_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_str': ['js_string']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert isinstance(gr['found_str'], str)
    assert gr['found_str'] == all_type_rest_response_nt.pi_str


def test_get_int_py_from_int_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_int': ['js_int']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert isinstance(gr['found_int'], int)
    assert gr['found_int'] == all_type_rest_response_nt.pi_int


def test_get_float_py_from_real_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_float': ['js_real']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert isinstance(gr['found_float'], float)
    assert gr['found_float'] == all_type_rest_response_nt.pi_float


def test_get_True_py_from_true_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_True': ['js_true']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert isinstance(gr['found_True'], bool)
    assert gr['found_True'] == all_type_rest_response_nt.pi_True


def test_get_False_py_from_false_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_False': ['js_false']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert isinstance(gr['found_False'], bool)
    assert gr['found_False'] == all_type_rest_response_nt.pi_False


def test_get_None_py_from_null_js(all_type_rest_response_nt, all_type_rest_obj):
    to_find = {'found_None': ['js_null']}
    gr = get_response(all_type_rest_obj, API_TYPE, to_find)

    assert gr['found_None'] is None
    assert gr['found_None'] == all_type_rest_response_nt.pi_None

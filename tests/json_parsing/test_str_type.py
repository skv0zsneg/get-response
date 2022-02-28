import pytest

from get_response import GetResponse


# set up
TESTING_MIME_TYPE = 'application/json'
TESTING_OBJ = """
{"menu": {
    "id": 101010101010101,
    "value": "File",
    "popup": {
        "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
        ]
    }
}}"""


class TestJsonParsing:
    def test_parsing_number_value(self):
        to_find_dict = {'my_id': ['menu', 'id']}
        gr = GetResponse(obj=TESTING_OBJ, to_find=to_find_dict,
                         mime_type=TESTING_MIME_TYPE)

        assert gr['my_id'] == '101010101010101'

    def test_parsing_string_value(self):
        to_find_dict = {'my_value': ['menu', 'value']}
        gr = GetResponse(obj=TESTING_OBJ, to_find=to_find_dict,
                         mime_type=TESTING_MIME_TYPE)

        assert gr['my_value'] == 'File'



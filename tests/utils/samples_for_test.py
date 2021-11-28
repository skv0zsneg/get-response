from collections import namedtuple


SimpleRestResponse = namedtuple('SimpleRestResponse',
                                ['name', 'age', 'books', 'family', 'rest_body'])
SIMPLE_REST_RESPONSE = SimpleRestResponse(
    name='Mike',
    age=19,
    books=["Fluent Python", "C++ for Dummies"],
    family={
        "mother": "Jane",
        "father": "Sam",
        "Sister": None,
        "cat": "ツ"
    },
    rest_body="""
    {
        "name": "Mike",
        "age": 19,
        "books": ["Fluent Python", "C++ for Dummies"],
        "family": {
            "mother": "Jane",
            "father": "Sam",
            "Sister": null, 
            "cat": "ツ"
        }
    }
    """
)

AllTypeRestResponse = namedtuple('AllTypeRestResponse',
                                 ['pi_dict', 'pi_list', 'pi_str', 'pi_int',
                                  'pi_float', 'pi_True', 'pi_False', 'pi_None',
                                  'rest_body'])
ALL_TYPE_REST_RESPONSE = AllTypeRestResponse(
    pi_dict={},
    pi_list=[],
    pi_str='str',
    pi_int=1010,
    pi_float=10.101,
    pi_True=True,
    pi_False=False,
    pi_None=None,
    rest_body="""
    {
        "js_object": {},
        "js_array": [],
        "js_string": "str",
        "js_int": 1010,
        "js_real": 10.101,
        "js_true": true,
        "js_false": false,
        "js_null": null
    }
    """
)

ListOfJsonsRestResponse = namedtuple('ListOfJsonsRestResponse',
                                     ['rest_body', 'all_js_object', 'all_js_array',
                                      'all_js_string', 'all_js_int', 'all_js_real',
                                      'js_true', 'js_false', 'js_null'])
LIST_OF_JSONS_REST_RESPONSE = ListOfJsonsRestResponse(
    all_js_object=({"obj": "obj"}, {"obj1": "obj1"}, {"obj2": "obj2"}),
    all_js_array=(["arr", "rar"], ["arr", "rar", "rra"], ["arr", "rar", "rra", "rrr"],),
    all_js_string=("str", "str1", "str100"),
    all_js_int=(1010, 1019, 9999),
    all_js_real=(10.101, 10.100001, 10.199901),
    js_true=True,
    js_false=False,
    js_null=None,
    rest_body="""
    {
        "link": "https://some_link_to_some_were.com/lists",
        "_embedded": {
            "lists_of_json": [
                "js_list": {
                    "js_object": {"obj": "obj"},
                    "js_array": ["arr", "rar"],
                    "js_string": "str",
                    "js_int": 1010,
                    "js_real": 10.101,
                    "js_true": true,
                    "js_false": false,
                    "js_null": null
                },
                "js_list": {
                    "js_object": {"obj1": "obj1"},
                    "js_array": ["arr", "rar", "rra"],
                    "js_string": "str1",
                    "js_int": 1019,
                    "js_real": 10.100001,
                    "js_true": true,
                    "js_false": false,
                    "js_null": null
                },
                "js_list": {
                    "js_object": {"obj2": "obj2"},
                    "js_array": ["arr", "rar", "rra", "rrr"],
                    "js_string": "str100",
                    "js_int": 9999,
                    "js_real": 10.199901,
                    "js_true": true,
                    "js_false": false,
                    "js_null": null
                },
            ]
        }
    }
    """
)

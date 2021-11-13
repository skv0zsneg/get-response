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

import pytest

from get_response import get_json


class TestGetJsonParsed:

    @pytest.fixture
    def json_message():
        message = """
        {
            "page": 20,
            "time": "2022-05-15T15:43:00Z",
            "persons": [
                {
                    "id": "abfa0c8a986bcabca9ba6c96a9",
                    "name": "Alex",
                    "surname": "Bernard",
                    "n_childrens": 15165136521356416541651,
                    "married": false,
                    "books": ["The Great Gatsby", "Another Book"]
                },
                {
                    "id": "abfa0c8a986bcabca9ba890bbc",
                    "name": "Vikki",
                    "surname": "Sweet",
                    "n_childrens": 0,
                    "married": true,
                    "books": null
                },
                {
                    "id": "abfa0c8a986bcabca9ba890123",
                    "name": "Lily",
                    "surname": "Sunshine",
                    "n_childrens": 2,
                    "married": true,
                    "books": []
                },
            ]
        }
        """
        return message

    def test_get_only_str_values(json_message):
        result = get_json(
            obj=json_message,
            to_find={
                'all_ids': ['persons', 'id'],
                'all_names': ['persons', 'names'],
                'all_surnames': ['persons', 'surname'],
                'message_time': ['time']
            })
        
        result_all_ids = result.get('all_ids')
        result_all_names = result.get('all_names')
        result_all_surnames = result.get('all_surnames')
        result_message_time = result.get('message_time')


        assert len(result_all_ids) == 3
        assert 'abfa0c8a986bcabca9ba6c96a9' in result_all_ids
        assert 'abfa0c8a986bcabca9ba890bbc' in result_all_ids
        assert 'abfa0c8a986bcabca9ba890123' in result_all_ids

        assert len(result_all_names) == 3
        assert 'Alex' in result_all_names
        assert 'Vikki' in result_all_names
        assert 'Lily' in result_all_names

        assert len(result_all_surnames) == 3
        assert 'Bernard' in result_all_surnames
        assert 'Sweet' in result_all_surnames
        assert 'Sunshine' in result_all_surnames

        assert '2022-05-15T15:43:00Z' == result_message_time
    
    def test_get_only_str_values_using_magic_method__getitem__(json_message):
        result = get_json(
            obj=json_message,
            to_find={
                'all_ids': ['persons', 'id'],
                'all_names': ['persons', 'names'],
                'all_surnames': ['persons', 'surname'],
                'message_time': ['time']
            })
        
        result_all_ids = result['all_ids']
        result_all_names = result['all_names']
        result_all_surnames = result['all_surnames']
        result_message_time = result['message_time']


        assert len(result_all_ids) == 3
        assert 'abfa0c8a986bcabca9ba6c96a9' in result_all_ids
        assert 'abfa0c8a986bcabca9ba890bbc' in result_all_ids
        assert 'abfa0c8a986bcabca9ba890123' in result_all_ids

        assert len(result_all_names) == 3
        assert 'Alex' in result_all_names
        assert 'Vikki' in result_all_names
        assert 'Lily' in result_all_names

        assert len(result_all_surnames) == 3
        assert 'Bernard' in result_all_surnames
        assert 'Sweet' in result_all_surnames
        assert 'Sunshine' in result_all_surnames

        assert '2022-05-15T15:43:00Z' == result_message_time
    
    def test_get_only_int_values(json_message):
        result = get_json(
            obj=json_message,
            to_find={
                'page': ['page'],
                'all_childrens': ['persons', 'n_childrens']
            })

        result_page = result.get('page')
        result_all_childrens = result.get('all_childrens')

        assert result_page == 20
        
        assert len(result_all_childrens) == 3
        assert 15165136521356416541651 in result_all_childrens
        assert 0 in result_all_childrens
        assert 2 in result_all_childrens

    
    def test_get_only_str_values_using_magic_method__getitem__(json_message):
        result = get_json(
            obj=json_message,
            to_find={
                'page': ['page'],
                'all_childrens': ['persons', 'n_childrens']
            })

        result_page = result['page']
        result_all_childrens = result['all_childrens']

        assert result_page == 20
        
        assert len(result_all_childrens) == 3
        assert 15165136521356416541651 in result_all_childrens
        assert 0 in result_all_childrens
        assert 2 in result_all_childrens


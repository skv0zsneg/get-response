import pytest

from get_response import get_response


class TestGetJsonParsed:

    @pytest.fixture()
    def json_message(self):
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
                }
            ]
        }
        """
        return message

    def test_get_all_id_values(self, json_message):
        parsed_json = get_response(
            obj=json_message, 
            message_type='json')

        all_ids_result = parsed_json.get_objects('id')
        
        assert len(all_ids_result) == 3
        assert all_ids_result == ['abfa0c8a986bcabca9ba6c96a9', 
                                  'abfa0c8a986bcabca9ba890bbc', 
                                  'abfa0c8a986bcabca9ba890123']

    def test_get_all_name_values(self, json_message):
        parsed_json = get_response(
            obj=json_message, 
            message_type='json')

        all_ids_result = parsed_json.get_objects('name')
        
        assert len(all_ids_result) == 3
        assert all_ids_result == ['Alex', 'Vikki', 'Lily']
        

import pytest

from get_response import get_response


class TestGetJsonParsed:

    @pytest.fixture()
    def parse_result(self):
        message = """
        {
            "page":20,
            "time":"2022-05-15T15:43:00Z",
            "persons":[
                {
                    "id":"abfa0c8a986bcabca9ba6c96a9",
                    "name":"Alex",
                    "surname":"Bernard",
                    "n_childrens":15165136521356416541651,
                    "married":false,
                    "books":[
                        "The Great Gatsby",
                        "Another Book"
                    ]
                },
                {
                    "id":"abfa0c8a986bcabca9ba890bbc",
                    "name":"Vikki",
                    "surname":"Sweet",
                    "n_childrens":0,
                    "married":true,
                    "books":null
                },
                {
                    "id":"abfa0c8a986bcabca9ba890123",
                    "name":"Lily",
                    "surname":"Sunshine",
                    "n_childrens":2,
                    "married":true,
                    "books":[]
                }
            ],
            "deep_list":[
                [
                    [],
                    [],
                    [
                        [],
                        [{"hide_value": "IAmVerySecret"}]
                    ]
                ],
                [],
                []
            ]
        }
        """
        parsed_json = get_response(
            obj=message, 
            message_type='json')

        yield parsed_json

    def test_get_all_id_values(self, parse_result):
        all_ids_result = parse_result.get_objects('id')
        
        assert len(all_ids_result) == 3
        assert all_ids_result == ('abfa0c8a986bcabca9ba6c96a9', 
                                  'abfa0c8a986bcabca9ba890bbc', 
                                  'abfa0c8a986bcabca9ba890123')

    def test_get_all_name_values(self, parse_result):
        all_ids_result = parse_result.get_objects('name')
        
        assert len(all_ids_result) == 3
        assert all_ids_result == ('Alex', 'Vikki', 'Lily')
    
    def test_get_all_surname_values(self, parse_result):
        all_surname_result = parse_result.get_objects('surname')
        
        assert len(all_surname_result) == 3
        assert all_surname_result == ('Bernard', 'Sweet', 'Sunshine')
    
    def test_get_all_n_childrens_values(self, parse_result):
        all_n_childrens_result = parse_result.get_objects('n_childrens')
        
        assert len(all_n_childrens_result) == 3
        assert all_n_childrens_result == (15165136521356416541651, 0, 2)
    
    def test_get_all_married_values(self, parse_result):
        all_married_result = parse_result.get_objects('married')
        
        assert len(all_married_result) == 3
        assert all_married_result == (False, True, True)

    def test_get_all_books_values(self, parse_result):
        all_books_result = parse_result.get_objects('books')
        
        assert len(all_books_result) == 3
        assert all_books_result == (["The Great Gatsby", "Another Book"],
                                    None, 
                                    [])
    
    def test_get_page_value(self, parse_result):
        page_result = parse_result.get_objects('page')

        assert page_result == (20,)

    def test_get_time_value(self, parse_result):
        time_result = parse_result.get_objects('time')

        assert time_result == ('2022-05-15T15:43:00Z',)
    
    def test_get_hide_value_value(self, parse_result):
        hide_result = parse_result.get_objects('hide_value')

        assert hide_result == ("IAmVerySecret",)

    def test_get_value_using_nonexistent_field(self, parse_result):
        parsing_result = parse_result.get_objects('nonexistent')

        assert parsing_result == ()

    def test_get_value_using_empty_field(self, parse_result):
        with pytest.raises(TypeError):
            parse_result.get_objects()


class TestGetXmlParsed:

    @pytest.fixture()
    def parse_result(self):
        message = """
            <soap:Envelope xmlns:soap="http://">
            <soap:Header>
                <ResponseHeader xmlns="https://">
                    <requestId>xxxxxxxxxxxxxxxxxxxx</requestId>
                    <responseTime>1063</responseTime>
                </ResponseHeader>
            </soap:Header>
            <soap:Body>
                <getAdUnitsByStatementResponse xmlns="https://">
                    <persons>
                        <person>
                            <id>abfa0c8a986bcabca9ba6c96a9</id>
                            <name>Alex</name>
                            <surname>Bernard</surname>
                            <nChildrens>15165136521356416541651</nChildrens>
                            <married>False</married>
                            <books>
                                <bookName>The Great Gatsby</bookName>
                                <bookName>Another Book</bookName>
                            </books>
                        </person>
                        <person>
                            <id>abfa0c8a986bcabca9ba890bbc</id>
                            <name>Vikki</name>
                            <surname>Sweet</surname>
                            <nChildrens>0</nChildrens>
                            <married>True</married>
                            <books></books>
                        </person>
                        <person>
                            <id>abfa0c8a986bcabca9ba890123</id>
                            <name>Lily</name>
                            <surname>Sunshine</surname>
                            <nChildrens>2</nChildrens>
                            <married>True</married>
                            <books>
                                <bookName></bookName>
                            </books>
                        </person>
                    </persons>
                </getAdUnitsByStatementResponse>
            </soap:Body>
            </soap:Envelope>
        """
        parsed_json = get_response(
            obj=message, 
            message_type='xml')

        yield parsed_json
    
    def test_get_all_id_values(self, parse_result):
        all_ids_result = parse_result.get_objects('id')
        
        assert len(all_ids_result) == 3
        assert all_ids_result == ('abfa0c8a986bcabca9ba6c96a9', 
                                  'abfa0c8a986bcabca9ba890bbc', 
                                  'abfa0c8a986bcabca9ba890123')
    


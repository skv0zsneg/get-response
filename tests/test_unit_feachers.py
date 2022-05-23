import pytest

from get_response.soap_parser import SoapParser


class TestSoapParserMethods:

    def test_prepare_object(self):
        test_xml = """
            <tag1>

    <tag2>

                            <tag3>
                                <tag4>VALUE</tag4>
                            </tag3>
    
    </tag2>
            
            </tag1>
        """
        result = SoapParser._prepare_obj(test_xml)

        assert result == "<tag1><tag2><tag3><tag4>VALUE</tag4></tag3></tag2></tag1>"
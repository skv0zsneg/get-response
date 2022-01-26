from requests import Response
from typing import Union, Type, Optional, Dict, List

from get_response.core.enums import ResponseType
from get_response.core.exceptions import WrongResponseType
from get_response.parsing_wrapper import ParsingWrapper
from get_response.parsing_xml import ParsingXml
from get_response.parsing_json import ParsingJson


__all__ = ['get_response', 'ResponseType']


def get_response(obj: Union[Response, bytes, str],
                 *,
                 to_find: Dict[str, List[str]],
                 response_type: ResponseType = None) -> ParsingWrapper:
    """Main function to run parsing the response object.
    
    :param obj: The object that need to be parsed.
    :param to_find: Special dict for parsing something specific.
    :param response_type: Explicit indication of response type.
    
    Example.
    >>> json_response = '{"pi_number": 3.14, "pi_mantissa": 14}'
    >>> find_matnissa = {'parsed_pi_mantissa': ['pi_mantissa']}
    >>> res = get_response(json_response, to_find=find_matnissa)
    >>> res['parsed_pi_mantissa']
    '14'
    """
    cur_parser: Optional[Type]

    if isinstance(obj, Response):
        obj = obj.text
    elif isinstance(obj, bytes):
        obj = obj.decode('utf-8')

    if response_type is not None:
        parse_map = {
            ResponseType.JSON: ParsingJson,
            ResponseType.XML: ParsingXml
        }
        cur_parser = parse_map[response_type]
    else:
        cur_parser = get_parser(obj)
        if cur_parser is None:
            raise WrongResponseType(WrongResponseType.MESSAGE)

    parsed_object = cur_parser(obj, to_find)
    parsed_object.parse()

    return parsed_object


def get_parser(obj: str) -> Optional[Type]:
    if obj.startswith(ResponseType.JSON.salt[0]) and obj.endswith(ResponseType.JSON.salt[1]):
        return ParsingJson
    if obj.startswith(ResponseType.XML.salt[0]) and obj.endswith(ResponseType.XML.salt[1]):
        return ParsingXml
    return None

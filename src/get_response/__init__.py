from requests import Response
from typing import Union, Optional

from .core.enums import ResponseType
from .core.interface import GetResponseDict
from .parsing_xml import ParsingXml
from .parsing_json import ParsingJson


def get_response(obj: Union[Response, bytes, str],
                 *,
                 to_find: GetResponseDict,
                 response_type: ResponseType = None) -> GetResponseDict:
    if isinstance(obj, Response):
        obj = obj.text
    elif isinstance(obj, bytes):
        obj = obj.decode('utf-8')

    cur_response_type = _get_parsing_method(response_type, obj)


def _get_parsing_method(response_type: Optional[ResponseType], obj: str) -> Union[ParsingXml, ParsingJson]:
    # TODO: закончить выбор парсера
    parsed_method_map = {
        ResponseType.XML: ParsingXml,
        ResponseType.JSON: ParsingJson
    }
    if response_type is not None:
        cur_response_type = parsed_method_map[response_type]
    else:
        for target_response_type in ResponseType:
            # For xml & json
            if obj.startswith(target_response_type.salt[0]) and obj.endswith(target_response_type.salt[1]):
                return parsed_method_map[target_response_type]

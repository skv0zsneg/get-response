from typing import Literal

from get_response.parsers import BaseParser
from get_response.parsers import JsonParser
from get_response.parsers import XmlParser


T_MESSAGE = Literal['json', 'xml']


def get_response(obj: str, message_type: T_MESSAGE) -> BaseParser:
    parser_factory = {
        'json': JsonParser,
        'xml': XmlParser,
    }

    return parser_factory[message_type](obj)


def get_json(obj: str) -> BaseParser:
    return get_response(obj, message_type='json')

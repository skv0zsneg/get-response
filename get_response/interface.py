from typing import Literal

from get_response.parsers import BaseParser
from get_response.parsers import JsonParser


T_MESSAGE = Literal['json']


def get_response(obj: str, message_type: T_MESSAGE) -> BaseParser:
    parser_factory = {
        'json': JsonParser,
    }

    return parser_factory[message_type](obj)

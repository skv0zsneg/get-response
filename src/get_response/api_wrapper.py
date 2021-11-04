from typing import Union
from requests import Response
from collections import namedtuple


class ApiWrapper:
    def __init__(self, obj: Union[Response, str, dict], to_find: dict) -> None:
        ...

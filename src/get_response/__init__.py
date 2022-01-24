from requests import Response
from typing import Union

from .core.enums import ResponseType
from .core.exceptions import WrongApiType


def get_response(obj: Union[Response, str],
                 to_find: dict,
                 response_type: Union[ResponseType, str] = None) -> ...:
    """ """

    return ...


from requests import Response
from typing import Union, Literal

from .api_wrapper import ApiWrapper


API_TYPES = Literal['REST', 'SOAP']


def get_response(obj: Union[Response, str, dict],
                 api_type: API_TYPES,
                 to_find: str) -> ApiWrapper:
    """Get Response using for getting parsed SOAP or REST like answers
    to a dict-view.

    :param obj: Parsed object.
    :param api_type: Type of API that parsed.
    :param to_find: Search dict.
    :return: An Instance of ApiWrapper class.
    """
    return ApiWrapper()

from requests import Response
from typing import Union, Literal, TypeVar

from .core.enums import ApiType
from .core.exceptions import WrongApiType
from .api_wrapper import ApiWrapper
from .rest_wrapper import RestWrapper
from .soap_wrapper import SoapWrapper


T = TypeVar('T')
API_TYPES = Literal[ApiType.REST, ApiType.SOAP]


def get_response(obj: Union[Response, str, dict],
                 api_type: Union[API_TYPES, str],
                 to_find: dict) -> ApiWrapper:
    """Get Response used for getting parsed SOAP or REST like response
    to a python dict-view.

    :param obj: Parsed object.
    :param api_type: Type of API that parsed.
    :param to_find: Search dict.
    :return: An Instance of ApiWrapper class.
    """
    current_wrapper = _get_api_wrapper(api_type)
    return current_wrapper(obj, to_find)


def _get_api_wrapper(target: Union[API_TYPES, str]) -> T:
    _type_map = {
        ApiType.REST: RestWrapper,
        ApiType.SOAP: SoapWrapper
    }
    for key in _type_map:
        if key.api_name == target:
            return _type_map[key]
    try:
        return _type_map[target]
    except KeyError:
        raise WrongApiType(f"The value '{target}' is not the API type.") from None

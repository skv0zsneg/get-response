from requests import Response
from typing import Union, Type

from .core.enums import ApiType
from .core.exceptions import WrongApiType
from .api_wrapper import ApiWrapper
from .rest_wrapper import RestWrapper
from .soap_wrapper import SoapWrapper


_R_TYPE = Type[Union[RestWrapper,
                     SoapWrapper]]


def get_response(obj: Union[Response, str],
                 api_type: Union[ApiType, str],
                 to_find: dict) -> _R_TYPE:
    """Get Response used for getting parsed SOAP or REST like response
    to a python dict-view.

    :param obj: Parsed object.
    :param api_type: Type of API that parsed.
    :param to_find: Search dict.
    :return: An Instance of ApiWrapper class.
    """
    current_wrapper: ApiWrapper
    current_wrapper = _get_api_wrapper_instance(api_type, obj, to_find)
    return current_wrapper


def _get_api_wrapper_instance(target: Union[ApiType, str], *args, **kwargs) -> _R_TYPE:
    _type_map = {
        ApiType.REST: RestWrapper,
        ApiType.SOAP: SoapWrapper
    }
    for key in _type_map:
        if key.api_name == target:
            return _type_map[key](*args, **kwargs)
    try:
        return _type_map[target](*args, **kwargs)
    except KeyError:
        raise WrongApiType(f"The value '{target}' is not the API type.") from None

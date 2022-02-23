from dataclasses import dataclass
from typing import Union, Dict, Any, List, Optional

import requests

from get_response.core import exceptions
from get_response.core import enums
from get_response.core import utils
import get_response.parsing_mime as parsing


@dataclass
class GetResponse(object):
    """Parsing objects to the one interface.

    The main task of the class - parsing object (in depend of it Mime Type) and
    return access to the parsed object in one interface. It is better to use
    this class for HTTP responses (for example instance of request.Response)
    that have headers with `Content-type`. Alson it поддерживает
    There is one condition you must accurately describe - the way to the object
    you need to get. For example if you want to get object `id` from json file:

    {
    "id": "fehhad342effe28991afe2",
    "author": "skvozsneg"
    }

    You need to create instance of class GetResponse and give to it:
        * object that need to be parsed - json above;
        * dictionary describe way to object that you need - {'my_id': ['id']};
        * Mime Type - application/json or MimeType.APPLICATION_JSON.
    Example of using with:
    >>> json_body = {
    ... "id": "fehhad342effe28991afe2",
    ... "author": "skvozsneg"
    ... }
    >>> gr = GetResponse(obj=json_body,
    ...                  get_response={'my_id': ['id']},
    ...                  mime_type=enums.MimeTypeEnum.APPLICATION_JSON)
    >>> gr['my_id']
    'fehhad342effe28991afe2'

    Attributes:
        obj: Object that need to be parsed.
        to_find: Dictionary that describe way to object that you need.
        mime_type: Mime Type of object for parsing.
    """
    obj: Union[requests.Response, str]
    to_find: Dict[str, Union[List, Dict]]
    mime_type: Optional[Union[enums.MimeTypeEnum, str]] = None

    def __post_init__(self):
        """Magic method from dataclasses."""
        self.mime_type = self._detect_mime_type(self.obj, self.mime_type)

    def __getitem__(self, item: str) -> Any:
        """Get parsed object by Python language syntax.

        Magic method from Python that using for giving access to parsed objects.
        The parsing for one target object launch only once than it's storage in
        cache for saving RAM.

        Args:
            item: Name that was specified as a key in `to_find` args of
             GetResponse class.

        Returns:
            Any type that have been parsed.
        """
        if isinstance(self.mime_type, enums.MimeTypeEnum):
            return parsing.MIME_TYPE_MAP[self.mime_type](self.obj,
                                                         self.to_find[item])

    def get_raw(self) -> Union[requests.Response, str]:
        """Getting the raw object."""
        return self.obj

    @staticmethod
    def _detect_mime_type(obj: Union[requests.Response, str],
                          mime_type: Optional[Union[enums.MimeTypeEnum, str]]
                          ) -> enums.MimeTypeEnum:
        """Detecting the Mime Type of giving object.

        Function detected mime type of object. It can be:
            * string;
            * a instance of class Response from request module.

        Args:
            obj: Object which mimetype need to be detected.
            mime_type: Сonjectural mime type.

        Returns:
            Filed of MimeTypeEnum class.

        Raises:
            CannotDetectMimeType: An error occurred if function can't detect the
             Mime type.
        """
        if isinstance(obj, requests.Response):
            return utils.get_mime_type(obj.headers['Content-Type'])

        if isinstance(mime_type, enums.MimeTypeEnum):
            return mime_type

        if isinstance(obj, str):
            return utils.get_mime_type(mime_type)

        raise exceptions.CannotDetectMimeType(mime_type)

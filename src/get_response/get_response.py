from dataclasses import dataclass
from typing import Union, Dict, Any, List, Optional

import requests

from get_response.core import gr_exceptions
from get_response.core import mime_type_enum
import get_response.parsing_mime as parsing


@dataclass
class GetResponse(object):
    """Parsing objects to the one interface.

    The main task of the class - parsing object (in depend of it Mime Type) and
    return access to the parsed object in one interface.
    There is one condition you must accurately describe the way to the object you
    need to get. For example if you want to get object `id` from json file:

    {"id": "fehhad342effe28991afe2",
    "author": "skvozsneg"}

    You need to create instance of class GetResponse and give to it:
        * object that need to be parsed - json above;
        * dictionary that describe way to object that you need - {'my_id': ['id']};
        * Mime Type - application/json or MimeType.APPLICATION_JSON.full_mime_type.

    Attributes:
        obj: Object that need to be parsed.
        to_find: Dictionary that describe way to object that you need.
        mime_type: Mime Type of object for parsing.
    """
    obj: Union[requests.Response, str]
    to_find: Dict[str, Union[List, Dict]]
    mime_type: Optional[Union[mime_type_enum.MimeTypeEnum, str]] = None

    def __post_init__(self):
        """Magic method from dataclasses."""
        self.mime_type = self._detect_mime_type().full_mime_type

    def __getitem__(self, item: str) -> Any:
        """Get parsed object by Python language syntax.

        The parsing for one object launch only once than it's storage in cache for
        saving RAM.
        Example of using:
        >>> gr = GetResponse(obj='{"name": "skvozsneg"}',
        ...                  get_response={'my_name': ['name']},
        ...                  mime_type=mime_type_enum.MimeTypeEnum.APPLICATION_JSON.full_mime_type)
        >>> gr['my_name']
        'skvozneg'

        Args:
            item: Name that was specified as a key in `to_find` args of GetResponse class.

        Returns:
            Any type that have been parsed.

        Raises:
             ...
        """
        if isinstance(self.mime_type, str):
            return parsing.MIME_TYPE_MAP[self.mime_type](
                self.obj, self.to_find[item])

    def get_raw(self) -> Union[requests.Response, str]:
        """Getting the raw object."""
        return self.obj

    def _detect_mime_type(self) -> mime_type_enum.MimeTypeEnum:
        """Detecting the Mime Type of giving object."""
        if isinstance(self.obj, requests.Response):
            return mime_type_enum.MimeTypeEnum.get_mime_type(
                self.obj.headers['Content-Type'])
        if isinstance(self.mime_type, mime_type_enum.MimeTypeEnum):
            return self.mime_type
        if isinstance(self.obj, str):
            return mime_type_enum.MimeTypeEnum.get_mime_type(self.mime_type)
        raise gr_exceptions.CannotDetectMimeType(
            gr_exceptions.CannotDetectMimeType.MESSAGE)

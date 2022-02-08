from dataclasses import dataclass
from typing import Union, Dict, Any, List, Optional
from requests import Response
from get_response.core.mime_type_enum import MimeTypeEnum


@dataclass
class GetResponse:
    obj: Union[Response, str, bytes]
    to_find: Dict[Any, Union[List, Dict]]
    mime_type: Optional[MimeTypeEnum] = None

from dataclasses import dataclass
from typing import Union, Dict, Any, List, Optional
from requests import Response
import get_response.parsing_mime as parsing
from get_response.core.mime_type_enum import MimeTypeEnum
from get_response.core.gr_exceptions import CannotDetectMimeType, UnexpectedMimeType


@dataclass
class GetResponse:
    obj: Union[Response, str]
    to_find: Dict[Any, Union[List, Dict]]
    mime_type: Optional[Union[MimeTypeEnum, str]] = None

    def __post_init__(self):
        self.mime_type = self._detect_mime_type().full_mime_type

    def __getitem__(self, item: Any) -> Any:
        if isinstance(self.mime_type, str):
            return parsing.MIME_TYPE_MAP[self.mime_type](
                self.obj,
                self.to_find[item]
            )

    def get_raw(self) -> Union[Response, str]:
        return self.obj

    def _detect_mime_type(self) -> MimeTypeEnum:
        if isinstance(self.obj, Response):
            return MimeTypeEnum.get_mime_type(self.obj.headers['Content-Type'])
        if isinstance(self.mime_type, MimeTypeEnum):
            return self.mime_type
        if isinstance(self.obj, str):
            return MimeTypeEnum.get_mime_type(self.mime_type)
        raise CannotDetectMimeType(CannotDetectMimeType.MESSAGE)

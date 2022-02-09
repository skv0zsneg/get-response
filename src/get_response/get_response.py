import mimetypes
from dataclasses import dataclass
from typing import Union, Dict, Any, List, Optional
from requests import Response
from get_response.core.mime_type_enum import MimeTypeEnum
import get_response.parsing_mime as parsing


@dataclass
class GetResponse:
    obj: Union[Response, str, bytes]
    to_find: Dict[Any, Union[List, Dict]]
    mime_type: Optional[MimeTypeEnum] = None

    def get_raw(self) -> Union[Response, str, bytes]:
        return self.obj

    @classmethod
    def _detect_mime_type(cls, obj: Union[Response, str, bytes]) -> MimeTypeEnum:
        if isinstance(obj, Response):
            return MimeTypeEnum.get_mime_type(obj.headers['Content-Type'])
        # TODO: дописать ф-цию
        return MimeTypeEnum.get_mime_type(mimetypes.guess_type(obj)[0])

    def __getitem__(self, item: Any) -> Any:
        if self.mime_type is not None:
            self.mime_type = self._detect_mime_type(self.obj)
        return parsing.MIME_TYPE_MAP[self.mime_type](self.to_find[item])

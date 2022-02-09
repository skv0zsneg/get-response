import enum
from typing import Union
from get_response.core.gr_exceptions import UnexpectedMimeType


class MimeTypeEnum(enum.Enum):
    APPLICATION_JSON = ('application', 'json')
    APPLICATION_SOAP_PLUS_XML = ('application', 'soap+xml')

    def __init__(self,
                 mime_type: str,
                 mime_subtype: str):
        self.mime_type = mime_type
        self.mime_subtype = mime_subtype
        self.full_mime_type = f"{mime_type}/{mime_subtype}"

    @staticmethod
    def get_mime_type(full_mime_type: Union[str, bool]) -> "MimeTypeEnum":
        mime_type_map = {
            mime_type_enum.full_mime_type: mime_type_enum
            for mime_type_enum in MimeTypeEnum
        }
        try:
            return mime_type_map[full_mime_type]
        except KeyError:
            raise UnexpectedMimeType(f"I don't know the mime type {full_mime_type}. "
                                     f"{UnexpectedMimeType.MESSAGE}")

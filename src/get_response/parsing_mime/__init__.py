from get_response.core.mime_type_enum import MimeTypeEnum
from get_response.parsing_mime.parsing_application_json import ParsingApplicationJson
from get_response.parsing_mime.parsing_text_xml import ParsingTextXml


__all__ = ['MIME_TYPE_MAP']

MIME_TYPE_MAP = {
    MimeTypeEnum.APPLICATION_JSON.full_mime_type: ParsingApplicationJson,
    MimeTypeEnum.TEXT_XML.full_mime_type: ParsingTextXml
}

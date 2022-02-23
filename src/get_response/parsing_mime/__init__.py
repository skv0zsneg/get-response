from get_response.core.enums import MimeTypeEnum
from get_response.parsing_mime.parsing_application_json import ParsingApplicationJson
from get_response.parsing_mime.parsing_text_xml import ParsingTextXml


__all__ = ['MIME_TYPE_MAP']

# Connections to parsing method is depend on this dictionary. It contains
# complete name of Mimetype in keys and parsing class as value. All direct
# calls of parsing classes are prohibited.
MIME_TYPE_MAP = {
    MimeTypeEnum.APPLICATION_JSON: ParsingApplicationJson,
    MimeTypeEnum.TEXT_XML: ParsingTextXml
}

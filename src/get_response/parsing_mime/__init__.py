from get_response.core.mime_type_enum import MimeTypeEnum
from get_response.parsing_mime.parsing_json import ParsingJson
from get_response.parsing_mime.parsing_soap_plus_xml import ParsingSoapPlusXml


MIME_TYPE_MAP = {
    MimeTypeEnum.APPLICATION_JSON.full_mime_type: ParsingJson,
    MimeTypeEnum.APPLICATION_SOAP_PLUS_XML.full_mime_type: ParsingSoapPlusXml
}

__all__ = ['MIME_TYPE_MAP']

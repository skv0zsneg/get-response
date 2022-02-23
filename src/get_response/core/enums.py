import enum


class MimeTypeEnum(enum.Enum):
    """Enum of Mimetypes that using in module.

    Enum of Mimetypes that are using for detecting object type. Type of value
    are getting from IANA (https://www.iana.org/assignments/media-types/media-types.xhtml).

    Attributes:
        type_name: First part of Mimetype (example 'application').
        subtype_name: Second part of Mimetype (example 'json').
        full_name: Full part of Mimetype (example 'application/json').
    """

    # application
    APPLICATION_JSON = ('application', 'json', 'application/json')

    # text
    TEXT_XML = ('application', 'soap+xml', 'application/soap+xml')

    def __init__(self, type_name: str, subtype_name: str, full_name: str):
        self.type_name = type_name
        self.subtype_name = subtype_name
        self.full_name = full_name

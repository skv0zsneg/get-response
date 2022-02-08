import enum


class MimeTypeEnum(enum.Enum):
    APPLICATION_JSON = ('application', 'json')
    APPLICATION_SOAP_PLUS_XML = ('application', 'soap+xml')

    def __init__(self,
                 mime_type: str,
                 mime_sub_type: str):
        self.mime_type = mime_type
        self.mime_sub_type = mime_sub_type
        self.full_mime_type = f"{mime_type}/{mime_sub_type}"

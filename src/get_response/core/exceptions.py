class MimeTypeException(Exception):
    pass


class UnexpectedMimeType(MimeTypeException):
    def __init__(self, mime_type: str):
        self.mime_type = mime_type
        super().__init__(f"Maybe mime type `{mime_type}` is wrong or get-response"
                         f" cannot parse and (or) detect this kind of response.")


class CannotDetectMimeType(MimeTypeException):
    def __init__(self, mime_type: str):
        self.mime_type = mime_type
        super().__init__(f"Type of 'obj' `{mime_type}` parameter is unexpected."
                         f" You have to fill 'mime_type' parameter.")

class UnexpectedMimeType(Exception):
    MESSAGE = "Maybe you write this type wrong or get-response cannot parse and (or) detect this kind of response."


class CannotDetectMimeType(Exception):
    MESSAGE = "Type of 'obj' parameter is unexpected. You have to fill 'mime_type' parameter."

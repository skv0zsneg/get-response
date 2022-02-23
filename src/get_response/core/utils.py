from typing import Optional

from get_response.core import exceptions
from get_response.core import enums


def get_mime_type(full_mime_type: Optional[str]) -> "enums.MimeTypeEnum":
    """Getting Mimetype enum by full Mimetype name.

    This functions detected a mime type and return a enum instance of Mimetype.
    It's necessary for correct work.

    Args:
        full_mime_type: Full string Mimetype name.

    Returns:
        A field of mime_type_enum.MimeTypeEnum.

    Raises:
        gr_exceptions.UnexpectedMimeType: An error occurred if full_mime_type
         is unexpected.
    """
    if full_mime_type is None:
        raise exceptions.UnexpectedMimeType('None')
    mime_type_map = {mime_type.full_name: mime_type
                     for mime_type in enums.MimeTypeEnum}
    try:
        return mime_type_map[full_mime_type]
    except KeyError:
        raise exceptions.UnexpectedMimeType(full_mime_type)

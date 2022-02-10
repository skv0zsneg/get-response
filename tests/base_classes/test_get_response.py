import pytest
import tests.utils.base_classes.utils_get_response as utils
from get_response import GetResponse
from get_response.core.mime_type_enum import MimeTypeEnum
from get_response.core.gr_exceptions import (UnexpectedMimeType,
                                             CannotDetectMimeType)


class TestGetResponseClass:
    def test_get_raw_object(self):
        gr = GetResponse(utils.TESTING_OBJ,
                         to_find={},
                         mime_type=utils.TESTING_MIME_TYPE)
        assert gr.get_raw() == utils.TESTING_OBJ

    def test_guessing_a_mime_type_specified_explicitly(self):
        gr = GetResponse(utils.TESTING_OBJ,
                         to_find={},
                         mime_type=utils.TESTING_MIME_TYPE)
        assert gr.mime_type == utils.TESTING_MIME_TYPE

    def test_set_mime_type_explicitly_by_mime_type_enum(self):
        gr = GetResponse(utils.TESTING_OBJ,
                         to_find={},
                         mime_type=MimeTypeEnum.APPLICATION_JSON)
        assert gr.mime_type == utils.TESTING_MIME_TYPE

    def test_get_unexpected_mime_type_exception_with_none_mime_type(self):
        with pytest.raises(UnexpectedMimeType):
            GetResponse(utils.TESTING_OBJ,
                        to_find={},
                        mime_type=None)

    def test_get_unexpected_mime_type_exception_with_non_existent_mime_type(self):
        with pytest.raises(UnexpectedMimeType):
            GetResponse(utils.TESTING_OBJ,
                        to_find={},
                        mime_type='non_existent/mimetype')

    def test_test_cannot_detect_mime_type(self):
        with pytest.raises(CannotDetectMimeType):
            GetResponse(Exception,
                        to_find={},
                        mime_type=utils.TESTING_MIME_TYPE)



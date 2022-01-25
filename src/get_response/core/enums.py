from enum import Enum
from typing import Union, List, Literal


class ResponseType(Enum):
    XML = ('xml', ['<', '>'])
    JSON = ('json', ['{', '}'])

    def __init__(self, response_type_name: str, salt: Union[List[str], str]):
        """Response types enum.

        :param response_type_name: Name of API response.
        :param salt: Salt of API response.
        """
        self.response_type_name = response_type_name
        self.salt = salt

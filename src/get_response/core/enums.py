from enum import Enum
from typing import Union, List


class ApiType(Enum):
    SOAP = ('SOAP', ['<', '>'])
    REST = ('REST', ['{', '}'])

    def __init__(self, api_name: str, salt: Union[List[str], str]):
        """API types enum for detecting API response
        which need to be parsed.

        :param api_name: Name of API response.
        :param salt: Salt of API response.
        """
        self.api_name = api_name
        self.salt = salt

    @classmethod
    def get_all_api_names(cls) -> List[str]:
        return list(map(lambda api_type: api_type.api_name, ApiType))

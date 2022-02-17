from typing import Any

from get_response.parsing import Parsing


class ParsingApplicationJson(Parsing):
    def get_obj(self) -> Any:
        print('You are in ParsingApplicationJson')

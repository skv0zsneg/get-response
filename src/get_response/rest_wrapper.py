import json
from typing import Optional

from .api_wrapper import ApiWrapper


class RestWrapper(ApiWrapper):
    def parse_rest_response(self) -> None:
        obj_for_parse = json.load(self.cur_obj)
        for field_name, to_find_road in self.to_find.items():
            parse_result = self._parse(obj_for_parse, to_find_road)
            self.founded.update({field_name: parse_result})
            exec(f"RestWrapper.{field_name} = '{parse_result}'")

    @classmethod
    def _parse(cls, obj_for_parse: dict, to_find_road: list) -> Optional[str]:
        ...





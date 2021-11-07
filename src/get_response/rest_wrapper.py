import json
from typing import Optional, Union

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

    @classmethod
    def _parse_one(cls, obj_for_parse: dict, to_find_field: str) -> Union[str, dict, list, None]:
        item: Union[str, dict, list, None] = None
        try:
            return obj_for_parse[to_find_field]
        except KeyError:
            for value in obj_for_parse.values():
                if isinstance(value, dict):
                    item = cls._parse_one(value, to_find_field)
                if isinstance(value, list):
                    for list_value in value:
                        if isinstance(list_value, dict):
                            item = cls._parse_one(list_value, to_find_field)
        return item

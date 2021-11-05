from json import load

from .api_wrapper import ApiWrapper


class RestWrapper(ApiWrapper):
    def parse_rest_response(self) -> None:
        obj_for_parse = load(self.c_obj)
        for field_name, to_find_road in self.to_find.items():
            parse_result = self._parse(obj_for_parse, to_find_road)
            self.founded.update({field_name: parse_result})
            exec(f"RestWrapper.{field_name} = '{parse_result}'")

    @staticmethod
    def _parse(obj_to_parse: dict, to_find_road: list) -> str:
        ...



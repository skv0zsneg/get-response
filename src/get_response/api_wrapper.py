from typing import Union
from requests import Response


class ApiWrapper:
    def __init__(self, obj: Union[Response, str], to_find: dict) -> None:
        self.cur_obj = self._get_current_obj(obj)
        self.to_find = to_find
        self.founded: dict = {}

    def __getitem__(self, item):
        return self.founded[item]

    def get_raw_obj(self):
        return self.cur_obj

    @staticmethod
    def _get_current_obj(obj: Union[Response, str]) -> str:
        if isinstance(obj, Response):
            return obj.text
        return obj

from dataclasses import dataclass
from typing import Any, Union
from requests import Response


@dataclass
class Parsing:
    obj: Union[Response, str]
    road_to_obj: Any
    parsed_obj: Any = None
    cache: Any = None

    def get_obj(self) -> Any:
        pass

from dataclasses import dataclass
from typing import Any


@dataclass
class Parsing:
    road_to_parsed_obj: Any
    parsed_obj: Any = None
    cache: Any = None

    def get_obj(self) -> Any:
        pass

from dataclasses import dataclass
from typing import Any


@dataclass
class Parsing:
    parsed_obj: Any
    cache: Any

    def get_obj(self) -> Any:
        pass

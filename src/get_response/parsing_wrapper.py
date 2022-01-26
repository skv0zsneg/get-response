from typing import Dict, List, Union, Optional
from dataclasses import dataclass


@dataclass
class ParsingWrapper:
    obj: str
    to_find: Dict[str, List[str]]
    parsed_object: Optional[Dict[str, Union[Dict, List, str]]] = None

    def str_obj(self) -> str:
        return self.obj

    def __len__(self):
        return len(self.parsed_object)

    def __getitem__(self, item):
        return self.parsed_object[item]

    def parse(self) -> None: ...

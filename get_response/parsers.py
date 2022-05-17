from abc import ABC
from abc import abstractmethod
import json
from typing import Any, Optional, List


T_GET_OBJECTS = List[Optional[Any]]


class BaseParser(ABC):

    @abstractmethod
    def __init__(self, obj: str) -> None:
        self.obj = obj

    @abstractmethod
    def get_objects(self, item: str, obj: Any = None) -> T_GET_OBJECTS:
        """Method parsing the object and return what he found by given
        key.

        Method get object and trying to found in it value that exist in
        it by the given key.

        Args:
            obj: Object that will be parsed.
            item: String - field which value must be found.

        Returns:
            List[Optional[Any]]: Method return a found values or None if 
             searching are failed. 
        """
        pass


class JsonParser(BaseParser):
    
    def __init__(self, obj: str) -> None:
        super().__init__(obj)
        self._obj_dict = json.loads(self.obj)

    def get_objects(self, field: str, obj: dict = None) -> T_GET_OBJECTS:
        # TODO: избавиться от рекурсии!!!
        fields_found = []

        for key, value in self._obj_dict.items():

            if key == field:
                fields_found.append(value)

            elif isinstance(value, dict):
                results = self.get_objects(field, value)
                for result in results:
                    fields_found.append(result)

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_results = self.get_objects(field, item)
                        for another_result in more_results:
                            fields_found.append(another_result)

        return fields_found
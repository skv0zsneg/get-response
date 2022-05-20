from abc import ABC
from abc import abstractmethod
import json
import re
from typing import Any, Tuple
from unittest import result
import xml.etree.ElementTree as ET


T_GET_OBJECTS = Tuple[Any, ...]


class BaseParser(ABC):

    @abstractmethod
    def __init__(self, obj: str) -> None:
        self.obj = obj

    @abstractmethod
    def get_objects(self, field: str) -> T_GET_OBJECTS:
        """Method parsing the object and return what he found by given
        key.

        Method get object and trying to found in it values that exist
        in it by the given key.

        Args:
            field: Field which value must be found.

        Returns:
            Tuple[Any]: Method return a found values or empty tuple if 
             searching are failed. 
        """
        pass


class JsonParser(BaseParser):
    
    def __init__(self, obj: str) -> None:
        super().__init__(obj)
        self._obj_dict = json.loads(self.obj)

    def get_objects(self, field: str) -> T_GET_OBJECTS:
        """Parsing a serialized to dict json object."""
        dicts_queue = [self._obj_dict,]
        fields_found = []

        for dictionary in dicts_queue:
            for key, value in dictionary.items():

                if key == field:
                    fields_found.append(value)

                elif isinstance(value, dict):
                    dicts_queue.append(value)

                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            dicts_queue.append(item)
                        if isinstance(item, list):
                            value.extend(item)
        
        return tuple(fields_found)


class SoapParser(BaseParser):

    def __init__(self, obj: str) -> None:
        super().__init__(obj)
        self._obj_xml = ET.fromstring(
            self._prepare_obj(obj))

    def get_objects(self, field: str) -> T_GET_OBJECTS:
        """Parsing a serialized by ElementTree object."""
        fields_found = []

        for childrens in self._obj_xml.iter():
            current_tag = childrens.tag
            tag_name = current_tag[current_tag.find('}') + 1::]

            if tag_name == field:
                for text in childrens.itertext():
                    print(repr(text))
                    fields_found.append(text)

        return tuple(fields_found)
    
    @staticmethod
    def _prepare_obj(obj: str) -> str:
        result = re.sub(r">(?:\W+)<", r"><", obj)
        return result.strip()
from dataclasses import dataclass
from typing import Any, Union, List, Dict

import requests


@dataclass
class Parsing(object):
    """Main abstract class for subsidiaries Parsing classes.

    This is abstract class that must be parent for subclasses that describe
    logic of parsing.

    Attributes:
        obj: Object that exposed for parsing.
        road_to_obj: List of values that describe way to object that need to
         be find.
        found_obj: Object that found in `obj`. None if nothing is found.
        cache: Special value that controls the cache logic.
    """
    obj: Union[requests.Response, str]
    road_to_obj: Union[List, Dict]
    found_obj: Any = None
    cache: Any = None

    def get_obj(self) -> Any:
        """Method for getting (parsing) objects.

        Main method for all subsidiaries Parsing classes. Method controls the
        logic of parsing and cache interaction.

        Returns:
            The return value can be anything type. It is depend on Mimetype
             of objects. See detailed information in specific classes.
        """
        pass

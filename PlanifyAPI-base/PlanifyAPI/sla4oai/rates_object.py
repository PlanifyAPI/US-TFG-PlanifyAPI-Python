"""
This module provides the RatesObject class for the SLA4OAI model.
"""

from typing import Any, Dict

from .path_object import PathObject


class RatesObject:
    """
    Represents the rates of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a rates object.

        Args:
            data (Dict[str, Any]): Data for initializing the rates.

        Returns:
            None
        """
        self._paths: Dict[str, PathObject] = {
            key: PathObject(data.get(key, {})) for key in data.keys()
        }

    def __repr__(self) -> str:
        return f"RatesObject({self._paths})"

    def get_paths(self) -> Dict[str, PathObject]:
        """
        Returns the paths.

        Returns:
            Dict[str, PathObject]: The paths.
        """
        return self._paths

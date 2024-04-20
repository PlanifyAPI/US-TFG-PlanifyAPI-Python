"""
This module provides the MetricsObject class for the SLA4OAI model.
"""

from typing import Any, Dict


class MetricsObject:
    """
    Represents the metrics of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a metrics object.

        Args:
            data (Dict[str, Any]): Data for initializing the metrics.

        Returns:
            None
        """
        self._metrics: Dict[str, Any] = data

    def __repr__(self) -> str:
        return f"MetricsObject({self._metrics})"

    def get_metrics(self) -> Dict[str, Any]:
        """
        Returns the metrics.

        Returns:
            Dict[str, Any]: The metrics.
        """
        return self._metrics

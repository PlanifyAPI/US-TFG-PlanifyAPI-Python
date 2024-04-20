"""
This module provides the PlansObject class for the SLA4OAI model.
"""

from typing import Any, Dict

from .plan_object import PlanObject


class PlansObject:
    """
    Represents the plans of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a plans object.

        Args:
            data (Dict[str, Any]): Data for initializing the plans.

        Returns:
            None
        """
        self._plan: Dict[str, PlanObject] = {
            plan_name: PlanObject(plan_data) for plan_name, plan_data in data.items()
        }

    def __repr__(self) -> str:
        return f"PlansObject({self._plan})"

    def get_plans(self) -> Dict[str, PlanObject]:
        """
        Returns the plans.

        Returns:
            Dict[str, PlanObject]: The plans.
        """
        return self._plan

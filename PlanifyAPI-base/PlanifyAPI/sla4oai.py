"""
This module provides the SLA (Service Level Agreement) model for OAI (OpenAPI Initiative).
"""

from typing import Dict, List, Any


class SLA4OAI:
    """
    Represents an SLA (Service Level Agreement) for OpenAPI.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes an SLA object.

        Args:
            data (Dict[str, Any]): Data for initializing the SLA.

        Returns:
            None
        """
        self.context: ContextObject = ContextObject(data.get("context", {}))
        self.infrastructure: InfrastructureObject = InfrastructureObject(
            data.get("infrastructure", {})
        )
        self.pricing: PricingObject = PricingObject(data.get("pricing", {}))
        self.metrics: MetricsObject = MetricsObject(data.get("metrics", {}))
        self.plans: PlansObject = PlansObject(data.get("plans", {}))
        self.quotas: QuotasObject = QuotasObject(data.get("quotas", {}))
        self.rates: RatesObject = RatesObject(data.get("rates", {}))
        self.guarantees: GuaranteesObject = GuaranteesObject(data.get("guarantees", {}))
        self.configuration: ConfigurationsObject = ConfigurationsObject(
            data.get("configuration", {})
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the SLA object.

        Returns:
            str: String representation of the SLA object.
        """
        return f"""SLA4OAI: 
        {{
            {self.context},
            {self.infrastructure},
            {self.pricing},
            {self.metrics},
            {self.plans},
            {self.quotas},
            {self.rates},
            {self.guarantees},
            {self.configuration}\n}}"""


class ContextObject:
    """
    Represents the context of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a context object.

        Args:
            data (Dict[str, Any]): Data for initializing the context.

        Returns:
            None
        """
        self.id: str = data.get("id", "")
        self.version: str = data.get("version", "")
        self.api: str = data.get("api", "")
        self.type: str = data.get("type", "")
        self.provider: str = data.get("provider", "")
        self.consumer: str = data.get("consumer", "")
        self.validity: ValidityObject = ValidityObject(data.get("validity", {}))

    def __str__(self) -> str:
        """
        Returns a string representation of the context object.

        Returns:
            str: String representation of the context object.
        """
        return "context: " + str(self.__dict__)


class ValidityObject:
    """
    Represents the validity period of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a validity object.

        Args:
            data (Dict[str, Any]): Data for initializing the validity.

        Returns:
            None
        """
        self.effective_date: str = data.get("effectiveDate", "")
        self.expiration_date: str = data.get("expirationDate", "")

    def __str__(self) -> str:
        """
        Returns a string representation of the validity object.

        Returns:
            str: String representation of the validity object.
        """
        return str(self.__dict__)


class InfrastructureObject:
    """
    Represents the infrastructure of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes an infrastructure object.

        Args:
            data (Dict[str, Any]): Data for initializing the infrastructure.

        Returns:
            None
        """
        self.supervisor: str = data.get("supervisor", "")
        self.monitor: str = data.get("monitor", "")

    def __str__(self) -> str:
        """
        Returns a string representation of the infrastructure object.

        Returns:
            str: String representation of the infrastructure object.
        """
        return "infrastructure: " + str(self.__dict__)


class PricingObject:
    """
    Represents the pricing information of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a pricing object.

        Args:
            data (Dict[str, Any]): Data for initializing the pricing.

        Returns:
            None
        """
        self.cost: float = data.get("cost", 0.0)
        self.custom: bool = data.get("custom", False)
        self.currency: str = data.get("currency", "USD")
        self.billing: str = data.get("billing", "monthly")

    def __str__(self) -> str:
        """
        Returns a string representation of the pricing object.

        Returns:
            str: String representation of the pricing object.
        """
        return str(self.__dict__)


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
        self.metrics: Dict[str, Any] = data

    def __str__(self) -> str:
        """
        Returns a string representation of the metrics object.

        Returns:
            str: String representation of the metrics object.
        """
        return str(self.__dict__)


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
        self.plan: Dict[str, PlanObject] = {
            plan_name: PlanObject(plan_data) for plan_name, plan_data in data.items()
        }

    def __str__(self) -> str:
        """
        Returns a string representation of the plans object.

        Returns:
            str: String representation of the plans object.
        """
        return str(self.__dict__)


class PlanObject:
    """
    Represents a specific plan within an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a plan object.

        Args:
            data (Dict[str, Any]): Data for initializing the plan.

        Returns:
            None
        """
        self.configuration: ConfigurationsObject = ConfigurationsObject(
            data.get("configuration", {})
        )
        self.availability: str = data.get("availability", "")
        self.pricing: PricingObject = PricingObject(data.get("pricing", {}))
        self.quotas: QuotasObject = QuotasObject(data.get("quotas", {}))
        self.rates: RatesObject = RatesObject(data.get("rates", {}))
        self.guarantees: GuaranteesObject = GuaranteesObject(data.get("guarantees", {}))

    def __str__(self) -> str:
        """
        Returns a string representation of the plan object.

        Returns:
            str: String representation of the plan object.
        """
        return str(self.__dict__)


class QuotasObject:
    """
    Represents the quotas of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a quotas object.

        Args:
            data (Dict[str, Any]): Data for initializing the quotas.

        Returns:
            None
        """
        self.paths: List[Dict[PathObject, Any]] = [
            PathObject(data.get(key, {})) for key in data.keys()
        ]

    def __str__(self) -> str:
        """
        Returns a string representation of the quotas object.

        Returns:
            str: String representation of the quotas object.
        """
        return str(self.__dict__)


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
        self.rates: Dict[str, Any] = data

    def __str__(self) -> str:
        """
        Returns a string representation of the rates object.

        Returns:
            str: String representation of the rates object.
        """
        return str(self.__dict__)


class GuaranteesObject:
    """
    Represents the guarantees of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a guarantees object.

        Args:
            data (Dict[str, Any]): Data for initializing the guarantees.

        Returns:
            None
        """
        self.guarantees: Dict[str, Any] = data

    def __str__(self) -> str:
        """
        Returns a string representation of the guarantees object.

        Returns:
            str: String representation of the guarantees object.
        """
        return str(self.__dict__)


class ConfigurationsObject:
    """
    Represents the configurations of an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a configurations object.

        Args:
            data (Dict[str, Any]): Data for initializing the configurations.

        Returns:
            None
        """
        self.configurations: Dict[str, Any] = data

    def __str__(self) -> str:
        """
        Returns a string representation of the configurations object.

        Returns:
            str: String representation of the configurations object.
        """
        return str(self.__dict__)


class OverageObject:
    """
    Represents overage information within an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes an overage object.

        Args:
            data (Dict[str, Any]): Data for initializing the overage.

        Returns:
            None
        """
        self.overage: int = data.get("excess", 0)
        self.cost: float = data.get("cost", 0.0)

    def __str__(self) -> str:
        """
        Returns a string representation of the overage object.

        Returns:
            str: String representation of the overage object.
        """

        return str(self.__dict__)


class CostObject:
    """
    Represents cost information within an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a cost object.

        Args:
            data (Dict[str, Any]): Data for initializing the cost.

        Returns:
            None
        """
        self.overage: OverageObject = OverageObject(data.get("overage", {}))

    def __str__(self) -> str:
        """
        Returns a string representation of the cost object.

        Returns:
            str: String representation of the cost object.
        """
        return str(self.__dict__)


class PeriodObject:
    """
    Represents a period within an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a period object.

        Args:
            data (Dict[str, Any]): Data for initializing the period.

        Returns:
            None
        """
        self.amount: int = data.get("amount", 0)
        self.unit: str = data.get("unit", "")

    def __str__(self) -> str:
        """
        Returns a string representation of the period object.

        Returns:
            str: String representation of the period object.
        """
        return str(self.__dict__)


class LimitObject:
    """
    Represents a limit within an SLA.
    """

    def __init__(self, *keys) -> None:
        """
        Initializes a limit object.

        Args:
            *keys: Variable number of dictionaries representing limit data.

        Returns:
            None
        """
        for key in keys:
            self.max: int = key.get("max", 0)
            self.custom: bool = key.get("custom", False)
            self.period: PeriodObject = PeriodObject(key.get("period", {}))
            self.cost: CostObject = CostObject(key.get("cost", {}))

    def __str__(self) -> str:
        """
        Returns a string representation of the limit object.

        Returns:
            str: String representation of the limit object.
        """
        return str(self.__dict__)


class OperationObject:
    """
    Represents an operation within an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes an operation object.

        Args:
            data (Dict[str, Any]): Data for initializing the operation.

        Returns:
            None
        """
        self.limits: List[LimitObject] = [
            LimitObject(*values) for values in data.values()
        ]

    def __str__(self) -> str:
        """
        Returns a string representation of the operation object.

        Returns:
            str: String representation of the operation object.
        """
        return str(self.__dict__)


class PathObject:
    """
    Represents a path within an SLA.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes a path object.

        Args:
            data (Dict[str, Any]): Data for initializing the path.

        Returns:
            None
        """
        self.operations: List[Dict[OperationObject, Any]] = [
            OperationObject(data.get(key, {})) for key in data.keys()
        ]

    def __str__(self) -> str:
        """
        Returns a string representation of the path object.

        Returns:
            str: String representation of the path object.
        """
        return str(self.__dict__)

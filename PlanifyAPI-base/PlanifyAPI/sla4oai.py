"""
This module provides the SLA (Service Level Agreement) model for OAI (OpenAPI Initiative).
"""

from typing import Dict, Any


class SLA4OAI:
    """
    Represents an SLA (Service Level Agreement) model for OAI (OpenAPI Initiative).
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the SLA4OAI object with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the SLA model data.
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
        return f"""SLA4OAI: 
        {{
            context: {self.context},
            infrastructure: {self.infrastructure},
            pricing: {self.pricing},
            metrics: {self.metrics},
            plans: {self.plans},
            quotas: {self.quotas},
            rates: {self.rates},
            guarantees: {self.guarantees},
            configuration: {self.configuration}\n}}"""


class ContextObject:
    """
    Represents the context object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the ContextObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the context data.
        """
        self.id: str = data.get("id", "")
        self.version: str = data.get("version", "")
        self.api: str = data.get("api", "")
        self.type: str = data.get("type", "")
        self.provider: str = data.get("provider", "")
        self.consumer: str = data.get("consumer", "")
        self.validity: ValidityObject = ValidityObject(data.get("validity", {}))

    def __str__(self) -> str:
        return str(self.__dict__)


class ValidityObject:
    """
    Represents the validity object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the ValidityObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the validity data.
        """
        self.effective_date: str = data.get("effectiveDate", "")
        self.expiration_date: str = data.get("expirationDate", "")

    def __str__(self) -> str:
        return str(self.__dict__)


class InfrastructureObject:
    """
    Represents the infrastructure object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the InfrastructureObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the infrastructure data.
        """
        self.supervisor: str = data.get("supervisor", "")
        self.monitor: str = data.get("monitor", "")

    def __str__(self) -> str:
        return str(self.__dict__)


class PricingObject:
    """
    Represents the pricing object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the PricingObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the pricing data.
        """
        self.cost: float = data.get("cost", 0.0)
        self.custom: bool = data.get("custom", False)
        self.currency: str = data.get("currency", "USD")
        self.billing: str = data.get("billing", "monthly")

    def __str__(self) -> str:
        return str(self.__dict__)


class MetricsObject:
    """
    Represents the metrics object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the MetricsObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the metrics data.
        """
        self.metrics: Dict[str, Any] = data

    def __str__(self) -> str:
        return str(self.__dict__)


class PlansObject:
    """
    Represents the plans object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the PlansObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the plans data.
        """
        self.plans: Dict[str, PlanObject] = {
            plan_name: PlanObject(plan_data) for plan_name, plan_data in data.items()
        }

    def __str__(self) -> str:
        return str(self.__dict__)


class PlanObject:
    """
    Represents a specific plan within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the PlanObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the plan data.
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
        return str(self.__dict__)


class QuotasObject:
    """
    Represents the quotas object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the QuotasObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the quotas data.
        """
        self.quotas: Dict[str, Any] = data

    def __str__(self) -> str:
        return str(self.__dict__)


class RatesObject:
    """
    Represents the rates object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the RatesObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the rates data.
        """
        self.rates: Dict[str, Any] = data

    def __str__(self) -> str:
        return str(self.__dict__)


class GuaranteesObject:
    """
    Represents the guarantees object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the GuaranteesObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the guarantees data.
        """
        self.guarantees: Dict[str, Any] = data

    def __str__(self) -> str:
        return str(self.__dict__)


class ConfigurationsObject:
    """
    Represents the configurations object within the SLA model.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initializes the ConfigurationsObject with the provided data.

        Args:
        - data (Dict[str, Any]): A dictionary containing the configurations data.
        """
        self.configurations: Dict[str, Any] = data

    def __str__(self) -> str:
        return str(self.__dict__)

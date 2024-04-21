"""
This module provides the SLA (Service Level Agreement) model for OAI (OpenAPI Initiative).
"""

from typing import Dict, Any

from PlanifyAPI.sla4oai.context_object import ContextObject
from PlanifyAPI.sla4oai.infrastructure_object import InfrastructureObject
from PlanifyAPI.sla4oai.pricing_object import PricingObject
from PlanifyAPI.sla4oai.metrics_object import MetricsObject
from PlanifyAPI.sla4oai.plans_object import PlansObject
from PlanifyAPI.sla4oai.quotas_object import QuotasObject
from PlanifyAPI.sla4oai.rates_object import RatesObject
from PlanifyAPI.sla4oai.guarantees_object import GuaranteesObject
from PlanifyAPI.sla4oai.configurations_object import ConfigurationsObject


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
        self._context: ContextObject = ContextObject(data.get("context", {}))
        self._infrastructure: InfrastructureObject = InfrastructureObject(
            data.get("infrastructure", {})
        )
        self._pricing: PricingObject = PricingObject(data.get("pricing", {}))
        self._metrics: MetricsObject = MetricsObject(data.get("metrics", {}))
        self._plans: PlansObject = PlansObject(data.get("plans", {}))
        self._quotas: QuotasObject = QuotasObject(data.get("quotas", {}))
        self._rates: RatesObject = RatesObject(data.get("rates", {}))
        self._guarantees: GuaranteesObject = GuaranteesObject(
            data.get("guarantees", {})
        )
        self._configuration: ConfigurationsObject = ConfigurationsObject(
            data.get("configuration", {})
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return f"""SLA4OAI(\n
                context={self._context},\n
                infrastructure={self._infrastructure},\n
                pricing={self._pricing},\n
                metrics={self._metrics},\n
                plans={self._plans},\n
                quotas={self._quotas},\n
                rates={self._rates},\n
                guarantees={self._guarantees},\n
                configuration={self._configuration}\n
            )"""

    def get_context(self):
        """
        Returns the context of the SLA.

        Returns:
            ContextObject: The context of the SLA.
        """
        return self._context

    def get_infrastructure(self):
        """
        Returns the infrastructure of the SLA.

        Returns:
            InfrastructureObject: The infrastructure of the SLA.
        """
        return self._infrastructure

    def get_pricing(self):
        """
        Returns the pricing of the SLA.

        Returns:
            PricingObject: The pricing of the SLA.
        """
        return self._pricing

    def get_metrics(self):
        """
        Returns the metrics of the SLA.

        Returns:
            MetricsObject: The metrics of the SLA.
        """
        return self._metrics

    def get_plans(self):
        """
        Returns the plans of the SLA.

        Returns:
            PlansObject: The plans of the SLA.
        """
        return self._plans

    def get_quotas(self):
        """
        Returns the quotas of the SLA.

        Returns:
            QuotasObject: The quotas of the SLA.
        """
        return self._quotas

    def get_rates(self):
        """
        Returns the rates of the SLA.

        Returns:
            RatesObject: The rates of the SLA.
        """
        return self._rates

    def get_guarantees(self):
        """
        Returns the guarantees of the SLA.

        Returns:
            GuaranteesObject: The guarantees of the SLA.
        """
        return self._guarantees

    def get_configuration(self):
        """
        Returns the configuration of the SLA.

        Returns:
            ConfigurationsObject: The configuration of the SLA.
        """
        return self._configuration

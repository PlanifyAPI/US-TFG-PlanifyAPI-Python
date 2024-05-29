from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.parser import Parser
from PlanifyAPI.rate_limiter import rate_limited
from PlanifyAPI.sla4oai.sla4oai import SLA4OAI

load_dotenv()

BASE_URL = "https://api.dhl.com"


parser = Parser("../models-sla4oai/dhl_locationFinderUnified.yaml")

sla = SLA4OAI(parser.yaml_to_dict())

quota = (
    sla.get_plans()
    .get_plan_by_name("Free")
    .get_quotas()
    .get_max_by_path_and_method("/*", "all")
)

period = (
    sla.get_plans()
    .get_plan_by_name("Free")
    .get_quotas()
    .get_period_by_path_and_method("/*", "all")
)

headers = {
    "DHL-API-Key": f"{environ.get('DHL_PUBLIC_KEY')}",
}

api_call_dhl = APICall(
    "dhl",
    f"{BASE_URL}/location-finder/v1/find-by-address?countryCode=GB&addressLocality=London",
    "GET",
    headers,
)

rate_dhl = api_call_dhl.get_calls_per_second(quota, timedelta(days=period.get_amount()))

print(
    f"""La cuota a cumplir es de {quota} cada {period.get_amount()} {period.get_unit()}. Por ello, se realizarán {rate_dhl} llamadas por segundo."""
)


@rate_limited(rate_dhl)
def call_api_dhl():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_dhl.execute()
    return f"Respuesta {response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_dhl()
    print("Respuesta:", response)

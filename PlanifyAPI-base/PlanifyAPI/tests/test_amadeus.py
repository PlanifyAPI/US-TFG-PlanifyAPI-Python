from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.parser import Parser
from PlanifyAPI.rate_limiter import rate_limited
from PlanifyAPI.sla4oai.sla4oai import SLA4OAI

load_dotenv()

BASE_URL = "https://test.api.amadeus.com"


parser = Parser("../models-sla4oai/amadeus.yaml")

sla = SLA4OAI(parser.yaml_to_dict())

quota = (
    sla.get_plans()
    .get_plan_by_name("Test")
    .get_quotas()
    .get_max_by_path_and_method("/v2/shopping/flight-offers", "get")
)

period = (
    sla.get_plans()
    .get_plan_by_name("Test")
    .get_quotas()
    .get_period_by_path_and_method("/v2/shopping/flight-offers", "get")
)

headers = {
    "Authorization": f"Bearer {environ.get('AMADEUS_API_KEY')}",
    "accept": "application/vnd.amadeus+json",
    "Content-Type": "application/vnd.amadeus+json",
}

api_call_amadeus = APICall(
    "amadeus",
    f"{BASE_URL}/v2/shopping/flight-offers?originLocationCode=SYD&destinationLocationCode=BKK&departureDate=2025-05-02&adults=1&nonStop=false&max=250",
    "GET",
    headers,
)

rate_amadeus = api_call_amadeus.get_calls_per_second(
    quota, timedelta(hours=period.get_amount())
)

print(
    f"""La cuota a cumplir es de {quota} cada {period.get_amount()} {period.get_unit()}. Por ello, se realizarán {rate_amadeus} llamadas por segundo."""
)


@rate_limited(rate_amadeus)
def call_api_amadeus():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_amadeus.execute()
    return f"Respuesta {response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_amadeus()
    print("Respuesta:", response)

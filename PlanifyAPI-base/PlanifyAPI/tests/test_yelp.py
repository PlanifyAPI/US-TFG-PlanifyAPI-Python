from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.parser import Parser
from PlanifyAPI.rate_limiter import rate_limited
from PlanifyAPI.sla4oai.sla4oai import SLA4OAI

load_dotenv()

BASE_URL = "https://api.yelp.com"


parser = Parser("../models-sla4oai/yelp.yaml")

sla = SLA4OAI(parser.yaml_to_dict())

quota = (
    sla.get_plans()
    .get_plan_by_name("Free")
    .get_quotas()
    .get_max_by_path_and_method("/v3/businesses/search/phone", "get")
)

period = (
    sla.get_plans()
    .get_plan_by_name("Free")
    .get_quotas()
    .get_period_by_path_and_method("/v3/businesses/search/phone", "get")
)

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {environ.get('YELP_API_KEY')}",
}

api_call_yelp = APICall(
    "yelp",
    f"{BASE_URL}/v3/businesses/search/phone?phone=%2B14159083801",
    "GET",
    headers,
)

rate_yelp = api_call_yelp.get_calls_per_second(
    quota, timedelta(days=period.get_amount())
)

print(
    f"""La cuota a cumplir es de {quota} cada {period.get_amount()} {period.get_unit()}. Por ello, se realizarán {rate_yelp} llamadas por segundo."""
)


@rate_limited(rate_yelp)
def call_api_yelp():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_yelp.execute()
    return f"{response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_yelp()
    print("Respuesta:", response)

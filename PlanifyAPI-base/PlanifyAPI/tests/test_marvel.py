from datetime import timedelta
from os import environ
import time
import hashlib

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.parser import Parser
from PlanifyAPI.rate_limiter import rate_limited
from PlanifyAPI.sla4oai.sla4oai import SLA4OAI

load_dotenv()

BASE_URL = "https://gateway.marvel.com"

PUBLIC_API_KEY = environ.get("MARVEL_PUBLIC_API_KEY")
PRIVATE_API_KEY = environ.get("MARVEL_PRIVATE_API_KEY")

ts = str(1717006441)
hash_input = ts + PRIVATE_API_KEY + PUBLIC_API_KEY
hash_result = hashlib.md5(hash_input.encode()).hexdigest()
print(PUBLIC_API_KEY, PRIVATE_API_KEY, hash_result)

parser = Parser("../models-sla4oai/marvel.yaml")

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
    "accept": "application/json",
    "Content-Type": "application/json",
}


api_call_marvel = APICall(
    "marvel",
    f"{BASE_URL}/v1/public/characters?ts={ts}&apikey={PUBLIC_API_KEY}&hash={hash_result}",
    "GET",
    headers,
)

rate_marvel = api_call_marvel.get_calls_per_second(
    quota, timedelta(days=period.get_amount())
)

print(
    f"""La cuota a cumplir es de {quota} cada {period.get_amount()} {period.get_unit()}. Por ello, se realizarán {rate_marvel} llamadas por segundo."""
)


@rate_limited(rate_marvel)
def call_api_marvel():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_marvel.execute()
    return response


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_marvel()
    print("Respuesta:", response.status_code)

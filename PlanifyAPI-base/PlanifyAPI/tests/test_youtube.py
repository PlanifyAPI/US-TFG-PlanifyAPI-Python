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

BASE_URL = "https://www.googleapis.com"

API_KEY = environ.get("YOUTUBE_API_KEY")

parser = Parser("../models-sla4oai/youtube.yaml")

sla = SLA4OAI(parser.yaml_to_dict())

quota = (
    sla.get_plans()
    .get_plan_by_name("Free")
    .get_quotas()
    .get_max_by_path_and_method("/search", "get")
)

period = (
    sla.get_plans()
    .get_plan_by_name("Free")
    .get_quotas()
    .get_period_by_path_and_method("/search", "get")
)

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}


api_call_youtube = APICall(
    "youtube",
    f"{BASE_URL}/youtube/v3/search?part=snippet&q=cats&key={API_KEY}",
    "GET",
    headers,
)

rate_youtube = api_call_youtube.get_calls_per_second(
    quota, timedelta(days=period.get_amount())
)

print(
    f"""La cuota a cumplir es de {quota} cada {period.get_amount()} {period.get_unit()}. Por ello, se realizarán {rate_youtube} llamadas por segundo."""
)


@rate_limited(rate_youtube)
def call_api_youtube():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_youtube.execute()
    return response


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_youtube()
    print("Respuesta:", response.status_code)

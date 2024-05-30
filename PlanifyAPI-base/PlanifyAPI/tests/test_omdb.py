from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.parser import Parser
from PlanifyAPI.rate_limiter import rate_limited
from PlanifyAPI.sla4oai.sla4oai import SLA4OAI

load_dotenv()

BASE_URL = "http://www.omdbapi.com"


parser = Parser("../models-sla4oai/omdb.yaml")

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


api_call_omdb = APICall(
    "OMDB",
    f"{BASE_URL}/?apikey={environ.get('OMDB_API_KEY')}&t=Harry+Potter&y=2002",
    "GET",
)

rate_omdb = api_call_omdb.get_calls_per_second(
    quota, timedelta(days=period.get_amount())
)

print(
    f"""La cuota a cumplir es de {quota} cada {period.get_amount()} {period.get_unit()}. Por ello, se realizarán {rate_omdb} llamadas por segundo."""
)


@rate_limited(rate_omdb)
def call_api_omdb():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_omdb.execute()
    return f"{response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_omdb()
    print("Respuesta:", response)

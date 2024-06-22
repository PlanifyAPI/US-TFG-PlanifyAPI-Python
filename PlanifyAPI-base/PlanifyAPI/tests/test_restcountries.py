from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

load_dotenv()

BASE_URL = "https://restcountries.com"

api_call_restcountries = APICall(
    "restcountries", f"{BASE_URL}/v3.1/name/aruba?fullText=true", "GET"
)

rate_restcountries = api_call_restcountries.get_calls_per_second(
    10000, timedelta(hours=1)
)

print(
    f"""La cuota a cumplir es de 10000 cada 1 hora. Por ello, se realizarán {rate_restcountries} llamadas por segundo."""
)


@rate_limited(rate_restcountries)
def call_api_restcountries():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_restcountries.execute()
    return f"{response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_restcountries()
    print("Respuesta:", response)

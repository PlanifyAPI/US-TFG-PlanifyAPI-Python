from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

load_dotenv()

BASE_URL = "https://api.foursquare.com"

headers = {
    "accept": "application/json",
    "Authorization": f"{environ.get("FOURSQUARE_API_KEY")}",
}

api_call_foursquare = APICall(
    "foursquare", f"{BASE_URL}/v3/places/search", "GET", headers
)

rate_foursquare = api_call_foursquare.get_calls_per_second(10000, timedelta(hours=1))

print(
    f"""La cuota a cumplir es de 10000 cada 1 hora. Por ello, se realizarán {rate_foursquare} llamadas por segundo."""
)


@rate_limited(rate_foursquare)
def call_api_foursquare():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_foursquare.execute()
    return f"{response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_foursquare()
    print("Respuesta:", response)

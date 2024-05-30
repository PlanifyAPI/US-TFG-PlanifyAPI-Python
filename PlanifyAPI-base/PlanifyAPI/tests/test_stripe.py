from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

load_dotenv()

BASE_URL = "https://api.stripe.com"

headers = {
    "Authorization": f"Bearer {environ.get('STRIPE_PRIVATE_KEY')}",
}

api_call_stripe = APICall(
    "stripe",
    f"{BASE_URL}/v1/files",
    "GET",
    headers,
)

rate_stripe = api_call_stripe.get_calls_per_second(10000, timedelta(days=31))

print(
    f"""La cuota a cumplir es de 10000 cada 1 mes. Por ello, se realizarán {rate_stripe} llamadas por segundo."""
)


@rate_limited(rate_stripe)
def call_api_stripe():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_stripe.execute()
    return f"{response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_stripe()
    print("Respuesta:", response)

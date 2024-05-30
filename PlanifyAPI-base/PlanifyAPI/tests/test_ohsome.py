from datetime import timedelta
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

load_dotenv()

BASE_URL = "https://api.ohsome.org"

api_call_ohsome = APICall(
    "ohsome",
    f"{BASE_URL}/v1/elements/area?bboxes=8.625%2C49.3711%2C8.7334%2C49.4397&format=json&time=2014-01-01&filter=landuse%3Dfarmland%20and%20type%3Away",
    "GET",
)

rate_ohsome = api_call_ohsome.get_calls_per_second(10000, timedelta(hours=1))

print(
    f"""La cuota a cumplir es de 10000 cada 1 hora. Por ello, se realizarán {rate_ohsome} llamadas por segundo."""
)


@rate_limited(rate_ohsome)
def call_api_ohsome():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_ohsome.execute()
    return f"{response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_ohsome()
    print("Respuesta:", response)

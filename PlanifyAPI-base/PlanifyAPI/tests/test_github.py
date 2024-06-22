from datetime import timedelta
from os import environ
import time

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

load_dotenv()

BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"Bearer {environ.get('GITHUB_TOKEN')}",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/vnd.github+json",
}

api_call_github = APICall(
    "github",
    f"{BASE_URL}/orgs/PlanifyAPI/repos",
    "GET",
    headers,
)

rate_github = api_call_github.get_calls_per_second(5000, timedelta(hours=1))

print(
    f"""La cuota a cumplir es de 5000 cada 1 hora. Por ello, se realizarán {rate_github} llamadas por segundo."""
)


@rate_limited(rate_github)
def call_api_github():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_github.execute()
    return f"Respuesta {response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_github()
    print("Respuesta:", response)

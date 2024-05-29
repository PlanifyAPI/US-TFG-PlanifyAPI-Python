from datetime import timedelta
import time

from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

BASE_URL = "https://banks.data.fdic.gov"

headers = {"accept": "application/json"}
api_call_fdic = APICall(
    "FDIC",
    f"{BASE_URL}/api/institutions?filters=STALP%3AIA%20AND%20ACTIVE%3A1&fields=ZIP%2COFFDOM%2CCITY%2CCOUNTY%2CSTNAME%2CSTALP%2CNAME%2CACTIVE%2CCERT%2CCBSA%2CASSET%2CNETINC%2CDEP%2CDEPDOM%2CROE%2CROA%2CDATEUPDT%2COFFICES&sort_by=OFFICES&sort_order=DESC&limit=10&offset=0&format=json&download=false&filename=data_file",
    "GET",
    headers,
)


rate_fdic = api_call_fdic.get_calls_per_second(10000, timedelta(hours=1))


@rate_limited(rate_fdic)
def call_api_fdic():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_fdic.execute()
    return f"Respuesta {response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_fdic()
    print("Respuesta:", response)

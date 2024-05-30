from datetime import timedelta
from os import environ
import time
import requests

from dotenv import load_dotenv
from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

load_dotenv()

BASE_URL = "https://api.spotify.com"
SPOTIFY_CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = environ.get("SPOTIFY_CLIENT_SECRET")

response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET,
    },
)

API_KEY = response.json().get("access_token")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

api_call_spotify = APICall(
    "spotify-6000",
    f"{BASE_URL}/v1/search?q=remaster%2520track%3ADoxy%2520artist%3AMiles%2520Davis&type=album",
    "GET",
    headers,
)

rate_spotify = api_call_spotify.get_calls_per_second(6000, timedelta(hours=1))

print(
    f"""La cuota a cumplir es de 6000 cada 1 hora. Por ello, se realizarán {rate_spotify} llamadas por segundo."""
)


@rate_limited(rate_spotify)
def call_api_spotify():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_spotify.execute()
    return f"{response.status_code}"


start_hour = time.monotonic()
while start_hour < time.monotonic() + 86400 * 3:
    response = call_api_spotify()
    print("Respuesta:", response)

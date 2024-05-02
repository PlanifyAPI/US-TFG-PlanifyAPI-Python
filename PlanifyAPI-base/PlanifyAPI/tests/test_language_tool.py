from datetime import timedelta

from PlanifyAPI.api_calls import APICall
from PlanifyAPI.rate_limiter import rate_limited

headers_language_tool = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
}

body_language_tool = "text=Hola%20mundo%20creuaoclm%20asoml%C3%B1aw%20kv%C3%B1lca%20mo%C3%B1l%20l%20vmkemsksscj%20kscj%20mke%20jemckme%20jaemck%20ekc%20jnmsv&language=auto&enabledOnly=false"

api_call_language_tool = APICall(
    "LanguageTool",
    "https://api.languagetoolplus.com/v2/check",
    "POST",
    headers_language_tool,
    body_language_tool,
)

rate_language_tool = api_call_language_tool.get_calls_per_second(
    10000, timedelta(hours=1)
)


@rate_limited(rate_language_tool)
def call_api_language_tool():
    """
    Función para realizar llamadas a la API.
    """

    response = api_call_language_tool.execute()
    return f"Respuesta {response.status_code}"

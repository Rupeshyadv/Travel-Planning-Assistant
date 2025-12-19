import requests
from langchain.tools import tool

@tool
def get_weather(latitude: float, longitude: float) -> dict:
    """Get weather forecast using Open-Meteo API."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&daily=temperature_2m_max,weathercode"
        "&timezone=auto"
    )
    return requests.get(url).json()["daily"]

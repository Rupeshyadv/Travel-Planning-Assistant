import json
from langchain.tools import tool

@tool
def recommend_hotels(city: str, max_price: int = 3000) -> list:
    """Recommend hotels based on city, rating and price."""
    with open("data/hotels.json") as f:
        hotels = json.load(f)

    return sorted(
        [h for h in hotels if h["city"].lower() == city.lower()
         and h["price_per_night"] <= max_price],
        key=lambda x: (-x["rating"], x["price_per_night"])
    )[:3]

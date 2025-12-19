import json
from langchain.tools import tool

@tool
def discover_places(city: str, interest: str) -> list:
    """Find top attractions based on interest."""
    with open("data/places.json") as f:
        places = json.load(f)

    return [
        p for p in places
        if p["city"].lower() == city.lower()
        and p["type"].lower() == interest.lower()
    ]
